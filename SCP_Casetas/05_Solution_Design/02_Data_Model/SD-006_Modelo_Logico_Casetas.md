# SD-006 — Modelo Lógico de Datos

## 1. Tabla: tb_r_casetas_checker

Campos principales:

- id_casexel (PK)
- economico
- fecha
- hora
- caseta
- carril
- importe
- estado
- empresa

## 2. Tabla: tb_r_checker_auth

- id
- id_caseta
- estado_autorizacion
- comentario
- usuario
- fecha

## 3. Relación

tb_r_casetas_checker (1) → (N) tb_r_checker_auth

## 4. Objetivo

Permitir:
- Auditoría
- Trazabilidad
- Control operativo