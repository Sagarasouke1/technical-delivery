# SCP_ReporteComercial_Ventas

![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![SQL](https://img.shields.io/badge/SQL-SQL%20Server%20%7C%20MariaDB-orange)

## Resumen Ejecutivo
Proyecto orientado a la conciliación entre facturación y contabilidad, con el objetivo de comparar de forma estructurada lo vendido/facturado contra lo contabilizado, consolidando la información en una capa analítica para consumo en BI.

## Objetivo
Desarrollar un proceso de extracción, transformación y carga de información desde ZAM hacia la base de datos analítica, permitiendo comparar importes facturados contra importes contabilizados y publicar el resultado en un dashboard de Metabase con filtros por Operación, Cliente y Rango de Fechas.

## Alcance
### Alcance actual
- Revisión por mes completo.
- Validación de cierre contable vs facturación.
- Persistencia de resultados para consulta en BI.

### Visión evolutiva
- Comparación día a día.
- Trazabilidad operativa continua.
- Mayor automatización de controles de calidad y monitoreo ETL.

## Arquitectura General
```text
Sistema ZAM (SQL Server)
   ↓
Procesos ETL (Python + SQL)
   ├── FacturacionElectronica.py
   ├── PolizaContableIngresos.py
   ├── PolizaIngresosExcel.py
   └── BackupMariadb.py
   ↓
Base Analítica (MySQL / MariaDB)
   ├── dm_factura_electronica_totales
   ├── cont_polizadet_ingresos_2026
   ├── cont_polizadet_ingresos_original_2026
   ├── vw_mb_conciliacion_fact_vs_conta_2026
   └── tb_mb_conciliacion_fact_vs_conta_2026
   ↓
Metabase
```
## 🚀 Componentes Técnicos

### 5.1 Extracción de Facturación
* **Script:** `FacturacionElectronica.py`
* **Query:** `FacturacionElectronica.sql`
* **Destino:** `dm_factura_electronica_totales`

### 5.2 Extracción de Contabilidad
* **Script:** `PolizaContableIngresos.py`
* **Query:** `PolizaContableIngresos.sql`
* **Destino:** `cont_polizadet_ingresos_2026`

### 5.3 Carga Auxiliar (Excel)
* **Script:** `PolizaIngresosExcel.py`
* **Destino:** `cont_polizadet_ingresos_original_2026`

### 5.4 Conciliación y Persistencia
* **Vista:** `vw_mb_conciliacion_fact_vs_conta_2026`
* **Tabla Persistida:** `tb_mb_conciliacion_fact_vs_conta_2026`

### 5.5 Respaldo (Backup)
* **Script:** `BackupMariadb.py`
* **Objetivo:** Respaldo de la tabla de conciliación principal.

## 🛠 Tecnologías Utilizadas

* **Lenguaje:** Python (Pandas, python-dotenv)
* **Bases de Datos:** SQL Server, MySQL / MariaDB
* **Conectores:** `pyodbc`, `pymysql`, `mysql.connector`
* **Herramientas de Backup:** `mariadb-dump` / `mysqldump`
* **Visualización:** Metabase

## 📋 Reglas Funcionales Principales

1.  **Comparación Core:** Contraste directo entre el importe facturado y el contabilizado.
2.  **Frecuencia:** Operativa actual mensual, con hoja de ruta hacia revisión diaria.
3.  **Dashboard BI:** El reporte final en Metabase debe ofrecer capacidades de filtrado por:
    * Operación
    * Cliente
    * Rango de Fechas

## 📂 Estructura Documental Clave

El proyecto sigue una estructura de gobernanza organizada:

| Categoría | Documento / Ruta |
| :--- | :--- |
| **Control** | `00_Project_Control/Project_Status.md` <br> `00_Project_Control/Version_Control.md` |
| **Reglas** | `02_Requirements_Validation/02_Business_Rules/Business_Rules_SCP.md` |
| **Diseño** | `05_Solution_Design/01_Architecture/Technical_Architecture.md` <br> `05_Solution_Design/02_Data_Model/Data_Dictionary.md` |
| **Mapping** | `05_Solution_Design/02_Data_Model/Source_to_Target_Mapping.md` |
| **SQL/DDL** | `05_Solution_Design/02_Data_Model/DDL_Tablas_Control.sql` |
| **QA/Despliegue** | `08_Testing_and_Validation/01_Test_Plan/Test_Plan_SCP.md` <br> `09_Release_Management/01_Deployment/Deployment_Guide.md` |

## 📈 Estado Actual

El componente cuenta actualmente con:
- [x] ETLs funcionales y queries de extracción.
- [x] Vistas de conciliación y persistencia analítica.
- [x] Evidencia de ejecución operativa satisfactoria.

*Enfoque actual: Fortalecimiento de documentación, control de procesos ETL y gobierno de datos.*

## 🛣 Próximos Pasos

- [ ] Formalizar la documentación oficial técnica y funcional.
- [ ] Implementar **Tablas de Control ETL** para auditoría.
- [ ] Incorporar una capa de **Staging** para la ingesta de archivos Excel.
- [ ] Validar e integrar la **Dimensión Cliente**.
- [ ] Diseñar la capa semántica final para el Dashboard Comercial.
- [ ] Ejecutar el plan de pruebas integrales y despliegue oficial.

---
**Desarrollado por el equipo de Datos y BI - 2026**
