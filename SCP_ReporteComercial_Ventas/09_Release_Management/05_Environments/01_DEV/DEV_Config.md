# DEV Configuration - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar la configuración funcional y operativa del ambiente DEV del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Propósito del Ambiente
El ambiente DEV está destinado a:

- desarrollo de scripts Python
- validación de queries SQL
- creación y ajuste de tablas
- validación técnica inicial
- pruebas unitarias y técnicas
- revisión preliminar de arquitectura y modelo de datos

---

## 3. Características Generales
- Ambiente de desarrollo
- Estructura de `.env` igual a QA y PROD
- Credenciales y base de datos similares a QA
- No debe considerarse fuente oficial para negocio
- Todo cambio debe validarse aquí antes de pasar a QA

---

## 4. Componentes a Validar en DEV
- `FacturacionElectronica.py`
- `PolizaContableIngresos.py`
- `PolizaIngresosExcel.py`
- `BackupMariadb.py`
- `FacturacionElectronica.sql`
- `PolizaContableIngresos.sql`
- `vw_mb_conciliacion_fact_vs_conta_2026`
- tablas analíticas
- tablas de control ETL propuestas

---

## 5. Estructura del `.env`
La estructura del archivo `.env` en DEV debe ser igual a la definida para el proyecto, incluyendo:

- variables de SQL Server
- variables de MySQL / MariaDB
- batch size
- rutas de logs
- rutas de queries
- rutas de Excel
- rutas de respaldo

**Nota:**  
No deben documentarse credenciales reales en este archivo, únicamente la estructura y lineamientos de configuración.

---

## 6. Reglas de Uso
1. Todo cambio técnico debe probarse primero en DEV.
2. No se debe promover un cambio a QA sin validación mínima en DEV.
3. Todo error identificado en DEV debe documentarse antes de avanzar.
4. Toda modificación relevante debe reflejarse en documentación y control de versiones.

---

## 7. Estado Actual del Ambiente
**Estado actual:** Apagado / no disponible al momento de esta documentación.

**Impacto:**  
La indisponibilidad del ambiente DEV bloquea:
- validaciones técnicas
- pruebas de ajustes
- creación o modificación controlada de objetos
- promoción segura hacia QA

**Acción realizada:**  
Se envió correo solicitando encendido del ambiente DEV a los Ingenieros Oswaldo y Daniela el día **13/04/2026 a las 09:54 AM**.

**Estatus actual:**  
Sin respuesta al momento de esta documentación.

---

## 8. Validaciones Recomendadas en DEV
- conectividad a SQL Server
- conectividad a MySQL / MariaDB
- ejecución de ETLs
- validación de vista
- validación de tabla persistida
- validación de logs
- validación de tablas de control ETL
- pruebas de rollback técnico

---

## 9. Criterio de Salida de DEV
Un cambio puede salir de DEV cuando:
- ejecuta sin error crítico
- los objetos se crean correctamente
- los datos son consistentes a nivel técnico
- existe evidencia mínima de validación
- se encuentra listo para QA