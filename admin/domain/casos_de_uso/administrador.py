from typing import List
from admin.domain.models.dto import PeticionParaCrearAdministrador
from admin.domain.models.models import Administrador
from commons.utils import crear_id

administradores: List[Administrador] = []

def create_admin(user_info: PeticionParaCrearAdministrador) -> Administrador:
    id_administrador = crear_id()
    administrador = Administrador(
        id=id_administrador, 
        nombre=user_info.nombre,
        correo=user_info.correo,
        contraseña=user_info.contraseña
    )
    administradores.append(administrador)
    return administrador

def consultar_administradores() -> List[Administrador]:
    return administradores

def consultar_administrador_por_id(id_administrador:str)-> Administrador:
    for administrador in administradores:
        if id_administrador == administrador.id:
            return administrador
    raise Exception(f"No encontre un administrador con el id {id_administrador}")
        
