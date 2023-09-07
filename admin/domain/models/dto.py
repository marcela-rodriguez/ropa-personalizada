class PeticionParaCrearAdministrador:
    def __init__(
            self, 
            nombre: str, 
            correo: str, 
            contraseña: str
    ) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

class PeticionParaConsultarAdministrador:
    def __init__(self) -> None:
        pass        