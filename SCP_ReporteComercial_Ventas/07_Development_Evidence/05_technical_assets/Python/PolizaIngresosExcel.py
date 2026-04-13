import os
import math
from pathlib import Path

import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# =========================
# === CONFIGURACIÓN =======
# =========================
EXCEL_DIR = Path(r"Q:\Python\Python\APIS\ContVSFact\Excel")
ENV_PATH = Path(r"Q:\Python\Python\APIS\ContVSFact\conexion\.env")

SHEET_NAME = "Auxiliar Cuentas"
TABLE_NAME = "cont_polizadet_ingresos_original_2026"
CHUNK_SIZE = 1000

TRUNCATE_BEFORE_LOAD = False  # True = vacía la tabla UNA sola vez antes del primer Excel

# =========================
# === UTILIDADES ==========
# =========================
def list_excel_files(excel_dir: Path) -> list[Path]:
    if not excel_dir.exists():
        raise SystemExit(f"❌ No existe la carpeta: {excel_dir}")

    excel_files = sorted(
        excel_dir.glob("*.xlsx"),
        key=lambda p: p.stat().st_mtime,  # mtime: last modified time
        reverse=False  # primero el más viejo, luego los más nuevos
    )

    if not excel_files:
        raise SystemExit(f"❌ No encontré archivos .xlsx en: {excel_dir}")

    return excel_files

def to_decimal(x):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return None
    try:
        if isinstance(x, str):
            x = x.replace(",", "").strip()
            if x == "" or x.lower() == "nan":
                return None
        return float(x)
    except Exception:
        return None

def get_mysql_cfg():
    host = os.getenv("MYSQL_HOST")
    db = os.getenv("MYSQL_DB")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD", "")
    port = int(os.getenv("MYSQL_PORT", "3306"))

    if not host or not db or not user:
        raise SystemExit("❌ Faltan variables requeridas en el .env.")

    return {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": db
    }

def prepare_dataframe(df: pd.DataFrame) -> tuple[pd.DataFrame, list[tuple]]:
    rename_map = {
        "Fecha": "fecha",
        "Póliza": "poliza",
        "Partida": "partida",
        "Centro Costo": "centro_costo",
        "Referencia": "referencia",
        "Concepto Mov.": "concepto_mov",
        "Saldo Inicial": "saldo_inicial",
        "Cargo": "cargo",
        "Abono": "abono",
        "Saldo Final": "saldo_final",
        "Tipo Póliza": "tipo_poliza",
        "Usuario": "usuario",
    }

    missing = [c for c in rename_map.keys() if c not in df.columns]
    if missing:
        raise SystemExit(f"❌ Columnas faltantes: {missing}")

    df = df.rename(columns=rename_map)

    # =========================
    # === LIMPIEZA PROFUNDA ===
    # =========================
    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True, errors="coerce")

    str_cols = ["poliza", "centro_costo", "referencia", "concepto_mov", "tipo_poliza", "usuario"]
    for c in str_cols:
        df[c] = df[c].astype(object).apply(lambda x: str(x).strip() if pd.notnull(x) else None)
        df[c] = df[c].replace({"nan": None, "None": None, "NaN": None, "<NA>": None})

    df["partida"] = pd.to_numeric(df["partida"], errors="coerce")

    decimal_cols = ["saldo_inicial", "cargo", "abono", "saldo_final"]
    for c in decimal_cols:
        df[c] = df[c].apply(to_decimal)

    ordered_cols = list(rename_map.values())

    data_to_insert = []
    for row in df[ordered_cols].itertuples(index=False, name=None):
        clean_row = tuple((None if pd.isna(val) or val is pd.NaT else val) for val in row)
        data_to_insert.append(clean_row)

    return df, data_to_insert

# =========================
# === MAIN ================
# =========================
def main():
    # 1) Cargar .env
    if not ENV_PATH.exists():
        raise SystemExit(f"❌ No se encontró el archivo .env en: {ENV_PATH}")

    load_dotenv(ENV_PATH)
    mysql_cfg = get_mysql_cfg()
    print(f"🔐 Conectando a MySQL: {mysql_cfg['database']}")

    # 2) Listar Excels (todos)
    excel_files = list_excel_files(EXCEL_DIR)
    print(f"📄 Archivos Excel detectados: {len(excel_files)}")
    for idx, p in enumerate(excel_files, 1):
        print(f"   {idx}. {p.name}")

    # 3) Conexión MySQL (una sola vez)
    cnx = None
    cur = None
    try:
        cnx = mysql.connector.connect(**mysql_cfg)
        cur = cnx.cursor()

        # Crear tabla
        create_sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            fecha DATE NULL,
            poliza VARCHAR(50) NULL,
            partida INT NULL,
            centro_costo VARCHAR(20) NULL,
            referencia VARCHAR(60) NULL,
            concepto_mov VARCHAR(255) NULL,
            saldo_inicial DECIMAL(18,2) NULL,
            cargo DECIMAL(18,2) NULL,
            abono DECIMAL(18,2) NULL,
            saldo_final DECIMAL(18,2) NULL,
            tipo_poliza VARCHAR(30) NULL,
            usuario VARCHAR(50) NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cur.execute(create_sql)

        # Truncar UNA vez si aplica
        if TRUNCATE_BEFORE_LOAD:
            print(f"⚠️ Vaciando tabla {TABLE_NAME} (solo una vez antes del primer archivo)...")
            cur.execute(f"TRUNCATE TABLE {TABLE_NAME}")
            cnx.commit()

        # SQL insert
        insert_sql = f"""
        INSERT INTO {TABLE_NAME}
        (fecha, poliza, partida, centro_costo, referencia, concepto_mov,
         saldo_inicial, cargo, abono, saldo_final, tipo_poliza, usuario)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # 4) Procesar archivo por archivo
        grand_total = 0
        for file_idx, excel_path in enumerate(excel_files, start=1):
            print(f"\n📥 ({file_idx}/{len(excel_files)}) Leyendo: {excel_path.name}")

            df = pd.read_excel(excel_path, sheet_name=SHEET_NAME)
            _, data_to_insert = prepare_dataframe(df)

            total = len(data_to_insert)
            grand_total += total
            print(f"📦 Filas listas para insertar en este archivo: {total}")

            inserted = 0
            for i in range(0, total, CHUNK_SIZE):
                batch = data_to_insert[i:i + CHUNK_SIZE]
                cur.executemany(insert_sql, batch)
                cnx.commit()
                inserted += len(batch)
                print(f"✅ Progreso archivo {file_idx}: {inserted}/{total}")

            print(f"🎯 Archivo terminado: {excel_path.name} (insertadas {inserted})")

        print(f"\n🎉 Proceso finalizado correctamente. Total filas procesadas (suma): {grand_total}")

    except Error as e:
        if cnx is not None and cnx.is_connected():
            cnx.rollback()
        print(f"❌ Error en MySQL: {e}")

    finally:
        if cur is not None:
            cur.close()
        if cnx is not None and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    main()