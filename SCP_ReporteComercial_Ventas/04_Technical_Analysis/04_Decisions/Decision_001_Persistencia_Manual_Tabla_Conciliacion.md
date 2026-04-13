# Decision 001 - Persistencia Manual de Tabla de Conciliación

## 1. Identificador
**Decision ID:** DEC-001

## 2. Título
Persistencia manual de `tb_mb_conciliacion_fact_vs_conta_2026` a partir de la vista `vw_mb_conciliacion_fact_vs_conta_2026`.

---

## 3. Contexto
El proyecto SCP_ReporteComercial_Ventas requiere una capa persistida para consumo en BI. La lógica principal de conciliación ya existe en la vista `vw_mb_conciliacion_fact_vs_conta_2026`, por lo que se definió generar una tabla física llamada `tb_mb_conciliacion_fact_vs_conta_2026` para que Metabase consuma una fuente más estable y de mejor desempeño.

Actualmente esta tabla se genera manualmente mediante query.

---

## 4. Decisión Tomada
Se decidió que, en la etapa actual del proyecto, la tabla `tb_mb_conciliacion_fact_vs_conta_2026` se genere manualmente ejecutando un query basado en la vista `vw_mb_conciliacion_fact_vs_conta_2026`.

El query actual es:

```sql
CREATE TABLE analytics_aeo.tb_mb_conciliacion_fact_vs_conta_2026 AS
SELECT 
    *,
    MONTH(fecha_contable) AS mes_num,
    UPPER(MONTHNAME(fecha_contable)) AS mes
FROM analytics_aeo.vw_mb_conciliacion_fact_vs_conta_2026
WHERE fecha_contable IS NOT NULL;

```
---

## 5. Justificación

La decisión se tomó por las siguientes razones:

1. Ya existe una vista funcional con la lógica central de conciliación.
1. Se requería una fuente física para Metabase.
1. La tabla persistida mejora estabilidad y desempeño de consulta.
1. La solución manual permite avanzar funcionalmente sin esperar automatización completa.
1. El proyecto aún se encuentra en una etapa donde la revisión es por mes completo y no se ha formalizado aún un proceso de actualización automatizado.

---

## 6. Beneficios

* capa física estable para BI
* menor dependencia de cálculos en tiempo real desde la vista
* posibilidad de agregar columnas derivadas como mes_num y mes
* lectura más simple para usuarios de BI
* implementación rápida para cubrir necesidad actual

---

## 7. Desventajas / Riesgos

el proceso es manual
depende del usuario técnico que ejecute el query
existe riesgo de desactualización
no hay trazabilidad formal de cada corrida
no se ha definido aún si en futuras corridas se usará DROP + CREATE, TRUNCATE + INSERT o una estrategia incremental
se excluyen registros con fecha_contable IS NOT NULL, lo que limita ciertos escenarios analíticos

---

## 8. Alternativas Consideradas

### Alternativa A

Consumir directamente la vista en Metabase.
Motivo de descarte parcial:
puede resultar menos controlado y menos eficiente para consumo repetitivo.

### Alternativa B

Automatizar desde el inicio un proceso ETL o procedimiento almacenado.
Motivo de descarte temporal:
requería una evolución técnica adicional que aún no se encontraba formalizada.

### Alternativa C

Construir desde el inicio una tabla final comercial más madura.
Motivo de descarte temporal:
Cliente aún no existe y la capa final comercial aún está pendiente de diseño completo.


---

## 9. Impacto de la Decisión

Impacto técnico: Alto
Impacto funcional: Medio-Alto
Impacto BI: Alto

La decisión resuelve la necesidad actual, pero deja pendiente una evolución hacia mayor automatización y control.


---

## 10. Decisión Futura Recomendada

Evolucionar esta estrategia a una de las siguientes opciones:

1. proceso automatizado controlado con trazabilidad
1. TRUNCATE + INSERT documentado y validado
1. proceso de refresco programado
1. capa final BI desacoplada de la tabla técnica

---

## 11. Estado de la Decisión

Estado actual: Vigente

Revisión futura recomendada:
cuando se implemente:

* control ETL
* integración de Cliente
* capa final BI
* automatización del refresco

---

## 12. Conclusión

La persistencia manual de tb_mb_conciliacion_fact_vs_conta_2026 fue una decisión válida para cubrir la necesidad actual del proyecto, permitiendo a Metabase consumir una fuente física y más simple. Sin embargo, debe considerarse una solución transitoria que posteriormente evolucione hacia un mecanismo más controlado, automatizado y auditable.

---