class Cliente:
    def __init__(self, id: str, nombre: str, correo: str, contraseña: str, direccion: str,telefono:str) -> None:
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.direccion = direccion
        self.telefono = telefono
        