import pytest

from src.datos import cargar_datos


@pytest.fixture(scope="session")
def datos():
    """Una muestra pequeña de un estado para que las pruebas sean rápidas (la primera vez descarga los datos)."""
    return cargar_datos("WV", semilla=1, n_max=3000)
