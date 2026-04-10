# BR-001 - Reglas de Negocio Casetas

## Objetivo
Consolidar las reglas de negocio que regirán el proceso de validación automatizada de casetas dentro del proyecto SCP_Casetas.

---

## Reglas de Negocio

### RN-01
Un viaje puede contener múltiples casetas.

### RN-02
Las casetas válidas dependen de la ruta autorizada.

### RN-03
Las casetas fuera de ruta deben marcarse como inconsistencias.

### RN-04
Los costos deben compararse contra tarifas vigentes.

### RN-05
Los registros duplicados deben identificarse como posibles cobros duplicados o cruces múltiples para una misma caseta.

### RN-06
Las autorizaciones operativas pueden modificar el tratamiento de una caseta dentro del proceso de validación.

### RN-07
Toda incidencia deberá registrar tipo, justificación, observaciones y, cuando aplique, evidencias asociadas.

### RN-08
Los resultados de validación deberán clasificarse al menos como válido, inconsistente, en aclaración, autorizado o rechazado.

### RN-09
Toda validación deberá registrar usuario, fecha y acción realizada, sin permitir alteración posterior.

### RN-10
La importación de archivos deberá realizarse sobre archivos descargados del portal PASE sin modificaciones manuales previas.

---

## Consideraciones Operativas
- La validación por viaje deberá considerar fechas del viaje, carta de instrucciones, ruta autorizada y casetas esperadas.
- Las incidencias deberán resolverse dentro del plazo operativo definido por negocio.
- Los catálogos de casetas y tarifas deberán mantenerse vigentes y controlados.

---

## Uso del Documento
Estas reglas sirven como base para:
- análisis técnico
- diseño de validaciones
- construcción de casos de prueba
- revisión funcional
- trazabilidad de cumplimiento