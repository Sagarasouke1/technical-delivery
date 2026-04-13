CREATE OR REPLACE VIEW vw_reporte_comercial_ventas_2026 AS
SELECT
    t.referencia,
    t.tipo_operacion,
    NULL AS cliente,
    t.fecha_factura,
    t.fecha_contable,
    t.total_facturado,
    t.total_contabilizado,
    t.diferencia,
    CASE
        WHEN t.estatus = 'CUADRADO' THEN 'CONCILIADO'
        ELSE t.estatus
    END AS estatus_conciliacion,
    MONTH(COALESCE(t.fecha_factura, t.fecha_contable)) AS mes_num,
    YEAR(COALESCE(t.fecha_factura, t.fecha_contable)) AS anio
FROM tb_mb_conciliacion_fact_vs_conta_2026 t;

CREATE TABLE IF NOT EXISTS tb_reporte_comercial_ventas_2026 (
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
    anio SMALLINT NULL,
    fecha_carga DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_referencia (referencia),
    INDEX idx_tipo_operacion (tipo_operacion),
    INDEX idx_cliente (cliente),
    INDEX idx_fecha_factura (fecha_factura),
    INDEX idx_fecha_contable (fecha_contable),
    INDEX idx_estatus (estatus_conciliacion)
);

INSERT INTO tb_reporte_comercial_ventas_2026 (
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
    anio
)
SELECT
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
    anio
FROM vw_reporte_comercial_ventas_2026;