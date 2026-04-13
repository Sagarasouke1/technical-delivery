# Data Dictionary - SCP_ReporteComercial_Ventas

## 1. Tabla: dm_factura_electronica_totales
**Tipo:** Tabla analítica  
**Origen:** ETL desde SQL Server / ZAM  
**Proceso origen:** `FacturacionElectronica.py`  
**Propósito:** Consolidar importes de facturación para conciliación analítica.

| Campo | Descripción |
|------|-------------|
| Referencia | Llave principal de guía o referencia comercial |
| tipo_operacion | Tipo de operación asociado |
| fecha_ingreso | Fecha operativa o de cancelación según lógica |
| Total_Correcto | Importe facturado ajustado |
| status_factura | Estado de facturación |

---

## 2. Tabla: cont_polizadet_ingresos_2026
**Tipo:** Tabla analítica  
**Origen:** ETL desde SQL Server / ZAM  
**Proceso origen:** `PolizaContableIngresos.py`  
**Propósito:** Consolidar importes contables de ingresos para conciliación.

| Campo | Descripción |
|------|-------------|
| fecha_creacion | Fecha de creación del movimiento |
| poliza | Identificador de póliza |
| partida | Número de partida |
| centro_costo | Centro de costo |
| referencia | Referencia comercial asociada |
| concepto_mov | Concepto del movimiento |
| cargo | Importe cargo |
| abono | Importe abono |
| fecha_ingreso | Fecha de ingreso |
| fecha_modifico | Fecha de modificación |

---

## 3. Tabla: cont_polizadet_ingresos_original_2026
**Tipo:** Tabla analítica auxiliar  
**Origen:** Excel  
**Proceso origen:** `PolizaIngresosExcel.py`  
**Propósito:** Consolidar auxiliares contables originales provenientes de archivos.

| Campo | Descripción |
|------|-------------|
| fecha | Fecha contable |
| poliza | Póliza |
| partida | Partida |
| centro_costo | Centro de costo |
| referencia | Referencia |
| concepto_mov | Concepto del movimiento |
| saldo_inicial | Saldo inicial |
| cargo | Cargo |
| abono | Abono |
| saldo_final | Saldo final |
| tipo_poliza | Tipo de póliza |
| usuario | Usuario origen |

---

## 4. Vista: vw_mb_conciliacion_fact_vs_conta_2026
**Tipo:** Vista lógica  
**Origen:** `dm_factura_electronica_totales` + `cont_polizadet_ingresos_2026`  
**Propósito:** Centralizar la lógica de conciliación.

| Campo | Descripción |
|------|-------------|
| referencia | Llave principal de conciliación |
| tipo_operacion | Operación comercial |
| fecha_factura | Fecha facturada agregada |
| fecha_contable | Fecha contable agregada |
| total_facturado | Monto facturado agregado |
| total_contabilizado | Monto contabilizado agregado |
| diferencia | Resultado de la resta facturado - contabilizado |
| estatus | Resultado de conciliación |

---

## 5. Tabla: tb_mb_conciliacion_fact_vs_conta_2026
**Tipo:** Tabla persistida BI  
**Origen:** Materialización de la vista de conciliación  
**Propósito:** Fuente oficial de consulta para dashboard en BI.

| Campo | Descripción |
|------|-------------|
| referencia | Llave principal |
| tipo_operacion | Operación |
| fecha_factura | Fecha de factura |
| fecha_contable | Fecha contable |
| total_facturado | Importe facturado |
| total_contabilizado | Importe contabilizado |
| diferencia | Diferencia detectada |
| estatus | Estado final de conciliación |