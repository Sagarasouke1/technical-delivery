# Risk Assessment - SCP_ReporteComercial_Ventas

## 1. Objetivo
Identificar y documentar los principales riesgos técnicos, operativos y analíticos del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Riesgos Identificados

### R-01. Diferencias de fecha entre facturación y contabilidad
**Descripción:** Los procesos de facturación y contabilidad pueden registrar la misma referencia en fechas distintas.  
**Impacto:** Alto  
**Probabilidad:** Alta  
**Mitigación:** Analizar diferencia por referencia y complementar con lógica de fecha en capa BI.

### R-02. Referencias inconsistentes
**Descripción:** Una misma referencia puede presentar diferencias de formato o asociación.  
**Impacto:** Alto  
**Probabilidad:** Media  
**Mitigación:** Normalización de referencia y validaciones en capa analítica.

### R-03. Reproceso no controlado de Excel
**Descripción:** Los archivos auxiliares podrían cargarse varias veces sin control estructurado.  
**Impacto:** Medio  
**Probabilidad:** Alta  
**Mitigación:** Crear `ctl_archivos_excel_procesados` y staging.

### R-04. Dependencia del `.env`
**Descripción:** Una mala configuración puede impedir extracción, carga o respaldo.  
**Impacto:** Alto  
**Probabilidad:** Media  
**Mitigación:** Validaciones tempranas, `.env.template` y checklist de despliegue.

### R-05. Falta de control ETL en base de datos
**Descripción:** Actualmente la trazabilidad depende principalmente de logs en archivo.  
**Impacto:** Alto  
**Probabilidad:** Alta  
**Mitigación:** Crear `etl_control_ejecucion` y `etl_log_errores`.

### R-06. Falta de dimensión Cliente
**Descripción:** El dashboard esperado requiere Cliente, pero aún no está integrado de forma formal en la capa final.  
**Impacto:** Alto  
**Probabilidad:** Alta  
**Mitigación:** Validar fuente de Cliente e incorporarla a capa BI.

### R-07. Dependencia de procesos separados
**Descripción:** El flujo actual no está orquestado por una bitácora central.  
**Impacto:** Medio  
**Probabilidad:** Media  
**Mitigación:** Definir script maestro o control central ETL.

---

## 3. Conclusión
El proyecto ya tiene una base funcional sólida, pero requiere fortalecimiento de gobierno técnico, control ETL y madurez del modelo BI para reducir riesgos operativos y analíticos.