# Checklist de Validación BI - SCP_ReporteComercial_Ventas

## 1. Objetivo
Validar que la capa analítica y el dashboard del proyecto SCP_ReporteComercial_Ventas sean funcionales, consistentes y útiles para consulta de negocio.

---

## 2. Fuente BI Oficial
- [ ] La fuente oficial actual es `tb_mb_conciliacion_fact_vs_conta_2026`
- [ ] La tabla fue generada desde `vw_mb_conciliacion_fact_vs_conta_2026`
- [ ] La tabla contiene `mes_num`
- [ ] La tabla contiene `mes`

---

## 3. Validación de Contenido Analítico
- [ ] Existe `referencia`
- [ ] Existe `tipo_operacion`
- [ ] Existe `fecha_factura`
- [ ] Existe `fecha_contable`
- [ ] Existe `total_facturado`
- [ ] Existe `total_contabilizado`
- [ ] Existe `diferencia`
- [ ] Existe `estatus`

---

## 4. Validación de Lógica de Negocio
- [ ] La comparación facturado vs contabilizado es visible
- [ ] Las diferencias son identificables
- [ ] Los registros conciliados son identificables
- [ ] Los registros no contabilizados son identificables
- [ ] La tabla refleja únicamente registros con `fecha_contable IS NOT NULL`

---

## 5. Validación de Filtros
- [ ] El filtro por operación funciona
- [ ] El filtro por rango de fechas funciona
- [ ] El filtro por mes funciona
- [ ] El filtro por referencia funciona
- [ ] El filtro por estatus funciona

### Filtro pendiente
- [ ] Cliente está documentado como requerimiento pendiente

---

## 6. Validación del Dashboard
- [ ] El dashboard carga correctamente
- [ ] El dashboard no presenta error de fuente
- [ ] Los datos mostrados son consistentes
- [ ] Los filtros responden correctamente
- [ ] La información es entendible para el usuario final
- [ ] La revisión por mes completo está soportada

---

## 7. Validación de Consistencia
- [ ] El total visible coincide con la fuente de tabla
- [ ] Las muestras revisadas coinciden con consulta SQL base
- [ ] No existen valores críticos inconsistentes en la muestra validada
- [ ] La tabla persistida está actualizada respecto de la vista al momento de revisión

---

## 8. Validación de Restricciones Actuales
- [ ] Se reconoce que Cliente aún no existe en el modelo
- [ ] Se reconoce que la persistencia es manual
- [ ] Se reconoce que el enfoque actual es mensual
- [ ] Las limitaciones actuales están documentadas

---

## 9. Validación por Ambiente
### QA
- [ ] El dashboard fue validado en QA antes de pasar a PROD

### PROD
- [ ] El dashboard en PROD muestra resultados correctos
- [ ] La fuente oficial en PROD es la esperada
- [ ] No existen errores visibles para el usuario final

---

## 10. Evidencias BI Requeridas
- [ ] captura del dashboard
- [ ] captura de filtros
- [ ] consulta SQL base de validación
- [ ] validación comparativa de muestra
- [ ] evidencia de tabla persistida

---

## 11. Criterio de Aprobación BI
La validación BI se considera satisfactoria cuando:
- la fuente oficial es correcta
- los datos son consistentes
- los filtros funcionales operan correctamente
- la revisión mensual es posible
- las limitaciones pendientes están documentadas