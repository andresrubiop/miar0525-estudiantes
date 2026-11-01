#!/usr/bin/env bash
# Prepara el Codespace del curso (se ejecuta una vez, al crearlo): entorno con las versiones exactas de uv.lock.
set -e
python3 -m pip install --quiet --user uv
python3 -m uv sync --frozen --extra mlflow --extra etica --group lab
echo
echo "Listo. Abre un notebook de semana-N/ y elige el kernel .venv."
