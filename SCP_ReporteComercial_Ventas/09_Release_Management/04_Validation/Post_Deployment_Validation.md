# Post Deployment Validation - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir las validaciones obligatorias después del despliegue de cambios en el proyecto SCP_ReporteComercial_Ventas.

---

## 2. Alcance
Aplica para:
- scripts Python
- vistas SQL
- tablas analíticas
- tablas de control ETL
- dashboard en Metabase

---

## 3. Validación por Ambiente

### 3.1 DEV
Validar:
- creación correcta de objetos
- ejecución de queries
- ejecución de scripts Python
- creación de logs
- estructura de tablas
- funcionamiento técnico sin error

### 3.2 QA
Validar:
- resultados consistentes
- conteos de registros
- conciliación correcta
- estatus correctos
- funcionamiento del dashboard
- aceptación técnica previa a PROD

### 3.3 PROD
Validar:
- datos visibles en capa final
- estabilidad del proceso
- consumo correcto en Metabase
- generación de logs y respaldo
- ausencia de error crítico

---

## 4. Checklist de Validación Técnica

### Scripts Python
- [ ] `FacturacionElectronica.py` ejecuta correctamente
- [ ] `PolizaContableIngresos.py` ejecuta correctamente
- [ ] `PolizaIngresosExcel.py` ejecuta correctamente
- [ ] `BackupMariadb.py` ejecuta correctamente

### SQL
- [ ] `FacturacionElectronica.sql` válido
- [ ] `PolizaContableIngresos.sql` válido
- [ ] `vw_mb_conciliacion_fact_vs_conta_2026` creada o actualizada
- [ ] tablas destino disponibles

### Datos
- [ ] `dm_factura_electronica_totales` con datos
- [ ] `cont_polizadet_ingresos_2026` con datos
- [ ] `tb_mb_conciliacion_fact_vs_conta_2026` poblada desde la vista
- [ ] estatus coherentes en conciliación

### BI
- [ ] Metabase consulta la fuente correcta
- [ ] filtros vigentes funcionan
- [ ] resultados visibles

---

## 5. Validaciones Funcionales
- [ ] la comparación facturado vs contabilizado es visible
- [ ] las diferencias son identificables
- [ ] la revisión mensual sigue disponible
- [ ] la capa final no genera error funcional
- [ ] la ausencia de Cliente queda documentada si aún no se integra

---

## 6. Evidencias Requeridas
- captura de tablas
- captura de vista
- logs de ejecución
- captura de dashboard
- evidencia de respaldo
- resultado de validación QA

---

## 7. Bloqueos Potenciales
La falta de disponibilidad de DEV puede impedir validaciones iniciales y retrasar promoción a QA y PROD.

Actualmente DEV se encuentra apagado y existe una solicitud de encendido enviada el **13/04/2026 a las 09:54 AM** a los Ingenieros Oswaldo y Daniela, sin respuesta al momento de esta documentación.

---

## 8. Criterio de Aprobación
El despliegue se considera validado cuando:
- no hay error técnico crítico
- los datos son consistentes
- la tabla persistida fue poblada correctamente
- Metabase consume correctamente la fuente
- QA valida el resultado
- PROD queda estable