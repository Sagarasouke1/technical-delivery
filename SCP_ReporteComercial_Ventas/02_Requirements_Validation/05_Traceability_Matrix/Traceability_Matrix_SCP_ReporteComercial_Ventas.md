# Traceability Matrix - SCP_ReporteComercial_Ventas

## 1. Objetivo
Mantener trazabilidad entre necesidad de negocio, reglas, solución técnica, objetos implementados, validaciones y evidencias del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Matriz de Trazabilidad

| ID | Necesidad / Requerimiento | Regla / Criterio asociado | Solución técnica | Objeto / Artefacto | Validación / Evidencia |
|----|---------------------------|---------------------------|------------------|--------------------|------------------------|
| TM-001 | Comparar facturado vs contabilizado | RN-01, AC-01 | Vista de conciliación | `vw_mb_conciliacion_fact_vs_conta_2026` | Validación de vista / BI |
| TM-002 | Conciliar por referencia | RN-30, AC-02 | Llave principal por referencia | Vista de conciliación | Consulta de muestra |
| TM-003 | Identificar diferencias | RN-35, RN-36, RN-37, AC-03 | cálculo de diferencia + estatus | Vista / tabla persistida | Validación funcional |
| TM-004 | Revisar por mes completo | RN-04, AC-04, AC-24 | cálculo de `mes_num` y `mes` | `tb_mb_conciliacion_fact_vs_conta_2026` | Dashboard / consulta SQL |
| TM-005 | Mostrar análisis por operación | RN-06, AC-05, AC-22 | `tipo_operacion` en capa analítica | tabla persistida / dashboard | Validación BI |
| TM-006 | Permitir rango de fechas | RN-06, AC-06, AC-23 | uso de fechas disponibles en capa analítica | vista / tabla persistida / dashboard | Validación BI |
| TM-007 | Cargar facturación desde ZAM | AC-10 | ETL de facturación | `FacturacionElectronica.py` / `FacturacionElectronica.sql` | Log y tabla cargada |
| TM-008 | Cargar contabilidad desde ZAM | AC-11 | ETL de contabilidad | `PolizaContableIngresos.py` / `PolizaContableIngresos.sql` | Log y tabla cargada |
| TM-009 | Cargar auxiliar desde Excel | AC-12 | ETL Excel | `PolizaIngresosExcel.py` | Tabla auxiliar cargada |
| TM-010 | Persistir conciliación para BI | AC-14, AC-20 | query manual `CREATE TABLE AS SELECT` | `tb_mb_conciliacion_fact_vs_conta_2026` | Validación de tabla |
| TM-011 | Respaldar tabla de conciliación | AC-16 | script de backup | `BackupMariadb.py` | Log de respaldo |
| TM-012 | Tener evidencia operativa | RN-50, AC-15 | logs por proceso | logs de ETL y backup | archivos `.log` |
| TM-013 | Cliente como filtro requerido | RN-06, AC-07 | mejora futura | dimensión pendiente | documento de gap |
| TM-014 | Promoción controlada por ambiente | AC-30, AC-31, AC-32 | DEV → QA → PROD | configuración por ambiente | validación por ambiente |
| TM-015 | Documentar bloqueo de DEV | dependencia operativa | documentación de riesgo y dependencia | `Project_Status.md`, `Technical_Dependencies.md` | evidencia documental |

---

## 3. Relación de Objetos Clave

### Reglas de negocio
- `02_Requirements_Validation/02_Business_Rules/Business_Rules_SCP_ReporteComercial_Ventas.md`

### Criterios de aceptación
- `02_Requirements_Validation/03_Acceptance_Criteria/Acceptance_Criteria_SCP_ReporteComercial_Ventas.md`

### Checklists de validación
- `02_Requirements_Validation/04_Validation_Checklists/Checklist_Validacion_Tecnica.md`
- `02_Requirements_Validation/04_Validation_Checklists/Checklist_Validacion_BI.md`

### Arquitectura y modelo
- `05_Solution_Design/01_Architecture/Technical_Architecture.md`
- `05_Solution_Design/04_Flows/ETL_Flow.md`
- `05_Solution_Design/04_Flows/Conciliation_Flow.md`
- `05_Solution_Design/04_Flows/Dashboard_Flow.md`
- `05_Solution_Design/02_Data_Model/Data_Dictionary.md`
- `05_Solution_Design/02_Data_Model/Entity_Relationship_Model.md`

### Evidencias
- logs
- tablas cargadas
- dashboard
- respaldos
- validación por ambiente

---

## 4. Uso de la Matriz
Esta matriz debe actualizarse cuando:
- se agregue Cliente
- cambie la estrategia de persistencia
- se automaticen procesos
- se agreguen tablas de control ETL
- cambie el modelo BI final