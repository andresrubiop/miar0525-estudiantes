"""Carga, grupos sensibles y partición de ACS Income para el examen práctico.

Datos: ACSIncome (Ding et al., 2021), distribuido por Fairlearn (`fetch_acs_income`, OpenML 43141).
Objetivo: ingreso personal anual (PINCP) mayor que 50 000 USD. Atributos sensibles: SEX y RAC1P.
"""
from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split

UMBRAL_INGRESO = 50_000
NUMERICAS = ["AGEP", "WKHP"]
CATEGORICAS = ["COW", "SCHL", "MAR", "OCCP", "POBP", "RELP", "SEX", "RAC1P"]
SENSIBLES = ["SEX", "RAC1P"]

DICCIONARIO = {
    "AGEP": "edad en años",
    "COW": "clase de trabajador (1 empleado privado con fines de lucro … 9 desempleado sin experiencia)",
    "SCHL": "nivel educativo alcanzado (1 sin escolaridad … 24 doctorado)",
    "MAR": "estado civil (1 casado, 2 viudo, 3 divorciado, 4 separado, 5 nunca casado)",
    "OCCP": "código de ocupación (cientos de categorías)",
    "POBP": "lugar de nacimiento (estado o país; cientos de categorías)",
    "RELP": "relación con la persona de referencia del hogar",
    "WKHP": "horas trabajadas por semana en el último año",
    "SEX": "sexo (1 hombre, 2 mujer) · sensible",
    "RAC1P": "raza (1 blanca, 2 negra, 3–5 indígena de EE. UU. o Alaska, 6 asiática, 7 isleña del Pacífico, 8 otra, 9 dos o más) · sensible",
}
RAZA = {1: "Blanca", 2: "Negra", 6: "Asiática"}          # el resto se agrupa en "Otra o multirracial"


def cargar_datos(estado: str, semilla: int, n_max: int = 40_000) -> tuple[pd.DataFrame, pd.Series]:
    """Devuelve (X, y) para un estado: y = 1 si el ingreso supera 50 000 USD. Si hay más de n_max filas, toma una muestra."""
    from fairlearn.datasets import fetch_acs_income

    datos = fetch_acs_income(as_frame=True, states=[estado])
    X = datos.data.reset_index(drop=True)
    y = (datos.target.reset_index(drop=True) > UMBRAL_INGRESO).astype(int).rename("ingreso_alto")
    if len(X) > n_max:
        idx = X.sample(n_max, random_state=semilla).index
        X, y = X.loc[idx].reset_index(drop=True), y.loc[idx].reset_index(drop=True)
    return X, y


def grupos_sensibles(X: pd.DataFrame) -> pd.DataFrame:
    """Sexo y raza legibles, para auditar (no para entrenar). La agrupación de raza es una decisión: justifícala."""
    return pd.DataFrame({
        "sexo": X["SEX"].map({1: "Hombre", 2: "Mujer"}),
        "raza": X["RAC1P"].map(lambda v: RAZA.get(int(v), "Otra o multirracial")),
    }, index=X.index)


def particion(X: pd.DataFrame, y: pd.Series, semilla: int, prueba: float = 0.25):
    """Partición estratificada y reproducible: (X_tr, X_te, y_tr, y_te). La prueba se separa primero y se usa una vez."""
    return train_test_split(X, y, test_size=prueba, stratify=y, random_state=semilla)
