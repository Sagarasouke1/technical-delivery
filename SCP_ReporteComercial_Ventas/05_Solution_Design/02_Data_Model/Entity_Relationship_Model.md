# Entity Relationship Model - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar el modelo entidad-relación lógico y técnico del proyecto SCP_ReporteComercial_Ventas, identificando tablas actuales, relaciones funcionales, llaves de integración y recomendaciones de madurez.

---

## 2. Alcance del Modelo
El modelo actual contempla:

- tablas analíticas de facturación
- tablas analíticas de contabilidad
- tabla analítica auxiliar proveniente de Excel
- vista de conciliación
- tabla persistida para BI
- ambientes DEV, QA y PROD
- tablas de control ETL recomendadas

---

## 3. Entidades Actuales

### 3.1 `dm_factura_electronica_totales`
**Tipo:** tabla analítica  
**Origen:** ETL de facturación  
**Función:** almacenar información facturada para conciliación.

**Campos funcionales relevantes:**
- `Referencia`
- `tipo_operacion`
- `fecha_ingreso`
- `Total_Correcto`
- `status_factura`

**Llave funcional principal:**
- `Referencia`
- complementada por `fecha_ingreso` para UPSERT actual

---

### 3.2 `cont_polizadet_ingresos_2026`
**Tipo:** tabla analítica  
**Origen:** ETL contable  
**Función:** almacenar información contable de ingresos para conciliación.

**Campos funcionales relevantes:**
- `fecha_creacion`
- `poliza`
- `partida`
- `centro_costo`
- `referencia`
- `concepto_mov`
- `cargo`
- `abono`
- `fecha_ingreso`
- `fecha_modifico`

**Llave funcional sugerida por script:**
- `poliza`
- `partida`
- `referencia`
- `concepto_mov`

---

### 3.3 `cont_polizadet_ingresos_original_2026`
**Tipo:** tabla analítica auxiliar  
**Origen:** Excel  
**Función:** resguardar auxiliar contable de carga manual o complementaria.

**Campos funcionales relevantes:**
- `fecha`
- `poliza`
- `partida`
- `centro_costo`
- `referencia`
- `concepto_mov`
- `saldo_inicial`
- `cargo`
- `abono`
- `saldo_final`
- `tipo_poliza`
- `usuario`

**Observación:**
Actualmente opera como tabla destino directa del Excel, pero funcionalmente debería evolucionar a una tabla staging o controlada por proceso ETL.

---

### 3.4 `vw_mb_conciliacion_fact_vs_conta_2026`
**Tipo:** vista lógica  
**Origen:** consolidación de facturación y contabilidad  
**Función:** comparar monto facturado vs monto contabilizado y clasificar el resultado.

**Campos relevantes:**
- `referencia`
- `tipo_operacion`
- `fecha_factura`
- `fecha_contable`
- `total_facturado`
- `total_contabilizado`
- `diferencia`
- `estatus`

**Relación funcional:**
- conecta `dm_factura_electronica_totales` con `cont_polizadet_ingresos_2026` por `referencia`

---

### 3.5 `tb_mb_conciliacion_fact_vs_conta_2026`
**Tipo:** tabla persistida BI  
**Origen:** materialización de la vista `vw_mb_conciliacion_fact_vs_conta_2026`  
**Función:** servir como fuente oficial actual para consultas en Metabase.

**Observación:**
Esta tabla sí existe físicamente y se llena con base en el resultado de la vista.

---

## 4. Relaciones Actuales del Modelo

### Relación 1
`dm_factura_electronica_totales` → `vw_mb_conciliacion_fact_vs_conta_2026`

**Tipo de relación:** lógica  
**Llave:** `Referencia` → `referencia`  
**Propósito:** aportar monto facturado y operación

---

### Relación 2
`cont_polizadet_ingresos_2026` → `vw_mb_conciliacion_fact_vs_conta_2026`

**Tipo de relación:** lógica  
**Llave:** `referencia`  
**Propósito:** aportar monto contabilizado

---

### Relación 3
`vw_mb_conciliacion_fact_vs_conta_2026` → `tb_mb_conciliacion_fact_vs_conta_2026`

**Tipo de relación:** persistencia  
**Propósito:** materializar el resultado para BI

---

### Relación 4
`cont_polizadet_ingresos_original_2026`

**Tipo de relación actual:** auxiliar / complementaria  
**Propósito:** servir de apoyo contable para validaciones o conciliaciones complementarias

---

## 5. Modelo Lógico Actual

```text
dm_factura_electronica_totales
        └─────┐
              │ referencia
              ▼
     vw_mb_conciliacion_fact_vs_conta_2026
              ▲
              │ referencia
        ┌─────┘
cont_polizadet_ingresos_2026

cont_polizadet_ingresos_original_2026
        │
        └── apoyo / validación auxiliar

vw_mb_conciliacion_fact_vs_conta_2026
        │
        ▼
tb_mb_conciliacion_fact_vs_conta_2026
        │
        ▼
Metabase

```
---

## 6. Limitaciones del Modelo Actual

1. No existe dimensión Cliente
1. No existe staging formal para Excel
1. No existe control ETL en BD
1. No existe tabla formal de archivos procesados
1. No existe entidad final comercial separada de la conciliación técnica
1. La tabla auxiliar Excel aún no está completamente integrada al modelo principal

---

## 7. Entidades Recomendadas para Madurez

### 7.1 etl_control_ejecucion

Función: registrar cada corrida ETL
Beneficio: trazabilidad, auditoría, monitoreo

### 7.2 etl_log_errores

Función: registrar errores técnicos y funcionales
Beneficio: soporte, RCA, control operativo

### 7.3 ctl_archivos_excel_procesados

Función: controlar archivos Excel cargados
Beneficio: evitar reprocesos, duplicados y pérdida de trazabilidad

### 7.4 stg_poliza_ingresos_excel

Función: staging previo a carga final
Beneficio: limpieza, validación y control

### 7.5 tb_reporte_comercial_ventas_2026

Función: capa final de negocio para Metabase
Beneficio: desacoplar conciliación técnica de capa comercial

---

## 8. Modelo Objetivo Recomendado

```
ZAM / Facturación
   ↓
dm_factura_electronica_totales

ZAM / Contabilidad
   ↓
cont_polizadet_ingresos_2026

Excel
   ↓
stg_poliza_ingresos_excel
   ↓
cont_polizadet_ingresos_original_2026

dm_factura_electronica_totales
        └─────┐
              │ referencia
              ▼
     vw_mb_conciliacion_fact_vs_conta_2026
              ▲
              │ referencia
        ┌─────┘
cont_polizadet_ingresos_2026

vw_mb_conciliacion_fact_vs_conta_2026
        │
        ▼
tb_mb_conciliacion_fact_vs_conta_2026
        │
        ▼
tb_reporte_comercial_ventas_2026
        │
        ▼
Metabase

etl_control_ejecucion
etl_log_errores
ctl_archivos_excel_procesados

```
---

## 9. Llaves de Integración

### Llave principal de conciliación

* referencia

### Llaves complementarias

* tipo_operacion
* fecha_factura
* fecha_contable

### Dimensión pendiente

* cliente

### Observación:

Actualmente no existe la dimensión Cliente en el modelo actual, por lo que su integración queda documentada como mejora futura necesaria para cubrir completamente los filtros esperados del dashboard.

---

## 10. Ambientes

El modelo y sus objetos deben gestionarse y validarse en los siguientes ambientes:

* DEV
* QA
* PROD

Todo cambio estructural debe promoverse de forma controlada entre estos ambientes.

---