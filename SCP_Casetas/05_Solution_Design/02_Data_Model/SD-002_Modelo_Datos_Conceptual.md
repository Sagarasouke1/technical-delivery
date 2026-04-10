# SD-002 - Modelo de Datos Conceptual

## Objetivo
Definir las entidades conceptuales principales requeridas para soportar la operación del sistema SCP_Casetas, de acuerdo con los requerimientos funcionales y operativos documentados.

---

## Entidades Conceptuales Propuestas

### 1. Usuario
Representa a la persona que interactúa con el sistema.

**Atributos sugeridos:**
- id_usuario
- nombre
- rol
- área
- estatus
- fecha_alta

---

### 2. Archivo_Importado
Representa cada archivo cargado desde el portal PASE.

**Atributos sugeridos:**
- id_archivo
- nombre_archivo
- fecha_carga
- usuario_carga
- estatus_procesamiento
- observaciones

---

### 3. Registro_Caseta
Representa cada registro individual derivado del archivo importado.

**Atributos sugeridos:**
- id_registro
- id_archivo
- numero_economico
- fecha_hora
- caseta
- importe
- clase_vehicular
- tag

---

### 4. Viaje
Representa el viaje contra el cual se validarán registros de caseta.

**Atributos sugeridos:**
- id_viaje
- numero_viaje
- unidad
- fecha_inicio
- fecha_fin
- tipo_operacion
- carta_instruccion

---

### 5. Ruta_Autorizada
Representa la ruta esperada o autorizada para un viaje.

**Atributos sugeridos:**
- id_ruta
- id_viaje
- origen
- destino
- observaciones

---

### 6. Caseta_Autorizada
Representa las casetas esperadas dentro de una ruta.

**Atributos sugeridos:**
- id_caseta_autorizada
- id_ruta
- nombre_caseta
- orden
- sentido
- tarifa_esperada

---

### 7. Tarifa
Representa el valor esperado de cobro para una caseta.

**Atributos sugeridos:**
- id_tarifa
- caseta
- clase_vehicular
- importe_vigente
- fecha_vigencia_inicio
- fecha_vigencia_fin
- estatus

---

### 8. Validacion
Representa el resultado del análisis de un registro o conjunto de registros.

**Atributos sugeridos:**
- id_validacion
- id_registro
- id_viaje
- resultado
- tipo_inconsistencia
- diferencia_importe
- duplicado
- fecha_validacion
- usuario_validacion

---

### 9. Incidencia
Representa una observación o excepción operativa asociada a una validación.

**Atributos sugeridos:**
- id_incidencia
- id_validacion
- tipo_incidencia
- justificacion
- observaciones
- estatus
- fecha_registro
- usuario_registro

---

### 10. Evidencia
Representa archivos o soportes asociados a una incidencia.

**Atributos sugeridos:**
- id_evidencia
- id_incidencia
- nombre_archivo
- ruta_archivo
- fecha_carga
- usuario_carga

---

### 11. Historial_Acciones
Representa la trazabilidad del sistema.

**Atributos sugeridos:**
- id_historial
- id_usuario
- accion
- fecha_hora
- modulo
- referencia
- detalle

---

## Relaciones Conceptuales
- Un usuario puede cargar muchos archivos.
- Un archivo puede contener muchos registros de caseta.
- Un viaje puede tener una ruta autorizada.
- Una ruta autorizada puede tener muchas casetas autorizadas.
- Un registro de caseta puede participar en una validación.
- Una validación puede generar cero o muchas incidencias.
- Una incidencia puede tener cero o muchas evidencias.
- Todo usuario puede generar múltiples registros de historial.

---

## Observaciones
Este modelo es conceptual y deberá madurar a modelo lógico y posteriormente a modelo físico una vez se definan decisiones técnicas y estructura de persistencia.