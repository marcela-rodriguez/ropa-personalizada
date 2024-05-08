from typing import List
from cliente.domain.modelos.modelos import Cliente
from cliente.domain.modelos.dto import PeticionParaCrearUsuario,PeticionParaLogin
from cliente.domain.modelos.excepciones import ErrorClienteNoEncontrado,ErrorClienteYaRegistrado, ContraseñaIncorrecta,CorreoYaRegistrado
from commons.utils import crear_id

clientes: list[Cliente] =[]

def crear_cliente(user:PeticionParaCrearUsuario)-> Cliente:
    
    id_cliente = crear_id()
    cliente = Cliente(
        id=id_cliente,
        nombre=user.nombre,
        correo=user.correo,
        contraseña=user.contraseña, 
        direccion=user.direccion,
        telefono=user.telefono
    )
    for cliente in clientes:
        if user.correo == cliente.correo:
            raise ErrorClienteYaRegistrado(f"Cliente con este correo ya esta registrdo{user.correo}")
    clientes.append(cliente)
    return cliente



def iniciar_sesion(datos_user: PeticionParaLogin) -> Cliente:
    for cliente in clientes:
        print(f"correo: {cliente.correo}, cont: {cliente.contraseña}")
        if datos_user.correo == cliente.correo:
            if datos_user.contraseña == cliente.contraseña:
                return cliente
            raise ContraseñaIncorrecta(f"contraseña incorrecta{datos_user.contraseña}")

    raise ErrorClienteNoEncontrado(f"No se encontro cliente con este correo{datos_user.correo}")
