import pytest
from src.tablaAsignacion import tablaAsignacion

@pytest.fixture
def inyector():
    tabla = tablaAsignacion()
    return tabla

def test_devolverTabla(inyector):
    assert inyector.getTabla() == [  
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