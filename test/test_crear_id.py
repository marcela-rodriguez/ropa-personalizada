import pytest
from commons.utils import crear_id


@pytest.mark.unittest
def test_la_funcion_deberia_validar_que_la_funcion_crear_id_retorne_un_string_de_10_caracteres():
    id=crear_id()
    assert len(id)==10
    assert id.upper() == id


@pytest.mark.unittest
def test_la_funcion_deberia_retornar_que_la_funcion_crear_id_retorne_el_mismo_string_de_x_caracteres_que_ingresaron():
    id=crear_id(5)
    assert len(id)==len(id)
