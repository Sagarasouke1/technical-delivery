# SD-001 - Arquitectura de Solución Casetas

## Objetivo
Definir la arquitectura funcional de alto nivel para el proyecto SCP_Casetas, estableciendo los componentes principales, su responsabilidad y su relación con sistemas e integraciones involucradas.

---

## Vista General
La solución SCP_Casetas se concibe como un sistema web corporativo orientado a la validación automatizada de casetas, soportado por componentes modulares que permiten importar, procesar, validar, registrar incidencias, generar reportes y conservar trazabilidad del proceso.

---

## Componentes Principales

### 1. Módulo de Importación y Procesamiento
**Responsabilidad:**
- Cargar archivos descargados del portal PASE
- Validar formato del archivo
- Procesar información importada
- Estructurar datos operativos

**Entradas esperadas:**
- Número económico
- Fecha y hora
- Caseta
- Importe
- Clase vehicular
- TAG

---

### 2. Módulo de Validación Operativa
**Responsabilidad:**
- Validar casetas por viaje
- Comparar contra ruta autorizada
- Detectar casetas no autorizadas
- Validar costos contra tarifas
- Detectar cobros duplicados

**Elementos considerados:**
- Rango de fechas del viaje
- Carta de instrucciones
- Ruta autorizada
- Casetas esperadas
- Tarifas vigentes

---

### 3. Módulo de Gestión de Incidencias
**Responsabilidad:**
- Registrar incidencias operativas
- Almacenar justificaciones
- Guardar observaciones
- Relacionar evidencias
- Dar seguimiento a casos observados

---

### 4. Módulo de Reportería y Análisis
**Responsabilidad:**
- Generar reportes consolidados
- Consultar inconsistencias
- Exportar resultados
- Apoyar análisis operativo y administrativo

**Dimensiones mínimas del reporte:**
- Unidad
- Viaje
- Tipo de inconsistencia
- Periodo
- Resultado de validación
- Estado de atención

---

### 5. Módulo de Trazabilidad
**Responsabilidad:**
- Registrar usuario, fecha y acción
- Mantener historial
- Proveer evidencia para auditoría
- Impedir alteración posterior de registros

---

## Integraciones Relacionadas
- SCP
- ZAM
- Metabase
- Sistemas de autenticación corporativa

---

## Principios de Diseño
- Operación orientada a usuario corporativo
- Minimización de trabajo manual
- Integridad de datos
- Trazabilidad completa
- Seguridad por roles
- Soporte a operación diaria
- Escalabilidad documental y funcional

---

## Observaciones
Esta arquitectura es de nivel funcional y deberá evolucionar posteriormente a una arquitectura lógica y técnica más detallada.