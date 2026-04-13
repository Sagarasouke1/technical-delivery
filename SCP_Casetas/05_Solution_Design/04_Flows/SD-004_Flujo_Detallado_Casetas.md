# SD-004 — Flujo Detallado del Sistema de Validación de Casetas

## 1. Objetivo
Documentar el flujo completo del sistema desde la carga del archivo hasta la generación de resultados.

## 2. Flujo General

1. Usuario accede a SCP WEB
2. Selecciona archivo (CSV o PDF)
3. Selecciona tipo de archivo (AEO / FLA)
4. Confirma carga
5. Sistema procesa archivo
6. Se generan resultados:
   - Correctos
   - Extraordinarios
   - Incorrectos

## 3. Validaciones

### 3.1 Validación de Casetas
- Comparación contra rutas autorizadas
- Identificación de:
  - Casetas faltantes
  - Casetas extra

### 3.2 Validación de Montos
- Comparación contra tarifas oficiales
- Detección de:
  - Cobros duplicados
  - Tarifas desactualizadas

## 4. Acciones del Usuario

- Aprobar caseta
- Rechazar caseta
- Agregar comentario
- Clasificar tipo de viaje

## 5. Resultado

- Registro en tabla `tb_r_casetas_checker`
- Registro de autorización en `tb_r_checker_auth`

## 6. Fin del proceso