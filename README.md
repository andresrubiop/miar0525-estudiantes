# Aprendizaje Automático · Aula interactiva (UEES)

**Aula en línea:** https://andresrubiop.github.io/miar0525-estudiantes/

Cuatro semanas con presentación, animaciones interactivas con algoritmos reales, manual, notebooks con su versión resuelta,
tareas, cuestionario y videos. En español. Asignatura MIAR0525 de la Maestría en Inteligencia Artificial, Postgrado
**UEES** (Período en Línea 4, 2026).

## Usarla

- **En línea:** abre https://andresrubiop.github.io/miar0525-estudiantes/ (tu progreso queda guardado en tu navegador).
- **Sin conexión:** *Code → Download ZIP* (o `git clone https://github.com/andresrubiop/miar0525-estudiantes.git`) y abre `index.html` con doble clic.
- **PDF:** `materiales/semana-N/` (manual `M#` y presentación `P#`).

| Qué | Dónde |
|---|---|
| Aula interactiva: presentaciones, animaciones, manuales, ejercicios y cuestionarios | `index.html` |
| Notebooks de ejercicios (con `TODO`) | `semana-1/` · `semana-2/` · `semana-3/` · `semana-4/` |
| Versiones resueltas de los ejercicios | `soluciones/semana-N/` |
| Plantillas de las tareas (lo que entregas) | `tareas/` |
| Manuales y presentaciones en PDF | `materiales/semana-N/` |
| Videos del curso | `videos/semana-N/` |
| Estilo de gráficos UEES para tus tareas | `utils/uees.mplstyle` |
| Examen práctico integrador (variantes, datos, pipeline y prueba mínima) | `examen-practico/` |

## Notebooks

Cada notebook tiene cuatro niveles (desde cero, con scikit-learn, datos reales y un reto), celdas `TODO` para completar,
una autoverificación y un **desafío opcional con IA agéntica** al final. Su versión resuelta está en
`soluciones/semana-N/`. Los datos se descargan solos (OpenML, scikit-learn o Fairlearn).

**En Google Colab (recomendado):** usa el botón **Abrir en Colab** de cada ejercicio en el aula, o en Colab
*Archivo → Abrir cuaderno → GitHub* y pega la dirección de este repositorio. Guarda tu copia en tu Drive.

**En GitHub Codespaces (no instalas nada):**

[![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/andresrubiop/miar0525-estudiantes)

1. Botón de arriba (o *Code → Codespaces → Create codespace on main*). La primera vez tarda unos minutos: instala el
   entorno del curso con las versiones exactas de `uv.lock`.
2. Abre un notebook de `semana-N/` y elige el kernel `.venv`.
3. Al terminar, detén el codespace: usa la cuota gratuita de tu cuenta de GitHub (se detiene solo tras 30 minutos sin uso).

**En tu equipo con [uv](https://docs.astral.sh/uv/):**

```bash
git clone https://github.com/andresrubiop/miar0525-estudiantes.git && cd miar0525-estudiantes
uv sync --extra mlflow --extra etica --group lab   # Python 3.13, scikit-learn, MLflow, Fairlearn, SHAP y JupyterLab
uv run jupyter lab
```

## IA en el curso

Este curso no es de programación en Python: el código es el medio para entender, comparar y validar métodos. Puedes
usar IA agéntica (Claude Code, Codex, Gemini CLI…) o de chat (ChatGPT, Claude, Gemini) en los ejercicios, los desafíos
y las tareas, **siempre que lo declares**: herramienta, prompts relevantes y qué verificaste tú (norma f del sílabo).
Las decisiones, su justificación y la verificación son tuyas.

## Normas

- Declara el uso de IA generativa y de código externo en cada entrega.
- No subas datos personales ni credenciales a tus repositorios.
- Dudas: por los canales del aula virtual.

---

# Machine Learning · Interactive course hub (UEES)

**Online:** https://andresrubiop.github.io/miar0525-estudiantes/ · **Offline:** *Code → Download ZIP* and open `index.html`. Spanish-language master's course: four
weeks of slides, interactive animations running real algorithms, a manual, notebooks with worked solutions and videos.
Run the notebooks in Google Colab, in GitHub Codespaces (button above) or locally with `uv` (commands above).
