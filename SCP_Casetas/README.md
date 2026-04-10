# 🚀 SCP_Casetas – Sistema de Validación de Casetas

## 🧠 Resumen Ejecutivo
El proyecto **SCP_Casetas** tiene como objetivo diseñar e implementar un sistema automatizado para la validación de casetas, eliminando la dependencia de procesos manuales basados en hojas de cálculo y mejorando la trazabilidad, control operativo y control financiero.

Este sistema permitirá validar archivos provenientes del portal PASE, detectar inconsistencias, controlar costos y registrar incidencias operativas de forma estructurada.

---

## 🎯 Objetivo del Proyecto
Implementar una solución tecnológica que permita:

- Automatizar la validación de casetas
- Reducir errores humanos
- Asegurar trazabilidad completa del proceso
- Optimizar tiempos de liquidación
- Fortalecer el control financiero

De acuerdo con la documentación base:
- HU Negocio → :contentReference[oaicite:0]{index=0}  
- HU Operativo → :contentReference[oaicite:1]{index=1}  
- Levantamiento de Requerimientos → :contentReference[oaicite:2]{index=2}  

---

## 📌 Problemática Actual
El proceso actual presenta:

- Alto esfuerzo operativo
- Dependencia de personal especializado
- Manipulación manual de archivos
- Falta de trazabilidad
- Riesgo de errores humanos
- Baja escalabilidad del proceso :contentReference[oaicite:3]{index=3}  

---

## 🧩 Alcance del Proyecto

### ✔ Incluye
- Importación directa de archivos del portal PASE
- Validación automática de casetas por viaje
- Comparación contra rutas autorizadas
- Identificación de inconsistencias
- Validación de costos y tarifas
- Detección de duplicados
- Gestión de incidencias
- Generación de reportes
- Trazabilidad completa
- Integración con SCP, ZAM y Metabase :contentReference[oaicite:4]{index=4}  

### ❌ No Incluye
- Automatización de descarga de archivos (CAPTCHA)
- Integración directa con concesionarios
- Modificación de sistemas actuales de liquidaciones :contentReference[oaicite:5]{index=5}  

---

## 🧱 Arquitectura Funcional (Nivel Alto)

### 🔹 Módulos Principales
1. **Importación y Procesamiento**
   - Carga de archivos PASE
   - Validación de formato
   - Estructuración de datos

2. **Validación Operativa**
   - Validación contra rutas autorizadas
   - Detección de casetas no autorizadas
   - Comparación de tarifas

3. **Gestión de Incidencias**
   - Registro de incidencias
   - Seguimiento
   - Justificación operativa

4. **Reportes y Análisis**
   - Reportes de inconsistencias
   - Exportación
   - Integración con Metabase

5. **Trazabilidad**
   - Registro de usuario, fecha y acción
   - Auditoría completa

---

## 👥 Tipos de Usuario

### 🧑‍💻 Operativo (Liquidaciones)
- Validación de casetas
- Registro de incidencias

### 🧑‍💼 Supervisor / Administrativo
- Análisis de información
- Auditoría

### 🚛 Operaciones (DOM / IE / DED / MAR)
- Justificación de incidencias
- Validación operativa :contentReference[oaicite:6]{index=6}  

---

## 📊 Funcionalidades Clave (Product Backlog)

### 🔥 Alta Prioridad
- Importación directa de archivos
- Validación automática de casetas
- Normalización mediante catálogos
- Validación de costos
- Detección de inconsistencias

### ⚙️ Media Prioridad
- Gestión de incidencias
- Trazabilidad
- Interfaz guiada :contentReference[oaicite:7]{index=7}  

---

## 📈 Métricas de Éxito

- ⏱ Reducción del tiempo ≥ 60%
- ❌ Disminución de errores ≥ 80%
- 🔍 Trazabilidad completa
- 👤 Uso por personal no especializado :contentReference[oaicite:8]{index=8}  

---

## 🔒 Requerimientos No Funcionales

- Integridad de datos
- Seguridad y control de accesos
- Disponibilidad ≥ 99%
- Trazabilidad completa
- Interfaz amigable :contentReference[oaicite:9]{index=9}  

---

## ⚠️ Riesgos Identificados

| Riesgo | Mitigación |
|------|--------|
| Cambios en formato PASE | Validaciones configurables |
| Alto volumen de datos | Pruebas de rendimiento |
| Errores en TAGs | Validaciones específicas |

---

## 🧪 Calidad y Metodología

### 📌 Metodología
- Scrum (iterativo e incremental)

### ✔ Definition of Ready
- Historia clara
- Criterios definidos
- Dependencias identificadas

### ✔ Definition of Done
- Funcionalidad implementada
- Pruebas exitosas
- Code Review aprobado
- Validación PO
- Deploy realizado :contentReference[oaicite:10]{index=10}  

---

## 🔗 Integraciones

- SCP (Sistema central)
- ZAM (rutas)
- Metabase (analítica)
- Autenticación corporativa :contentReference[oaicite:11]{index=11}  

---

## 📂 Estructura del Proyecto

El proyecto sigue una estructura estándar corporativa basada en:

SCP_Casetas/
│
├── 00_Project_Control
├── 01_Request_Intake
├── 02_Requirements
├── 03_User_Stories
├── 04_Design
├── 05_Development
├── 06_Testing
├── 07_Release
├── 08_Support
└── 09_Documentation

---

## 🧾 Estado del Proyecto
Ver archivo:
📄 `00_Project_Control/Project_Status.md`

---

## ✍️ Firmas

| Nombre | Rol |
|------|------|
| Oswaldo Ortiz | Product Owner |
| Emanuel Simón Zepeda | Desarrollador Analista |

---

## 🏁 Conclusión

Este proyecto representa una evolución crítica hacia la automatización del control de casetas, impactando directamente en:

- Operación
- Finanzas
- Auditoría
- Escalabilidad del negocio

---
