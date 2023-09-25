from typing import List
from admin.domain.modelos.dto import PeticionParaCrearAdministrador,PeticionParaLogin
from admin.domain.modelos.models import Administrador
from admin.domain.modelos.excepciones import ErrorAdministradorNoEncontrado,ContraseñaIncorrecta,CorreoYaRegistrado
from commons.utils import crear_id

administradores: List[Administrador] = []

def create_admin(user_info: PeticionParaCrearAdministrador) -> Administrador:
    for administrador in administradores:
        if user_info.correo == administrador.correo:
            raise CorreoYaRegistrado()
        
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
    raise ErrorAdministradorNoEncontrado(f"No encontre un administrador con el id {id_administrador}")

def iniciar_sesion(datos_user: PeticionParaLogin)-> Administrador:
    for administrador in administradores:
        if datos_user.correo==administrador.correo:
            if datos_user.contraseña==administrador.contraseña:
                return administrador
            raise ContraseñaIncorrecta(f"contraseña incorrecta{datos_user.contraseña}")

    raise ErrorAdministradorNoEncontrado(f"No se encontro el administrados con este correo{datos_user.correo}")
   
         

        
