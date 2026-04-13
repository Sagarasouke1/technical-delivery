DECLARE @Inicio date = DATEFROMPARTS(YEAR(GETDATE()), 1, 1);  -- 01 Enero
DECLARE @Fin    date = DATEFROMPARTS(YEAR(GETDATE()), 5, 1);  -- 01 Abril

;WITH fe10 AS (
    SELECT 
        fe.num_guia,
        fe.accion,
        fe.fecha_ingreso,
        fe.fecha_solicitud_cancelacion,
        fe.status,
        fe.status_cancel
    FROM trafico_factura_electronica fe
    WHERE fe.fecha_ingreso >= @Inicio
      AND fe.fecha_ingreso <  @Fin
      AND fe.tipo_doc <> 6
)
SELECT
    fe10.num_guia AS Referencia,
    COALESCE(dto.tipo_operacion, dto_nc.tipo_operacion, dto_ncr.tipo_operacion) AS tipo_operacion,
    CASE 
        WHEN fe10.accion = 2
         AND fe10.status = 2 
         AND fe10.status_cancel <> 0
        THEN fe10.fecha_solicitud_cancelacion
        ELSE fe10.fecha_ingreso
    END AS fecha_ingreso,
    CASE 
        WHEN fe10.accion = 2 THEN 
            -1 * COALESCE(nc.monto_cargo_total,
                          (tg.subtotal * tg.monto_tipo_cambio),
                          ncr.monto_credito_total)
        ELSE 
            COALESCE(nc.monto_cargo_total,
                     (tg.subtotal * tg.monto_tipo_cambio),
                     ncr.monto_credito_total)
    END AS Total_Correcto,
    CASE 
        WHEN fe10.accion = 2
         AND fe10.status = 2 
         AND fe10.status_cancel <> 0
        THEN 'CANCELADA'
        ELSE 'FACTURACION'
    END AS status_factura
FROM fe10
LEFT JOIN trafico_guia tg
    ON tg.num_guia = fe10.num_guia
LEFT JOIN desp_tipooperacion dto
    ON dto.id_tipo_operacion = tg.id_tipo_operacion
OUTER APPLY (
    SELECT TOP 1 NCC.num_guia AS num_guia_rel
    FROM trafico_nota_cargo NCC
    WHERE NCC.num_ncargo = fe10.num_guia
      AND NCC.status_ncargo <> 'C'
) nc_rel
LEFT JOIN trafico_guia tg_nc
    ON tg_nc.num_guia = nc_rel.num_guia_rel
LEFT JOIN desp_tipooperacion dto_nc
    ON dto_nc.id_tipo_operacion = tg_nc.id_tipo_operacion
OUTER APPLY (
    SELECT TOP 1 NCR.num_guia AS num_guia_rel
    FROM trafico_nota_credito NCR
    WHERE NCR.num_ncredito = fe10.num_guia
      AND NCR.status_ncred <> 'C'
) ncr_rel
LEFT JOIN trafico_guia tg_ncr
    ON tg_ncr.num_guia = ncr_rel.num_guia_rel
LEFT JOIN desp_tipooperacion dto_ncr
    ON dto_ncr.id_tipo_operacion = tg_ncr.id_tipo_operacion
OUTER APPLY (
    SELECT SUM(NCC.monto_cargo) AS monto_cargo_total
    FROM trafico_nota_cargo NCC
    WHERE NCC.num_ncargo = fe10.num_guia
      AND NCC.status_ncargo <> 'C'
) nc
OUTER APPLY (
    SELECT SUM(NCR.monto_credito) AS monto_credito_total
    FROM trafico_nota_credito NCR
    WHERE NCR.num_ncredito = fe10.num_guia
      AND NCR.status_ncred <> 'C'
) ncr
WHERE NOT (
    COALESCE(dto.tipo_operacion, dto_nc.tipo_operacion, dto_ncr.tipo_operacion) IS NULL
    AND
    COALESCE(nc.monto_cargo_total,
             (tg.subtotal * tg.monto_tipo_cambio),
             ncr.monto_credito_total) IS NULL
)
ORDER BY 
    CASE 
        WHEN fe10.accion = 2
         AND fe10.status = 2 
         AND fe10.status_cancel <> 0
        THEN fe10.fecha_solicitud_cancelacion
        ELSE fe10.fecha_ingreso
    END ASC;