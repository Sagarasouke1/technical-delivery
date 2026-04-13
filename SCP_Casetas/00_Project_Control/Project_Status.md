# Project Status - SCP_Casetas

## Información General
**Proyecto:** SCP_Casetas  
**Nombre formal:** Sistema de Gestión y Validación de Casetas  
**Área solicitante:** Negocio / Liquidaciones / Operaciones  
**Áreas impactadas:** Liquidaciones / TI  
**Product Owner:** Oswaldo Ortiz  
**Metodología:** Scrum  
**Estado actual:** En fase de transición de análisis funcional a diseño de solución

---

## Resumen Ejecutivo del Estado
El proyecto ha evolucionado de una fase inicial de levantamiento y definición funcional hacia una fase estructurada de análisis técnico y diseño de solución.

Actualmente se cuenta con una base documental sólida que incluye:
- Historias de Usuario (Negocio y Operación)
- Levantamiento de Requerimientos (LR)
- Reglas de Negocio iniciales
- Flujo operativo del proceso
- Diccionario de datos preliminar
- Evidencia visual de interfaz (SCP WEB)

Adicionalmente, se ha iniciado la generación de artefactos técnicos y de diseño alineados a buenas prácticas de ingeniería, auditoría TI y trazabilidad completa del ciclo de vida.

---

## Avances Registrados

### 18/03/2026
**(Hecho):**
- Se documenta la Historia de Usuario de Negocio HU-001.
- Se define la problemática del proceso actual de validación de casetas.
- Se establece la necesidad de automatización del proceso (importación, validación y trazabilidad).
- Se identifican áreas impactadas: Liquidaciones y TI.

---

### 19/03/2026
**(Hecho):**
- Se documenta la Historia de Usuario Operativa HU-002.
- Se consolida el enfoque funcional orientado al área de Liquidaciones.
- Se genera el documento de Levantamiento de Requerimientos LR-001.
- Se documentan:
  - Requerimientos funcionales y no funcionales
  - Reglas de negocio iniciales
  - Interfaces
  - Usuarios
  - Riesgos y dependencias

---

### 10/04/2026
**(Hecho):**
- Se estructura el repositorio bajo modelo enterprise orientado a auditoría TI.
- Se organiza la documentación bajo capas:
  - Request Intake
  - Requirements Validation
  - User Stories
  - Technical Analysis
  - Solution Design
  - Testing & Validation
- Se integra documentación técnica inicial:
  - Flujo detallado del proceso de validación de casetas
  - Arquitectura de solución (SCP + ZAM + Metabase)
  - Modelo lógico de datos basado en tablas:
    - tb_r_casetas_checker
    - tb_r_checker_auth
- Se documenta algoritmo funcional del proceso de validación:
  - Identificación de viajes
  - Validación de casetas
  - Validación de montos
  - Clasificación de resultados
- Se documentan reglas operativas de interfaz:
  - Confirmación de carga
  - Selección de tipo de archivo
  - Aprobación / rechazo de casetas
  - Clasificación de viajes
- Se documenta evidencia visual del sistema:
  - Carga de archivos
  - Validación
  - Resultados
  - Histórico
  - Actualización de precios

---

## En Proceso
- Consolidación de reglas de negocio finales (BR).
- Construcción de matriz de trazabilidad:
  - HU → RF → BR → TA → SD → TC
- Formalización del análisis técnico por historia de usuario.
- Refinamiento del modelo de datos físico.
- Definición de arquitectura técnica detallada (componentes y flujo de datos).
- Elaboración del plan de pruebas completo (Test Plan + Test Cases).
- Integración de evidencias en repositorio para auditoría.

---

## Stoppers
- Pendiente validación formal final con Product Owner (aprobación funcional).
- Pendiente definición oficial de catálogos de:
  - Casetas
  - Tarifas vigentes
- Pendiente confirmación de estructura estable de archivos del portal PASE (CSV/PDF).
- Pendiente definición de reglas operativas completas para autorizaciones (flujo de aprobación/rechazo).
- Dependencia de validación de negocio para clasificación de viajes (cargado, pagado, vacío).

---

## Riesgo Actual
**Nivel:** Medio

### Riesgos identificados
- Cambios en la estructura del portal PASE.
- Variabilidad en formato de archivos de entrada.
- Alto volumen de datos en procesamiento.
- Dependencia de validación manual en casos excepcionales.
- Diferencias entre tarifas reales y catálogos internos.
- Falta de estandarización en criterios operativos de autorización.

---

## Dependencias Actuales
- Archivos descargados del portal PASE (CSV / PDF).
- Catálogos de casetas y tarifas actualizados.
- Usuarios autorizados para validación y aprobación.
- Infraestructura SCP (WEB).
- Integración con:
  - ZAM (operación)
  - Metabase (analítica)
- Acceso a red corporativa interna.

---

## Próximos Pasos
1. Validación documental final con negocio, operación y Product Owner.
2. Cierre de reglas de negocio (BR consolidadas).
3. Construcción de matriz de trazabilidad completa.
4. Finalización del análisis técnico por HU.
5. Definición final de arquitectura de solución.
6. Refinamiento del modelo de datos físico.
7. Elaboración del plan de pruebas completo.
8. Preparación para inicio de Sprint de desarrollo.

---

## Nivel de Madurez del Proyecto

| Área | Nivel |
|------|-------|
| Definición funcional | Alto |
| Requerimientos | Alto |
| Reglas de negocio | Medio-Alto |
| Análisis técnico | Medio |
| Diseño de solución | Medio |
| Modelo de datos | Medio |
| Plan de pruebas | Inicial |
| Desarrollo | No iniciado |

---

## Observaciones
El proyecto presenta un nivel de madurez adecuado para iniciar la fase de diseño técnico detallado y planificación de desarrollo.

La estructura documental implementada permite:
- Trazabilidad completa
- Control de cambios
- Soporte a auditoría TI
- Escalabilidad del proyecto

La prioridad actual es cerrar validaciones con negocio y consolidar artefactos técnicos antes de iniciar desarrollo.

---

## Responsable
**Emanuel Simón Zepeda**  
Desarrollador Analista / Líder Técnico