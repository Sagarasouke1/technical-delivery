# SD-003 - Flujo de Validación de Casetas

## Objetivo
Documentar el flujo funcional de alto nivel del proceso de validación de casetas dentro del proyecto SCP_Casetas.

---

## Flujo General

### Paso 1. Carga de archivo
El usuario operativo ingresa al sistema y selecciona un archivo descargado del portal PASE para iniciar el proceso.

### Paso 2. Validación de formato
El sistema valida que el archivo sea compatible y que pueda procesarse sin modificaciones manuales previas.

### Paso 3. Procesamiento de información
El sistema procesa el archivo y estructura la información por:
- Número económico
- Fecha y hora
- Caseta
- Importe
- Clase vehicular
- TAG

### Paso 4. Asociación operativa
El sistema relaciona la información importada con el viaje correspondiente, considerando:
- Rango de fechas del viaje
- Carta de instrucciones
- Ruta autorizada
- Casetas esperadas

### Paso 5. Validación operativa
El sistema analiza si las casetas registradas:
- Corresponden a la ruta esperada
- Presentan diferencias de costo
- Son duplicadas
- Requieren aclaración

### Paso 6. Identificación de inconsistencias
El sistema marca como inconsistencias los registros que presenten:
- Casetas fuera de ruta
- Diferencias de tarifa
- Duplicados
- Registros no contemplados

### Paso 7. Gestión de incidencias
Cuando aplique, el usuario registra:
- Tipo de incidencia
- Justificación
- Observaciones
- Evidencias

### Paso 8. Aclaraciones operativas
Los usuarios de operación pueden revisar observaciones, justificar registros y apoyar en la resolución de discrepancias detectadas.

### Paso 9. Generación de resultados
El sistema clasifica y presenta resultados de validación, tales como:
- Válido
- Inconsistente
- En aclaración
- Autorizado
- Rechazado

### Paso 10. Reporte consolidado
El sistema genera reportes organizados por:
- Unidad
- Viaje
- Tipo de inconsistencia
- Periodo
- Resultado
- Estado de atención

### Paso 11. Registro de trazabilidad
Cada acción relevante del proceso queda registrada con usuario, fecha y acción, para fines de control y auditoría.

---

## Resultado Esperado
Contar con un proceso estructurado, repetible, trazable y menos dependiente de trabajo manual para la validación de casetas.