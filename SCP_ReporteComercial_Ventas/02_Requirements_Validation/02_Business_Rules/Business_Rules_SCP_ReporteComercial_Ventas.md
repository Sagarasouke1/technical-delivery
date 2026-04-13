# Business Rules - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir las reglas de negocio y operación que rigen el proceso de conciliación entre facturación y contabilidad para el proyecto SCP_ReporteComercial_Ventas.

---

## 2. Reglas Generales del Proyecto

**RN-01**  
La comparación principal del proyecto se realiza entre el importe facturado y el importe contabilizado.

**RN-02**  
La fuente operativa de información es ZAM.

**RN-03**  
La información se extrae desde ZAM, se transforma y se carga a la base analítica para consumo en BI.

**RN-04**  
El enfoque operativo actual del proyecto es la revisión por mes completo.

**RN-05**  
La solución debe evolucionar a revisión día a día.

**RN-06**  
El dashboard final debe permitir filtros por Operación, Cliente y Rango de Fechas.

---

## 3. Reglas de Facturación

**RN-10**  
La extracción de facturación considera un rango de fechas controlado en el query de origen.

**RN-11**  
Se excluyen documentos con `tipo_doc = 6`.

**RN-12**  
Cuando la operación corresponde a cancelación, el importe debe reflejarse con signo negativo.

**RN-13**  
Si la factura cumple condición de cancelación válida, se utiliza `fecha_solicitud_cancelacion`; en caso contrario se conserva `fecha_ingreso`.

**RN-14**  
El importe facturado oficial del modelo se obtiene del campo `Total_Correcto`.

**RN-15**  
El estado de facturación debe clasificar al menos entre `FACTURACION` y `CANCELADA`.

---

## 4. Reglas de Contabilidad

**RN-20**  
Solo se consideran registros del año actual en la extracción contable.

**RN-21**  
Solo se consideran registros con `abono <> 0`.

**RN-22**  
Solo se consideran registros con centro de costo válido.

**RN-23**  
Se excluyen tipos de póliza no contemplados por la lógica actual del modelo.

**RN-24**  
Para evitar duplicidad funcional, se conserva la versión más reciente por referencia, concepto e importe contable.

**RN-25**  
El importe contabilizado oficial del modelo se obtiene del campo `abono`.

---

## 5. Reglas de Conciliación

**RN-30**  
La conciliación se realiza por `referencia`.

**RN-31**  
La vista `vw_mb_conciliacion_fact_vs_conta_2026` concentra la lógica de conciliación.

**RN-32**  
El total facturado se obtiene de `dm_factura_electronica_totales`.

**RN-33**  
El total contabilizado se obtiene de `cont_polizadet_ingresos_2026`.

**RN-34**  
La diferencia se calcula como:
`total_facturado - total_contabilizado`

**RN-35**  
Si no existe coincidencia contable para una referencia facturada, el estatus será `NO CONTABILIZADO`.

**RN-36**  
Si la diferencia absoluta es menor a 1, el registro se considera conciliado.

**RN-37**  
Si existe diferencia material, el estatus será `DIFERENCIA`.

**RN-38**  
La persistencia BI debe generarse a partir de la vista de conciliación.

---

## 6. Reglas de BI

**RN-40**  
La tabla persistida de conciliación será la fuente oficial de consulta para BI.

**RN-41**  
Metabase debe consumir una capa analítica preparada, evitando cálculos repetitivos complejos desde múltiples fuentes.

**RN-42**  
La dimensión Cliente deberá incorporarse a la capa final cuando exista disponibilidad consistente desde origen o capa analítica.

---

## 7. Reglas de Calidad y Control

**RN-50**  
Todo proceso ETL debe dejar evidencia en log.

**RN-51**  
La carga debe minimizar duplicidad mediante claves únicas o lógica UPSERT.

**RN-52**  
Los procesos deben operar con configuración centralizada en `.env`.

**RN-53**  
Toda mejora futura deberá fortalecer trazabilidad, staging y control ETL.

---

## 8. Observaciones
Estas reglas deberán actualizarse cuando:
- se habilite análisis diario,
- se incorpore Cliente,
- se modifique la lógica de conciliación,
- se formalice la capa final BI comercial.