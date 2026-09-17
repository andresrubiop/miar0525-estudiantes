# Aprendizaje Automático · MIAR0525 · material del estudiante

Maestría en Inteligencia Artificial · Postgrado **UEES** · Período en Línea 4, 2026 (19/09 – 24/10).

| Qué | Dónde |
|---|---|
| Aula interactiva: presentaciones, animaciones, manuales, ejercicios y cuestionarios (ábrela en el navegador; funciona sin conexión) | `hub/dist/index.html` |
| Notebooks de ejercicios (con `TODO`) | `semana-1/` · `semana-2/` · `semana-3/` · `semana-4/` |
| Versiones resueltas de los ejercicios | `soluciones/semana-N/` |
| Plantillas de las tareas (lo que entregas) | `tareas/` |
| Manuales y presentaciones en PDF | `materiales/semana-N/` |
| Estilo de gráficos UEES para tus tareas | `utils/uees.mplstyle` |

## Cómo trabajar los notebooks

**En Google Colab (recomendado):** usa el botón **Abrir en Colab** de cada ejercicio en el aula, o en Colab
*Archivo → Abrir cuaderno → GitHub* y pega la dirección de este repositorio. Guarda tu copia en tu Drive.

**En tu equipo con [uv](https://docs.astral.sh/uv/):**

```bash
git clone <dirección de este repositorio>
cd miar0525-estudiantes
uv sync --extra mlflow --extra etica --group lab   # Python 3.13, scikit-learn, MLflow, Fairlearn, SHAP y JupyterLab
uv run jupyter lab
```

Cada notebook tiene cuatro niveles (desde cero, con scikit-learn, datos reales y un reto), celdas `TODO` para
completar, una autoverificación y un **desafío opcional con IA agéntica** al final. Su versión resuelta está en
`soluciones/semana-N/`. Los datos se descargan solos (OpenML, scikit-learn o Fairlearn).

## IA en el curso

Este curso no es de programación en Python: el código es el medio para entender, comparar y validar métodos. Puedes
usar IA agéntica (Claude Code, Codex, Gemini CLI…) o de chat (ChatGPT, Claude, Gemini) en los ejercicios, los desafíos
y las tareas, **siempre que lo declares**: herramienta, prompts relevantes y qué verificaste tú (norma f del sílabo).
Las decisiones, su justificación y la verificación son tuyas.

## Normas

- Declara el uso de IA generativa y de código externo en cada entrega.
- No subas datos personales ni credenciales a tus repositorios.
- Dudas: en la tutoría del sábado o por los canales del aula virtual.
