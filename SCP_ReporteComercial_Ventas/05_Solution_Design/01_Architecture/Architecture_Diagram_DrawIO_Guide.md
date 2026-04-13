# Architecture Diagram Draw.io Guide - SCP_ReporteComercial_Ventas

## 1. Objetivo
Proveer una guía textual para construir en draw.io el diagrama de arquitectura del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Estructura Recomendada del Diagrama
Dibuja el diagrama en 6 carriles horizontales:

1. Origen
2. Queries SQL
3. Procesos Python
4. Base Analítica
5. BI
6. Ambientes

---

## 3. Bloques que debes dibujar

### Carril 1. Origen
Crear un bloque grande:
- **ZAM / SQL Server**

Dentro del bloque, agrega:
- Facturación
- Contabilidad

---

### Carril 2. Queries SQL
Crear 2 bloques:
- `FacturacionElectronica.sql`
- `PolizaContableIngresos.sql`

---

### Carril 3. Procesos Python
Crear 4 bloques:
- `FacturacionElectronica.py`
- `PolizaContableIngresos.py`
- `PolizaIngresosExcel.py`
- `BackupMariadb.py`

---

### Carril 4. Base Analítica
Crear 5 bloques:
- `dm_factura_electronica_totales`
- `cont_polizadet_ingresos_2026`
- `cont_polizadet_ingresos_original_2026`
- `vw_mb_conciliacion_fact_vs_conta_2026`
- `tb_mb_conciliacion_fact_vs_conta_2026`

Agregar un bloque punteado adicional como mejora futura:
- `tb_reporte_comercial_ventas_2026`

Agregar también bloques punteados de mejora:
- `etl_control_ejecucion`
- `etl_log_errores`
- `ctl_archivos_excel_procesados`
- `stg_poliza_ingresos_excel`

---

### Carril 5. BI
Crear un bloque:
- `Metabase`

Dentro del bloque agrega:
- Dashboard conciliación
- Filtros actuales
- Cliente pendiente

---

### Carril 6. Ambientes
Crear 3 bloques conectados:
- DEV
- QA
- PROD

Con flechas:
DEV → QA → PROD

---

## 4. Flechas recomendadas

### Origen a queries
- ZAM / SQL Server → FacturacionElectronica.sql
- ZAM / SQL Server → PolizaContableIngresos.sql

### Queries a Python
- FacturacionElectronica.sql → FacturacionElectronica.py
- PolizaContableIngresos.sql → PolizaContableIngresos.py

### Python a analítico
- FacturacionElectronica.py → dm_factura_electronica_totales
- PolizaContableIngresos.py → cont_polizadet_ingresos_2026
- PolizaIngresosExcel.py → cont_polizadet_ingresos_original_2026

### Analítico a conciliación
- dm_factura_electronica_totales → vw_mb_conciliacion_fact_vs_conta_2026
- cont_polizadet_ingresos_2026 → vw_mb_conciliacion_fact_vs_conta_2026

### Vista a tabla persistida
- vw_mb_conciliacion_fact_vs_conta_2026 → tb_mb_conciliacion_fact_vs_conta_2026

### Tabla persistida a BI
- tb_mb_conciliacion_fact_vs_conta_2026 → Metabase

### Backup
- tb_mb_conciliacion_fact_vs_conta_2026 → BackupMariadb.py
o
- BackupMariadb.py → respaldo `.sql`

---

## 5. Anotaciones importantes en el diagrama

### Nota 1
Colocar una nota junto a `tb_mb_conciliacion_fact_vs_conta_2026`:
- “Se llena a partir del resultado de la vista”

### Nota 2
Colocar una nota junto a Metabase:
- “Cliente aún no integrado”

### Nota 3
Colocar una nota junto a DEV:
- “Ambiente apagado al 13/04/2026 09:54 AM - solicitud enviada a Oswaldo y Daniela”

---

## 6. Recomendaciones visuales
- azul para origen
- verde para ETL
- amarillo para base analítica
- morado para BI
- gris punteado para mejoras futuras
- rojo o naranja para dependencias / bloqueos

---

## 7. Resultado esperado
El diagrama final debe permitir entender:
- de dónde salen los datos
- qué procesos los transforman
- en qué tablas quedan
- cómo se concilian
- qué consume BI
- cómo se promueve entre ambientes
- qué dependencias y mejoras existen