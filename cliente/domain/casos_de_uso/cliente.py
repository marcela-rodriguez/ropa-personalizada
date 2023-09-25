from typing import List
from cliente.domain.modelos.modelos import Cliente
from cliente.domain.modelos.dto import PeticionParaCrearUsuario
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
    clientes.append(cliente)
    return cliente
