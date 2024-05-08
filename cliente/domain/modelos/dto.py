class PeticionParaCrearUsuario:
   def __init__(self,nombre: str, correo: str, contraseña: str, direccion: str,telefono:str) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.direccion = direccion
        self.telefono = telefono

class PeticionParaLogin:
    def __init__(self,correo: str,contraseña:str) -> None:
        self.contraseña=contraseña
        self.correo=correo