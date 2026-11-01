from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.datos import particion
from src.pipeline import construir_pipeline


def test_preprocesamiento_dentro_del_pipeline():
    p = construir_pipeline()
    assert isinstance(p, Pipeline)
    assert isinstance(p.steps[0][1], ColumnTransformer), "El preprocesamiento debe ser el primer paso del pipeline."


def test_pipeline_entrena_y_predice_probabilidades(datos):
    X, y = datos
    X_tr, X_te, y_tr, _ = particion(X, y, semilla=5)
    p = construir_pipeline().fit(X_tr, y_tr)
    prob = p.predict_proba(X_te)[:, 1]
    assert prob.shape == (len(X_te),) and ((prob >= 0) & (prob <= 1)).all()
