# TM-001 — Matriz de Trazabilidad HU → RF → BR → TA → SD → TC

## Información General
**Proyecto:** SCP_Casetas  
**Nombre formal:** Sistema de Gestión y Validación de Casetas  
**Código:** TM-001  
**Versión:** 1.0  
**Fecha:** 13/04/2026  
**Objetivo:** Mantener trazabilidad completa entre Historias de Usuario, Requerimientos Funcionales, Reglas de Negocio, componentes técnicos, diseño, pruebas y evidencias del proyecto.

---

## Convenciones
- **HU-N:** Historia de Usuario de Negocio
- **HU-O:** Historia de Usuario Operativa
- **RF:** Requerimiento Funcional
- **RN:** Regla de Negocio
- **RNF:** Requerimiento No Funcional
- **TA:** Análisis Técnico
- **SD:** Solution Design
- **TC:** Test Case
- **EVD:** Evidencia
- **DB:** Objeto de datos / tabla

---

## Matriz de Trazabilidad

| ID | Origen | Historia / Necesidad | RF asociados | RN / RNF asociados | Módulo / Pantalla | Datos / Tablas | TA / SD | TC sugeridos | Evidencia |
|---|---|---|---|---|---|---|---|---|---|
| TM-001 | HU-N HU-001 | Importar archivos descargados del portal PASE sin manipulación manual | RF-01, RF-02 | RNF-02, RNF-04 | Importación y Procesamiento / pantalla de carga | `tb_r_casetas_checker` | AT_HU-001, SD-004 | TC-001 Importación válida, TC-003 Manejo de error de formato | Pantalla carga de archivo |
| TM-002 | HU-N HU-002 / HU-O HU-003 | Normalización mediante catálogos de casetas, ejes y tarifas | RF-02, RF-05 | RN-04, RNF-01 | Procesamiento / catálogos / actualización de precios | `tb_c_casetas_tarifas` | AT_HU-002, SD-006 | TC-004 Reconocimiento de caseta, TC-005 asociación de tarifa | Pantalla actualización de precios |
| TM-003 | HU-N HU-003 / HU-O HU-004 | Validación automática de costos y detección de diferencias | RF-05, RF-06 | RN-04, RNF-01, RNF-04 | Validación Operativa / Summary resultados | `tb_r_casetas_checker`, `tb_c_casetas_tarifas` | AT_HU-002, SD-004 | TC-006 Detección de costo incorrecto, TC-007 cobro duplicado | Pantalla Result Summary |
| TM-004 | HU-N HU-004 | Gestión de TAGs y diferenciación entre TAG fijo y compartido | RF-02 | RN-08 | Procesamiento de viaje | Datos importados / TAG | AT_HU-003 | TC-008 Identificación de TAG | Evidencia de procesamiento |
| TM-005 | HU-N HU-005 / HU-O HU-008 | Trazabilidad de validaciones, registro de usuario, fecha y acción | RF-10 | RNF-04, RNF-05 | Histórico / aprobación / rechazo | `tb_r_checker_auth`, `tb_r_casetas_checker` | AT_HU-004, SD-005 | TC-009 Registro de acción, TC-010 consulta histórica | Pantalla histórico |
| TM-006 | HU-N HU-006 | Interfaz guiada para usuario no especializado | RF-01, RF-08 | RNF-02 | Flujo guiado de importación, confirmación y operación | N/A | SD-004 | TC-011 flujo guiado, TC-012 validaciones visuales | Confirmación y selección de tipo |
| TM-007 | HU-O HU-001 | Validación automatizada de casetas por ruta, carta y parámetros operativos | RF-03, RF-04 | RN-01, RN-02, RN-03, RN-06 | Validación Operativa | `tb_r_casetas_checker` | AT_HU-002, SD-004 | TC-013 caseta fuera de ruta, TC-014 caseta faltante | Result Summary / detalle |
| TM-008 | HU-O HU-002 | Importación directa de archivos del portal con validación de formato | RF-01 | RNF-02 | Importación y Procesamiento | `tb_r_casetas_checker` | AT_HU-001 | TC-001 importación válida, TC-003 error de carga | Pantalla de carga |
| TM-009 | HU-O HU-005 | Identificación de casetas no autorizadas | RF-04 | RN-03, RN-07 | Gestión de incidencias / detalle de registros | `tb_r_casetas_checker`, `tb_r_checker_auth` | AT_HU-002 | TC-015 marcar inconsistencia, TC-016 flujo de autorización | Pantallas de aprobación / rechazo |
| TM-010 | HU-O HU-006 | Gestión de incidencias operativas y justificación | RF-07 | RN-06, RN-07 | Gestión de incidencias | `tb_r_checker_auth` | AT_HU-004, SD-005 | TC-017 registrar comentario, TC-018 vincular incidencia a caseta | Alertas por acción |
| TM-011 | HU-O HU-007 | Generación de reportes consolidados de inconsistencias | RF-09 | RNF-06 | Histórico / reportes / exportación | `tb_r_casetas_checker` | SD-004, SD-005 | TC-019 reporte por unidad, TC-020 exportación | Pantalla histórico y Excel |
| TM-012 | LR-001 | Consulta histórica con filtros avanzados y exportación | RF-09, RF-10 | RNF-02, RNF-06 | Histórico / filtros / Excel | `tb_r_casetas_checker`, `tb_r_checker_auth` | SD-004 | TC-021 filtros por económico/fecha/caseta, TC-022 exportación | Pantalla histórico con filtros |
| TM-013 | LR-001 | Actualización de precios mediante catálogo | RF-05 | RN-04, RNF-01 | Actualización de precios | `tb_c_casetas_tarifas` | SD-006 | TC-023 carga de URL de tarifas, TC-024 actualización de catálogo | Pantalla URL actualizar precios |
| TM-014 | Algoritmo | Procesamiento por TAG y fecha, loop por viajes, validación casetas y monto | RF-02, RF-03, RF-05 | RN-01, RN-02, RN-04, RN-05 | Motor de validación | `tb_r_casetas_checker`, `tb_c_casetas_tarifas` | AT_HU-002, SD-004 | TC-025 procesamiento por viaje, TC-026 cálculo de monto | Flujo técnico |
| TM-015 | Diccionario | Persistencia de resultados clasificados, empresa, achieved, estado | RF-02, RF-10 | RNF-01, RNF-04 | Persistencia / histórico | `tb_r_casetas_checker` | SD-006 | TC-027 guardado de estado, TC-028 guardado de empresa/timestamp | Evidencia DB |
| TM-016 | Diccionario | Registro de aprobación con comentario y usuario | RF-07, RF-10 | RN-07, RNF-05 | Aprobación / rechazo | `tb_r_checker_auth` | SD-005, SD-006 | TC-029 aprobación con comentario, TC-030 rechazo con comentario | Pantallas de alerta |

---

## Requerimientos Funcionales Base
- **RF-01:** Importación de archivos
- **RF-02:** Procesamiento de información
- **RF-03:** Validación por viaje
- **RF-04:** Identificación de casetas no autorizadas
- **RF-05:** Validación de tarifas
- **RF-06:** Detección de cobros duplicados o incorrectos
- **RF-07:** Registro y gestión de incidencias operativas
- **RF-08:** Consulta y visualización de resultados
- **RF-09:** Reporte de inconsistencias y resultados de validación
- **RF-10:** Trazabilidad de validaciones :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

## Reglas de Negocio Base
- **RN-01:** Un viaje puede contener múltiples casetas
- **RN-02:** Las casetas válidas dependen de la ruta autorizada
- **RN-03:** Las casetas fuera de ruta deben marcarse como inconsistencias
- **RN-04:** Los costos deben compararse contra tarifas vigentes
- **RN-05:** Los registros duplicados deben identificarse
- **RN-06:** Los viajes en vacío pueden requerir validación manual del Supervisor de Peaje
- **RN-07:** Las autorizaciones operativas pueden modificar el tratamiento de una caseta
- **RN-08:** Los TAG pueden estar asociados a una unidad o ser compartidos en casos específicos :contentReference[oaicite:19]{index=19}

## Requerimientos No Funcionales Base
- **RNF-01:** Integridad de datos
- **RNF-02:** Usabilidad
- **RNF-03:** Disponibilidad
- **RNF-04:** Trazabilidad
- **RNF-05:** Seguridad
- **RNF-06:** Reportería y análisis :contentReference[oaicite:20]{index=20}

## Tablas Base Relacionadas
- `tb_r_casetas_checker`: almacena registros importados, clasificación, timestamps y empresa. :contentReference[oaicite:21]{index=21}
- `tb_r_checker_auth`: almacena aprobación, comentario y usuario asociado a la caseta. :contentReference[oaicite:22]{index=22}
- `tb_c_casetas_tarifas`: catálogo de tarifas por ruta, caseta, tipo de vehículo y clase. :contentReference[oaicite:23]{index=23}

## Evidencias funcionales disponibles
- Confirmación de carga y selección de tipo de archivo AEO/FLA. :contentReference[oaicite:24]{index=24}
- Pantallas de summary y detalle de resultados.
- Pantallas de aprobación / rechazo con comentario.
- Pantalla de histórico con filtros y exportación.
- Pantalla de actualización de precios mediante URL.