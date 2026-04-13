# Checklist de Validación Técnica - SCP_ReporteComercial_Ventas

## 1. Objetivo
Validar que el componente SCP_ReporteComercial_Ventas cumpla con los requisitos técnicos mínimos para su operación, validación y promoción entre ambientes.

---

## 2. Checklist General de Componentes

### Estructura del proyecto
- [ ] Existe README del proyecto
- [ ] Existe Project Status
- [ ] Existe Version Control
- [ ] Existe documentación técnica base
- [ ] Existe documentación de riesgos y dependencias

### Scripts Python
- [ ] Existe `FacturacionElectronica.py`
- [ ] Existe `PolizaContableIngresos.py`
- [ ] Existe `PolizaIngresosExcel.py`
- [ ] Existe `BackupMariadb.py`

### Queries SQL
- [ ] Existe `FacturacionElectronica.sql`
- [ ] Existe `PolizaContableIngresos.sql`
- [ ] Existe `vw_mb_conciliacion_fact_vs_conta_2026.sql`

---

## 3. Validación de Configuración

### `.env`
- [ ] Existe estructura `.env` definida
- [ ] El `.env` contiene variables de SQL Server
- [ ] El `.env` contiene variables de MySQL / MariaDB
- [ ] El `.env` contiene configuración de batch
- [ ] El `.env` contiene rutas requeridas
- [ ] No se exponen credenciales reales en documentación

### Conectividad
- [ ] Existe conectividad a SQL Server
- [ ] Existe conectividad a MySQL / MariaDB
- [ ] Existen permisos mínimos requeridos
- [ ] Las rutas técnicas están disponibles

---

## 4. Validación de ETL de Facturación
- [ ] `FacturacionElectronica.py` ejecuta sin error crítico
- [ ] El query de facturación se lee correctamente
- [ ] La tabla destino existe o se crea correctamente
- [ ] La carga por lotes funciona
- [ ] El log se genera correctamente
- [ ] Los registros quedan disponibles en `dm_factura_electronica_totales`

---

## 5. Validación de ETL de Contabilidad
- [ ] `PolizaContableIngresos.py` ejecuta sin error crítico
- [ ] El query contable se lee correctamente
- [ ] La tabla destino existe o se crea correctamente
- [ ] La carga por lotes funciona
- [ ] El log se genera correctamente
- [ ] Los registros quedan disponibles en `cont_polizadet_ingresos_2026`

---

## 6. Validación de Carga desde Excel
- [ ] La carpeta de Excel existe
- [ ] Los archivos `.xlsx` son detectados
- [ ] La hoja `Auxiliar Cuentas` existe
- [ ] Las columnas requeridas existen
- [ ] La conversión de fechas funciona
- [ ] La conversión de montos funciona
- [ ] La carga queda disponible en `cont_polizadet_ingresos_original_2026`

---

## 7. Validación de Vista de Conciliación
- [ ] La vista `vw_mb_conciliacion_fact_vs_conta_2026` existe
- [ ] La vista devuelve datos
- [ ] El campo `referencia` está presente
- [ ] El campo `total_facturado` está presente
- [ ] El campo `total_contabilizado` está presente
- [ ] El campo `diferencia` está presente
- [ ] El campo `estatus` está presente
- [ ] La lógica de conciliación es consistente

---

## 8. Validación de Tabla Persistida
- [ ] La tabla `tb_mb_conciliacion_fact_vs_conta_2026` existe
- [ ] La tabla se genera con base en la vista
- [ ] Incluye `mes_num`
- [ ] Incluye `mes`
- [ ] Se aplica `WHERE fecha_contable IS NOT NULL`
- [ ] Los conteos son consistentes respecto de la vista
- [ ] La tabla es apta para consumo en BI

---

## 9. Validación de Respaldo
- [ ] `BackupMariadb.py` ejecuta correctamente
- [ ] El ejecutable `mariadb-dump` o `mysqldump` está disponible
- [ ] El archivo de respaldo se genera
- [ ] El log de respaldo se genera
- [ ] Existe ruta de salida válida

---

## 10. Validación por Ambientes

### DEV
- [ ] Ambiente DEV disponible
- [ ] Validaciones técnicas ejecutadas
- [ ] Evidencia mínima generada

### QA
- [ ] Ambiente QA disponible
- [ ] Validación técnica completada
- [ ] Validación funcional completada

### PROD
- [ ] Ambiente PROD disponible
- [ ] Cambio promovido desde QA
- [ ] Respaldo previo realizado
- [ ] Validación posterior ejecutada

---

## 11. Validación de Dependencias y Bloqueos
- [ ] Dependencias técnicas documentadas
- [ ] Riesgos documentados
- [ ] Bloqueos operativos documentados
- [ ] Estado actual de DEV documentado
- [ ] Seguimiento a solicitud de encendido documentado

---

## 12. Observaciones Técnicas Actuales
- [ ] Cliente se documenta como dimensión pendiente
- [ ] Persistencia manual de tabla de conciliación documentada
- [ ] Tablas de control ETL documentadas como mejora futura
- [ ] Staging de Excel documentado como mejora futura

---

## 13. Criterio de Aprobación Técnica
La validación técnica se considera satisfactoria cuando:
- no existen errores críticos
- la extracción y carga operan correctamente
- la conciliación es consistente
- la tabla persistida es utilizable
- la evidencia técnica es suficiente