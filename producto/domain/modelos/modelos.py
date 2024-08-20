# todo lo que sean clases son entidades que se refiera a la abstraccion del mundo real
class Producto:
    def __init__(self, id: str, imagen: str, nombre_producto: str, color: str, talla: str, precio: int) -> None:
        self.id = id
        self.imagen = imagen
        self.nombre = nombre_producto
        self.color = color
        self.talla = talla
        self.precio = precio
