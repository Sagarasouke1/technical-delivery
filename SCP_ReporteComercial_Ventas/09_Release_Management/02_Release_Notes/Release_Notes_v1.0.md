# Release Notes - SCP_ReporteComercial_Ventas v1.0

## 1. Información General
**Proyecto:** SCP_ReporteComercial_Ventas  
**Versión:** 1.0  
**Fecha:** 13/04/2026  
**Tipo de liberación:** Inicial documentada / estabilización técnica  
**Ambientes considerados:** DEV, QA, PROD

---

## 2. Resumen de la Liberación
La versión 1.0 formaliza la base técnica y documental del componente SCP_ReporteComercial_Ventas, orientado a la conciliación entre facturación y contabilidad a partir de información proveniente de ZAM, consolidada en base analítica y publicada en Metabase.

---

## 3. Componentes Incluidos

### 3.1 Procesos ETL
- `FacturacionElectronica.py`
- `PolizaContableIngresos.py`
- `PolizaIngresosExcel.py`
- `BackupMariadb.py`

### 3.2 Queries y vista
- `FacturacionElectronica.sql`
- `PolizaContableIngresos.sql`
- `vw_mb_conciliacion_fact_vs_conta_2026.sql`

### 3.3 Tablas analíticas
- `dm_factura_electronica_totales`
- `cont_polizadet_ingresos_2026`
- `cont_polizadet_ingresos_original_2026`
- `tb_mb_conciliacion_fact_vs_conta_2026`

### 3.4 Documentación formal
- README del proyecto
- Project Status
- Version Control
- Business Rules
- Technical Architecture
- Data Dictionary
- Source to Target Mapping
- ETL Flow
- Entity Relationship Model
- Rollback Plan
- Test Plan
- Test Cases
- Post Deployment Validation
- Technical Dependencies

---

## 4. Capacidades de la Versión
- extracción de facturación desde ZAM
- extracción de contabilidad desde ZAM
- carga auxiliar desde Excel
- conciliación lógica a través de vista
- persistencia para consumo en BI
- respaldo de tabla principal
- documentación base del proyecto
- control de promoción por ambientes

---

## 5. Restricciones Conocidas
- no existe aún dimensión Cliente
- la revisión actual está orientada a mes completo
- no se encuentran aún implementadas tablas de control ETL
- no existe staging formal para Excel
- la capa final comercial BI aún está pendiente de madurez

---

## 6. Riesgos Vigentes
- ambiente DEV apagado al momento de la documentación
- dependencia de terceros para habilitación de DEV
- reproceso de Excel sin control estructurado
- falta de capa final BI con Cliente
- dependencia de `.env` correctamente configurado

---

## 7. Bloqueos Operativos
El ambiente DEV se encuentra apagado y se solicitó su encendido por correo a los Ingenieros Oswaldo y Daniela el día 13/04/2026 a las 09:54 AM, sin respuesta al momento de esta liberación documental.

---

## 8. Validaciones Requeridas Previas a Cierre
- validar ejecución en DEV
- validar promoción a QA
- validar consistencia en QA
- validar consumo en Metabase
- validar respaldo
- documentar aprobación técnica

---

## 9. Próximas Mejoras
1. implementar tablas de control ETL
2. integrar staging de Excel
3. integrar dimensión Cliente
4. diseñar capa final BI comercial
5. fortalecer trazabilidad operativa

---

## 10. Conclusión
La versión 1.0 deja establecida la base funcional y documental del proyecto SCP_ReporteComercial_Ventas, permitiendo continuidad técnica, validación por ambientes y evolución controlada hacia una solución más madura y auditable.