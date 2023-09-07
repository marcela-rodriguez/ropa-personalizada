from admin.domain.casos_de_uso.administrador import create_admin
from admin.domain.models.dto import PeticionParaCrearAdministrador
from admin.domain.casos_de_uso.administrador import consultar_administradores 
import json # se importa la libreria json
from flask import Flask, Response, request # se importan las clases Flask y Response

app = Flask(__name__) # Se crea una instancia de la clase Flask

# Utilizamos el decorador route de la aplicacon flask 
# para definir un servicio en el recurso /users y el metodo POST
@app.route("/users", methods=["POST"]) 
def pepito_dasdas():
    return Response(
        response=json.dumps({"mensaje": "Mi primera respuesta"}),
        status=200
    ) # Se retorna un objeto Response que tiene el cuerpo de la respuesta y el status code3

@app.route("/admin", methods=["POST"]) 
def create_user():
    cuerpo_peticion = request.get_json()
    user_info=PeticionParaCrearAdministrador(
            nombre=cuerpo_peticion["nombre"],
            correo=cuerpo_peticion["correo"],
            contraseña=cuerpo_peticion["contraseña"],
        )
    administrador = create_admin(user_info=user_info)
    return Response(
        response=json.dumps({"usuario_creado": administrador.__dict__}),
        status=201
    )

@app.route("/admin", methods=["GET"]) 
def consultarUsuario():
    lista_respuesta=[]
    for a in consultar_administradores():
        lista_respuesta.append(a.__dict__)
    
    return Response(
        response=json.dumps({"usuarios creados": lista_respuesta}),
        status=201
      )
  
