# QA Configuration - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar la configuración funcional y operativa del ambiente QA del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Propósito del Ambiente
El ambiente QA está destinado a:

- validación técnica controlada
- pruebas funcionales
- validación de conciliación
- validación de persistencia BI
- validación previa a liberación productiva

---

## 3. Características Generales
- Ambiente de calidad
- Estructura de `.env` igual a DEV y PROD
- Credenciales y base de datos similares a DEV
- Debe representar el comportamiento esperado antes de pasar a PROD
- No debe usarse como ambiente oficial de operación

---

## 4. Componentes a Validar en QA
- scripts ETL
- queries SQL
- vista de conciliación
- tabla persistida
- capa BI actual
- tablas de control ETL si se implementan
- validaciones funcionales y analíticas

---

## 5. Estructura del `.env`
La estructura del archivo `.env` en QA debe ser igual a la definida para el proyecto.

Debe incluir:
- variables de conexión a SQL Server
- variables de conexión a MySQL / MariaDB
- batch size
- rutas de logs
- rutas de queries
- rutas de Excel
- rutas de respaldo

**Nota:**  
Aunque DEV y QA son similares en credenciales y bases, todo valor real debe mantenerse fuera de la documentación pública del repositorio.

---

## 6. Reglas de Uso
1. Solo deben llegar a QA cambios ya probados en DEV.
2. QA debe validar comportamiento técnico y funcional.
3. Toda observación detectada en QA debe documentarse.
4. Ningún cambio debe pasar a PROD sin validación en QA.

---

## 7. Validaciones Requeridas en QA
- ejecución correcta de ETLs
- consistencia de datos en tablas analíticas
- consistencia de vista de conciliación
- consistencia de tabla persistida
- validación de dashboard
- validación de filtros activos
- validación de logs y respaldo

---

## 8. Criterio de Salida de QA
Un cambio puede salir de QA cuando:
- no presenta error técnico crítico
- la conciliación funciona correctamente
- la tabla persistida refleja correctamente la vista
- el dashboard es consistente
- existe validación suficiente para pasar a PROD