import pytest
from src.DNI import Dni


@pytest.mark.checkLen
def test_checkLen():
    assert Dni("12312312A").checkLen()
    assert not Dni("123123ASFSD12A").checkLen()
    assert not Dni("1231").checkLen()

@pytest.mark.checkNumbers
def test_checkNumbers():
    assert Dni('12345678A').checkNumbers()
    assert not Dni('A1234567B').checkNumbers()

@pytest.mark.checkLetter
def test_checkLetter():
    assert Dni('12345678A').checkLetter()
    assert not Dni('123456789O').checkLetter()