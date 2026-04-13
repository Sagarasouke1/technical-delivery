/* =========================================================
   PROYECTO: SCP_ReporteComercial_Ventas
   OBJETIVO:
   Definir scripts base de creación / recreación de objetos
   analíticos principales del modelo actual.
   ========================================================= */

/* =========================================================
   1. TABLA PERSISTIDA DE CONCILIACIÓN (MODELO ACTUAL)
   OBSERVACIÓN:
   Actualmente esta tabla se genera manualmente a partir
   de la vista vw_mb_conciliacion_fact_vs_conta_2026
   ========================================================= */

DROP TABLE IF EXISTS analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026;

CREATE TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026 AS
SELECT 
    *,
    MONTH(fecha_contable) AS mes_num,
    UPPER(MONTHNAME(fecha_contable)) AS mes
FROM analytics_aeo.vw_mb_conciliacion_fact_vs_conta_2026
WHERE fecha_contable IS NOT NULL;

/* =========================================================
   2. ÍNDICES RECOMENDADOS PARA TABLA PERSISTIDA
   ========================================================= */

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_referencia (referencia);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_tipo_operacion (tipo_operacion);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_fecha_factura (fecha_factura);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_fecha_contable (fecha_contable);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_estatus (estatus);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_mes_num (mes_num);

ALTER TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026
ADD INDEX idx_mes (mes);

/* =========================================================
   3. PROPUESTA FUTURA: TABLA FINAL DE REPORTE COMERCIAL
   OBSERVACIÓN:
   Esta tabla se deja como propuesta para desacoplar la
   conciliación técnica de la capa final comercial para BI.
   Actualmente Cliente no existe en el modelo.
   ========================================================= */

CREATE TABLE IF NOT EXISTS analytics_aeo.tb_reporte_comercial_ventas_2026 (
    id BIGINT NOT NULL AUTO_INCREMENT,
    referencia VARCHAR(100) NOT NULL,
    tipo_operacion VARCHAR(100) NULL,
    cliente VARCHAR(150) NULL,
    fecha_factura DATE NULL,
    fecha_contable DATE NULL,
    total_facturado DECIMAL(18,2) NOT NULL DEFAULT 0,
    total_contabilizado DECIMAL(18,2) NOT NULL DEFAULT 0,
    diferencia DECIMAL(18,2) NOT NULL DEFAULT 0,
    estatus_conciliacion VARCHAR(50) NOT NULL,
    mes_num TINYINT NULL,
    mes VARCHAR(20) NULL,
    anio SMALLINT NULL,
    fecha_carga DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_referencia (referencia),
    INDEX idx_tipo_operacion (tipo_operacion),
    INDEX idx_cliente (cliente),
    INDEX idx_fecha_factura (fecha_factura),
    INDEX idx_fecha_contable (fecha_contable),
    INDEX idx_estatus (estatus_conciliacion),
    INDEX idx_mes_num (mes_num),
    INDEX idx_mes (mes),
    INDEX idx_anio (anio)
);

/* =========================================================
   4. PROPUESTA DE CARGA FUTURA A CAPA FINAL BI
   OBSERVACIÓN:
   El campo cliente queda en NULL mientras no exista
   integración real desde origen o dimensión auxiliar.
   ========================================================= */

INSERT INTO analytics_aeo.tb_reporte_comercial_ventas_2026 (
    referencia,
    tipo_operacion,
    cliente,
    fecha_factura,
    fecha_contable,
    total_facturado,
    total_contabilizado,
    diferencia,
    estatus_conciliacion,
    mes_num,
    mes,
    anio
)
SELECT
    referencia,
    tipo_operacion,
    NULL AS cliente,
    fecha_factura,
    fecha_contable,
    total_facturado,
    total_contabilizado,
    diferencia,
    CASE
        WHEN estatus = 'CUADRADO' THEN 'CONCILIADO'
        ELSE estatus
    END AS estatus_conciliacion,
    mes_num,
    mes,
    YEAR(fecha_contable) AS anio
FROM analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026;