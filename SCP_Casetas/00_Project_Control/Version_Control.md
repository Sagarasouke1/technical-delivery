# Version Control - SCP_Casetas

## Información General
**Proyecto:** SCP_Casetas  
**Nombre formal:** Sistema de Gestión y Validación de Casetas  
**Objetivo del control:** Mantener trazabilidad formal de cambios documentales, funcionales, técnicos y de validación del proyecto  
**Metodología:** Scrum  
**Responsable de control documental:** Emanuel Simón Zepeda  

---

## Lineamientos de Versionamiento

### Tipos de versión
- **Mayor (Major):** Cambio estructural relevante en alcance, arquitectura, reglas de negocio o artefactos base.
- **Menor (Minor):** Incorporación de nuevos artefactos, ampliación de contenido o consolidación documental.
- **Parche (Patch):** Correcciones de redacción, ajuste de referencias, nombres, rutas o formato sin impacto funcional.

### Convención sugerida
`v[Mayor].[Menor].[Patch]`

Ejemplo:
- `v1.0.0` → versión base aprobada
- `v1.1.0` → incorporación de nuevos documentos
- `v1.1.1` → corrección menor sin impacto de alcance

### Reglas de control
- Todo cambio debe registrar fecha, responsable, descripción e impacto.
- Todo cambio que afecte HU, LR, BR, TA, SD, TEST o evidencias debe reflejarse en este documento.
- Ningún documento validado debe sobrescribirse sin dejar rastro de versión.
- Los cambios deben poder trazarse contra requerimientos y artefactos relacionados.
- La documentación debe permanecer alineada con DoR y DoD definidos en HU. 
- Una historia solo debe considerarse cerrada cuando funcionalidad, pruebas, documentación y validación del PO estén actualizadas. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

---

## Historial de Versiones

### v1.0.0 — 18/03/2026
**Responsable:** Emanuel Simón Zepeda  
**Tipo de cambio:** Versión base funcional inicial  
**Descripción:**
- Se genera la base documental inicial del proyecto.
- Se documenta HU-001 Negocio.
- Se formaliza el objetivo de automatizar la importación de archivos descargados del portal PASE y evitar manipulación manual.
- Se establecen criterios de aceptación iniciales para importación, conservación de estructura y manejo de errores. :contentReference[oaicite:5]{index=5}

**Impacto:**
- Se habilita el backlog funcional inicial.
- Se define el punto de partida del proyecto.

---

### v1.1.0 — 19/03/2026
**Responsable:** Emanuel Simón Zepeda  
**Tipo de cambio:** Ampliación funcional y levantamiento formal  
**Descripción:**
- Se integra HU-002 Operativo.
- Se genera LR-001.
- Se documentan requerimientos funcionales, no funcionales, interfaces, riesgos, dependencias y alcance.
- Se consolida el enfoque de validación automática por viaje, detección de casetas fuera de ruta, validación de tarifas, registro de incidencias y trazabilidad. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}

**Impacto:**
- El proyecto pasa de idea funcional a definición documental formal.
- Se habilita la base para análisis técnico, diseño y pruebas.

---

### v1.2.0 — 10/04/2026
**Responsable:** Emanuel Simón Zepeda  
**Tipo de cambio:** Consolidación enterprise documental  
**Descripción:**
- Se reorganiza el repositorio bajo estructura corporativa orientada a auditoría TI.
- Se incorporan o preparan artefactos para:
  - Requirements Validation
  - User Stories
  - Technical Analysis
  - Solution Design
  - Testing and Validation
  - Development Evidence
- Se documenta el flujo detallado del proceso de validación.
- Se incorpora el algoritmo funcional del sistema.
- Se integra el diccionario de datos preliminar con tablas clave:
  - `tb_r_casetas_checker`
  - `tb_r_checker_auth`
  - `tb_c_casetas_tarifas` :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

**Impacto:**
- Se fortalece la trazabilidad de extremo a extremo.
- Se deja la base documental preparada para diseño técnico y control de cambios.

---

### v1.2.1 — 10/04/2026
**Responsable:** Emanuel Simón Zepeda  
**Tipo de cambio:** Ajuste documental de seguimiento  
**Descripción:**
- Se actualiza `Project_Status.md`.
- Se incorpora nivel de madurez del proyecto.
- Se integran riesgos, dependencias, stoppers y siguientes pasos.
- Se alinea el estado del proyecto con la fase de transición de análisis funcional a diseño de solución. 

**Impacto:**
- Mejora visibilidad ejecutiva.
- Facilita seguimiento para PO, negocio, QA y auditoría.

---

### v1.3.0 — 13/04/2026
**Responsable:** Emanuel Simón Zepeda  
**Tipo de cambio:** Formalización de trazabilidad y control  
**Descripción:**
- Se actualiza `Version_Control.md`.
- Se construye o actualiza la matriz de trazabilidad HU → RF → BR/RNF → TA → SD → TC → Evidencia.
- Se vinculan requerimientos con módulos del sistema, reglas de negocio, datos y pantallas clave.
- Se deja preparada la base documental para Sprint Planning técnico y validación con PO. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14}

**Impacto:**
- Se fortalece control documental y gobernanza.
- Se incrementa la capacidad de auditoría y seguimiento por sprint.

---

## Estado Actual de Versionamiento
**Versión vigente:** `v1.3.0`  
**Estado:** Activa / En evolución controlada  
**Última actualización:** 13/04/2026  

---

## Artefactos Bajo Control de Versión
- Project_Status.md
- Version_Control.md
- HU-001 Negocio
- HU-002 Operativo
- LR-001
- BR
- AC
- Checklist de validación
- Matriz de trazabilidad
- Análisis técnico
- Diseño de solución
- Plan de pruebas
- Casos de prueba
- Evidencias de desarrollo
- Evidencias funcionales
- Release Notes
- Hallazgos y soluciones

---

## Criterios para Incrementar Versión

### Major
Incrementar cuando:
- cambie el alcance del proyecto
- cambien reglas de negocio críticas
- cambie arquitectura principal
- cambie el modelo de datos de forma relevante
- se redefina el flujo operativo del sistema

### Minor
Incrementar cuando:
- se agreguen documentos nuevos
- se amplíen HU, LR, BR o SD
- se agreguen matrices, planes de prueba o evidencias
- se integre nueva funcionalidad documentada

### Patch
Incrementar cuando:
- se corrija redacción
- se ajusten nombres de archivos
- se mejoren referencias
- se corrijan rutas o formato

---

## Observaciones
El proyecto ya cuenta con base documental suficiente para mantener un control de cambios formal. La prioridad es que cualquier modificación futura en reglas, flujos, tarifas, catálogos, autorizaciones o estructura de entrada desde PASE quede reflejada tanto en esta bitácora como en la matriz de trazabilidad, ya que el formato del portal, los catálogos vigentes y la definición de autorizaciones son dependencias y riesgos identificados del proyecto. :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}