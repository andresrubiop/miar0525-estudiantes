# Informe · Examen práctico integrador · MIAR0525

**Estudiante:** (código) · **Variante:** estado ___ · semilla ___ · **Fecha:** ___

## 1. Problema y datos
¿Qué se predice, para qué decisión y quién se ve afectado? Resumen de la ficha de datos (ver `datasheet.md`).

## 2. Partición y pipeline sin fuga
Cómo separaste la prueba, qué preprocesamiento va dentro del pipeline y por qué. Resultado de `pytest`.

## 3. Comparación de modelos
Tabla con al menos 3 modelos: búsqueda de hiperparámetros, métrica de validación cruzada (media ± DE) y enlace o captura de MLflow.

## 4. Selección, calibración y umbral
Modelo elegido y por qué; calibración (Brier o diagrama de fiabilidad); criterio del umbral. Resultado en la prueba (una sola vez).

## 5. Auditoría de equidad
`MetricFrame` por sexo y por raza (tamaños e intervalos). Métrica de equidad elegida y por qué. Mitigación, si corresponde, con su costo.

## 6. Explicabilidad
Global (permutación, PDP/ICE) y local (SHAP de al menos dos casos), con sus límites.

## 7. Documentación, monitoreo y riesgos
Resumen de `model_card.md`, `plan_monitoreo.md` y `registro_riesgos.md`.

## 8. Limitaciones y recomendación
¿Recomendarías usar el modelo? ¿Para qué sí y para qué no?

## 9. Declaración de uso de IA
Herramientas de IA generativa y código externo usados, para qué y cómo verificaste el resultado. Prompts relevantes en `prompts.md`.
