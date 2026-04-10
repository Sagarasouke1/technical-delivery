# Test Plan - SCP_Casetas v1

## Objetivo
Definir la estrategia inicial de pruebas para validar que la solución SCP_Casetas cumpla con los requerimientos funcionales, no funcionales y criterios de aceptación documentados.

---

## Alcance de Pruebas
Las pruebas deberán cubrir como mínimo los siguientes componentes:

### 1. Importación y Procesamiento
- Carga de archivo válido
- Manejo de archivo inválido
- Validación de formato
- Estructuración de información

### 2. Validación Operativa
- Validación por viaje
- Identificación de casetas fuera de ruta
- Validación de tarifas
- Detección de diferencias de costo
- Detección de duplicados

### 3. Gestión de Incidencias
- Registro de incidencia
- Registro de justificación
- Asociación de observaciones
- Asociación de evidencias

### 4. Reportería
- Generación de reporte consolidado
- Filtros de consulta
- Exportación de resultados

### 5. Trazabilidad
- Registro de usuario
- Registro de acción
- Registro de fecha
- Consulta histórica

---

## Tipos de Prueba Contemplados
- Pruebas funcionales
- Pruebas de validación de datos
- Pruebas de integración
- Pruebas de trazabilidad
- Pruebas de usabilidad
- Pruebas UAT

---

## Entradas de Prueba
- Archivos del portal PASE válidos
- Archivos del portal PASE inválidos o incompletos
- Catálogos de casetas y tarifas
- Información de viaje
- Escenarios con incidencias operativas
- Escenarios con duplicados
- Escenarios con diferencias de costo

---

## Criterios de Aceptación de la Fase de Pruebas
- Los RF críticos deben quedar cubiertos
- Los criterios de aceptación deben ser verificables
- Los defectos críticos deben resolverse antes de liberación
- La trazabilidad debe quedar funcional
- El usuario debe validar el flujo operativo principal

---

## Roles Involucrados
### TI / Desarrollo
Responsable de pruebas unitarias, soporte a integración y corrección de hallazgos.

### QA / Validación
Responsable de ejecución formal de casos de prueba, registro de defectos y seguimiento.

### Usuario Operativo / UAT
Responsable de validar que el sistema responda a la operación real del proceso.

---

## Entregables Esperados
- Casos de prueba
- Registro de ejecución
- Log de defectos
- Evidencias
- Resultados de UAT