class PeticionParaCrearProducto:
    def __init__(self,imagen:str, nombreProducto:str, color:str, talla:str, precio:int ) -> None:
        self.imagen = imagen
        self.nombre = nombreProducto
        self.color = color
        self.talla = talla
        self.precio = precio


