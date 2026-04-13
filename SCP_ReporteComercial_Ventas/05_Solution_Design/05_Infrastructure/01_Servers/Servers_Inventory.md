# Servers Inventory - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar el inventario de ambientes, su propósito funcional y su relación con el proyecto SCP_ReporteComercial_Ventas.

---

## 2. Ambientes Disponibles

### 2.1 DEV
**Nombre:** Ambiente de Desarrollo  
**Propósito:**  
- desarrollo de scripts
- pruebas técnicas iniciales
- validación de cambios SQL
- revisión de arquitectura y modelo de datos

**Estado actual:**  
Apagado / no disponible al momento de esta documentación.

**Impacto actual:**  
- retrasa desarrollo
- retrasa validación técnica
- retrasa promoción a QA

**Observación:**  
Se solicitó encendido por correo a los Ingenieros Oswaldo y Daniela el 13/04/2026 a las 09:54 AM, sin respuesta al momento.

---

### 2.2 QA
**Nombre:** Ambiente de Calidad  
**Propósito:**  
- pruebas técnicas
- pruebas funcionales
- validación previa a PROD
- revisión de consistencia analítica

**Estado actual:**  
Disponible sujeto a validación operativa.

---

### 2.3 PROD
**Nombre:** Ambiente Productivo  
**Propósito:**  
- operación oficial del componente
- consulta final en BI
- soporte a usuarios de negocio

**Estado actual:**  
Activo como ambiente objetivo de operación.

---

## 3. Componentes por Ambiente

### DEV
- scripts Python de desarrollo
- SQL de validación
- cambios en tablas y vistas
- pruebas unitarias y técnicas

### QA
- validación de procesos ETL
- validación de conciliación
- validación de dashboard
- validación pre-liberación

### PROD
- ejecución oficial
- persistencia analítica oficial
- dashboard final en Metabase
- respaldo controlado

---

## 4. Dependencias Relacionadas
- disponibilidad del ambiente
- permisos de acceso
- configuración correcta del `.env`
- conectividad con SQL Server
- conectividad con MySQL / MariaDB
- disponibilidad de Metabase

---

## 5. Recomendaciones
1. mantener actualizado el estado de cada ambiente
2. registrar indisponibilidades como riesgo y dependencia
3. no promover cambios sin validación previa en DEV y QA
4. documentar evidencia de liberación por ambiente