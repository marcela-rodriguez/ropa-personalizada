class PeticionParaCrearAdministrador:
    def __init__(self, nombre: str, correo: str, contraseña: str) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        
class PeticionParaLogin:
    def __init__(self,correo: str,contraseña:str) -> None:
        self.contraseña=contraseña
        self.correo=correo