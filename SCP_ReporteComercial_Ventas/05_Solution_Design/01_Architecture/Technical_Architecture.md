# 🏗️ Technical Architecture - SCP_ReporteComercial_Ventas

---

## 1. 📌 Propósito
Documentar la arquitectura técnica del componente de conciliación entre facturación y contabilidad, incluyendo:

- Fuentes de datos
- Procesos ETL
- Capa analítica
- Lógica de conciliación
- Persistencia para BI
- Respaldo operativo

---

## 2. 🎯 Objetivo Técnico

Extraer información desde **ZAM**, consolidarla en una base analítica y generar una capa confiable de comparación entre:

- Importes facturados  
- Importes contabilizados  

Para su consumo en **Metabase**.

---

## 3. 🧠 Arquitectura de Alto Nivel

```text
ZAM / SQL Server
   ↓
Queries SQL
   ├── FacturacionElectronica.sql
   └── PolizaContableIngresos.sql
   ↓
Procesos Python
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
4. ⚙️ Componentes Técnicos
4.1 🧾 FacturacionElectronica.py

Responsabilidades:

Leer variables desde .env
Leer query SQL externo
Conectarse a SQL Server
Conectarse a MySQL
Ejecutar extracción
Crear o verificar tabla destino
Insertar por lotes con UPSERT
Generar log de ejecución

Tabla destino:

dm_factura_electronica_totales
4.2 📊 PolizaContableIngresos.py

Responsabilidades:

Cargar configuración desde .env
Validar conectividad a SQL Server
Leer query SQL de origen
Extraer información contable
Crear o verificar tabla destino
Insertar por lotes con UPSERT
Registrar log operativo

Tabla destino:

cont_polizadet_ingresos_2026
4.3 📂 PolizaIngresosExcel.py

Responsabilidades:

Identificar archivos Excel desde carpeta configurada
Validar columnas obligatorias
Limpiar y normalizar datos
Convertir tipos
Insertar en tabla analítica auxiliar

Tabla destino:

cont_polizadet_ingresos_original_2026
4.4 🔄 vw_mb_conciliacion_fact_vs_conta_2026

Responsabilidades:

Consolidar facturación por:
referencia
operación
fecha
Consolidar contabilidad por:
referencia
fecha
Comparar importes
Calcular diferencias
Clasificar resultado de conciliación
4.5 📦 tb_mb_conciliacion_fact_vs_conta_2026

Responsabilidades:

Persistir resultado de conciliación
Optimizar consumo desde BI
Reducir recálculo repetitivo de lógica
4.6 💾 BackupMariadb.py

Responsabilidades:

Ejecutar respaldo de tabla(s) analíticas
Usar:
mariadb-dump
mysqldump
Generar archivo de salida
Dejar evidencia en log
5. 🔄 Flujo Técnico de Datos
🟢 Flujo 1: Facturación
FacturacionElectronica.py lee FacturacionElectronica.sql
Ejecuta consulta en SQL Server
Obtiene registros de facturación

Inserta o actualiza en:

dm_factura_electronica_totales
Registra log
🔵 Flujo 2: Contabilidad
PolizaContableIngresos.py lee PolizaContableIngresos.sql
Ejecuta consulta en SQL Server
Obtiene registros contables

Inserta o actualiza en:

cont_polizadet_ingresos_2026
Registra log
🟡 Flujo 3: Auxiliar Excel
PolizaIngresosExcel.py detecta archivos .xlsx
Valida hoja Auxiliar Cuentas
Renombra y transforma columnas

Inserta registros en:

cont_polizadet_ingresos_original_2026
🟣 Flujo 4: Conciliación

La vista:

vw_mb_conciliacion_fact_vs_conta_2026

agrupa y compara información

Se persiste el resultado en:

tb_mb_conciliacion_fact_vs_conta_2026
Metabase consume la capa persistida
⚫ Flujo 5: Respaldo
BackupMariadb.py selecciona tablas configuradas
Ejecuta dump
Genera archivo de salida
Registra evidencia en log
6. 🧩 Dependencias Técnicas
SQL Server
MySQL / MariaDB
Python

Librerías:

pyodbc
pymysql
mysql.connector
pandas
python-dotenv

Herramientas:

mariadb-dump
mysqldump
Metabase
7. ⚠️ Consideraciones Operativas
Enfoque actual: revisión por mes completo
Visión futura: comparativo día a día
Dependencia crítica: configuración correcta de .env
La capa de conciliación aún requiere madurez en:
Control ETL
Staging
8. 🚨 Riesgos Técnicos
Diferencias temporales entre facturación y contabilidad
Referencias inconsistentes
Reprocesos no controlados de Excel
Falta de dimensión Cliente
Falta de tablas de control ETL
Dependencia de variables de entorno
9. 📈 Recomendaciones de Madurez
Crear tablas de control ETL
Incorporar capa staging para Excel
Crear capa final oficial para dashboard comercial
Documentar matriz fuente-destino completa
Estandarizar logs y trazabilidad operativa