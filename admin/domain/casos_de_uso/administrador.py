from typing import List
from admin.domain.modelos import dto as dto_admi
from admin.domain.modelos.models import Administrador
from admin.domain.modelos.excepciones import ErrorAdministradorNoEncontrado, ContraseñaIncorrecta, CorreoYaRegistrado
from commons.utils import crear_id
from bases_de_datos import administrador_db as repositorio_admin


def create_admin(user_info: dto_admi.PeticionParaCrearAdministrador) -> Administrador:
    for administrador in repositorio_admin.consultar_lista_administradores():
        if user_info.correo == administrador.correo:
            raise CorreoYaRegistrado()

    id_administrador = crear_id()
    administrador = Administrador(
        id=id_administrador,
        nombre=user_info.nombre,
        correo=user_info.correo,
        contraseña=user_info.contraseña
    )
    repositorio_admin.guardar_administrador(administrador=administrador)
    return administrador


def consultar_administradores() -> List[Administrador]:
    return repositorio_admin.consultar_lista_administradores()


def consultar_administrador_por_id(id_administrador: str) -> Administrador:
    return repositorio_admin.consultar_administrador_id(id_administrador=id_administrador)


def login_administrador(datos_user: dto_admi.PeticionParaLogin) -> Administrador:
    a = repositorio_admin.consultar_administrador_correo(correo=datos_user.correo)
    if datos_user.correo == a.correo:
        if datos_user.contraseña == a.contraseña:
            return a
        raise ContraseñaIncorrecta(f"contraseña incorrecta{datos_user.contraseña}")

    raise ErrorAdministradorNoEncontrado(f"No se encontro el administrados con este correo{datos_user.correo}")
