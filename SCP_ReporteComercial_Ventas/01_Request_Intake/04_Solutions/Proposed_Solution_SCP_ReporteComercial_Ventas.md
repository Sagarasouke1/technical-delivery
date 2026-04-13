# Proposed Solution - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir formalmente la solución propuesta para atender la necesidad de comparar lo facturado contra lo contabilizado, consolidando la información en una capa analítica explotable mediante BI.

---

## 2. Contexto de la Necesidad
Se requiere contar con un componente que permita comparar de forma confiable la información de facturación contra la información contable, facilitando la identificación de diferencias y soportando su revisión en Metabase.

Actualmente, la necesidad del negocio está orientada a:
- revisar por mes completo
- validar diferencias entre facturación y contabilidad
- analizar resultados por operación
- habilitar rango de fechas
- incorporar Cliente como dimensión futura

---

## 3. Problema a Resolver
Hoy la información de facturación y contabilidad no se encuentra presentada en una sola capa consolidada de análisis de manera formal, reusable y controlada para BI.

Los principales problemas identificados son:
- necesidad de comparación entre dos fuentes funcionalmente distintas
- ausencia de una capa final analítica consolidada completamente madura
- dependencia de procesos ETL separados
- persistencia manual de la tabla de conciliación
- falta actual del campo Cliente
- falta de tablas formales de control ETL

---

## 4. Solución Propuesta
La solución propuesta consiste en construir un flujo analítico controlado que:

1. extraiga facturación desde ZAM
2. extraiga contabilidad desde ZAM
3. cargue auxiliares contables desde Excel cuando aplique
4. consolide la lógica de conciliación en una vista
5. materialice el resultado en una tabla persistida para BI
6. publique el resultado en Metabase
7. permita evolucionar a una capa final comercial más robusta

---

## 5. Componentes de la Solución

### 5.1 Origen
- ZAM / SQL Server
- archivos Excel auxiliares

### 5.2 Procesamiento
- `FacturacionElectronica.py`
- `PolizaContableIngresos.py`
- `PolizaIngresosExcel.py`

### 5.3 Capa analítica
- `dm_factura_electronica_totales`
- `cont_polizadet_ingresos_2026`
- `cont_polizadet_ingresos_original_2026`

### 5.4 Capa lógica
- `vw_mb_conciliacion_fact_vs_conta_2026`

### 5.5 Persistencia BI actual
- `tb_mb_conciliacion_fact_vs_conta_2026`

### 5.6 Consumo final
- Metabase

---

## 6. Arquitectura Propuesta

```text
ZAM / SQL Server
   ├── Facturación
   └── Contabilidad
         ↓
ETLs Python + Querys SQL
         ↓
Base Analítica
   ├── dm_factura_electronica_totales
   ├── cont_polizadet_ingresos_2026
   └── cont_polizadet_ingresos_original_2026
         ↓
vw_mb_conciliacion_fact_vs_conta_2026
         ↓
tb_mb_conciliacion_fact_vs_conta_2026
         ↓
Metabase
```

---

## 7. Beneficios Esperados

* comparación centralizada entre facturación y * contabilidad
* identificación clara de diferencias
* soporte para revisión mensual
* consumo simplificado en BI
* mayor claridad para usuario final
* base para evolución a análisis diario
* base para integración futura de Cliente

---

## 8. Limitaciones Actuales de la Solución

* la persistencia de la tabla de conciliación es manual
* Cliente no existe aún en la capa analítica actual
* no se cuenta aún con tablas de control ETL
* no existe staging formal para Excel
* la revisión actual está orientada a mes completo

---

## 9. Evolución Recomendada

La solución debe evolucionar hacia:

1. control ETL en base de datos
1. staging de Excel
1. automatización de persistencia
1. integración de Cliente
1. capa final BI comercial
1. análisis día a día

---

## 10. Ambientes

La solución deberá gestionarse y validarse en:

* DEV
* QA
* PROD

Todo cambio debe seguir la ruta:
DEV → QA → PROD


---

## 11. Dependencia Actual Relevante

Actualmente el ambiente DEV se encuentra apagado, lo que afecta la validación técnica y promoción controlada. Existe solicitud de encendido enviada por correo a los Ingenieros Oswaldo y Daniela el 13/04/2026 a las 09:54 AM, sin respuesta al momento.


---

## 12. Conclusión

La solución propuesta para SCP_ReporteComercial_Ventas atiende la necesidad actual de comparar lo facturado contra lo contabilizado mediante una arquitectura funcional y analítica ya operativa, con capacidad de evolucionar hacia una solución más madura, automatizada y orientada plenamente al negocio.

---