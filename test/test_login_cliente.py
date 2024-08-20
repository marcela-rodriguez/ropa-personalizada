import pytest
from unittest import mock
from cliente.domain.casos_de_uso.cliente import login_cliente
from cliente.domain.modelos.dto import PeticionParaLogin
from cliente.domain.modelos.modelos import Cliente
from cliente.domain.modelos.excepciones import ErrorClienteNoEncontrado, ContraseñaIncorrecta

@pytest.mark.unittest
@mock.patch("bases_de_datos.cliente_db.consultar_cliente_correo", return_value= Cliente(
        id="frse",
        nombre="Homero Simpson",
        correo="homero@gmail.com",
        contraseña="123456789",
        direccion="Calle Falsa 123",
        telefono="3111111111"))
def test_la_funcion_deberia_validar_que_el_cliente_sea_logiado_de_manera_exitosa(
        consultar_cliente_correo_mock
):
    peticion_login = PeticionParaLogin (
        correo="homero@gmail.com",
        contraseña="123456789",
    )
    client = login_cliente(datos_user=peticion_login)
    assert client is not None


@pytest.mark.unittest
@mock.patch("bases_de_datos.cliente_db.consultar_cliente_correo",return_value= Cliente(
        id="frse",
        nombre="Homero Simpson",
        correo="homero@gmail.com",
        contraseña="123456789",
        direccion="Calle Falsa 123",
        telefono="3111111111"))
def test_la_funcion_deberia_lanzar_una_exepcion_cuando_no_encuentra_el_correo_ingresado(
        consultar_cliente_correo_mock
):
    peticion_login = PeticionParaLogin(
        correo="homero@gmai.com",
        contraseña="123456789",
    )

    with pytest.raises(ErrorClienteNoEncontrado):
        login_cliente(datos_user=peticion_login)


@pytest.mark.unittest
@mock.patch("bases_de_datos.cliente_db.consultar_cliente_correo",return_value=Cliente(
    id="frse",
    nombre="Homero Simpson",
    correo="homero@gmail.com",
    contraseña="123456789",
    direccion="Calle Falsa 123",
    telefono="3111111111"))
def test_la_funcion_deberia_lanzar_una_exepcion_cuando_la_contraseña_es_incorrecta(
        consultar_cliente_correo_mock
):
    peticion_login = PeticionParaLogin(
        correo="homero@gmail.com",
        contraseña="123456789",
    )

    with pytest.raises(ContraseñaIncorrecta):
        login_cliente(datos_user=peticion_login)







