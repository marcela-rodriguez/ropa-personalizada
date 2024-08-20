from typing import List
from producto.domain.modelos.modelos import Producto
from producto.domain.modelos.dto import PeticionParaCrearProducto
from commons.utils import crear_id
# funcionalidades o acciones del sistema

productos: List[Producto] = []
def crear_producto(datos_prod: PeticionParaCrearProducto) -> Producto:
    id_prod = crear_id()
    producto = Producto( # instancia o objeto de la clase producto
        id=id_prod,
        imagen=datos_prod.imagen,
        nombre_producto=datos_prod.nombre,
        color=datos_prod.color,
        talla=datos_prod.talla,
        precio=datos_prod.precio
    )
    productos.append(producto)
    return producto

def consultar_productos()-> List[Producto]:
    return productos
