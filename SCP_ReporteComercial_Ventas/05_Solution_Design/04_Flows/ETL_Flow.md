# ETL Flow - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar el flujo completo de extracción, transformación, carga, conciliación, persistencia y respaldo del proyecto SCP_ReporteComercial_Ventas, describiendo el comportamiento actual y la evolución recomendada para fortalecer trazabilidad, control y consumo en BI.

---

## 2. Alcance del Flujo
Este flujo contempla los siguientes componentes:

- Extracción de facturación desde ZAM
- Extracción de contabilidad desde ZAM
- Carga auxiliar desde archivos Excel
- Conciliación de facturación vs contabilidad
- Persistencia de resultados para BI
- Respaldo de tabla analítica
- Promoción entre ambientes DEV, QA y PROD
- Recomendaciones de control ETL

---

## 3. Flujo General de la Solución

```text
ZAM / SQL Server
   ├── Facturación
   └── Contabilidad
          ↓
   Queries SQL de extracción
          ↓
   Scripts ETL en Python
          ↓
   Base Analítica MySQL / MariaDB
          ├── dm_factura_electronica_totales
          ├── cont_polizadet_ingresos_2026
          ├── cont_polizadet_ingresos_original_2026
          ├── vw_mb_conciliacion_fact_vs_conta_2026
          └── tb_mb_conciliacion_fact_vs_conta_2026
          ↓
        Metabase
          ↓
        Respaldo
```
---
## 4. Flujo 1: Extracción de Facturación

### 4.1 Origen

La extracción de facturación se realiza desde ZAM mediante un query SQL ejecutado en SQL Server. El query obtiene referencia, tipo de operación, fecha de ingreso o cancelación, total correcto y estatus de factura. La lógica contempla exclusión de tipo_doc = 6, manejo de cancelaciones y ajuste de signo en montos.

### 4.2 Proceso

El script FacturacionElectronica.py realiza las siguientes acciones:

1. Carga variables desde .env
1. Lee el archivo FacturacionElectronica.sql
1. Abre conexión a SQL Server
1. Abre conexión a MySQL
1. Ejecuta la consulta en origen
1. Crea o verifica tabla destino
1. Inserta datos por lotes con UPSERT
1. Registra log del proceso

### 4.3 Destino

La información se almacena en:

- dm_factura_electronica_totales

### 4.4 Evidencia actual

Los logs muestran ejecución exitosa del proceso, incluyendo lectura del query, conteo de registros y carga por lotes.

---

## 5. Flujo 2: Extracción de Contabilidad

### 5.1 Origen

La extracción contable se realiza desde ZAM mediante el query PolizaContableIngresos.sql, el cual obtiene fecha de creación, póliza, partida, centro de costo, referencia, concepto, cargo, abono, fecha de ingreso y fecha de modificación. El query filtra registros del año actual, considera solo abonos no cero, centro de costo válido y excluye cierto tipo de póliza.

### 5.2 Proceso

El script PolizaContableIngresos.py realiza:

1. Carga variables desde .env
1. Lee el query PolizaContableIngresos.sql
1. Valida conectividad con SQL Server
1. Abre conexión a SQL Server
1. Abre conexión a MySQL
1. Ejecuta extracción
1. Crea o verifica tabla destino
1. Inserta datos por lotes con UPSERT
1. Registra log del proceso

### 5.3 Destino

La información se almacena en:

- cont_polizadet_ingresos_2026

### 5.4 Evidencia actual

Los logs muestran ejecución exitosa con batches guardados y resumen final del proceso.

---
## 6. Flujo 3: Carga Auxiliar desde Excel

### 6.1 Origen

Se cargan archivos Excel desde la carpeta configurada en el proceso. Los archivos contienen hoja Auxiliar Cuentas y columnas como Fecha, Póliza, Partida, Centro Costo, Referencia, Concepto Mov., Saldo Inicial, Cargo, Abono, Saldo Final, Tipo Póliza y Usuario. El script valida la estructura, renombra columnas y convierte tipos.

### 6.2 Proceso

El script PolizaIngresosExcel.py realiza:

1. Lee .env
1. Detecta archivos .xlsx
1. Valida existencia de carpeta y archivos
1. Lee la hoja Auxiliar Cuentas
1. Renombra columnas
1. Normaliza cadenas
1. Convierte fechas y montos
1. Inserta registros en MySQL

### 6.3 Destino

La información se almacena en:

- cont_polizadet_ingresos_original_2026

### 6.4 Riesgo actual

Actualmente el Excel carga directo a tabla analítica auxiliar, sin staging formal ni control estructurado de archivo procesado.

---
## 7. Flujo 4: Conciliación

### 7.1 Origen de conciliación

La conciliación se construye sobre:

- dm_factura_electronica_totales
- cont_polizadet_ingresos_2026

### 7.2 Proceso lógico

La vista vw_mb_conciliacion_fact_vs_conta_2026:

1. Agrupa facturación por referencia, operación y fecha
2. Agrupa contabilidad por referencia y fecha
3. Compara importes
4. Calcula diferencia
5. Asigna estatus

La lógica actual clasifica en:

- NO CONTABILIZADO
- CUADRADO
- DIFERENCIA

### 7.3 Persistencia

La tabla tb_mb_conciliacion_fact_vs_conta_2026 se llena con base en el resultado de la vista vw_mb_conciliacion_fact_vs_conta_2026.

### 7.4 Consumo

tb_mb_conciliacion_fact_vs_conta_2026 es la fuente oficial actual para consumo en Metabase.

### 7.5 Limitación actual

Aún no existe la dimensión Cliente en la capa final del modelo, por lo que el filtro correspondiente permanece pendiente de integración.

---
## 8. Flujo 5: Respaldo

### 8.1 Proceso

El script BackupMariadb.py:

1. Carga variables desde .env
1. Localiza mariadb-dump o mysqldump
1. Determina tabla(s) a respaldar
1. Genera archivo .sql
1. Registra evidencia en log

### 8.2 Tabla principal configurada

Actualmente el respaldo apunta a:

- tb_mb_conciliacion_fact_vs_conta_2026

### 8.3 Evidencia actual

Se observa respaldo correcto con archivo generado y log de salida.

---
## 9. Promoción entre Ambientes

### 9.1 Ambiente DEV

Ambiente destinado a desarrollo, ajustes técnicos, creación de objetos y validaciones iniciales.

### 9.2 Ambiente QA

Ambiente destinado a pruebas controladas, validación técnica y validación funcional previa a liberación.

### 9.3 Ambiente PROD

Ambiente productivo destinado a operación oficial y consumo final en BI.

### 9.4 Regla de promoción

Ningún cambio debe promoverse directamente a PROD sin haber sido validado previamente en DEV y QA.

## 10. Bloqueo Operativo Vigente

Actualmente el ambiente DEV se encuentra apagado, lo que representa una dependencia operativa para continuar con actividades de desarrollo, validación y fortalecimiento técnico del proyecto.

Se tiene registro de solicitud de encendido enviada por correo a los Ingenieros Oswaldo y Daniela el día 13/04/2026 a las 09:54 AM, sin respuesta al momento de la documentación.

---
##  11. Flujo Objetivo Recomendado
```text
ZAM / SQL Server
   ↓
ETL Facturación
   ↓
stg_facturacion (recomendado)
   ↓
dm_factura_electronica_totales

ZAM / SQL Server
   ↓
ETL Contabilidad
   ↓
stg_contabilidad (recomendado)
   ↓
cont_polizadet_ingresos_2026

Excel
   ↓
stg_poliza_ingresos_excel
   ↓
cont_polizadet_ingresos_original_2026

Consolidación
   ↓
vw_mb_conciliacion_fact_vs_conta_2026
   ↓
tb_mb_conciliacion_fact_vs_conta_2026
   ↓
vw_reporte_comercial_ventas_2026 / tb_reporte_comercial_ventas_2026
   ↓
Metabase
```
---
