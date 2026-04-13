# Execution Strategy - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir la estrategia de ejecución técnica y operativa del proyecto SCP_ReporteComercial_Ventas, incluyendo orden lógico, validaciones y promoción entre ambientes.

---

## 2. Principio General
El proyecto se basa en la extracción y consolidación de información de facturación y contabilidad desde ZAM hacia una base analítica, para posteriormente realizar conciliación y consumo en BI.

---

## 3. Estrategia de Ejecución Actual
La solución actual opera mediante procesos técnicos separados:

- extracción de facturación
- extracción de contabilidad
- carga auxiliar desde Excel
- conciliación lógica
- persistencia para BI
- respaldo

Actualmente el enfoque operativo está orientado a revisión por **mes completo**.

---

## 4. Orden Lógico de Ejecución

### Paso 1
Validar disponibilidad de ambiente correspondiente.

### Paso 2
Validar `.env`, rutas y conectividad.

### Paso 3
Ejecutar extracción de facturación:
- `FacturacionElectronica.py`

### Paso 4
Ejecutar extracción de contabilidad:
- `PolizaContableIngresos.py`

### Paso 5
Ejecutar carga auxiliar Excel si aplica:
- `PolizaIngresosExcel.py`

### Paso 6
Ejecutar o validar la lógica de conciliación:
- `vw_mb_conciliacion_fact_vs_conta_2026`

### Paso 7
Poblar tabla persistida:
- `tb_mb_conciliacion_fact_vs_conta_2026`

### Paso 8
Validar dashboard en Metabase.

### Paso 9
Ejecutar respaldo:
- `BackupMariadb.py`

---

## 5. Regla sobre Orden de ETL
Aunque funcionalmente se ha indicado que el orden de ejecución de los Python no afecta el resultado final, operativamente se recomienda mantener un orden estándar para facilitar:

- trazabilidad
- soporte
- troubleshooting
- repetibilidad
- auditoría técnica

**Orden recomendado:**
1. Facturación
2. Contabilidad
3. Excel auxiliar
4. Persistencia BI
5. Respaldo

---

## 6. Promoción entre Ambientes
Todo cambio debe seguir la ruta:

- DEV
- QA
- PROD

### Reglas
- DEV: desarrollo y pruebas iniciales
- QA: validación técnica y funcional
- PROD: operación oficial

No debe promoverse ningún cambio directamente a PROD.

---

## 7. Bloqueos Operativos
La indisponibilidad de un ambiente puede impedir la ejecución o promoción controlada.

**Bloqueo actual:**  
El ambiente DEV se encuentra apagado, con solicitud de encendido enviada por correo a los Ingenieros Oswaldo y Daniela el **13/04/2026 a las 09:54 AM**, sin respuesta al momento de esta documentación.

---

## 8. Recomendaciones de Ejecución Futura
1. Crear tablas de control ETL
2. Implementar staging
3. Registrar errores en BD
4. Formalizar proceso de llenado de tabla persistida
5. Definir ejecución automatizada o script maestro
6. Integrar dimensión Cliente en capa final BI

---

## 9. Criterios de Ejecución Correcta
Un ciclo de ejecución se considera correcto cuando:
- no hay error crítico
- los ETLs cargan correctamente
- la vista de conciliación refleja datos consistentes
- la tabla persistida se llena correctamente
- el dashboard funciona
- existe respaldo y log