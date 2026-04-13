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
```
