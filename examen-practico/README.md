# Examen práctico integrador · MIAR0525 · Aprendizaje Automático

**Peso:** 25 % · **Publicación:** sábado 17/10/2026 · **Entrega:** hasta el sábado 24/10/2026, 23:59 (hora de Ecuador)

Clasificación de ingresos con **ACS Income** (Ding et al., 2021; `fairlearn.datasets.fetch_acs_income`): predecir si el
ingreso personal anual supera 50 000 USD. Atributos sensibles: sexo (`SEX`) y raza (`RAC1P`). El examen integra las cuatro
unidades del curso.

## 1. Tu variante
```bash
python variante.py <tu código de estudiante>     # p. ej. A00123456 → Estado: NC · semilla: 3312
```
Cada estudiante trabaja con un estado y una semilla propios: tus resultados serán distintos a los de tus compañeros.

## 2. Entorno
- Entorno del curso: `uv sync --extra mlflow --extra etica` (desde la raíz del repositorio).
- Colab o pip: `pip install -r requirements.txt`.

## 3. Estructura
```
examen-practico/
├── variante.py                  # estado y semilla
├── src/datos.py                 # cargar_datos, grupos_sensibles, particion, DICCIONARIO
├── src/pipeline.py              # construir_pipeline (preprocesamiento dentro del pipeline)
├── tests/                       # prueba mínima: pytest -q
├── notebooks/examen_practico.ipynb
└── reports/                     # informe, datasheet, model_card, plan_monitoreo, registro_riesgos, prompts
```
Ejecuta las pruebas desde esta carpeta: `pytest -q` (deben pasar también con tu pipeline final).

## 4. Qué debes hacer
1. Repositorio reproducible con la prueba mínima en verde.
2. Pipeline sin fuga (prueba separada primero; todo el preprocesamiento dentro del pipeline).
3. Al menos 3 modelos con búsqueda de hiperparámetros y seguimiento en MLflow (`sqlite:///mlflow.db`).
4. Selección justificada, con calibración y umbral.
5. Auditoría de equidad con `MetricFrame` por sexo y raza y, si corresponde, mitigación con su costo.
6. Explicabilidad global y local.
7. Model Card, Datasheet, plan de monitoreo y registro de riesgos alineado con el NIST AI RMF.

## 5. Rúbrica (100 puntos)
| Criterio | Pts |
|---|---:|
| Reproducibilidad, estructura y prueba mínima | 10 |
| Datos y pipeline sin fuga | 15 |
| Comparación de modelos, búsqueda y selección justificada | 20 |
| Seguimiento de experimentos (MLflow) | 10 |
| Auditoría de equidad y mitigación | 15 |
| Explicabilidad | 10 |
| Model Card y Datasheet | 10 |
| Plan de monitoreo y registro de riesgos | 10 |

Niveles de desempeño: excelente 100 %, suficiente 70 %, insuficiente ≤ 40 %.

## 6. Entrega
Sube a Blackboard un `.zip` de esta carpeta (sin `mlruns/` si pesa mucho; incluye `mlflow.db`) y la presentación o el informe
en PDF. **Declaración de uso de IA obligatoria** (norma f): completa la sección 9 del informe y `reports/prompts.md`. El
docente puede pedir una verificación oral breve (5 minutos) a una muestra de estudiantes.
