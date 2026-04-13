# Architecture Diagram - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir la estructura visual de la arquitectura del proyecto SCP_ReporteComercial_Ventas para su posterior representación en draw.io, Visio o herramienta equivalente.

---

## 2. Diagrama Lógico General

```text
┌──────────────────────────────┐
│      ZAM / SQL Server        │
│  - Facturación               │
│  - Contabilidad              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Queries de extracción    │
│  - FacturacionElectronica.sql│
│  - PolizaContableIngresos.sql│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Procesos Python       │
│  - FacturacionElectronica.py │
│  - PolizaContableIngresos.py │
│  - PolizaIngresosExcel.py    │
│  - BackupMariadb.py          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Base Analítica MySQL/MariaDB │
│ - dm_factura_electronica...  │
│ - cont_polizadet_ingresos... │
│ - cont_polizadet_ingresos... │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Vista de conciliación      │
│ vw_mb_conciliacion_fact_...  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Tabla persistida BI          │
│ tb_mb_conciliacion_fact_...  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Metabase             │
│ Dashboard / Análisis         │
└──────────────────────────────┘
```

---

## 3. Diagrama con Soporte de Excel

```text

                    ┌──────────────────────┐
                    │ Excel Auxiliar       │
                    │ Auxiliar Cuentas     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ PolizaIngresosExcel  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ cont_polizadet_      │
                    │ ingresos_original... │
                    └──────────────────────┘
```

---

## 4. Diagrama de Ambientes

```text
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│     DEV      │ ---> │      QA      │ ---> │     PROD     │
│ Desarrollo   │      │ Validación   │      │ Operación    │
└──────────────┘      └──────────────┘      └──────────────┘

```
###  Regla

Todo cambio técnico, SQL, Python o de modelo de datos debe seguir la ruta:

* DEV
* QA
* PROD

--- 
## 5. Dependencia Operativa Crítica

Actualmente el ambiente DEV se encuentra apagado, lo cual representa una dependencia operativa para:

* pruebas de desarrollo
* creación de objetos
* validación técnica
* promoción a QA

Se tiene registro de solicitud de encendido enviada el 13/04/2026 a las 09:54 AM a los Ingenieros Oswaldo y Daniela, sin respuesta al momento de esta documentación.