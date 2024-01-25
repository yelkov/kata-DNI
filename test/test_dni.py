import pytest
from src.DNI import Dni


@pytest.mark.checkLen
def test_checkLen():
    assert Dni("12312312A").checkLen()
    assert not Dni("123123ASFSD12A").checkLen()
    assert not Dni("1231").checkLen()