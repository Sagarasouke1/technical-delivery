# Version Control - SCP_ReporteComercial_Ventas

## 1. Historial de Versiones

| Versión | Fecha       | Responsable        | Tipo de cambio | Descripción |
|--------:|-------------|--------------------|----------------|-------------|
| 0.1     | 2026-03-03  | TI / Data Eng.     | Inicial        | Primera ejecución funcional de extracción de facturación y contabilidad hacia base analítica. |
| 0.2     | 2026-03-03  | TI / Data Eng.     | Operativo      | Validación de cargas por lotes, logs de ejecución y persistencia en tablas analíticas. |
| 0.3     | 2026-03-19  | TI / Data Eng.     | Continuidad    | Validación de respaldo sobre tabla de conciliación. |
| 0.4     | 2026-04-13  | Líder Técnico      | Documental     | Formalización de README, estado del proyecto, reglas de negocio y arquitectura técnica. |
| 0.5     | Pendiente   | TI / BI / Data     | Mejora         | Incorporación de tablas de control ETL, staging y fortalecimiento de capa BI final. |

---

## 2. Criterios de Versionamiento
- Los cambios funcionales o lógicos relevantes incrementan versión menor.
- Los cambios estructurales en el modelo de datos incrementan versión menor.
- Las correcciones documentales o de naming podrán registrarse como ajuste documental.
- Toda modificación relevante debe acompañarse de evidencia técnica o documental.

---

## 3. Resumen por Versión

### Versión 0.1
- Se habilita extracción de facturación desde ZAM hacia `dm_factura_electronica_totales`.
- Se habilita extracción contable hacia `cont_polizadet_ingresos_2026`.

### Versión 0.2
- Se validan inserciones por lotes.
- Se consolidan logs operativos.
- Se estabiliza carga analítica inicial.

### Versión 0.3
- Se configura y valida respaldo de `tb_mb_conciliacion_fact_vs_conta_2026`.

### Versión 0.4
- Se inicia construcción formal de documentación del proyecto dentro del repositorio.

### Versión 0.5
- Planeada para incorporar control ETL, staging de Excel y capa final BI más robusta.

---

## 4. Política de Control
- No se deben realizar cambios a producción sin quedar registrados en este documento.
- Toda mejora de arquitectura debe reflejarse también en el diseño técnico y modelo de datos.
- Toda modificación en queries, scripts o vistas debe quedar asociada a una versión del proyecto.