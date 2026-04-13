# Test Plan - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir el plan de pruebas funcionales, técnicas y analíticas del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Alcance de Pruebas
- extracción de facturación
- extracción de contabilidad
- carga auxiliar desde Excel
- vista de conciliación
- persistencia analítica
- consumo en BI
- proceso de respaldo

---

## 3. Casos de Prueba Principales

### TP-01 Extracción de facturación
**Objetivo:** validar que la información de facturación se cargue correctamente.  
**Resultado esperado:** registros insertados/actualizados en `dm_factura_electronica_totales`.

### TP-02 Extracción de contabilidad
**Objetivo:** validar que la información contable se cargue correctamente.  
**Resultado esperado:** registros insertados/actualizados en `cont_polizadet_ingresos_2026`.

### TP-03 Carga de Excel
**Objetivo:** validar que el auxiliar contable se procese correctamente.  
**Resultado esperado:** registros cargados en `cont_polizadet_ingresos_original_2026`.

### TP-04 Vista de conciliación
**Objetivo:** validar cálculo de total facturado, total contabilizado, diferencia y estatus.  
**Resultado esperado:** conciliación consistente por referencia.

### TP-05 Persistencia BI
**Objetivo:** validar que la tabla final refleje correctamente la vista.  
**Resultado esperado:** datos consistentes y consultables desde Metabase.

### TP-06 Filtros en dashboard
**Objetivo:** validar filtros de Operación, Cliente y Rango de Fechas.  
**Resultado esperado:** filtrado correcto conforme a datos disponibles.

### TP-07 Respaldo
**Objetivo:** validar la generación del dump de respaldo.  
**Resultado esperado:** archivo de salida correctamente generado y log registrado.

---

## 4. Criterios de Aceptación
- ETL ejecuta sin error crítico
- datos cargados en tablas destino
- conciliación consistente
- persistencia BI funcional
- dashboard consultable
- respaldo exitoso

---

## 5. Evidencias Requeridas
- logs de ejecución
- capturas de consultas
- capturas de dashboard
- evidencia de dump
- validación por negocio