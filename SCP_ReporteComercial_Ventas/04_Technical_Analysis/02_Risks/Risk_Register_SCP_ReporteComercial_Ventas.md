# Risk Register - SCP_ReporteComercial_Ventas

## 1. Objetivo
Registrar y controlar de forma estructurada los riesgos técnicos, operativos y analíticos del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Escala de Evaluación

### Impacto
- Bajo
- Medio
- Alto
- Crítico

### Probabilidad
- Baja
- Media
- Alta

---

## 3. Registro de Riesgos

| ID | Riesgo | Tipo | Impacto | Probabilidad | Estado | Mitigación | Responsable sugerido |
|----|--------|------|---------|--------------|--------|------------|----------------------|
| R-001 | Diferencias de fecha entre facturación y contabilidad | Analítico | Alto | Alta | Abierto | Validar lógica por referencia y revisar fechas en BI | TI / BI |
| R-002 | Referencias inconsistentes | Datos | Alto | Media | Abierto | Normalización y validación de muestra | TI / Data |
| R-003 | Reproceso no controlado de Excel | Operativo | Medio-Alto | Alta | Abierto | staging + control de archivos procesados | TI / Data |
| R-004 | Configuración incorrecta del `.env` | Técnico | Alto | Media | Abierto | checklist técnico + `.env.template` | TI |
| R-005 | Falta de tablas de control ETL | Técnico | Medio-Alto | Alta | Abierto | implementar `etl_control_ejecucion` y `etl_log_errores` | TI / Data |
| R-006 | Falta de Cliente en capa analítica | Funcional / BI | Alto | Alta | Abierto | documentar gap e integrar dimensión futura | BI / Negocio / TI |
| R-007 | Persistencia manual de tabla de conciliación | Operativo / BI | Alto | Alta | Abierto | formalizar proceso y automatización futura | TI / BI |
| R-008 | Indisponibilidad del ambiente DEV | Infraestructura | Alto | Alta | Abierto | seguimiento y escalación de solicitud de encendido | TI / Infra |
| R-009 | Falta de staging para Excel | Técnico / Datos | Medio | Alta | Abierto | crear `stg_poliza_ingresos_excel` | TI / Data |
| R-010 | Desactualización de dashboard por no refrescar tabla persistida | BI / Operativo | Alto | Media | Abierto | definir frecuencia y proceso de actualización | BI / TI |
| R-011 | Promoción no controlada entre ambientes | Gobierno técnico | Alto | Media | Abierto | reforzar DEV → QA → PROD | Líder Técnico |
| R-012 | Cambio en la vista sin regenerar tabla persistida | BI / Datos | Alto | Media | Abierto | documentar y validar post-deployment | TI / BI |

---

## 4. Riesgos Críticos / Prioritarios

### R-006 Falta de Cliente en capa analítica
**Descripción:**  
El dashboard esperado contempla Cliente, pero actualmente esa dimensión no existe en la capa analítica final.

**Impacto:** Alto  
**Probabilidad:** Alta  
**Efecto:** limitación funcional del dashboard.

**Mitigación propuesta:**  
documentar el gap y planear integración futura.

---

### R-007 Persistencia manual de tabla de conciliación
**Descripción:**  
La tabla `tb_mb_conciliacion_fact_vs_conta_2026` se genera manualmente mediante query.

**Impacto:** Alto  
**Probabilidad:** Alta  
**Efecto:** riesgo de desactualización, dependencia operativa y menor trazabilidad.

**Mitigación propuesta:**  
definir estrategia formal de refresco y posteriormente automatizar.

---

### R-008 Indisponibilidad del ambiente DEV
**Descripción:**  
El ambiente DEV está apagado al momento de esta documentación.

**Impacto:** Alto  
**Probabilidad:** Alta  
**Efecto:** bloqueo del desarrollo, validación técnica y promoción controlada a QA.

**Mitigación propuesta:**  
dar seguimiento al correo enviado el **13/04/2026 a las 09:54 AM** a los Ingenieros Oswaldo y Daniela; escalar si continúa sin respuesta.

---

## 5. Revisión del Registro
Este registro debe revisarse cuando:
- cambie el modelo de datos
- se agregue Cliente
- se automaticen procesos
- cambie la estrategia de persistencia
- cambie la disponibilidad de ambientes
- existan incidentes relevantes

---

## 6. Conclusión
El proyecto SCP_ReporteComercial_Ventas presenta riesgos manejables, pero varios de ellos son de impacto alto por su relación directa con datos, BI, operación y ambientes. Este registro debe mantenerse vivo y actualizado para soportar la toma de decisiones técnicas y operativas.