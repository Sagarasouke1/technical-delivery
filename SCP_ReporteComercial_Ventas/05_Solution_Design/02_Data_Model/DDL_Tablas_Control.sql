CREATE TABLE IF NOT EXISTS etl_control_ejecucion (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre_proceso VARCHAR(150) NOT NULL,
    fecha_ejecucion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_datos DATE NULL,
    hora_inicio DATETIME NULL,
    hora_fin DATETIME NULL,
    estatus VARCHAR(30) NOT NULL,
    registros_leidos INT DEFAULT 0,
    registros_insertados INT DEFAULT 0,
    registros_actualizados INT DEFAULT 0,
    registros_rechazados INT DEFAULT 0,
    mensaje_resultado VARCHAR(500) NULL,
    origen_datos VARCHAR(150) NULL,
    usuario_ejecucion VARCHAR(100) NULL,
    PRIMARY KEY (id),
    INDEX idx_proceso_fecha (nombre_proceso, fecha_ejecucion),
    INDEX idx_estatus (estatus)
);

CREATE TABLE IF NOT EXISTS etl_log_errores (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre_proceso VARCHAR(150) NOT NULL,
    fecha_evento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_error VARCHAR(100) NULL,
    detalle_error TEXT NOT NULL,
    archivo_origen VARCHAR(255) NULL,
    tabla_afectada VARCHAR(150) NULL,
    referencia VARCHAR(100) NULL,
    stack_trace TEXT NULL,
    estatus_revision VARCHAR(30) DEFAULT 'PENDIENTE',
    PRIMARY KEY (id),
    INDEX idx_proceso_fecha (nombre_proceso, fecha_evento),
    INDEX idx_referencia (referencia),
    INDEX idx_estatus_revision (estatus_revision)
);

CREATE TABLE IF NOT EXISTS ctl_archivos_excel_procesados (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre_archivo VARCHAR(255) NOT NULL,
    ruta_archivo VARCHAR(500) NULL,
    hash_archivo VARCHAR(128) NULL,
    fecha_detectado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_procesado DATETIME NULL,
    estatus_proceso VARCHAR(30) NOT NULL DEFAULT 'PENDIENTE',
    registros_cargados INT DEFAULT 0,
    observaciones VARCHAR(500) NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_archivo_hash (nombre_archivo, hash_archivo),
    INDEX idx_estatus (estatus_proceso)
);

CREATE TABLE IF NOT EXISTS stg_poliza_ingresos_excel (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nombre_archivo VARCHAR(255) NULL,
    fecha_carga DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha DATE NULL,
    poliza VARCHAR(100) NULL,
    partida INT NULL,
    centro_costo VARCHAR(100) NULL,
    referencia VARCHAR(100) NULL,
    concepto_mov VARCHAR(255) NULL,
    saldo_inicial DECIMAL(18,2) NULL,
    cargo DECIMAL(18,2) NULL,
    abono DECIMAL(18,2) NULL,
    saldo_final DECIMAL(18,2) NULL,
    tipo_poliza VARCHAR(100) NULL,
    usuario VARCHAR(100) NULL,
    estatus_validacion VARCHAR(30) DEFAULT 'PENDIENTE',
    motivo_rechazo VARCHAR(500) NULL,
    PRIMARY KEY (id),
    INDEX idx_referencia (referencia),
    INDEX idx_fecha (fecha),
    INDEX idx_estatus_validacion (estatus_validacion)
);