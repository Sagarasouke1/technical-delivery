CREATE OR REPLACE VIEW `vw_mb_conciliacion_fact_vs_conta_2026` AS
WITH
    facturacion
    AS
    (
        SELECT
            d.`Referencia
    ` AS `referencia`,
        d.`tipo_operacion` AS `tipo_operacion`,
        CAST
(d.`fecha_ingreso` AS DATE) AS `fecha_factura`,
        SUM
(IFNULL
(d.`Total_Correcto`, 0)) AS `total_facturado`
    FROM `analytics_aeo`.`dm_factura_electronica_totales` d
    WHERE YEAR
(d.`fecha_ingreso`) = 2026
    GROUP BY
        d.`Referencia`,
        d.`tipo_operacion`,
        CAST
(d.`fecha_ingreso` AS DATE)
),
contabilidad AS
(
    SELECT
    cpi.`referencia
` AS `referencia`,
        CAST
(cpi.`fecha_creacion` AS DATE) AS `fecha_contable`,
        SUM
(IFNULL
(cpi.`abono`, 0)) AS `total_contabilizado`
    FROM `analytics_aeo`.`cont_polizadet_ingresos_2026` cpi
    WHERE IFNULL
(cpi.`abono`, 0) <> 0
    GROUP BY
        cpi.`referencia`,
        CAST
(cpi.`fecha_creacion` AS DATE)
),
fact_vs_conta AS
(
    SELECT
    f.`referencia
`,
        f.`tipo_operacion`,
        f.`fecha_factura`,
        c.`fecha_contable`,
        f.`total_facturado`,
        IFNULL
(c.`total_contabilizado`, 0) AS `total_contabilizado`,
        f.`total_facturado` - IFNULL
(c.`total_contabilizado`, 0) AS `diferencia`,
        CASE
            WHEN c.`referencia` IS NULL THEN 'NO CONTABILIZADO'
            WHEN ABS
(f.`total_facturado` - c.`total_contabilizado`) < 1 THEN 'CUADRADO'
            ELSE 'DIFERENCIA'
END AS `estatus`
    FROM facturacion f
    LEFT JOIN contabilidad c
        ON c.`referencia` = f.`referencia`
       AND SIGN
(c.`total_contabilizado`) = SIGN
(f.`total_facturado`)
)
SELECT
    fvc.`referencia`,
    fvc.`tipo_operacion`,
    fvc.`fecha_factura
`,
    fvc.`fecha_contable`,
    fvc.`total_facturado`,
    fvc.`total_contabilizado`,
    fvc.`diferencia`,
    fvc.`estatus`
FROM fact_vs_conta fvc

UNION ALL

SELECT
    c.`referencia`,
    NULL,
    NULL,
    c.`fecha_contable`,
    0,
    c.`total_contabilizado`,
    0 - c.`total_contabilizado
`,
    'SOLO CONTABILIDAD'
FROM contabilidad c
LEFT JOIN facturacion f
    ON f.`referencia` = c.`referencia`
WHERE f.`referencia` IS NULL;