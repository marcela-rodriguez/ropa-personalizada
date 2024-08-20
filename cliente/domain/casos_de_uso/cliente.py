from typing import List
from cliente.domain.modelos.modelos import Cliente
from cliente.domain.modelos.dto import PeticionParaCrearUsuario,PeticionParaLogin
from cliente.domain.modelos.excepciones import ErrorClienteNoEncontrado,ErrorClienteYaRegistrado, ContraseñaIncorrecta,CorreoYaRegistrado
from commons.utils import crear_id
from bases_de_datos import cliente_db as repositorio_cli
from cliente.domain.modelos import excepciones
#casos de uso
clientes: list[Cliente] =[]
#funcion para crear los clientes y validad si el cliente ya esta registrado
def crear_cliente(user:PeticionParaCrearUsuario)-> Cliente:
    try:
        repositorio_cli.consultar_cliente_correo(correo=user.correo)
        raise ErrorClienteYaRegistrado(f"Cliente con este correo ya esta registrado{user.correo}")
    except excepciones.ErrorClienteNoEncontrado:
        id_cliente = crear_id()
        cliente = Cliente(
            id=id_cliente,
            nombre=user.nombre,
            correo=user.correo,
            contraseña=user.contraseña,
            direccion=user.direccion,
            telefono=user.telefono
        )
        repositorio_cli.guardar_cliente(cliente=cliente)
        return cliente


#funcion para validar si el usuario ya existe por medio del correo y contraseña incorrecta
def login_cliente(datos_user: PeticionParaLogin) -> Cliente:
    cliente=repositorio_cli.consultar_cliente_correo(correo=datos_user.correo)
    if datos_user.correo == cliente.correo:
        if datos_user.contraseña == cliente.contraseña:
            return cliente
        raise ContraseñaIncorrecta(f"contraseña incorrecta{datos_user.contraseña}")

    raise ErrorClienteNoEncontrado(f"No se encontro cliente con este correo{datos_user.correo}")
