import pytest
from src.tablaAsignacion import tablaAsignacion

@pytest.fixture
def inyector():
    tabla = tablaAsignacion()
    return tabla

@pytest.mark.getTabla
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

@pytest.mark.getLetra 
def test_getLetra(inyector):
    assert inyector.getLetra(0) == 'T'
    assert inyector.getLetra(2) == 'W'
    assert inyector.getLetra(5) == 'M'

@pytest.mark.getLength
def test_getLenght(inyector):
    assert inyector.getLength() == 23
