# Conciliation Flow - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar el flujo específico de conciliación entre facturación y contabilidad dentro del proyecto SCP_ReporteComercial_Ventas, desde sus fuentes analíticas hasta la persistencia final utilizada por BI.

---

## 2. Propósito del Flujo
El flujo de conciliación permite comparar los importes facturados contra los importes contabilizados, identificar diferencias y generar una capa persistida para su consulta y análisis en Metabase.

---

## 3. Fuentes del Flujo

### 3.1 Fuente de facturación
La facturación es consolidada en:

- `analytics_aeo.dm_factura_electronica_totales`

Esta tabla contiene:
- referencia
- tipo de operación
- fecha de ingreso
- importe facturado correcto
- estatus de factura

---

### 3.2 Fuente de contabilidad
La contabilidad es consolidada en:

- `analytics_aeo.cont_polizadet_ingresos_2026`

Esta tabla contiene:
- fecha contable
- referencia
- póliza
- partida
- centro de costo
- concepto
- cargo
- abono

---

## 4. Lógica de Conciliación

### 4.1 Vista de conciliación
La lógica principal de conciliación se encuentra en:

- `analytics_aeo.vw_mb_conciliacion_fact_vs_conta_2026`

### 4.2 Qué hace la vista
La vista:
1. agrupa facturación por referencia, operación y fecha
2. agrupa contabilidad por referencia y fecha
3. compara importes
4. calcula diferencia
5. asigna estatus

### 4.3 Reglas actuales del estatus
La lógica actual clasifica registros como:

- `NO CONTABILIZADO`
- `CUADRADO`
- `DIFERENCIA`

### 4.4 Llave principal de conciliación
La conciliación se realiza principalmente por:

- `referencia`

### 4.5 Campos resultantes principales
- `referencia`
- `tipo_operacion`
- `fecha_factura`
- `fecha_contable`
- `total_facturado`
- `total_contabilizado`
- `diferencia`
- `estatus`

---

## 5. Persistencia Actual del Resultado

### 5.1 Tabla persistida
La salida de la conciliación se materializa manualmente en:

- `analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026`

### 5.2 Forma actual de llenado
Actualmente la tabla se genera manualmente mediante query directo:

```sql
CREATE TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026 AS
SELECT 
    *,
    MONTH(fecha_contable) AS mes_num,
    UPPER(MONTHNAME(fecha_contable)) AS mes
FROM analytics_aeo.vw_mb_conciliacion_fact_vs_conta_2026
WHERE fecha_contable IS NOT NULL;
```

### 5.3 Observaciones sobre el llenado actual

* el proceso es manual
* la tabla se construye a partir de la vista
* agrega mes_num y mes
* solo se consideran registros con fecha_contable IS NOT NULL

--- 

## 6. Flujo Actual de Conciliación

```text
dm_factura_electronica_totales
        └─────┐
              │
              ▼
vw_mb_conciliacion_fact_vs_conta_2026
              ▲
              │
        ┌─────┘
cont_polizadet_ingresos_2026
              │
              ▼
tb_mb_conciliacion_fact_vs_conta_2026
              │
              ▼
Metabase

```
---

## 7. Limitaciones del Flujo Actual

1. el llenado de la tabla persistida es manual
1. no existe proceso controlado formal para recreación o actualización
1. no existe tabla de control ETL para esta etapa
1. no existe Cliente como dimensión de análisis
1. la persistencia actual depende de fecha_contable IS NOT NULL
1. no se ha formalizado si el proceso debe ser DROP + CREATE, TRUNCATE + INSERT o similar

---

## 8. Riesgos del Flujo Actual
* recreación manual sin trazabilidad formal
posible pérdida de continuidad si no se documenta el * proceso
* dependencia operativa del usuario técnico que ejecuta el query
* impacto en BI si la tabla no se actualiza a tiempo
* inconsistencia si la vista cambia y la tabla persistida no se regenera

---

## 9. Flujo Objetivo Recomendado

### Escenario recomendado

Formalizar la persistencia como un proceso controlado:

1. validar existencia de vista
1. generar respaldo previo
1. limpiar o recrear tabla según estrategia definida
1. poblar tabla persistida
1. registrar ejecución
1. validar conteo y consistencia
1. actualizar dashboard

--- 