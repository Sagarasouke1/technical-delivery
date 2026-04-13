# Test Cases - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir los casos de prueba funcionales, técnicos y operativos del proyecto SCP_ReporteComercial_Ventas para validar la extracción, transformación, carga, conciliación, persistencia y consumo en BI.

---

## 2. Alcance
Estos casos de prueba cubren:

- extracción de facturación
- extracción de contabilidad
- carga auxiliar desde Excel
- vista de conciliación
- persistencia de conciliación
- dashboard en Metabase
- respaldo
- validación por ambientes DEV, QA y PROD

---

## 3. Casos de Prueba

---

## TC-001 Validar extracción de facturación

**Objetivo:**  
Validar que el proceso de facturación extraiga datos desde ZAM y los cargue correctamente en `dm_factura_electronica_totales`.

**Precondiciones:**  
- SQL Server disponible  
- MySQL disponible  
- `.env` configurado  
- `FacturacionElectronica.sql` disponible  
- `FacturacionElectronica.py` disponible  

**Pasos:**  
1. Ejecutar `FacturacionElectronica.py`
2. Verificar conexión a SQL Server
3. Verificar conexión a MySQL
4. Verificar que el query se lea correctamente
5. Verificar creación o existencia de tabla destino
6. Validar inserción por lotes
7. Revisar log de salida

**Resultado esperado:**  
- El proceso termina sin error crítico
- Los registros quedan insertados o actualizados en `dm_factura_electronica_totales`
- El log muestra tiempo de ejecución y total procesado

**Criterio de aceptación:**  
Carga correcta y log generado.

---

## TC-002 Validar extracción de contabilidad

**Objetivo:**  
Validar que el proceso contable extraiga datos desde ZAM y los cargue correctamente en `cont_polizadet_ingresos_2026`.

**Precondiciones:**  
- SQL Server disponible  
- MySQL disponible  
- `.env` configurado  
- `PolizaContableIngresos.sql` disponible  
- `PolizaContableIngresos.py` disponible  

**Pasos:**  
1. Ejecutar `PolizaContableIngresos.py`
2. Validar conectividad a SQL Server
3. Validar conectividad a MySQL
4. Verificar lectura del query
5. Validar creación o existencia de tabla destino
6. Validar batches insertados
7. Revisar log

**Resultado esperado:**  
- El proceso termina correctamente
- Los datos quedan en `cont_polizadet_ingresos_2026`
- El log muestra resumen final con registros procesados

**Criterio de aceptación:**  
Carga correcta y evidencia operativa.

---

## TC-003 Validar carga auxiliar desde Excel

**Objetivo:**  
Validar que los archivos Excel se procesen correctamente y se carguen en `cont_polizadet_ingresos_original_2026`.

**Precondiciones:**  
- carpeta Excel disponible  
- archivo(s) válidos `.xlsx`  
- hoja `Auxiliar Cuentas` presente  
- `.env` configurado  
- `PolizaIngresosExcel.py` disponible  

**Pasos:**  
1. Colocar archivo Excel en carpeta de entrada
2. Ejecutar `PolizaIngresosExcel.py`
3. Validar lectura de hoja
4. Validar existencia de columnas requeridas
5. Verificar renombre de columnas
6. Verificar conversión de fechas y montos
7. Verificar inserción en tabla destino

**Resultado esperado:**  
- El Excel es leído correctamente
- Los datos quedan insertados en `cont_polizadet_ingresos_original_2026`
- No hay error crítico en estructura ni tipos

**Criterio de aceptación:**  
Carga correcta del auxiliar.

---

## TC-004 Validar lógica de conciliación

**Objetivo:**  
Validar que la vista `vw_mb_conciliacion_fact_vs_conta_2026` compare correctamente facturación y contabilidad.

**Precondiciones:**  
- `dm_factura_electronica_totales` poblada  
- `cont_polizadet_ingresos_2026` poblada  
- vista creada  

**Pasos:**  
1. Ejecutar consulta a `vw_mb_conciliacion_fact_vs_conta_2026`
2. Validar presencia de `referencia`
3. Validar `total_facturado`
4. Validar `total_contabilizado`
5. Validar cálculo de `diferencia`
6. Validar estatus generado

**Resultado esperado:**  
- La vista devuelve datos
- Los cálculos son consistentes
- Los estatus corresponden a la lógica implementada

**Criterio de aceptación:**  
La conciliación funciona correctamente.

---

## TC-005 Validar persistencia de conciliación

**Objetivo:**  
Validar que `tb_mb_conciliacion_fact_vs_conta_2026` se llene correctamente con base en la vista `vw_mb_conciliacion_fact_vs_conta_2026`.

**Precondiciones:**  
- vista de conciliación disponible  
- tabla persistida existente  

**Pasos:**  
1. Ejecutar el proceso de llenado de la tabla persistida
2. Consultar conteo de registros en la vista
3. Consultar conteo de registros en la tabla
4. Comparar resultados
5. Validar muestra aleatoria de registros

**Resultado esperado:**  
- La tabla se llena correctamente
- La tabla refleja el resultado esperado de la vista

**Criterio de aceptación:**  
Consistencia entre vista y tabla persistida.

---

## TC-006 Validar consumo en Metabase

**Objetivo:**  
Validar que Metabase consuma correctamente `tb_mb_conciliacion_fact_vs_conta_2026`.

**Precondiciones:**  
- tabla persistida poblada  
- conexión Metabase configurada  

**Pasos:**  
1. Abrir dashboard en Metabase
2. Validar carga de resultados
3. Aplicar filtro por operación
4. Aplicar filtro por rango de fechas
5. Validar consulta de muestra
6. Confirmar comportamiento esperado

**Resultado esperado:**  
- El dashboard carga sin error
- Los datos visibles son consistentes
- Los filtros activos funcionan

**Criterio de aceptación:**  
Consulta y visualización correctas.

---

## TC-007 Validar restricción actual de Cliente

**Objetivo:**  
Validar que la ausencia actual del campo Cliente quede documentada y controlada.

**Precondiciones:**  
- modelo actual vigente  
- dashboard o diseño BI en revisión  

**Pasos:**  
1. Revisar estructura de tabla fuente BI
2. Confirmar que no existe campo Cliente
3. Verificar que el gap quede documentado
4. Verificar que no se publique funcionalidad no soportada

**Resultado esperado:**  
- Se reconoce que Cliente aún no está integrado
- El gap queda documentado como mejora futura

**Criterio de aceptación:**  
Gap controlado y documentado.

---

## TC-008 Validar respaldo

**Objetivo:**  
Validar que el proceso `BackupMariadb.py` genere respaldo de la tabla principal.

**Precondiciones:**  
- `.env` configurado  
- utilitario `mariadb-dump` o `mysqldump` disponible  
- permisos de escritura en ruta de salida  

**Pasos:**  
1. Ejecutar `BackupMariadb.py`
2. Validar identificación de ejecutable
3. Validar selección de tabla
4. Validar generación de archivo `.sql`
5. Revisar log

**Resultado esperado:**  
- Se genera respaldo correctamente
- El archivo queda en la ruta configurada
- El log refleja resultado exitoso

**Criterio de aceptación:**  
Respaldo correcto.

---

## TC-009 Validar promoción por ambientes

**Objetivo:**  
Validar que los cambios sigan la ruta DEV → QA → PROD.

**Precondiciones:**  
- existencia de ambientes  
- artefactos listos para promoción  

**Pasos:**  
1. Validar despliegue en DEV
2. Validar evidencia en DEV
3. Promover a QA
4. Validar en QA
5. Autorizar promoción a PROD
6. Validar en PROD

**Resultado esperado:**  
- Ningún cambio pasa directo a PROD
- La promoción queda controlada

**Criterio de aceptación:**  
Flujo de promoción correcto.

---

## TC-010 Validar bloqueo por indisponibilidad de DEV

**Objetivo:**  
Validar el impacto operativo cuando DEV no está disponible.

**Precondiciones:**  
- ambiente DEV apagado o indisponible  

**Pasos:**  
1. Confirmar indisponibilidad de DEV
2. Revisar si existe solicitud de habilitación
3. Confirmar documentación del bloqueo
4. Validar impacto en desarrollo y pruebas

**Resultado esperado:**  
- El bloqueo queda registrado
- Se identifica impacto en proyecto
- Se documenta seguimiento

**Criterio de aceptación:**  
Dependencia técnica correctamente documentada.

---

## 4. Evidencias Esperadas
- logs de ejecución
- capturas de consultas SQL
- capturas de tablas
- capturas de dashboard
- evidencia de respaldo
- evidencia de validación por ambiente

---

## 5. Observaciones
Estos casos de prueba deberán evolucionar cuando:
- se integre Cliente
- se implementen tablas de control ETL
- se agregue staging
- se formalice la capa final BI comercial