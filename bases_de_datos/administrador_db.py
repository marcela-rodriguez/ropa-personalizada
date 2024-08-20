# para manipular la base de datos usamos una libreria llamada sqlalchemy
# Debemos de instalar la lbreria sqlchemy en el entorno virtual que estamos creado
# Typing paquete de python para usar los tipar el codigo
from sqlalchemy import create_engine, text
from typing import List, Dict, Any
from admin.domain.modelos.models import  Administrador
from admin.domain.modelos.excepciones import ErrorAdministradorNoEncontrado

def guardar_administrador(administrador:Administrador) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_insert = text(
        f"INSERT INTO Administradores (`id_administrador`,`nombre`, `contraseña`, `correo`) VALUES ('{administrador.id}','{administrador.nombre}', '{administrador.contraseña}', '{administrador.correo}')")
    connectio.execute(sql_insert)


# crear(nombre_admi="serrato", contraseña_admi="123df", numero_telefonico_admi=2123)
def consultar_lista_administradores() -> List[Administrador]:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()

    consulta = text("SELECT * FROM Administradores")
    result = connectio.execute(consulta)
    administradores = []
    for i in result:
        administradores.append(Administrador(
            id= i[0],
            nombre= i[1],
            contraseña= i[2],
            correo= i[3]
        ))
    return administradores


# print(consultar())
def consultar_administrador_id(id_administrador:str)-> Administrador:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()

    consultar_administrador = text(f"SELECT * FROM Administradores WHERE id_administrador= '{id_administrador}'")

    resultado = connectio.execute(consultar_administrador).first()
    if resultado:
        administrador=Administrador(
            id=resultado[0],
            nombre=resultado[1],
            contraseña=resultado[2],
            correo=resultado[3],
        )
        return administrador

    raise ErrorAdministradorNoEncontrado(f"No se encontro el administrados con este id {id_administrador}")
def consultar_administrador_correo(correo:str)-> Administrador:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()

    consultar_administrador = text(f"SELECT * FROM Administradores WHERE correo = '{correo}'")

    resultado = connectio.execute(consultar_administrador).first()
    if resultado:
        administrador=Administrador(
            id=resultado[0],
            nombre=resultado[1],
            contraseña=resultado[2],
            correo=resultado[3],
        )
        return administrador

    raise ErrorAdministradorNoEncontrado(f"No se encontro el administradosr con este correo {correo}")


def actualizar(id_administrador: int, nombre_admi: str) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_actualizar = text(
        f"UPDATE administradores SET nombre_admi='{nombre_admi}' WHERE id_administrador= '{id_administrador}'")
    connectio.execute(sql_actualizar)


# actualizar(id_administrador=5, nombre_admi="serrato sanchez")
# print(consultar())

def eliminar(id_administrador: int) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_eliminar = text(f"DELETE FROM Administradores WHERE id_administrador='{id_administrador}'")
    connectio.execute(sql_eliminar)


# eliminar(id_administrador=6)

# Usamos un menu de opcines para provar las funciones creadas y mayor usablidad
