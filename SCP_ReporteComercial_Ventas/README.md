# 📊 SCP_ReporteComercial_Ventas
**Reporte Comercialización – Ventas Consolidadas**

---

## 🧠 Resumen Ejecutivo

El proyecto **SCP_ReporteComercial_Ventas** tiene como finalidad diseñar e implementar un reporte consolidado de ventas que permita integrar en un solo punto de consulta la información comercial proveniente de múltiples documentos y fuentes.

Actualmente, la información de ventas se encuentra distribuida en distintos reportes y documentos, lo que dificulta el análisis integral del desempeño comercial. Este proyecto busca centralizar dicha información, permitiendo su análisis por operación, cliente y periodo, así como la comparación histórica para la toma de decisiones estratégicas.

Como parte fundamental del modelo de negocio, la operación **Dedicados** deberá identificarse y visualizarse obligatoriamente bajo la razón social **FLA**.

---

## 🎯 Objetivo del Proyecto

Implementar un reporte de **Ventas Consolidadas** que permita:

- Centralizar la información de ventas.
- Filtrar datos por operación, cliente y rango de fechas.
- Integrar todos los documentos que impactan la venta.
- Generar comparativos históricos (mensual y anual).
- Homologar la visualización de la operación **Dedicados** como **FLA**.
- Proveer información confiable para la toma de decisiones.

---

## 🏢 Información General

| Campo | Detalle |
|------|--------|
| **Proyecto** | SCP_ReporteComercial_Ventas |
| **Nombre funcional** | Reporte Comercialización – Ventas Consolidadas |
| **Empresa** | Auto Express Oriente / Fletes Línea Azul |
| **Sistema** | Metabase / ZAM |
| **Área solicitante** | Comercialización |
| **Tipo de solución** | Reporte analítico / BI |
| **Metodología** | Scrum |
| **Código HU base** | HU-001 |

---

## ❗ Problemática de Negocio

La información comercial actual presenta las siguientes problemáticas:

- Se encuentra distribuida en múltiples fuentes.
- No existe una vista consolidada de ventas.
- Dificulta el análisis por cliente, operación y periodo.
- Complica la generación de comparativos históricos.
- Existe falta de estandarización en la visualización de operaciones.
- No se tiene homologación clara de la operación **Dedicados (FLA)**.

---

## 👤 Historia de Usuario Principal

**Como** usuario directivo y administrativo del sistema SCP,  
**quiero** contar con un reporte de Ventas Consolidadas que integre todos los documentos de venta, con filtros y comparativos por periodo, operación y cliente,  
**para** analizar el desempeño comercial de la empresa y facilitar la toma de decisiones estratégicas con información confiable y segmentada.

---

## 📦 Alcance Funcional

### ✅ Incluye

- Totales de ventas consolidados.
- Filtros por:
  - Operación(es)
  - Rango de fechas (semanal o mensual)
  - Cliente(s)
- Inclusión de documentos:
  - CFDI
  - Facturas directas
  - Notas de cargo
  - Notas de crédito
  - Cancelaciones
  - Refacturaciones
- Comparativos:
  - Año contra año
  - Mes contra mes
- Identificación obligatoria de:
  - **Dedicados → FLA**

---

### ❌ No Incluye

- Modificación de información contable origen.
- Reprocesos fiscales.
- Cambios en la generación de documentos.
- Alteración de lógica en sistemas fuente.

---

## 🧩 Requerimientos Funcionales

### RF-01 Consolidación de ventas
El sistema deberá mostrar los totales de ventas en un solo reporte consolidado.

### RF-02 Filtro por operación
Permitir seleccionar una o múltiples operaciones.

### RF-03 Filtro por fechas
Permitir consulta por rango de fechas (semanal o mensual).

### RF-04 Filtro por cliente
Permitir segmentación por uno o varios clientes.

### RF-05 Integración documental
El reporte deberá considerar:
- CFDI
- Facturas
- Notas de cargo
- Notas de crédito
- Cancelaciones
- Refacturaciones

### RF-06 Comparativos históricos
Permitir:
- Comparativo año contra año
- Comparativo mes contra mes

### RF-07 Homologación Dedicados
Toda la operación **Dedicados** deberá visualizarse como **FLA**.

### RF-08 Filtros acumulativos
Los filtros deberán funcionar de manera combinada.

### RF-09 Disponibilidad
El reporte deberá estar disponible en el sistema definido.

---

## 📌 Reglas de Negocio

### RN-01
El reporte es únicamente informativo.

### RN-02
No genera movimientos contables.

### RN-03
Dedicados siempre debe mostrarse como FLA.

### RN-04
Los filtros deben ser acumulativos.

### RN-05
El resultado debe ser validado por el área solicitante.

---

## 🛠️ Enfoque de Implementación

El desarrollo del proyecto se realizará por fases:

1. Consolidación de información de diferentes documentos.
2. Homologación de criterios de operación.
3. Desarrollo de filtros combinados.
4. Construcción de comparativos históricos.
5. Validación funcional con Comercialización.
6. Liberación controlada.

---

## 🏗️ Estructura del Proyecto

```bash
SCP_ReporteComercial_Ventas/
│
├── README.md
│
├── 00_Project_Control/
│   ├── Project_Status.md
│   ├── Version_Control.md
│   ├── Traceability_Matrix.md
│
├── 01_Request_Intake/
├── 02_Requirements_Validation/
├── 03_User_Stories/
├── 04_Architecture_Design/
├── 05_Development/
├── 06_Quality_Assurance/
├── 07_Deployment_and_Release/
└── 08_Monitoring_and_Support/


---
