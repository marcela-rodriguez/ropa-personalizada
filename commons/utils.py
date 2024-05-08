import random
import string

def crear_id(lenght: int = 10)-> str:
    # return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lenght)).upper()
    id_creado = ""
    for _ in range(lenght):
        id_creado = id_creado + random.choice(string.ascii_letters + string.digits)
    return id_creado.upper()