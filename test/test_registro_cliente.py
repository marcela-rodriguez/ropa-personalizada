import pytest
from unittest import mock
from cliente.domain.casos_de_uso.cliente import crear_cliente
from cliente.domain.modelos.dto import PeticionParaCrearUsuario
from cliente.domain.modelos.excepciones import ErrorClienteNoEncontrado, ErrorClienteYaRegistrado


@pytest.mark.unittest
@mock.patch("bases_de_datos.cliente_db.consultar_cliente_correo", side_effect=ErrorClienteNoEncontrado)
@mock.patch("bases_de_datos.cliente_db.guardar_cliente")
def test_la_funcion_deberia_validar_que_al_crear_cliente_sea_creado_de_manera_exitosa(
        guardar_cliente_mock,
        consultar_cliente_correo_mock
):
    peticion_crear_usuario = PeticionParaCrearUsuario(
        nombre="Homero Simpson",
        correo="homero@gmail.com",
        contraseña="123456789",
        direccion="Calle Falsa 123",
        telefono="3111111111"
    )
    client = crear_cliente(user=peticion_crear_usuario)
    assert client is not None
    assert len(client.id) == 10


@pytest.mark.unittest
@mock.patch("bases_de_datos.cliente_db.consultar_cliente_correo")
@mock.patch("bases_de_datos.cliente_db.guardar_cliente")
def test_la_funcion_deberia_lanzar_una_exepcion_cuando_el_correo_ya_se_encentra_registrado(
        guardar_cliente_mock,
        consultar_cliente_correo_mock
):
    peticion_crear_usuario = PeticionParaCrearUsuario(
        nombre="Homero Simpson",
        correo="homero@gmail.com",
        contraseña="123456789",
        direccion="Calle Falsa 123",
        telefono="3111111111"
    )

    with pytest.raises(ErrorClienteYaRegistrado):
        crear_cliente(user=peticion_crear_usuario)
