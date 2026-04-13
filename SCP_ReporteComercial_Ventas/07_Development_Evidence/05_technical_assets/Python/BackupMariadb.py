import os
import sys
import shutil
import subprocess
import tempfile
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv


# =========================================================
# ✅ LO ÚNICO QUE EDITAS: NOMBRE(S) DE TABLA(S) A RESPALDAR
# =========================================================
TABLES = ["tb_mb_conciliacion_fact_vs_conta_2026"]  # <- cambia aquí
# Si quieres TODA la BD: TABLES = []


# =========================
# RUTAS FIJAS DEL PROYECTO
# =========================
ENV_PATH = Path(r"Q:\Python\Python\APIS\ContVSFact\Conexion\.env")
LOG_DIR  = Path(r"Q:\Python\Python\APIS\ContVSFact\Logs")

OUTPUT_DIR = Path(r"Q:\Backups_scp")
OUTPUT_PREFIX = "tabla_meta"

DUMP_EXE_OVERRIDE = ""  # ej: r"C:\Program Files\MariaDB 10.6\bin\mariadb-dump.exe"


# =========================
# LOGGING
# =========================
def setup_logger() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / "backup_dump.log"

    logger = logging.getLogger("dump_backup")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = RotatingFileHandler(
        log_file,
        maxBytes=2_000_000,
        backupCount=5,
        encoding="utf-8"
    )
    fh.setFormatter(fmt)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


def die(logger: logging.Logger, msg: str, code: int = 1):
    logger.error(msg)
    sys.exit(code)


# =========================
# DUMP EXE
# =========================
def candidate_dump_paths() -> list[str]:
    return [
        # MariaDB
        r"C:\Program Files\MariaDB 11.0\bin\mariadb-dump.exe",
        r"C:\Program Files\MariaDB 10.11\bin\mariadb-dump.exe",
        r"C:\Program Files\MariaDB 10.6\bin\mariadb-dump.exe",
        r"C:\Program Files\MariaDB 10.6\bin\mysqldump.exe",
        r"C:\Program Files\MariaDB 10.5\bin\mariadb-dump.exe",
        r"C:\Program Files\MariaDB 10.5\bin\mysqldump.exe",
        r"C:\Program Files\MariaDB 10.4\bin\mariadb-dump.exe",
        r"C:\Program Files\MariaDB 10.4\bin\mysqldump.exe",
        # XAMPP
        r"C:\xampp\mysql\bin\mysqldump.exe",
        r"C:\xampp\mariadb\bin\mariadb-dump.exe",
        r"C:\xampp\mariadb\bin\mysqldump.exe",
        # MySQL
        r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe",
        r"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe",
    ]


def find_dump_exe(logger: logging.Logger) -> str:
    if DUMP_EXE_OVERRIDE:
        if os.path.exists(DUMP_EXE_OVERRIDE):
            return DUMP_EXE_OVERRIDE
        die(logger, f"DUMP_EXE_OVERRIDE está definido pero no existe:\n{DUMP_EXE_OVERRIDE}")

    for exe in ("mariadb-dump.exe", "mariadb-dump", "mysqldump.exe", "mysqldump"):
        path = shutil.which(exe)
        if path:
            return path

    for path in candidate_dump_paths():
        if os.path.exists(path):
            return path

    die(
        logger,
        "No se encontró 'mariadb-dump' ni 'mysqldump'.\n"
        "Solución rápida: pega la ruta en DUMP_EXE_OVERRIDE."
    )
    return ""


def dump_type(dump_exe: str) -> str:
    exe_lower = os.path.basename(dump_exe).lower()

    if "mariadb-dump" in exe_lower:
        return "mariadb"

    try:
        r = subprocess.run([dump_exe, "--version"], capture_output=True, text=True, check=False)
        txt = (r.stdout + " " + r.stderr).lower()
        if "mysqldump" in txt and (" 8." in txt or "distrib 8" in txt):
            return "mysqldump_mysql8"
        return "mysqldump_other"
    except Exception:
        return "mysqldump_other"


# =========================
# ENV (TU FORMATO)
# =========================
def get_env(logger: logging.Logger) -> dict:
    if not ENV_PATH.exists():
        die(logger, f"No existe el .env en:\n{ENV_PATH}")

    load_dotenv(ENV_PATH)

    host = (os.getenv("MYSQL_HOST") or "").strip()
    db   = (os.getenv("MYSQL_DB") or "").strip()
    user = (os.getenv("MYSQL_USER") or "").strip()
    pwd  = os.getenv("MYSQL_PASSWORD") or ""
    port_raw = (os.getenv("MYSQL_PORT") or "").strip()

    if not db:
        die(logger, "No encontré MYSQL_DB en tu .env (es obligatorio).")

    try:
        port = int(port_raw)
    except ValueError:
        die(logger, f"MYSQL_PORT inválido en .env: '{port_raw}' (debe ser número)")

    return {"host": host, "port": port, "user": user, "password": pwd, "name": db}


def build_temp_cnf(host: str, port: int, user: str, password: str) -> str:
    content = "[client]\n"
    content += f"user={user}\n"
    content += f"password={password}\n"
    content += f"host={host}\n"
    content += f"port={port}\n"

    fd, cnf_path = tempfile.mkstemp(suffix=".cnf", prefix="dump_")
    os.close(fd)
    with open(cnf_path, "w", encoding="utf-8") as f:
        f.write(content)
    return cnf_path


def main():
    logger = setup_logger()
    logger.info("===== INICIO RESPALDO =====")

    env = get_env(logger)
    db_host = env["host"]
    db_port = env["port"]
    db_user = env["user"]
    db_password = env["password"]
    db_name = env["name"]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dump_exe = find_dump_exe(logger)
    dtype = dump_type(dump_exe)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = OUTPUT_DIR / f"{OUTPUT_PREFIX}_{db_name}_{ts}.sql"

    cnf_path = build_temp_cnf(db_host, db_port, db_user, db_password)

    try:
        cmd = [
            dump_exe,
            f"--defaults-extra-file={cnf_path}",
            "--protocol=tcp",
            "--default-character-set=utf8",
            "--skip-triggers",
            "--routines",
            "--events",
            "--single-transaction",
            "--quick",
        ]

        # ✅ Solo mysqldump MySQL 8 necesita esto para no fallar contra MariaDB
        if dtype == "mysqldump_mysql8":
            cmd.append("--column-statistics=0")

        cmd.append(db_name)
        if TABLES:
            cmd.extend(TABLES)

        logger.info("🟦 Ejecutando respaldo...")
        logger.info(f"Ejecutable: {dump_exe}")
        logger.info(f"Tipo: {dtype}")
        logger.info(f"Host: {db_host}:{db_port}")
        logger.info(f"Usuario: {db_user}")
        logger.info(f"BD: {db_name}")
        logger.info(f"Tablas: {', '.join(TABLES) if TABLES else '(toda la BD)'}")
        logger.info(f"Salida: {out_file}")

        with open(out_file, "w", encoding="utf-8", newline="") as f:
            r = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)

        if r.returncode != 0:
            err = (r.stderr or "").strip()
            die(logger, f"Falló el respaldo (exitcode {r.returncode}).\nDetalle:\n{err}")

        logger.info(f"✅ Respaldo terminado correctamente: {out_file}")
        logger.info("===== FIN RESPALDO OK =====")

    finally:
        try:
            os.remove(cnf_path)
        except Exception:
            pass


if __name__ == "__main__":
    main()