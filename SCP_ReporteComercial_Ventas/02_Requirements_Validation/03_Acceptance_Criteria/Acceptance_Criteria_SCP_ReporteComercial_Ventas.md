# Acceptance Criteria - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir los criterios de aceptación funcionales, técnicos y analíticos que deberán cumplirse para considerar válido el componente SCP_ReporteComercial_Ventas.

---

## 2. Alcance de Aceptación
Los criterios de aceptación aplican a:

- extracción de facturación
- extracción de contabilidad
- carga auxiliar desde Excel
- lógica de conciliación
- persistencia de la tabla analítica
- visualización en Metabase
- validación por ambientes

---

## 3. Criterios de Aceptación Funcionales

### AC-01 Comparación principal disponible
El sistema debe permitir comparar el monto facturado contra el monto contabilizado para cada referencia.

**Se considera cumplido cuando:**  
la capa analítica y el dashboard permiten visualizar `total_facturado`, `total_contabilizado` y `diferencia`.

---

### AC-02 Conciliación por referencia
La conciliación debe realizarse utilizando la referencia como llave principal de integración.

**Se considera cumplido cuando:**  
la vista y la tabla persistida muestran resultados consistentes por referencia.

---

### AC-03 Identificación de diferencias
El modelo debe permitir identificar registros conciliados, no contabilizados o con diferencia.

**Se considera cumplido cuando:**  
la vista y la tabla persistida reflejan correctamente el estatus generado por la lógica de conciliación.

---

### AC-04 Revisión por mes completo
La solución debe soportar el enfoque actual de revisión por mes completo.

**Se considera cumplido cuando:**  
la tabla persistida incluye `mes_num` y `mes`, y el dashboard permite consulta mensual.

---

### AC-05 Soporte para operación
El dashboard debe permitir análisis por operación.

**Se considera cumplido cuando:**  
el campo `tipo_operacion` está disponible en la capa analítica y el filtro correspondiente funciona en BI.

---

### AC-06 Soporte para rango de fechas
El dashboard debe permitir análisis por rango de fechas.

**Se considera cumplido cuando:**  
la visualización permite consultar información por fechas disponibles en la tabla persistida.

---

### AC-07 Gap de Cliente documentado
La dimensión Cliente deberá estar identificada como requerimiento del proyecto, aunque no esté disponible en la primera versión.

**Se considera cumplido cuando:**  
la ausencia de Cliente está documentada como limitación actual y mejora futura.

---

## 4. Criterios de Aceptación Técnicos

### AC-10 Extracción de facturación funcional
El proceso `FacturacionElectronica.py` debe ejecutar correctamente y poblar `dm_factura_electronica_totales`.

**Se considera cumplido cuando:**  
el ETL termina sin error crítico, inserta o actualiza registros y genera log.

---

### AC-11 Extracción de contabilidad funcional
El proceso `PolizaContableIngresos.py` debe ejecutar correctamente y poblar `cont_polizadet_ingresos_2026`.

**Se considera cumplido cuando:**  
el ETL termina sin error crítico, inserta o actualiza registros y genera log.

---

### AC-12 Carga auxiliar desde Excel funcional
El proceso `PolizaIngresosExcel.py` debe procesar correctamente los archivos auxiliares y poblar `cont_polizadet_ingresos_original_2026`.

**Se considera cumplido cuando:**  
el archivo es leído, validado, transformado y cargado sin error crítico.

---

### AC-13 Vista de conciliación funcional
La vista `vw_mb_conciliacion_fact_vs_conta_2026` debe calcular correctamente la conciliación.

**Se considera cumplido cuando:**  
devuelve resultados consistentes con `referencia`, `total_facturado`, `total_contabilizado`, `diferencia` y `estatus`.

---

### AC-14 Persistencia de conciliación funcional
La tabla `tb_mb_conciliacion_fact_vs_conta_2026` debe llenarse correctamente a partir del resultado de la vista.

**Se considera cumplido cuando:**  
la tabla refleja el resultado esperado del query manual definido para su generación.

---

### AC-15 Logs de ejecución disponibles
Todos los procesos principales deben generar evidencia operativa en logs.

**Se considera cumplido cuando:**  
existen logs de facturación, contabilidad y respaldo con trazabilidad suficiente.

---

### AC-16 Respaldo funcional
El proceso `BackupMariadb.py` debe generar un respaldo correcto de la tabla de conciliación.

**Se considera cumplido cuando:**  
se genera el archivo de respaldo y queda evidencia en log.

---

## 5. Criterios de Aceptación Analíticos / BI

### AC-20 Fuente BI oficial definida
Metabase debe consumir una fuente oficial de análisis.

**Se considera cumplido cuando:**  
el dashboard consume `tb_mb_conciliacion_fact_vs_conta_2026`.

---

### AC-21 Datos visibles y consistentes
Los datos mostrados en el dashboard deben ser consistentes con la tabla persistida.

**Se considera cumplido cuando:**  
los resultados visibles coinciden con la consulta base.

---

### AC-22 Filtro por operación funcional
El filtro de operación debe funcionar correctamente.

**Se considera cumplido cuando:**  
el usuario puede aplicar operación y observar resultados correctos.

---

### AC-23 Filtro por rango de fechas funcional
El filtro por rango de fechas debe funcionar correctamente dentro de la lógica actual del modelo.

**Se considera cumplido cuando:**  
el usuario puede acotar resultados por fecha disponible.

---

### AC-24 Revisión mensual funcional
El dashboard debe permitir lectura mensual del resultado conciliado.

**Se considera cumplido cuando:**  
`mes_num` y `mes` son utilizables en consultas y visualizaciones.

---

## 6. Criterios de Aceptación por Ambiente

### AC-30 DEV
Todo cambio debe validarse inicialmente en DEV.

### AC-31 QA
Todo cambio debe validarse funcional y técnicamente en QA.

### AC-32 PROD
Solo deben llegar a PROD cambios ya validados en DEV y QA.

**Se considera cumplido cuando:**  
existe evidencia de promoción controlada entre ambientes.

---

## 7. Restricciones Aceptadas
- la primera versión se enfoca en revisión por mes completo
- Cliente no forma parte aún del modelo operativo actual
- la persistencia de la tabla de conciliación es manual
- las tablas de control ETL aún están pendientes de implementación

---

## 8. Criterio General de Aceptación
El componente SCP_ReporteComercial_Ventas se considerará aceptado cuando:
- los ETLs funcionen correctamente
- la conciliación sea consistente
- la tabla persistida esté correctamente generada
- el dashboard muestre resultados válidos
- las limitaciones actuales estén documentadas
- exista evidencia mínima técnica y funcional