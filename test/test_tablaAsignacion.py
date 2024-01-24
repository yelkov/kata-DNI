import pytest
from src.tablaAsignacion import tablaAsignacion

@pytest.fixture
def inyector():
    tabla = tablaAsignacion()
    return tabla

def test_devolverListaLetras(inyector):
    assert inyector.getListaLetras() == [  
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]