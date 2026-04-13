# -*- coding: utf-8 -*-
"""
SQL Server -> MySQL: Carga dinámica según SQL (desde archivo .sql)
- Lee credenciales desde .env
- Lee el query desde un .sql en disco
- Ejecuta consulta en SQL Server
- Crea tabla en MySQL si no existe (dinámica según columnas/tipos devueltos)
- Inserta por lotes con UPSERT (evita duplicados) usando UNIQUE KEY automático si existe (Referencia, fecha_ingreso)
- Log a archivo

Requisitos:
    pip install pyodbc pymysql python-dotenv
"""

import os
import sys
import logging
from datetime import datetime, date
from decimal import Decimal
from typing import Any, Dict, List, Tuple, Optional

import pyodbc
import pymysql
from dotenv import load_dotenv


# =========================
# Rutas y constantes
# =========================
ENV_PATH = r"Q:\Python\Python\APIS\ContVSFact\conexion\.env"
LOG_DIR  = r"Q:\Python\Python\APIS\ContVSFact\logs"
TABLE_DEST = "dm_factura_electronica_totales"
BATCH_SIZE = 2000

# ✅ Query externo (archivo .sql)
QUERY_PATH = r"Q:\Python\Python\APIS\ContVSFact\Querys\FacturacionElectronica.sql"


# =========================
# Utilidades
# =========================
def setup_logger() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"FacturacionElectronica.log")

    logger = logging.getLogger("carga_sqlserver_mysql")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    logger.info(f"LOG_FILE: {log_path}")
    return logger


def get_env(key: str, default: str = None, required: bool = False) -> str:
    val = os.getenv(key, default)
    if required and (val is None or str(val).strip() == ""):
        raise ValueError(f"Falta variable requerida en .env: {key}")
    return val


def normalize_value(v: Any) -> Any:
    """Convierte tipos Python a algo compatible con pymysql."""
    if v is None:
        return None
    return v


def safe_col_name(name: str) -> str:
    """Nombre de columna seguro para MySQL (entre backticks lo protegemos)."""
    return name.strip()


def load_sql_query(path: str) -> str:
    """Lee el archivo SQL desde disco."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"No existe el archivo SQL: {path}")

    # utf-8-sig soporta BOM si el archivo viene de SSMS / Windows
    with open(path, "r", encoding="utf-8-sig") as f:
        sql_text = f.read().strip()

    if not sql_text:
        raise ValueError(f"El archivo SQL está vacío: {path}")

    return sql_text


def _infer_mysql_type(value: Any, precision: Optional[int] = None, scale: Optional[int] = None) -> str:
    """Infere tipo MySQL por valor real (mejor que solo type_code)."""
    if value is None:
        return "VARCHAR(255)"

    if isinstance(value, bool):
        return "TINYINT(1)"
    if isinstance(value, int):
        return "BIGINT"
    if isinstance(value, float):
        return "DOUBLE"
    if isinstance(value, Decimal):
        p = precision or 18
        s = 6 if scale is None else scale
        p = max(1, min(int(p), 65))
        s = max(0, min(int(s), 30))
        if s >= p:
            p = min(65, s + 5)
        return f"DECIMAL({p},{s})"
    if isinstance(value, datetime):
        return "DATETIME"
    if isinstance(value, date):
        return "DATE"
    if isinstance(value, (bytes, bytearray)):
        return "LONGBLOB"

    return "VARCHAR(255)"


# =========================
# Conexiones
# =========================
def connect_sqlserver(logger: logging.Logger):
    sqlserver_host = get_env("SQLSERVER_HOST", required=True)
    sqlserver_db = get_env("SQLSERVER_DB", required=True)
    sqlserver_user = get_env("SQLSERVER_USER", required=True)
    sqlserver_password = get_env("SQLSERVER_PASSWORD", required=True)
    sqlserver_driver = get_env("SQLSERVER_DRIVER", "ODBC Driver 17 for SQL Server")

    conn_str = (
        f"DRIVER={{{sqlserver_driver}}};"
        f"SERVER={sqlserver_host};"
        f"DATABASE={sqlserver_db};"
        f"UID={sqlserver_user};"
        f"PWD={sqlserver_password};"
        "TrustServerCertificate=yes;"
    )
    logger.info("Conectando a SQL Server...")
    return pyodbc.connect(conn_str, autocommit=True)


def connect_mysql(logger: logging.Logger):
    mysql_host = get_env("MYSQL_HOST", required=True)
    mysql_db = get_env("MYSQL_DB", required=True)
    mysql_user = get_env("MYSQL_USER", required=True)
    mysql_password = get_env("MYSQL_PASSWORD", "")
    mysql_port = int(get_env("MYSQL_PORT", "3306"))

    logger.info("Conectando a MySQL...")
    return pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db,
        port=mysql_port,
        charset="utf8mb4",
        autocommit=False,
        cursorclass=pymysql.cursors.Cursor,
    )


# =========================
# Extracción SQL Server (dinámica desde archivo)
# =========================
def fetch_sqlserver(sql_conn, logger: logging.Logger) -> Tuple[List[str], List[Dict[str, Any]], List[Tuple[Any, ...]]]:
    logger.info(f"Leyendo archivo SQL: {QUERY_PATH}")
    sql_text = load_sql_query(QUERY_PATH)

    logger.info("Ejecutando consulta en SQL Server...")
    cur = sql_conn.cursor()
    cur.execute(sql_text)

    cols = [d[0] for d in cur.description]

    # description: (name, type_code, display_size, internal_size, precision, scale, null_ok)
    meta: List[Dict[str, Any]] = []
    for d in cur.description:
        meta.append(
            {
                "name": d[0],
                "type_code": d[1],
                "precision": d[4],
                "scale": d[5],
                "null_ok": d[6],
            }
        )

    rows = cur.fetchall()
    logger.info(f"Columnas devueltas: {cols}")
    logger.info(f"Registros obtenidos de SQL Server: {len(rows)}")

    return cols, meta, rows


# =========================
# DDL MySQL (dinámico)
# =========================
def ensure_table_mysql(mysql_conn, cols: List[str], meta: List[Dict[str, Any]], rows: List[Tuple[Any, ...]], logger: logging.Logger):
    """
    Crea la tabla destino en MySQL según las columnas devueltas por el .sql.
    Agrega:
      - id autoincrement
      - fecha_carga
      - UNIQUE KEY si existen Referencia y fecha_ingreso (para UPSERT)
    """
    logger.info(f"Creando/verificando tabla MySQL dinámica: {TABLE_DEST}")

    first = rows[0] if rows else None

    col_defs: List[str] = []
    for i, col in enumerate(cols):
        col_name = safe_col_name(col)

        null_ok = True
        try:
            null_ok = bool(meta[i].get("null_ok", True))
        except Exception:
            null_ok = True

        precision = meta[i].get("precision") if i < len(meta) else None
        scale = meta[i].get("scale") if i < len(meta) else None

        sample_val = first[i] if first else None
        mysql_type = _infer_mysql_type(sample_val, precision=precision, scale=scale)

        if first is None:
            nullable_sql = "NULL"
        else:
            nullable_sql = "NULL" if null_ok else "NOT NULL"

        # Forzar NOT NULL en columnas clave si existen
        if col_name.lower() in ("referencia", "fecha_ingreso"):
            nullable_sql = "NOT NULL"

        col_defs.append(f"`{col_name}` {mysql_type} {nullable_sql}")

    lower_cols = [c.lower().strip() for c in cols]
    unique_cols: Optional[List[str]] = None
    if "referencia" in lower_cols and "fecha_ingreso" in lower_cols:
        ref_col = cols[lower_cols.index("referencia")]
        fec_col = cols[lower_cols.index("fecha_ingreso")]
        unique_cols = [safe_col_name(ref_col), safe_col_name(fec_col)]

    unique_sql = ""
    if unique_cols:
        unique_sql = f",\n        UNIQUE KEY `ux_ref_fecha` (`{unique_cols[0]}`, `{unique_cols[1]}`)"

    ddl = f"""
    CREATE TABLE IF NOT EXISTS `{TABLE_DEST}` (
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
        {",\n        ".join(col_defs)},
        `fecha_carga` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        {unique_sql}
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """

    with mysql_conn.cursor() as cur:
        cur.execute(ddl)
    mysql_conn.commit()

    if unique_cols:
        logger.info(f"Tabla lista con UNIQUE (UPSERT): {unique_cols[0]}, {unique_cols[1]}")
    else:
        logger.warning(
            "Tabla lista, PERO no se creó UNIQUE KEY porque no existen columnas Referencia y fecha_ingreso en el SELECT. "
            "El UPSERT podría no funcionar como esperas."
        )


# =========================
# Carga a MySQL (UPSERT dinámico)
# =========================
def upsert_mysql(mysql_conn, cols: List[str], rows: List[Tuple[Any, ...]], logger: logging.Logger):
    """
    UPSERT dinámico según columnas del query.
    - Inserta todas las columnas del SELECT
    - fecha_carga se actualiza en cada upsert
    - Requiere UNIQUE KEY (idealmente Referencia + fecha_ingreso)
    """
    if not rows:
        logger.info("No hay datos para insertar.")
        return

    insert_cols = [safe_col_name(c) for c in cols]
    placeholders = ", ".join(["%s"] * len(insert_cols))
    col_sql = ", ".join([f"`{c}`" for c in insert_cols])

    # no actualizamos columnas "clave" si existen
    lower_cols = [c.lower() for c in insert_cols]
    key_like = set()
    if "referencia" in lower_cols:
        key_like.add(insert_cols[lower_cols.index("referencia")])
    if "fecha_ingreso" in lower_cols:
        key_like.add(insert_cols[lower_cols.index("fecha_ingreso")])

    update_cols = [c for c in insert_cols if c not in key_like]
    update_sql = ",\n        ".join([f"`{c}` = VALUES(`{c}`)" for c in update_cols])

    insert_sql = f"""
    INSERT INTO `{TABLE_DEST}` (
        {col_sql}, `fecha_carga`
    ) VALUES (
        {placeholders}, NOW()
    )
    ON DUPLICATE KEY UPDATE
        {update_sql if update_sql else "`fecha_carga` = NOW()"},
        `fecha_carga` = NOW();
    """

    total = 0
    with mysql_conn.cursor() as cur:
        batch: List[Tuple[Any, ...]] = []

        for r in rows:
            batch.append(tuple(normalize_value(v) for v in r))

            if len(batch) >= BATCH_SIZE:
                cur.executemany(insert_sql, batch)
                mysql_conn.commit()
                total += len(batch)
                logger.info(f"Insertados/actualizados: {total}")
                batch.clear()

        if batch:
            cur.executemany(insert_sql, batch)
            mysql_conn.commit()
            total += len(batch)
            logger.info(f"Insertados/actualizados: {total}")

    logger.info("Carga finalizada correctamente.")


# =========================
# Main
# =========================
def main():
    logger = setup_logger()

    if not os.path.exists(ENV_PATH):
        raise FileNotFoundError(f"No existe el .env en: {ENV_PATH}")

    if not os.path.exists(QUERY_PATH):
        raise FileNotFoundError(f"No existe el archivo SQL en: {QUERY_PATH}")

    load_dotenv(ENV_PATH)
    logger.info(f"ENV cargado desde: {ENV_PATH}")

    sql_conn = None
    mysql_conn = None

    t0 = datetime.now()
    try:
        sql_conn = connect_sqlserver(logger)
        mysql_conn = connect_mysql(logger)

        # 1) Ejecuta query y obtiene columnas/meta/rows
        cols, meta, rows = fetch_sqlserver(sql_conn, logger)

        # 2) Crea tabla MySQL dinámica en base al SELECT
        ensure_table_mysql(mysql_conn, cols, meta, rows, logger)

        # 3) UPSERT dinámico
        upsert_mysql(mysql_conn, cols, rows, logger)

        dt = datetime.now() - t0
        logger.info(f"Tiempo total: {dt}")

    except Exception as e:
        logger.exception(f"ERROR: {e}")
        try:
            if mysql_conn:
                mysql_conn.rollback()
        except Exception:
            pass
        raise
    finally:
        try:
            if sql_conn:
                sql_conn.close()
        except Exception:
            pass
        try:
            if mysql_conn:
                mysql_conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()