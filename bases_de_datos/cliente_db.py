from sqlalchemy import create_engine, text, Engine
from typing import List, Dict, Any
from cliente.domain.modelos.modelos import Cliente
from cliente.domain.modelos import excepciones
from cliente.domain.modelos.modelos import Cliente


def guardar_cliente(cliente: Cliente) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_insert = text(
        f"INSERT INTO Clientes (`id_cliente`,`nombre`, `contraseña`, `correo`,`numero_telefonico`,`direccion`) VALUES ('{cliente.id}','{cliente.nombre}', '{cliente.contraseña}', '{cliente.correo}', '{cliente.telefono}','{cliente.direccion}')")
    connectio.execute(sql_insert)
    connectio.commit()


def consultar_cliente_correo(correo: str) -> Cliente:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()

    consultar_cliente = text(f"SELECT * FROM Clientes WHERE correo='{correo}'")

    resultado = connectio.execute(consultar_cliente).first()
    if resultado:
        cliente = Cliente(
            id=resultado[0],
            nombre=resultado[1],
            contraseña=resultado[2],
            correo=resultado[3],
            telefono=resultado[4],
            direccion=resultado[5]
        )
        return cliente

    raise excepciones.ErrorClienteNoEncontrado(f"No se encontro el cliente con este correo {correo}")
