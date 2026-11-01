"""Pipeline base del examen práctico. Modifícalo, pero conserva el preprocesamiento DENTRO del pipeline."""
from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .datos import CATEGORICAS, NUMERICAS, SENSIBLES


def construir_pipeline(modelo=None, usar_sensibles: bool = False, denso: bool = False) -> Pipeline:
    """Preprocesamiento (escalado + one-hot con categorías raras agrupadas) y modelo.

    Por defecto NO usa sexo ni raza como variables: se conservan aparte para auditar. Si decides incluirlos,
    justifícalo en el informe. Usa denso=True con modelos que no aceptan matrices dispersas
    (p. ej. HistGradientBoostingClassifier).
    """
    categoricas = [c for c in CATEGORICAS if usar_sensibles or c not in SENSIBLES]
    preprocesamiento = ColumnTransformer([
        ("num", StandardScaler(), NUMERICAS),
        ("cat", OneHotEncoder(handle_unknown="infrequent_if_exist", min_frequency=20), categoricas),
    ], sparse_threshold=0 if denso else 0.3)
    return Pipeline([("prep", preprocesamiento), ("modelo", modelo if modelo is not None else LogisticRegression(max_iter=2000))])
