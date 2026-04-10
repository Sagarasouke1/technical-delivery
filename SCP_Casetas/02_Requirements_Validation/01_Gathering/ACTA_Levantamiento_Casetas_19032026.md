# Acta de Levantamiento - SCP_Casetas

## Información General
**Proyecto:** SCP_Casetas  
**Nombre formal:** Sistema de Gestión y Validación de Casetas  
**Código de referencia:** LR-001  
**Fecha:** 19/03/2026  
**Tipo:** Desarrollo Interno

---

## Objetivo de la Sesión
Definir de forma clara los requerimientos funcionales, no funcionales, reglas de negocio, interfaces, usuarios y condiciones técnicas necesarias para el desarrollo del sistema de validación y gestión de casetas.

---

## Áreas Involucradas
- Liquidaciones / Operaciones
- TI

---

## Sistemas Involucrados
- SCP
- ZAM
- Metabase
- Sistemas de autenticación corporativa

---

## Problemática Expuesta
Se documentó que el proceso actual de validación de casetas se basa en:
- Descarga manual de archivos desde el portal PASE
- Procesamiento en hojas de cálculo
- Validación visual de rutas y costos
- Consulta a múltiples portales
- Revisión manual contra cartas de instrucción y liquidaciones
- Gestión manual de incidencias y aclaraciones

Esto genera alto esfuerzo operativo, dependencia de conocimiento experto, riesgo elevado de errores humanos, falta de trazabilidad, demoras en liquidaciones y dificultad para auditoría.

---

## Acuerdos Funcionales Principales
- El sistema deberá permitir importar archivos descargados del portal PASE sin modificaciones manuales.
- El sistema deberá procesar la información importada y estructurarla por número económico, fecha y hora, caseta, importe, clase vehicular y TAG.
- El sistema deberá validar las casetas asociadas a un viaje considerando rango de fechas, carta de instrucciones, ruta autorizada y casetas esperadas.
- El sistema deberá detectar casetas fuera de ruta o no contempladas.
- El sistema deberá comparar importes contra tarifas esperadas.
- El sistema deberá identificar cobros duplicados.
- El sistema deberá permitir registro de incidencias, observaciones, justificaciones y evidencias.
- El sistema deberá generar reportes consolidados por unidad, viaje, tipo de inconsistencia, periodo, resultado de validación y estado de atención.
- El sistema deberá registrar trazabilidad de usuario, fecha y acciones realizadas.

---

## Acuerdos No Funcionales Principales
- Se deberá cuidar la integridad de datos.
- La interfaz deberá ser sencilla y orientada a operación diaria.
- La disponibilidad mínima esperada será de 99% mensual en horario operativo.
- Deberá existir control por roles, autenticación y registro de accesos.
- La solución deberá permitir exportación de datos y consulta analítica.

---

## Usuarios Identificados
### Usuario Operativo (Liquidaciones)
Descarga archivos, valida casetas, detecta inconsistencias, registra incidencias e integra costos a liquidaciones.

### Usuario Supervisor / Administrativo
Analiza información, revisa anomalías, da seguimiento a autorizaciones y consulta reportes.

### Usuario Operaciones (DOM / IE / DED / MAR)
Registra motivos de autorización, justifica casetas inconsistentes y apoya en la resolución de discrepancias.

---

## Dependencias Identificadas
- Disponibilidad de archivos del portal PASE
- Usuarios autorizados
- Catálogos de casetas y costos
- Acceso a la red corporativa interna
- Compatibilidad con navegadores soportados
- Integración con SCP, ZAM y Metabase

---

## Riesgos Identificados
- Cambios en formato del portal
- Volumen alto de datos
- Errores en asignación
- Información de catálogo incorrecta o no vigente

---

## Próximos Pasos
1. Consolidar reglas de negocio.
2. Consolidar criterios de aceptación.
3. Construir matriz de trazabilidad.
4. Elaborar análisis técnico.
5. Elaborar diseño de solución.
6. Preparar plan de pruebas.