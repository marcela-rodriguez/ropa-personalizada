from admin.domain.casos_de_uso.administrador import create_admin,iniciar_sesion
from cliente.domain.casos_de_uso.cliente import crear_cliente,iniciar_sesion
from admin.domain.modelos.dto import PeticionParaCrearAdministrador,PeticionParaLogin
from cliente.domain.modelos.dto import PeticionParaCrearUsuario, PeticionParaLogin
from admin.domain.modelos.excepciones import ErrorAdministradorNoEncontrado,ContraseñaIncorrecta,CorreoYaRegistrado
from cliente.domain.modelos.excepciones import ErrorClienteNoEncontrado,ErrorClienteYaRegistrado,ContraseñaIncorrecta,CorreoYaRegistrado
from admin.domain.casos_de_uso.administrador import consultar_administradores, consultar_administrador_por_id
import json # se importa la libreria json
from flask import Flask, Response, request# se importan las clases Flask y Response
from flask_cors import CORS

app = Flask(__name__) # Se crea una instancia de la clase Flask
CORS(app, origins=["*"])

# Utilizamos el decorador route de la aplicacion flask 
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
    try:
        administrador = create_admin(user_info=user_info)
        return Response(
            response=json.dumps({"usuario_creado": administrador.__dict__}),
            status=201
        )
    except CorreoYaRegistrado:
        return Response(
            response=json.dumps({"mensaje":"correo ya registrado"})
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
    except ErrorAdministradorNoEncontrado:
        return Response(
            response=json.dumps({"error": "Administrador no encontrado"}),
            status=404
        )
    
@app.route("/admin/login", methods=["POST"])
def login():
    cuerpo_peticion=request.get_json()
    datos_user=PeticionParaLogin(
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"]
    )

    try:
        iniciar_sesion(datos_user=datos_user)
        return Response(
            response=json.dumps({}),
            status=200
        )
    except ErrorAdministradorNoEncontrado:
        return Response(
            response=json.dumps({"error": "administrador no encontrado"}),
            status=404
        )
    except ContraseñaIncorrecta:
        return Response(
            response=json.dumps({"error":"contraseña incorrecta"}),
            status=404
        )

@app.route("/cliente",methods=["POST"])
def servicio_crear_comprador():
    print("iniciando al servicio")
    cuerpo_peticion = request.get_json()
    user=PeticionParaCrearUsuario(
        nombre=cuerpo_peticion["nombre"],
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"], 
        direccion=cuerpo_peticion["direccion"],
        telefono=cuerpo_peticion["telefono"]
    )
    try:
        cliente= crear_cliente(user=user)
        return Response(
            response=json.dumps({"usuario_creado": cliente.__dict__}),
            status=201
        )
    except ErrorClienteYaRegistrado:
        return Response(
            response=json.dumps({"error": "El cliente ya exixiste"}),
            status=400
        )

@app.route("/cliente/login", methods=["POST"])
def loginCliente():
    cuerpo_peticion=request.get_json()
    datos_user=PeticionParaLogin(
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"]
    )

    try:
        iniciar_sesion(datos_user=datos_user)
        return Response(
            response=json.dumps({"mensaje": "ingreso exito"}),
            status=200

        )
    except ErrorClienteNoEncontrado:
        return Response(
            response=json.dumps({"error": "cliente no encontrado"}),
            status=404
        )
    except ContraseñaIncorrecta:
        return Response(
            response=json.dumps({"error":"contraseña incorrecta"}),
            status=404
        )