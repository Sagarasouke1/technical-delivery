# Technical Impact Analysis - SCP_ReporteComercial_Ventas

## 1. Objetivo
Analizar el impacto técnico del proyecto SCP_ReporteComercial_Ventas sobre arquitectura, procesos ETL, base analítica, BI y operación por ambientes.

---

## 2. Contexto
El proyecto tiene como finalidad comparar el monto facturado contra el monto contabilizado, consolidando información desde ZAM hacia una base analítica para su posterior explotación en Metabase.

Actualmente:
- la revisión está orientada a mes completo
- la conciliación se centraliza en una vista
- la tabla persistida se genera manualmente a partir de dicha vista
- Cliente aún no forma parte del modelo
- existen ambientes DEV, QA y PROD
- el ambiente DEV está apagado al momento de esta documentación

---

## 3. Impacto en Arquitectura

### Impacto actual
El proyecto introduce una arquitectura con:
- origen operacional en ZAM
- ETLs en Python
- almacenamiento analítico en MySQL / MariaDB
- capa lógica vía vista
- persistencia para BI
- consumo final en Metabase

### Evaluación
**Impacto:** Alto  
**Justificación:** afecta directamente la forma en que se integran, transforman y consumen datos operativos.

---

## 4. Impacto en Procesos ETL

### Procesos afectados
- `FacturacionElectronica.py`
- `PolizaContableIngresos.py`
- `PolizaIngresosExcel.py`
- `BackupMariadb.py`

### Impacto identificado
- dependencia de `.env`
- dependencia de conectividad a SQL Server y MySQL
- necesidad de trazabilidad operativa
- necesidad de estandarización futura
- oportunidad de centralizar control ETL

### Evaluación
**Impacto:** Alto  
**Justificación:** el funcionamiento del componente depende directamente de estos procesos.

---

## 5. Impacto en Modelo de Datos

### Objetos impactados
- `dm_factura_electronica_totales`
- `cont_polizadet_ingresos_2026`
- `cont_polizadet_ingresos_original_2026`
- `vw_mb_conciliacion_fact_vs_conta_2026`
- `tb_mb_conciliacion_fact_vs_conta_2026`

### Impacto identificado
- la tabla persistida depende de una vista
- la tabla persistida se genera manualmente
- no existe aún capa final comercial desacoplada
- no existe Cliente
- no existen tablas de control ETL

### Evaluación
**Impacto:** Alto  
**Justificación:** cualquier cambio en el modelo puede impactar conciliación, dashboard y operación.

---

## 6. Impacto en BI

### Impacto identificado
- Metabase depende de la actualización correcta de `tb_mb_conciliacion_fact_vs_conta_2026`
- la ausencia de Cliente limita filtros esperados
- el enfoque mensual actual condiciona la lectura de negocio
- la dependencia de persistencia manual representa riesgo operativo

### Evaluación
**Impacto:** Alto  
**Justificación:** BI depende directamente de la consistencia de la capa persistida.

---

## 7. Impacto en Operación por Ambientes

### DEV
- impacto crítico por indisponibilidad actual
- impide pruebas iniciales y ajustes controlados

### QA
- impacto alto, ya que depende de la liberación validada desde DEV

### PROD
- impacto crítico, por ser ambiente oficial de consumo

### Evaluación global
**Impacto:** Alto  
**Justificación:** el proyecto requiere flujo DEV → QA → PROD y actualmente DEV está bloqueado.

---

## 8. Impacto en Gobierno Técnico

### Impacto identificado
- necesidad de documentación formal
- necesidad de trazabilidad
- necesidad de control de cambios
- necesidad de gestión de dependencias
- necesidad de plan de rollback y validación

### Evaluación
**Impacto:** Alto  
**Justificación:** el proyecto ya no debe manejarse solo como scripts aislados, sino como componente controlado.

---

## 9. Impacto de Restricciones Actuales

### Restricción 1: Cliente no existe
**Impacto:** Medio-Alto  
**Efecto:** limita el alcance funcional del dashboard

### Restricción 2: Persistencia manual
**Impacto:** Alto  
**Efecto:** dependencia operativa y riesgo de desactualización

### Restricción 3: DEV apagado
**Impacto:** Alto  
**Efecto:** bloqueo en validación y avance técnico

### Restricción 4: Sin tablas ETL de control
**Impacto:** Medio-Alto  
**Efecto:** menor trazabilidad y menor auditabilidad

---

## 10. Conclusión
El impacto técnico del proyecto SCP_ReporteComercial_Ventas es alto, ya que involucra integración de fuentes operativas, procesos ETL, modelo analítico, vista lógica, persistencia para BI, validación por ambientes y dependencia de infraestructura. La solución ya es funcional, pero requiere fortalecimiento estructural para elevarse a un nivel enterprise auditable y mantenible.