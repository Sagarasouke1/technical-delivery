# SD-005 — Arquitectura de Procesamiento de Casetas

## 1. Componentes

- Frontend: SCP WEB
- Backend: Procesamiento Python / API
- Base de Datos: MySQL (scp_system)
- Fuente: Portal PASE

## 2. Flujo de Datos

Archivo CSV/PDF → Parser → Validación → Clasificación → Persistencia

## 3. Tablas Clave

### tb_r_casetas_checker
Tabla principal de registros cargados :contentReference[oaicite:5]{index=5}

### tb_r_checker_auth
Tabla de autorizaciones operativas

## 4. Integración

- Entrada: Archivo manual
- Salida: Reportes + Metabase

## 5. Consideraciones

- No duplicidad de registros
- Control de versiones de carga (Achieved)
- Trazabilidad completa