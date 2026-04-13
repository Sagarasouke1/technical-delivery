# Technical Dependencies - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar las dependencias técnicas, operativas y de infraestructura que impactan el desarrollo, validación, despliegue y operación del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Dependencias Técnicas Principales

### D-01. Sistema origen ZAM
**Tipo:** dependencia de origen  
**Descripción:** fuente operativa de datos de facturación y contabilidad  
**Impacto:** crítico  
**Observación:** sin acceso o conectividad al origen no puede ejecutarse la extracción

---

### D-02. Base Analítica MySQL / MariaDB
**Tipo:** dependencia de almacenamiento  
**Descripción:** destino de los ETLs y persistencia de conciliación  
**Impacto:** crítico

---

### D-03. Scripts ETL Python
**Tipo:** dependencia técnica  
**Descripción:** procesos responsables de extracción, carga, Excel y respaldo  
**Impacto:** alto

---

### D-04. Vista `vw_mb_conciliacion_fact_vs_conta_2026`
**Tipo:** dependencia lógica  
**Descripción:** centraliza la lógica de conciliación  
**Impacto:** crítico

---

### D-05. Tabla `tb_mb_conciliacion_fact_vs_conta_2026`
**Tipo:** dependencia BI  
**Descripción:** fuente oficial actual para Metabase  
**Impacto:** crítico

---

### D-06. Metabase
**Tipo:** dependencia de consumo  
**Descripción:** plataforma BI para consulta final  
**Impacto:** alto

---

## 3. Dependencias de Infraestructura por Ambiente

### DEV
**Estado actual:** no disponible / apagado  
**Impacto:** alto  
**Efecto:**
- detiene validaciones de desarrollo
- impide pruebas iniciales
- retrasa promoción a QA
- retrasa despliegues controlados

**Acción realizada:**
Se envió correo solicitando encendido del ambiente DEV a los Ingenieros Oswaldo y Daniela el día **13/04/2026 a las 09:54 AM**.

**Estatus actual:**
Sin respuesta al momento de esta documentación.

---

### QA
**Estado:** disponible sujeto a validación operativa  
**Impacto:** alto  
**Uso:** pruebas técnicas y funcionales previas a PROD

---

### PROD
**Estado:** ambiente productivo  
**Impacto:** crítico  
**Uso:** operación oficial del componente y consumo en BI

---

## 4. Dependencias Operativas
- disponibilidad de ambientes
- respuesta de responsables de infraestructura
- configuración correcta de `.env`
- disponibilidad de rutas de logs, queries, Excel y backups
- ejecución coordinada de procesos ETL

---

## 5. Bloqueos Actuales

### B-01. Ambiente DEV apagado
**Fecha de identificación:** 13/04/2026  
**Responsables relacionados:** Ing. Oswaldo / Ing. Daniela  
**Impacto en proyecto:**
- frena desarrollo
- frena validación técnica
- frena promoción controlada
- incrementa riesgo de retraso documental y técnico

**Acción de seguimiento recomendada:**
- registrar en `Project_Status.md`
- registrar en `Risk_Assessment_SCP_ReporteComercial_Ventas.md`
- registrar en control de dependencias
- dar seguimiento formal por correo o reunión

---

## 6. Recomendaciones
1. Mantener este documento actualizado
2. Registrar todo bloqueo de infraestructura en Project Status
3. No promover cambios sin disponibilidad de DEV y QA
4. Mantener trazabilidad de solicitudes a terceros responsables
5. Escalar dependencias críticas si impactan fechas del proyecto