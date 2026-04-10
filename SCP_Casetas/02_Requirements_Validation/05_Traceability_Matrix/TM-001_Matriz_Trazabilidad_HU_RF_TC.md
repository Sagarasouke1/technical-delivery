# TM-001 - Matriz de Trazabilidad HU / RF / Módulo / Caso de Prueba

## Objetivo
Establecer la trazabilidad entre historias de usuario, requerimientos funcionales, módulos del sistema y casos de prueba del proyecto SCP_Casetas.

---

## Matriz de Trazabilidad

| HU | Descripción HU | RF Relacionado | Descripción RF | Módulo | Caso(s) de Prueba |
|----|----------------|----------------|----------------|--------|-------------------|
| HU-001 | Importación de archivos | RF-01 | Importación de archivos | Importación y Procesamiento | TC-001, TC-002 |
| HU-001 | Importación de archivos | RF-02 | Procesamiento de información | Importación y Procesamiento | TC-003 |
| HU-002 | Normalización mediante catálogos | RF-02 | Procesamiento de información | Importación y Procesamiento | TC-004 |
| HU-002 | Normalización mediante catálogos | RF-05 | Validación de costos | Validación Operativa | TC-005 |
| HU-003 / HU-004 | Validación automática de costos | RF-05 | Validación de costos | Validación Operativa | TC-006 |
| HU-004 | Gestión de TAGs / identificación operativa | RF-03 | Validación por viaje | Validación Operativa | TC-007 |
| HU-005 | Trazabilidad de validaciones | RF-10 | Trazabilidad de validaciones | Trazabilidad | TC-010 |
| HU-006 | Interfaz guiada para el usuario | RF-01 / RF-02 | Importación y procesamiento | Importación y Procesamiento | TC-011 |
| HU-001 Operativa | Validación automatizada de casetas operativas | RF-03 | Validación por viaje | Validación Operativa | TC-008 |
| HU-001 Operativa | Validación automatizada de casetas operativas | RF-04 | Identificación de casetas no autorizadas | Validación Operativa | TC-009 |
| HU-002 Operativa | Importación directa de archivos del portal | RF-01 | Importación de archivos | Importación y Procesamiento | TC-001, TC-002 |
| HU-003 Operativa | Normalización mediante catálogos | RF-02 | Procesamiento de información | Importación y Procesamiento | TC-004 |
| HU-004 Operativa | Validación automática de costos | RF-05 | Validación de costos | Validación Operativa | TC-006 |
| HU-005 Operativa | Identificación de casetas no autorizadas | RF-04 | Identificación de casetas no autorizadas | Validación Operativa | TC-009 |
| HU-006 Operativa | Gestión de incidencias operativas | RF-07 | Gestión de incidencias | Gestión de Incidencias | TC-012 |
| HU-007 Operativa | Generación de reportes de inconsistencias | RF-09 | Reporte de inconsistencias y resultados | Reportería y Análisis | TC-013 |
| HU-008 Operativa | Trazabilidad de validaciones | RF-10 | Trazabilidad de validaciones | Trazabilidad | TC-010 |

---

## Catálogo de Casos de Prueba Referenciados

| Código | Nombre |
|--------|--------|
| TC-001 | Importación de archivo válido |
| TC-002 | Validación de archivo inválido |
| TC-003 | Estructuración correcta de datos importados |
| TC-004 | Reconocimiento de casetas y tarifas por catálogo |
| TC-005 | Validación de asociación correcta de tarifa |
| TC-006 | Detección de diferencia de costo |
| TC-007 | Validación de datos operativos asociados al viaje |
| TC-008 | Validación de casetas por viaje |
| TC-009 | Detección de casetas fuera de ruta |
| TC-010 | Registro de trazabilidad |
| TC-011 | Flujo guiado de operación |
| TC-012 | Registro y seguimiento de incidencia |
| TC-013 | Generación y exportación de reporte |

---

## Observaciones
- Esta matriz deberá actualizarse conforme se definan casos de prueba detallados, decisiones técnicas y tareas de sprint.
- La trazabilidad es obligatoria para asegurar control funcional, calidad y soporte de auditoría.