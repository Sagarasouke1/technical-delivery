# Rollback Plan - SCP_ReporteComercial_Ventas

## 1. Objetivo
Definir el procedimiento de reversa controlada ante fallas funcionales, técnicas o de datos derivadas del despliegue del componente SCP_ReporteComercial_Ventas.

---

## 2. Alcance
Este plan aplica para:
- despliegue de vistas
- despliegue de tablas de control ETL
- despliegue de capa BI final
- cambios en scripts Python
- cambios en configuración de ejecución
- cargas que impacten tablas analíticas
- promoción entre ambientes DEV, QA y PROD

---

## 3. Ambientes Alcanzados
- DEV
- QA
- PROD

### Regla general
Ningún cambio debe desplegarse directamente en PROD sin haber sido validado previamente en DEV y QA.

---

## 4. Escenarios de Rollback

### RB-01
Falla en creación o actualización de vista de conciliación.

### RB-02
Falla en creación de tablas de control ETL.

### RB-03
Falla en modificación de scripts ETL.

### RB-04
Carga incorrecta de datos en tablas analíticas.

### RB-05
Inconsistencia entre vista, tabla persistida y dashboard.

### RB-06
Falla en integración de nueva capa BI final.

### RB-07
Falla por indisponibilidad de ambiente requerido para validación o promoción.

---

## 5. Objetos Críticos a Recuperar
- `dm_factura_electronica_totales`
- `cont_polizadet_ingresos_2026`
- `cont_polizadet_ingresos_original_2026`
- `vw_mb_conciliacion_fact_vs_conta_2026`
- `tb_mb_conciliacion_fact_vs_conta_2026`
- `tb_reporte_comercial_ventas_2026` *(si se implementa)*
- scripts Python modificados
- configuración de despliegue

---

## 6. Precondiciones para Rollback
Antes de cualquier despliegue se debe contar con:

1. Respaldo vigente de tabla(s) críticas
2. Copia de versión anterior de scripts Python
3. Copia de versión anterior de vistas SQL
4. Registro del cambio en `Version_Control.md`
5. Evidencia de validación previa al cambio
6. Identificación clara del ambiente afectado

---

## 7. Procedimiento General de Rollback

### Paso 1. Detener ejecución operativa
Suspender ejecución manual, programada o automática del proceso afectado para evitar más cambios.

### Paso 2. Identificar ambiente afectado
Confirmar si la reversa aplica en:
- DEV
- QA
- PROD

### Paso 3. Identificar alcance del problema
Determinar si la falla impacta:
- scripts ETL
- tablas de datos
- vistas
- dashboard
- configuración
- promoción entre ambientes

### Paso 4. Aislar el objeto afectado
Identificar exactamente qué objeto requiere reversa:
- vista
- tabla
- script
- carga de datos
- integración BI

### Paso 5. Restaurar versión anterior
Aplicar según el tipo de objeto:

#### 5.1 Para scripts Python
- restaurar archivo previo desde repositorio o respaldo local
- validar rutas, `.env` y dependencias

#### 5.2 Para vistas
- recrear vista anterior con script previo validado

#### 5.3 Para tablas
- restaurar tabla desde dump o backup validado

#### 5.4 Para datos
- revertir registros incorrectos si existe estrategia controlada
- en caso necesario, truncar y recargar desde versión validada

### Paso 6. Validar integridad
Después de la reversa, validar:
- existencia de objetos
- conteo de registros
- consistencia de conciliación
- consulta en Metabase
- logs de ejecución

### Paso 7. Documentar incidente
Registrar:
- causa
- ambiente afectado
- objeto afectado
- fecha/hora
- responsable
- acción correctiva
- evidencia

---

## 8. Estrategia Específica por Tipo de Cambio

### 8.1 Cambio en vista `vw_mb_conciliacion_fact_vs_conta_2026`
**Acción de rollback:**
- ejecutar script SQL anterior de la vista
- validar consulta de salida
- comparar conteos básicos y estatus

### 8.2 Cambio en tabla persistida `tb_mb_conciliacion_fact_vs_conta_2026`
**Acción de rollback:**
- restaurar dump previo
- validar estructura
- validar registros
- reprobar dashboard

### 8.3 Cambio en scripts ETL
**Acción de rollback:**
- restaurar versión previa del `.py`
- validar query asociado
- realizar corrida controlada de prueba

### 8.4 Cambio en carga Excel
**Acción de rollback:**
- identificar archivos procesados
- limpiar registros incorrectos
- recargar solo versión válida

### 8.5 Cambio en capa final BI
**Acción de rollback:**
- deshabilitar vista o tabla nueva
- regresar consumo de Metabase a tabla anterior validada

---

## 9. Validaciones por Ambiente

### DEV
- validar creación correcta de objetos
- validar estructura
- validar ejecución técnica

### QA
- validar resultado funcional y analítico
- validar comportamiento del dashboard
- validar criterios de aceptación

### PROD
- validar estabilidad, datos y consumo final
- revisar logs y evidencia operativa

---

## 10. Bloqueos Operativos Relacionados
La indisponibilidad de un ambiente puede impedir o retrasar la validación previa a promoción y, por lo tanto, bloquear la liberación controlada.

Actualmente el ambiente DEV se encuentra apagado y existe una solicitud de encendido enviada por correo el **13/04/2026 a las 09:54 AM** a los Ingenieros Oswaldo y Daniela, sin respuesta al momento de esta documentación.

---

## 11. Evidencias Requeridas
- log del error
- log del rollback
- dump restaurado
- script restaurado
- evidencia de validación
- registro en `Version_Control.md`
- registro en incidentes / RCA si aplica

---

## 12. Responsables Sugeridos

### Líder Técnico
- decidir estrategia de rollback
- validar impacto
- autorizar reversa

### Desarrollador / Data Engineer
- ejecutar reversa técnica
- validar scripts y datos

### BI / Analista
- validar funcionamiento en dashboard

### Usuario clave / negocio
- validar consistencia funcional posterior

---

## 13. Criterios de Cierre de Rollback
Un rollback se considera exitoso cuando:
- el objeto afectado vuelve a una versión estable
- los datos son consistentes
- la conciliación vuelve a comportarse correctamente
- el dashboard es usable
- el incidente queda documentado

---

## 14. Conclusión
Toda liberación del proyecto SCP_ReporteComercial_Ventas debe ir acompañada de un rollback plan operativo y validado, debido a que los cambios pueden impactar directamente la conciliación entre facturación y contabilidad, así como la confianza del usuario en la información mostrada en BI.