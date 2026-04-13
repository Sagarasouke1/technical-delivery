# Source to Target Mapping - SCP_ReporteComercial_Ventas

## 1. Facturación

| Fuente | Campo fuente | Transformación | Destino | Campo destino |
|-------|--------------|----------------|---------|---------------|
| trafico_factura_electronica / joins relacionados | num_guia | Alias | dm_factura_electronica_totales | Referencia |
| desp_tipooperacion y relaciones derivadas | tipo_operacion | COALESCE | dm_factura_electronica_totales | tipo_operacion |
| trafico_factura_electronica | fecha_ingreso / fecha_solicitud_cancelacion | CASE según cancelación | dm_factura_electronica_totales | fecha_ingreso |
| trafico_nota_cargo / trafico_guia / trafico_nota_credito | montos y subtotal * tipo_cambio | cálculo de total con ajuste de signo | dm_factura_electronica_totales | Total_Correcto |
| trafico_factura_electronica | accion, status, status_cancel | clasificación por CASE | dm_factura_electronica_totales | status_factura |

---

## 2. Contabilidad

| Fuente | Campo fuente | Transformación | Destino | Campo destino |
|-------|--------------|----------------|---------|---------------|
| cont_poliza | fecha_creacion | directo | cont_polizadet_ingresos_2026 | fecha_creacion |
| cont_poliza | identificador_poliza | alias | cont_polizadet_ingresos_2026 | poliza |
| cont_polizadet | num_partida | alias | cont_polizadet_ingresos_2026 | partida |
| cont_polizadet | centrocosto | renombre | cont_polizadet_ingresos_2026 | centro_costo |
| cont_polizadet | referencia | directo | cont_polizadet_ingresos_2026 | referencia |
| cont_polizadet | concepto_individual | renombre | cont_polizadet_ingresos_2026 | concepto_mov |
| cont_polizadet | mm_cargo | alias | cont_polizadet_ingresos_2026 | cargo |
| cont_polizadet | mm_abono | alias | cont_polizadet_ingresos_2026 | abono |
| cont_poliza | fecha_ingreso | directo | cont_polizadet_ingresos_2026 | fecha_ingreso |
| cont_poliza | fecha_modifico | directo | cont_polizadet_ingresos_2026 | fecha_modifico |

---

## 3. Excel auxiliar

| Fuente | Campo fuente | Transformación | Destino | Campo destino |
|-------|--------------|----------------|---------|---------------|
| Auxiliar Cuentas | Fecha | renombre y conversión fecha | cont_polizadet_ingresos_original_2026 | fecha |
| Auxiliar Cuentas | Póliza | renombre | cont_polizadet_ingresos_original_2026 | poliza |
| Auxiliar Cuentas | Partida | cast numérico | cont_polizadet_ingresos_original_2026 | partida |
| Auxiliar Cuentas | Centro Costo | renombre | cont_polizadet_ingresos_original_2026 | centro_costo |
| Auxiliar Cuentas | Referencia | renombre | cont_polizadet_ingresos_original_2026 | referencia |
| Auxiliar Cuentas | Concepto Mov. | renombre | cont_polizadet_ingresos_original_2026 | concepto_mov |
| Auxiliar Cuentas | Saldo Inicial | conversión decimal | cont_polizadet_ingresos_original_2026 | saldo_inicial |
| Auxiliar Cuentas | Cargo | conversión decimal | cont_polizadet_ingresos_original_2026 | cargo |
| Auxiliar Cuentas | Abono | conversión decimal | cont_polizadet_ingresos_original_2026 | abono |
| Auxiliar Cuentas | Saldo Final | conversión decimal | cont_polizadet_ingresos_original_2026 | saldo_final |
| Auxiliar Cuentas | Tipo Póliza | renombre | cont_polizadet_ingresos_original_2026 | tipo_poliza |
| Auxiliar Cuentas | Usuario | renombre | cont_polizadet_ingresos_original_2026 | usuario |

---

## 4. Conciliación

| Fuente | Campo fuente | Transformación | Destino | Campo destino |
|-------|--------------|----------------|---------|---------------|
| dm_factura_electronica_totales | Referencia | agrupación | vw_mb_conciliacion_fact_vs_conta_2026 | referencia |
| dm_factura_electronica_totales | tipo_operacion | agrupación | vw_mb_conciliacion_fact_vs_conta_2026 | tipo_operacion |
| dm_factura_electronica_totales | fecha_ingreso | cast date | vw_mb_conciliacion_fact_vs_conta_2026 | fecha_factura |
| dm_factura_electronica_totales | Total_Correcto | SUM | vw_mb_conciliacion_fact_vs_conta_2026 | total_facturado |
| cont_polizadet_ingresos_2026 | referencia | agrupación | vw_mb_conciliacion_fact_vs_conta_2026 | referencia |
| cont_polizadet_ingresos_2026 | fecha_creacion | cast date | vw_mb_conciliacion_fact_vs_conta_2026 | fecha_contable |
| cont_polizadet_ingresos_2026 | abono | SUM | vw_mb_conciliacion_fact_vs_conta_2026 | total_contabilizado |
| lógica de vista | total_facturado - total_contabilizado | cálculo | vw_mb_conciliacion_fact_vs_conta_2026 | diferencia |
| lógica de vista | CASE | clasificación | vw_mb_conciliacion_fact_vs_conta_2026 | estatus |