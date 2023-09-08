from admin.domain.casos_de_uso.administrador import create_admin
from admin.domain.models.dto import PeticionParaCrearAdministrador
from admin.domain.casos_de_uso.administrador import consultar_administradores, consultar_administrador_por_id
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
def servicio_crear_administrador():
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
def servicio_consultar_administradores():
    lista_respuesta=[]
    for administrador in consultar_administradores():
        lista_respuesta.append(administrador.__dict__)
    
    return Response(
        response=json.dumps({"administradores": lista_respuesta}),
        status=201
      )
  
@app.route("/admin/<id_administrador>", methods=["GET"])
def servicio_consultar_administrador(id_administrador:str):
    print(id_administrador)
    try:
        return Response(
            response=json.dumps(consultar_administrador_por_id(id_administrador=id_administrador).__dict__),
            status=201
        )
    except Exception:
        return Response(
            response=json.dumps({"error": "Administrador no encontrado"}),
            status=404
        )