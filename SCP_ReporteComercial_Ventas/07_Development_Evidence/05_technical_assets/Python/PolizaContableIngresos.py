import os
import sys
import socket
import time as time_mod
import re
import pyodbc
import mysql.connector
from mysql.connector import Error as MySQLError
from dotenv import load_dotenv
from datetime import datetime, date, time as dt_time
from decimal import Decimal

# =========================
# Cargar .env
# =========================
ENV_PATH = r"Q:\Python\Python\APIS\ContVSFact\conexion\.env"

if not os.path.exists(ENV_PATH):
    print(f"❌ No existe el .env en: {ENV_PATH}")
    sys.exit(1)

load_dotenv(ENV_PATH)

# =========================
# Rutas / Archivos
# =========================
SQL_FILE_PATH = r"Q:\Python\Python\APIS\ContVSFact\Querys\PolizaContableIngresos.sql"

LOG_DIR = r"Q:\Python\Python\APIS\ContVSFact\logs"
LOG_PATH = os.path.join(LOG_DIR, "PolizaContableIngresos.log")
os.makedirs(LOG_DIR, exist_ok=True)

# =========================
# Destino MySQL
# =========================
DEST_TABLE = "cont_polizadet_ingresos_2026"

# Llave única para UPSERT (ajústala si tu lógica es otra)
UPSERT_UNIQUE_KEY = ["poliza", "partida", "referencia", "concepto_mov"]

# =========================
# Helpers
# =========================
def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg: str):
    print(f"[{now_str()}] {msg}")


def log_file(msg: str):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{now_str()}] {msg}\n")


def die(msg: str, code: int = 1):
    print(f"\n❌ {msg}")
    log_file(f"❌ {msg}")
    sys.exit(code)


def get_env(key: str, default=None, required: bool = False):
    v = os.getenv(key, default)
    if required and (v is None or str(v).strip() == ""):
        die(f"Falta variable requerida en .env: {key}")
    return v


def test_tcp_port(host: str, port: int, timeout: int = 3) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def load_sql_query(path: str) -> str:
    """
    Lee un archivo .sql y devuelve el query listo para ejecutar.
    - Soporta UTF-8 con BOM (utf-8-sig)
    - Remueve líneas 'GO' (SSMS) para evitar errores con pyodbc
    """
    if not os.path.exists(path):
        die(f"No existe el archivo SQL en: {path}")

    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            sql = f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1") as f:
            sql = f.read()

    # Remover líneas "GO"
    sql = re.sub(r"(?im)^\s*GO\s*$", "", sql)
    sql = sql.strip()

    if not sql:
        die(f"El archivo SQL está vacío: {path}")

    return sql


# =========================
# Variables desde .env
# =========================
SQLSERVER_HOST = get_env("SQLSERVER_HOST", required=True)
SQLSERVER_DB = get_env("SQLSERVER_DB", required=True)
SQLSERVER_USER = get_env("SQLSERVER_USER", required=True)
SQLSERVER_PASS = get_env("SQLSERVER_PASSWORD", required=True)
SQLSERVER_DRIVER = get_env("SQLSERVER_DRIVER", "ODBC Driver 17 for SQL Server")

SQLSERVER_PORT = get_env("SQLSERVER_PORT", "").strip()
SQLSERVER_TIMEOUT = int(get_env("SQLSERVER_TIMEOUT", "15"))
SQLSERVER_ENCRYPT = get_env("SQLSERVER_ENCRYPT", "no")
SQLSERVER_TRUST_CERT = get_env("SQLSERVER_TRUST_CERT", "yes")

MYSQL_HOST = get_env("MYSQL_HOST", "127.0.0.1")
MYSQL_DB = get_env("MYSQL_DB", required=True)
MYSQL_USER = get_env("MYSQL_USER", "root")
MYSQL_PASSWORD = get_env("MYSQL_PASSWORD", "")
MYSQL_PORT = int(get_env("MYSQL_PORT", "3306"))

BATCH_SIZE = int(get_env("MYSQL_BATCH_SIZE", "2000"))

# =========================
# Normalizar server ODBC
# =========================
if SQLSERVER_PORT:
    try:
        int(SQLSERVER_PORT)
    except ValueError:
        die("SQLSERVER_PORT debe ser numérico si lo defines en .env")
    SQLSERVER_SERVER = f"{SQLSERVER_HOST},{SQLSERVER_PORT}"
else:
    SQLSERVER_SERVER = SQLSERVER_HOST


# =========================
# Conectores
# =========================
def connect_sqlserver():
    conn_str = (
        f"DRIVER={{{SQLSERVER_DRIVER}}};"
        f"SERVER={SQLSERVER_SERVER};"
        f"DATABASE={SQLSERVER_DB};"
        f"UID={SQLSERVER_USER};"
        f"PWD={SQLSERVER_PASS};"
        "Trusted_Connection=No;"
        "Network=DBMSSOCN;"
        f"Connection Timeout={SQLSERVER_TIMEOUT};"
        f"Encrypt={SQLSERVER_ENCRYPT};"
        f"TrustServerCertificate={SQLSERVER_TRUST_CERT};"
    )

    log(f"🔌 SQL Server => {SQLSERVER_SERVER} | DB: {SQLSERVER_DB} | Driver: {SQLSERVER_DRIVER}")
    log_file(f"🔌 SQL Server => {SQLSERVER_SERVER} | DB: {SQLSERVER_DB} | Driver: {SQLSERVER_DRIVER}")
    return pyodbc.connect(conn_str)


def connect_mysql():
    log(f"🔌 MySQL => {MYSQL_HOST}:{MYSQL_PORT} | DB: {MYSQL_DB}")
    log_file(f"🔌 MySQL => {MYSQL_HOST}:{MYSQL_PORT} | DB: {MYSQL_DB}")
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=MYSQL_PORT,
        autocommit=False,
    )


# =========================
# Mapeo de nombres (para respetar tu esquema)
# =========================
COLUMN_RENAMES = {
    "Poliza": "poliza",
    "Partida": "partida",
    "CentroCosto": "centro_costo",
    "Centro_Costo": "centro_costo",
    "Referencia": "referencia",
    "ConceptoMov": "concepto_mov",
    "Concepto_Mov": "concepto_mov",
    "Cargo": "cargo",
    "Abono": "abono",
    "fecha_creacion": "fecha_creacion",
    "fecha_ingreso": "fecha_ingreso",
    "fecha_modifico": "fecha_modifico",
}


def normalize_col(name: str) -> str:
    """
    - Primero aplica renombres conocidos
    - Si no existe, normaliza a snake-ish
    """
    if name in COLUMN_RENAMES:
        return COLUMN_RENAMES[name]

    n = (name or "").strip()
    n = re.sub(r"\s+", "_", n)
    n = re.sub(r"[^\w]+", "_", n)
    n = n.lower().strip("_")
    return n or "col"


# =========================
# Tipos MySQL (sin constantes pyodbc)
# =========================
def mysql_type_from_pyodbc(type_code, internal_size=None, precision=None, scale=None) -> str:
    """
    Mapeo robusto que NO depende de pyodbc.SQL_DATE / SQL_TIME / etc.
    type_code normalmente viene como clase Python (str/int/datetime/etc).
    """
    # Algunos drivers retornan una clase/type, ej: <class 'datetime.datetime'>
    if isinstance(type_code, type):
        py_type = type_code
        if py_type is datetime:
            return "DATETIME"
        if py_type is date:
            return "DATE"
        if py_type is dt_time:
            return "TIME"
        if py_type is int:
            return "BIGINT"
        if py_type is float:
            return "DOUBLE"
        if py_type is Decimal:
            p = precision if isinstance(precision, int) and precision > 0 else 18
            s = scale if isinstance(scale, int) and scale >= 0 else 6
            p = min(max(p, 1), 65)
            s = min(max(s, 0), 30)
            if s > p:
                s = p
            return f"DECIMAL({p},{s})"
        if py_type is bytes or py_type is bytearray:
            return "BLOB"
        # default para str u otros
        size = internal_size if isinstance(internal_size, int) and internal_size > 0 else 255
        size = min(max(size, 10), 2000)
        return f"VARCHAR({size})"

    # Si llegara como string o algo raro
    type_name = str(type_code).lower()

    if "datetime" in type_name or "timestamp" in type_name:
        return "DATETIME"
    if "date" in type_name:
        return "DATE"
    if "time" in type_name:
        return "TIME"
    if "int" in type_name:
        return "BIGINT"
    if "decimal" in type_name or "numeric" in type_name:
        p = precision if isinstance(precision, int) and precision > 0 else 18
        s = scale if isinstance(scale, int) and scale >= 0 else 6
        return f"DECIMAL({p},{s})"
    if "float" in type_name or "real" in type_name:
        return "DOUBLE"
    if "char" in type_name or "text" in type_name or "varchar" in type_name:
        size = internal_size if isinstance(internal_size, int) and internal_size > 0 else 255
        size = min(max(size, 10), 2000)
        return f"VARCHAR({size})"
    if "binary" in type_name or "varbinary" in type_name:
        return "BLOB"

    return "VARCHAR(255)"


# =========================
# Crear tabla MySQL desde cursor.description
# =========================
def build_create_table_sql(desc, table_name: str) -> str:
    """
    desc: cursor.description
    Crea tabla con columnas del SELECT + fecha_consulta
    Incluye UNIQUE KEY para UPSERT.
    """
    cols = []
    for (name, type_code, display_size, internal_size, precision, scale, null_ok) in desc:
        col = normalize_col(name)
        col_type = mysql_type_from_pyodbc(type_code, internal_size, precision, scale)
        cols.append(f"`{col}` {col_type} NULL")

    cols.append("`fecha_consulta` DATETIME NULL")

    uq_cols = ", ".join([f"`{c}`" for c in UPSERT_UNIQUE_KEY])

    create_sql = f"""
CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  {",\n  ".join(cols)},
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_upsert` ({uq_cols})
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""".strip()

    return create_sql


def ensure_table_from_query(my_cur, desc):
    create_sql = build_create_table_sql(desc, DEST_TABLE)
    log(f"🧱 Creando/verificando tabla destino: {DEST_TABLE}")
    log_file(f"🧱 Creando/verificando tabla destino: {DEST_TABLE}")
    try:
        my_cur.execute(create_sql)
    except MySQLError as e:
        die(f"❌ No se pudo crear/verificar tabla {DEST_TABLE}. Detalle: {e}\n\nSQL:\n{create_sql}")


# =========================
# INSERT/UPSERT dinámico
# =========================
def build_insert_sql_from_desc(desc, table_name: str):
    cols = [normalize_col(d[0]) for d in desc]
    all_cols = cols + ["fecha_consulta"]

    col_list_sql = ", ".join([f"`{c}`" for c in all_cols])
    placeholders = ", ".join(["%s"] * len(all_cols))

    update_cols = [c for c in all_cols if c not in UPSERT_UNIQUE_KEY]
    update_sql = ", ".join([f"`{c}` = VALUES(`{c}`)" for c in update_cols])

    sql = f"""
INSERT INTO `{table_name}` ({col_list_sql})
VALUES ({placeholders})
ON DUPLICATE KEY UPDATE
  {update_sql};
""".strip()

    return sql, cols


def to_mysql_value(v):
    # Normalización de tipos para mysql-connector
    if isinstance(v, Decimal):
        return float(v)
    return v


# =========================
# Query ORIGEN (SQL Server) - desde archivo .sql
# =========================
query_origen = load_sql_query(SQL_FILE_PATH)


# =========================
# Main
# =========================
def main():
    start = time_mod.time()

    log("🚀 Iniciando proceso (PolizaContableIngresos)...")
    log_file("===================================")
    log_file("🚀 Iniciando proceso (PolizaContableIngresos)")
    log_file("===================================")

    log(f"📄 Query origen leído desde: {SQL_FILE_PATH}")
    log_file(f"📄 Query origen leído desde: {SQL_FILE_PATH}")

    # Test rápido de puerto
    if not SQLSERVER_PORT:
        default_port = 1433
        ok = test_tcp_port(SQLSERVER_HOST, default_port, timeout=3)
        log(f"🔎 Test TCP {SQLSERVER_HOST}:{default_port} => {'OK' if ok else 'FALLÓ'}")
        log_file(f"🔎 Test TCP {SQLSERVER_HOST}:{default_port} => {'OK' if ok else 'FALLÓ'}")
    else:
        ok = test_tcp_port(SQLSERVER_HOST, int(SQLSERVER_PORT), timeout=3)
        log(f"🔎 Test TCP {SQLSERVER_HOST}:{SQLSERVER_PORT} => {'OK' if ok else 'FALLÓ'}")
        log_file(f"🔎 Test TCP {SQLSERVER_HOST}:{SQLSERVER_PORT} => {'OK' if ok else 'FALLÓ'}")

    sql_conn = sql_cur = None
    my_conn = my_cur = None

    total_leidos = 0
    total_guardados = 0
    errores_mysql_batches = 0

    try:
        # Conectar SQL Server
        try:
            sql_conn = connect_sqlserver()
            sql_cur = sql_conn.cursor()
            log("✅ Conectado a SQL Server")
            log_file("✅ Conectado a SQL Server")
        except pyodbc.Error as e:
            die(
                "No se pudo conectar a SQL Server.\n"
                f"Detalle: {e}\n\n"
                "Causas típicas:\n"
                "- No estás en la red/VPN correcta\n"
                "- Puerto bloqueado por firewall\n"
                "- SQL Server sin TCP/IP habilitado\n"
                "- Puerto real diferente (usa SQLSERVER_PORT)\n"
            )

        # Conectar MySQL
        try:
            my_conn = connect_mysql()
            my_cur = my_conn.cursor()
            log("✅ Conectado a MySQL")
            log_file("✅ Conectado a MySQL")
        except MySQLError as e:
            die(f"No se pudo conectar a MySQL. Detalle: {e}")

        # Ejecutar query origen
        log("📥 Ejecutando query origen (SQL Server) desde archivo...")
        log_file("📥 Ejecutando query origen (SQL Server) desde archivo...")

        try:
            sql_cur.execute(query_origen)
        except pyodbc.Error as e:
            die(f"❌ Error ejecutando query en SQL Server: {e}")

        if not sql_cur.description:
            die("❌ La consulta no devolvió metadata de columnas (cursor.description vacío).")

        # Crear tabla destino en base a la consulta
        ensure_table_from_query(my_cur, sql_cur.description)
        my_conn.commit()

        # Generar INSERT dinámico
        insert_destino, select_cols = build_insert_sql_from_desc(sql_cur.description, DEST_TABLE)
        log("🧩 INSERT/UPSERT dinámico generado.")
        log_file("🧩 INSERT/UPSERT dinámico generado.")

        fecha_consulta = datetime.now()

        # Insertar por lotes
        while True:
            rows = sql_cur.fetchmany(BATCH_SIZE)
            if not rows:
                break

            total_leidos += len(rows)

            valores = []
            for r in rows:
                row_vals = []
                for i in range(len(select_cols)):
                    row_vals.append(to_mysql_value(r[i]))

                row_vals.append(fecha_consulta)
                valores.append(tuple(row_vals))

            try:
                my_cur.executemany(insert_destino, valores)
                my_conn.commit()
                total_guardados += len(valores)
                log(f"✔ Batch guardado: {len(valores)} | Total: {total_guardados}")
                log_file(f"✔ BATCH GUARDADO | Registros: {len(valores)} | Total: {total_guardados}")
            except MySQLError as e:
                my_conn.rollback()
                errores_mysql_batches += 1
                log(f"❌ Error insertando batch en MySQL: {e} (rollback)")
                log_file(f"❌ ERROR MYSQL BATCH | {e} | (rollback)")

        elapsed = time_mod.time() - start

        print("\n===================================")
        print("✅ Proceso finalizado (PolizaContableIngresos)")
        print(f"📥 Total leídos de SQL Server: {total_leidos}")
        print(f"💾 Total guardados en MySQL:  {total_guardados}")
        print(f"🔴 Batches con error MySQL:   {errores_mysql_batches}")
        print(f"⏱ Tiempo total:              {elapsed:.2f} segundos")
        print("===================================\n")

        log_file("===================================")
        log_file("RESUMEN FINAL")
        log_file(f"Total leídos SQL Server: {total_leidos}")
        log_file(f"Total guardados MySQL: {total_guardados}")
        log_file(f"Batches con error MySQL: {errores_mysql_batches}")
        log_file(f"Tiempo total (seg): {elapsed:.2f}")
        log_file("===================================")

        print("📌 Log guardado en:")
        print(f" {LOG_PATH}\n")

    finally:
        # Cierre seguro
        try:
            if sql_cur:
                sql_cur.close()
        except Exception:
            pass

        try:
            if sql_conn:
                sql_conn.close()
        except Exception:
            pass

        try:
            if my_cur:
                my_cur.close()
        except Exception:
            pass

        try:
            if my_conn:
                my_conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()