# Deployment Guide - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir el procedimiento de despliegue y validación inicial del componente SCP_ReporteComercial_Ventas.

---

## 2. Pre-requisitos
- acceso a SQL Server / ZAM
- acceso a MySQL / MariaDB
- Python y dependencias instaladas
- `.env` correctamente configurado
- rutas de logs y queries disponibles
- permisos de escritura en base analítica

---

## 3. Orden de Despliegue Recomendado

### Paso 1
Crear tablas de control ETL:
- ejecutar `DDL_Tablas_Control.sql`

### Paso 2
Crear o actualizar vista de conciliación:
- ejecutar `vw_mb_conciliacion_fact_vs_conta_2026.sql`

### Paso 3
Crear capa BI final:
- ejecutar `DDL_Vistas_BI.sql`

### Paso 4
Validar variables de entorno:
- SQL Server host
- DB origen
- DB destino
- puertos
- usuario
- password
- rutas de queries
- rutas de logs

### Paso 5
Ejecutar ETL de facturación:
- `FacturacionElectronica.py`

### Paso 6
Ejecutar ETL de contabilidad:
- `PolizaContableIngresos.py`

### Paso 7
Ejecutar carga auxiliar:
- `PolizaIngresosExcel.py`

### Paso 8
Persistir tabla de conciliación si aplica proceso materializado.

### Paso 9
Validar consumo en Metabase.

### Paso 10
Ejecutar respaldo:
- `BackupMariadb.py`

---

## 4. Validaciones Post-Deployment
- verificar existencia de tablas
- verificar existencia de vista
- validar conteos de registros
- revisar logs
- validar dashboard
- validar dump de respaldo

---

## 5. Rollback
- restaurar dump previo si existe afectación
- revertir vista o tabla modificada
- restaurar versión anterior de scripts si aplica

---

## 6. Observaciones
No debe subirse `.env` real al repositorio.  
Debe usarse `.env.template` con valores enmascarados para documentación y despliegue controlado.