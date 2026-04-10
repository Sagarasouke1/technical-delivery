# TA-002 - Riesgos Técnicos

## Objetivo
Registrar los riesgos técnicos iniciales del proyecto SCP_Casetas y establecer una línea base de mitigación temprana.

---

## Riesgos Identificados

| ID | Riesgo | Descripción | Impacto | Mitigación Inicial |
|----|--------|-------------|---------|--------------------|
| RT-001 | Cambio de formato del portal PASE | El archivo de entrada puede variar en estructura o contenido respecto a lo esperado | Alto | Diseñar validaciones configurables y control de errores de carga |
| RT-002 | Volumen alto de datos | El procesamiento de grandes volúmenes puede afectar tiempos de respuesta o análisis | Alto | Considerar pruebas de rendimiento y diseño eficiente de procesamiento |
| RT-003 | Errores en asignación | Puede existir información operativa o relación de datos incorrecta | Medio | Implementar validaciones específicas y reglas de consistencia |
| RT-004 | Catálogos desactualizados | Tarifas o catálogos pueden no reflejar información vigente | Alto | Establecer control de actualización de catálogos |
| RT-005 | Dependencia de sistemas externos internos | La validación puede depender de disponibilidad de SCP, ZAM o accesos corporativos | Medio | Identificar puntos críticos de integración y fallback operativo |
| RT-006 | Ambigüedad operativa en incidencias | Algunas justificaciones pueden depender de interpretación humana no estandarizada | Medio | Formalizar tipos de incidencia, criterios y responsables |
| RT-007 | Insuficiente trazabilidad | Si no se registra adecuadamente la acción del usuario, se debilita auditoría | Alto | Diseñar bitácora obligatoria desde el inicio |
| RT-008 | Errores de importación por manipulación previa | El usuario puede intentar cargar archivos alterados manualmente | Medio | Validar origen, estructura y consistencia del archivo cargado |

---

## Clasificación General del Riesgo
**Nivel global inicial:** Medio - Alto

---

## Recomendaciones
- Incorporar control de validación de archivo desde el primer sprint.
- Diseñar catálogo y reglas de negocio con control de vigencia.
- No diferir la trazabilidad para etapas posteriores.
- Considerar pruebas funcionales y de datos desde fases tempranas.