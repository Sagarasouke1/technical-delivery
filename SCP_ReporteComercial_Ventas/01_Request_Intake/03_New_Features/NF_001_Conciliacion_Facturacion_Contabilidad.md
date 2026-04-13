# NF-001 - Conciliación Facturación vs Contabilidad

## 1. Identificador
**NF ID:** NF-001

## 2. Nombre de la Funcionalidad
Conciliación de Facturación vs Contabilidad para Reporte Comercial de Ventas.

---

## 3. Tipo de Solicitud
Nueva funcionalidad analítica / BI.

---

## 4. Objetivo
Incorporar una funcionalidad que permita comparar de manera centralizada la información facturada contra la información contabilizada, facilitando la revisión operativa y financiera mediante dashboard.

---

## 5. Justificación de Negocio
Se requiere visibilidad confiable sobre:
- qué se ha facturado
- qué se ha contabilizado
- qué diferencias existen
- en qué referencias y operaciones se concentran dichas diferencias

Esto permitirá mejorar el análisis, la revisión y la toma de decisiones.

---

## 6. Descripción Funcional
La nueva funcionalidad debe:
1. obtener información desde ZAM
2. consolidar facturación
3. consolidar contabilidad
4. comparar ambas fuentes
5. calcular diferencias
6. persistir resultados para BI
7. permitir análisis en Metabase

---

## 7. Alcance Actual
- revisión por mes completo
- análisis por operación
- análisis por rango de fechas disponible
- visualización de diferencias
- persistencia analítica para BI

---

## 8. Alcance Evolutivo
- análisis día a día
- integración de Cliente
- automatización del refresco de tabla persistida
- control ETL y trazabilidad reforzada
- capa final BI más madura

---

## 9. Entradas de la Funcionalidad
### Facturación
- datos de facturación extraídos desde ZAM

### Contabilidad
- datos contables extraídos desde ZAM

### Auxiliares
- archivos Excel cuando aplique

---

## 10. Salidas Esperadas
- vista lógica de conciliación
- tabla persistida de conciliación
- dashboard en Metabase
- análisis mensual de diferencias

---

## 11. Reglas de Negocio Relacionadas
- conciliación por referencia
- comparación facturado vs contabilizado
- clasificación de estatus
- revisión mensual actual
- Cliente como dimensión futura

---

## 12. Restricciones Actuales
- Cliente no existe aún en la capa analítica
- la tabla persistida se genera manualmente
- la revisión actual no está completamente orientada al día a día
- faltan tablas de control ETL

---

## 13. Dependencias
- disponibilidad de ZAM
- disponibilidad de MySQL / MariaDB
- disponibilidad de Metabase
- disponibilidad de ambientes DEV, QA y PROD
- disponibilidad del ambiente DEV para validación y promoción

---

## 14. Riesgos Iniciales
- diferencia entre fechas facturadas y contables
- referencias inconsistentes
- dependencia operativa de persistencia manual
- bloqueo del ambiente DEV
- ausencia actual de Cliente

---

## 15. Estado Actual
**Estado:** En construcción documental, validación técnica y fortalecimiento de arquitectura.

---

## 16. Conclusión
La funcionalidad NF-001 constituye el núcleo del proyecto SCP_ReporteComercial_Ventas, ya que habilita la comparación entre facturación y contabilidad en una capa analítica consumible por BI, sentando las bases para futuras mejoras de trazabilidad, automatización y análisis comercial.