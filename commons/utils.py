import random
import string

def crear_id(lenght: int = 10)-> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lenght)).upper()