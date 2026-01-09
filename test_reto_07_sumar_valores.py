import pytest
from reto_07_sumar_valores import sumar_valores


def test_lista_enteros():
    assert sumar_valores([1, 2, 3]) == 6


def test_lista_mixta():
    assert sumar_valores([1, 2.5, 3]) == 6.5


def test_lista_con_valores_invalidos():
    assert sumar_valores([1, "2", None, 3]) == 4


def test_lista_vacia():
    assert sumar_valores([]) == 0


def test_none_devuelve_cero():
    assert sumar_valores(None) == 0


def test_tipo_incorrecto_lanza_typeerror():
    with pytest.raises(TypeError):
        sumar_valores("123")
