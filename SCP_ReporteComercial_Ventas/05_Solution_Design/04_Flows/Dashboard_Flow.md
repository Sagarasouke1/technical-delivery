# Dashboard Flow - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar el flujo de consumo del dashboard del proyecto SCP_ReporteComercial_Ventas, desde la capa analítica persistida hasta la visualización final en Metabase.

---

## 2. Propósito del Dashboard
El dashboard tiene como finalidad permitir la revisión de la conciliación entre facturación y contabilidad, ayudando a identificar diferencias y apoyar el análisis operativo y financiero.

---

## 3. Fuente Actual del Dashboard

### Fuente oficial actual
El dashboard consume actualmente la tabla:

- `analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026`

### Origen de la tabla
Esta tabla se genera a partir de:

- `analytics_aeo.vw_mb_conciliacion_fact_vs_conta_2026`

### Forma de generación
Actualmente la tabla se genera manualmente mediante query.

---

## 4. Datos que alimentan el Dashboard
La tabla actual contiene al menos los siguientes elementos de análisis:

- referencia
- tipo_operacion
- fecha_factura
- fecha_contable
- total_facturado
- total_contabilizado
- diferencia
- estatus
- mes_num
- mes

---

## 5. Flujo Actual del Dashboard

```text
ZAM / SQL Server
   ↓
ETLs Python
   ↓
Tablas analíticas base
   ├── dm_factura_electronica_totales
   └── cont_polizadet_ingresos_2026
   ↓
vw_mb_conciliacion_fact_vs_conta_2026
   ↓
tb_mb_conciliacion_fact_vs_conta_2026
   ↓
Metabase Dashboard

```

---

## 6. Filtros del Dashboard

### Filtros actualmente soportados o parcialmente soportados

Operación
Rango de fechas
Mes
Estatus
Referencia

### Filtro esperado pero aún no disponible

Cliente

### Observación:
El filtro por Cliente está definido como necesidad del proyecto, pero aún no existe en la capa analítica actual.

---

## 7. Revisión Actual del Dashboard

El enfoque operativo actual del dashboard está orientado a:

* revisión por mes completo
* comparación de facturado vs contabilizado
* identificación de diferencias
* revisión de registros contabilizados

---

## 8. Limitaciones Actuales del Dashboard
* depende de una tabla que se genera manualmente
no cuenta aún con Cliente
* la revisión está más orientada a mes completo que a día a día
* no existe aún una capa final comercial desacoplada de la conciliación técnica
*depende de que la tabla persistida se mantenga actualizada manualmente

---

## 9. Flujo Objetivo Recomendado

### Modelo recomendado a futuro

```text
vw_mb_conciliacion_fact_vs_conta_2026
        ↓
tb_mb_conciliacion_fact_vs_conta_2026
        ↓
tb_reporte_comercial_ventas_2026
        ↓
Metabase
```

### Beneficios del modelo futuro
* mejor separación entre lógica técnica y consumo comercial
* posibilidad de incorporar Cliente
* renombre de estatus a lenguaje más ejecutivo
* mejora en filtros y visualizaciones
* menor dependencia de cambios directos sobre la tabla técnica

---

## 10. Dependencias del Dashboard
* disponibilidad de ETLs
* disponibilidad de vista de conciliación
* actualización manual de tabla persistida
* disponibilidad de Metabase
* disponibilidad del ambiente correspondiente
* consistencia de datos

---

## 11. Riesgos del Dashboard
* datos desactualizados si no se ejecuta la persistencia manual
* limitación funcional por falta de Cliente
* dependencia operativa del usuario técnico que ejecuta el query
* posibles diferencias entre vista y tabla si no se regeneran oportunamente

---