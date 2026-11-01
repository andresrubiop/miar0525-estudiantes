from src.datos import CATEGORICAS, NUMERICAS, grupos_sensibles, particion
from variante import ESTADOS, asignar_variante


def test_variante_determinista():
    assert asignar_variante("A001") == asignar_variante(" a001 ")
    assert asignar_variante("A001") != asignar_variante("A002")
    estado, semilla = asignar_variante("A001")
    assert estado in ESTADOS and 1000 <= semilla < 10000


def test_objetivo_binario_sin_fuga(datos):
    X, y = datos
    assert set(y.unique()) == {0, 1}
    assert "PINCP" not in X.columns, "El ingreso no puede ser una variable: es el objetivo."
    assert len(X) == len(y) <= 3000


def test_columnas_esperadas(datos):
    X, _ = datos
    assert set(NUMERICAS + CATEGORICAS) <= set(X.columns)


def test_grupos_sensibles(datos):
    A = grupos_sensibles(datos[0])
    assert set(A["sexo"].unique()) <= {"Hombre", "Mujer"}
    assert A.notna().all().all()


def test_particion_reproducible_y_estratificada(datos):
    X, y = datos
    a, b = particion(X, y, semilla=5), particion(X, y, semilla=5)
    assert a[0].index.equals(b[0].index)
    assert abs(a[2].mean() - a[3].mean()) < 0.02
