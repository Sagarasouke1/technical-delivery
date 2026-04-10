# AC-001 - Criterios de Aceptación Consolidados

## Objetivo
Consolidar en un solo documento los criterios de aceptación funcionales definidos en las historias de usuario del proyecto SCP_Casetas.

---

## 1. Importación de Archivos
- El sistema debe permitir importar archivos descargados del portal sin modificaciones manuales.
- La información debe cargarse sin alterar su estructura base.
- El sistema debe validar compatibilidad del formato.
- Ante un archivo inválido, el sistema debe mostrar un mensaje claro indicando el error.

---

## 2. Normalización y Catálogos
- El sistema debe reconocer casetas mediante catálogo.
- El sistema debe reconocer ejes, costos o tarifas según catálogos estructurados.
- Debe clasificar registros automáticamente.
- Debe permitir actualización controlada de catálogos.

---

## 3. Validación de Costos
- El sistema debe comparar costos registrados contra tarifas esperadas.
- Debe detectar diferencias de costo.
- Debe identificar cobros incorrectos o variaciones.
- Debe permitir revisión de diferencias detectadas.

---

## 4. Casetas No Autorizadas
- El sistema debe detectar casetas fuera de ruta.
- Debe marcar registros no contemplados o excedentes.
- Debe permitir revisión operativa de los casos detectados.

---

## 5. Cobros Duplicados
- El sistema debe identificar duplicados o cruces múltiples para una misma caseta.
- Debe señalar los registros para revisión.

---

## 6. Gestión de Incidencias
- El sistema debe permitir registrar tipo de incidencia.
- Debe asociar la incidencia al registro correspondiente.
- Debe mantener historial de incidencias.
- Debe permitir justificación operativa.

---

## 7. Reportes
- El sistema debe generar reportes consolidados por unidad y viaje.
- Debe incluir tipo de inconsistencia.
- Debe permitir exportación.
- Debe mostrar resultados de validación y estado de atención.

---

## 8. Trazabilidad
- El sistema debe registrar usuario, fecha y acción.
- Debe permitir consulta histórica.
- No debe permitir alteración de registros de trazabilidad.

---

## 9. Interfaz y Uso
- El flujo de operación debe ser claro y secuencial.
- Deben existir mensajes de ayuda.
- Deben existir validaciones en cada paso.
- La interfaz debe facilitar operación por usuarios no especializados.