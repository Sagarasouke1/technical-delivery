# PROD Configuration - SCP_ReporteComercial_Ventas

## 1. Objetivo
Documentar la configuración funcional y operativa del ambiente PROD del proyecto SCP_ReporteComercial_Ventas.

---

## 2. Propósito del Ambiente
El ambiente PROD está destinado a:

- operación oficial del componente
- almacenamiento productivo de resultados
- consumo oficial en BI
- soporte a revisión de negocio y análisis operativo

---

## 3. Características Generales
- Ambiente productivo
- Estructura de `.env` igual a DEV y QA
- Credenciales y base productiva distintas a DEV y QA
- Fuente oficial de consulta para negocio
- Todo cambio en PROD debe estar previamente validado

---

## 4. Componentes Productivos
- ETLs productivos
- queries productivos
- vista de conciliación productiva
- tabla persistida productiva
- dashboard oficial en Metabase
- proceso de respaldo productivo

---

## 5. Estructura del `.env`
La estructura del `.env` productivo debe ser la misma que en DEV y QA, incluyendo:

- variables de SQL Server
- variables de MySQL / MariaDB
- batch size
- rutas de logs
- rutas de queries
- rutas de Excel
- rutas de respaldo

**Diferencia principal:**  
En PROD cambian credenciales y base de datos respecto de DEV y QA.

---

## 6. Reglas de Uso
1. Ningún cambio debe entrar a PROD sin pasar por DEV y QA.
2. Todo despliegue en PROD debe contar con respaldo previo.
3. Todo cambio en PROD debe tener documentación y validación asociada.
4. Toda incidencia en PROD debe documentarse en incidentes o RCA.

---

## 7. Validaciones Requeridas en PROD
- conectividad correcta
- ETLs funcionando
- datos consistentes
- vista operativa
- tabla persistida poblada
- dashboard funcional
- respaldo ejecutado correctamente
- logs generados correctamente

---

## 8. Riesgos de PROD
- error en ETLs con impacto directo en datos visibles
- error en vista con impacto en conciliación
- error en tabla persistida con impacto en dashboard
- configuración incorrecta del `.env`
- despliegue sin respaldo previo

---

## 9. Criterio de Operación Estable
Se considera operación estable cuando:
- el proceso corre sin error crítico
- el dashboard refleja información consistente
- la tabla persistida se genera correctamente
- existe respaldo y trazabilidad operativa