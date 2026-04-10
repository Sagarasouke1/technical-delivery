# TA-001 - Impacto Técnico SCP / ZAM / Metabase

## Objetivo
Documentar el impacto técnico inicial del proyecto SCP_Casetas sobre sistemas, dependencias e integraciones relacionadas.

---

## Sistemas Involucrados

### 1. SCP
Sistema principal involucrado en la operación del proceso de validación y posible punto de acceso funcional para los usuarios.

**Impacto esperado:**
- Incorporación de funcionalidad de validación de casetas
- Control de acceso por roles
- Registro de trazabilidad de acciones
- Consulta de resultados del proceso
- Soporte para operación diaria

---

### 2. ZAM
Sistema requerido como fuente de consulta de rutas autorizadas o información operativa relacionada con validación por viaje.

**Impacto esperado:**
- Consulta de información de rutas autorizadas
- Validación contra datos operativos
- Apoyo para identificación de casetas fuera de ruta

---

### 3. Metabase
Herramienta contemplada para consumo analítico y explotación de información consolidada.

**Impacto esperado:**
- Consulta analítica de resultados
- Explotación de reportes de inconsistencias
- Generación de indicadores operativos
- Apoyo a supervisión y seguimiento

---

### 4. Sistemas de Autenticación Corporativa
Mecanismo previsto para control de acceso y seguridad del sistema.

**Impacto esperado:**
- Validación de usuarios
- Asignación de permisos por rol
- Registro de accesos
- Protección de información sensible

---

## Impacto por Componente Funcional

### Importación y Procesamiento
- Requiere capacidad de cargar archivos del portal PASE
- Validación de formato
- Estructuración de información

### Validación Operativa
- Requiere reglas de negocio para comparación de rutas, costos, duplicados y consistencia

### Gestión de Incidencias
- Requiere almacenamiento de justificaciones, observaciones y evidencias

### Reportería y Análisis
- Requiere consolidación de resultados y exportación

### Trazabilidad
- Requiere registro histórico de usuario, fecha y acción

---

## Impacto en Infraestructura
- Requiere operación en red corporativa interna
- Compatibilidad con navegadores corporativos
- Acceso a sistemas involucrados
- Disponibilidad de catálogos vigentes

---

## Consideraciones Iniciales
- El diseño técnico deberá minimizar dependencia manual.
- Se deberá proteger la integridad de datos.
- La solución deberá soportar operación diaria.
- La arquitectura deberá contemplar trazabilidad y seguridad desde el inicio.