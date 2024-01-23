import pytest
from src.tablaAsignacion import tablaAsignacion

def test_prueba():
    inyector = tablaAsignacion()
    resultado = inyector.getListaLetra()

    valor_esperado = ["T",
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
            "E"] 
    assert resultado == valor_esperado
