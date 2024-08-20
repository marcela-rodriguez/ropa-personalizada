from admin.domain.casos_de_uso import administrador as casos_admi
from cliente.domain.casos_de_uso import cliente as casos_cli
from admin.domain.modelos import dto as dto_admi
from cliente.domain.modelos.dto import PeticionParaCrearUsuario, PeticionParaLogin
from admin.domain.modelos import excepciones as excepciones_admi
from cliente.domain.modelos import excepciones as excepciones_cliente
from producto.domain.modelos.dto import PeticionParaCrearProducto
from producto.domain.casos_de_uso import producto as casos
import json # se importa la libreria json
from flask import Flask, Response, request# se importan las clases Flask y Response
from flask_cors import CORS # se importa cors para validar el dominio de la peticion
app = Flask(__name__) # Se crea una instancia de la clase Flask
CORS(app, origins=["*"])#configurar flask con Cors

# Utilizamos el decorador route de la aplicacion flask 
# para definir un servicio en el recurso /users y el metodo POST
@app.route("/users", methods=["POST"]) 
def pepito_dasdas():
    return Response(
        response=json.dumps({"mensaje": "Mi primera respuesta"}),
        status=200
    ) # Se retorna un objeto Response que tiene el cuerpo de la respuesta y el status code3

#se crea el servicio de creacion de administrador en el recurso admin con metodo POST
@app.route("/admin", methods=["POST"]) 
def servicio_crear_administrador():
    cuerpo_peticion = request.get_json()
    user_info=dto_admi.PeticionParaCrearAdministrador(
            nombre=cuerpo_peticion["nombre"],
            correo=cuerpo_peticion["correo"],
            contraseña=cuerpo_peticion["contraseña"],
        )
    try:
        administrador = casos_admi.create_admin(user_info=user_info)
        return Response(
            response=json.dumps({"usuario_creado": administrador.__dict__}),
            status=201
        )
    except excepciones_admi.CorreoYaRegistrado:
        return Response(
            response=json.dumps({"mensaje":"correo ya registrado"})
        )


#se crea el servicio de consultar administradores en el recurso admin con metodo GET
@app.route("/admin", methods=["GET"]) 
def servicio_consultar_administradores():
    lista_respuesta=[]
    for administrador in casos_admi.consultar_administradores():
        lista_respuesta.append(administrador.__dict__)
    
    return Response(
        response=json.dumps({"administradores": lista_respuesta}),
        status=201
      )
#se crea el servicio de consultar administradores por id en el recurso admin/id_adminitrador con metodo GET
@app.route("/admin/<id_administrador>", methods=["GET"])
def servicio_consultar_administrador(id_administrador:str):
    # controlas las excepciones
    try:
        return Response(
            response=json.dumps(casos_admi.consultar_administrador_por_id(id_administrador=id_administrador).__dict__),
            status=201
        )
    except excepciones_admi.ErrorAdministradorNoEncontrado as e:
        print(str(e))
        return Response(
            response=json.dumps({"error": "Administrador no encontrado"}),
            status=404
        )

# se crea el servicio de login para administradores en el recurso admin/login con metodo POST
@app.route("/admin/login", methods=["POST"])
def login_administrador():
    cuerpo_peticion=request.get_json()
    datos_user=dto_admi.PeticionParaLogin(
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"]
    )#controlas las excepciones

    try:
        a=casos_admi.login_administrador(datos_user=datos_user)
        return Response(
            response=json.dumps({"mensaje": a.__dict__}),
            status=200
        )
    except excepciones_admi.ErrorAdministradorNoEncontrado:
        return Response(
            response=json.dumps({"error": "administrador no encontrado"}),
            status=404
        )
    except excepciones_admi.ContraseñaIncorrecta:
        return Response(
            response=json.dumps({"error":"contraseña incorrecta"}),
            status=404
        )
# se crea el servicio para crear cliente  en el recurso cliente con metodo POST
@app.route("/cliente",methods=["POST"])
def servicio_crear_Cliente():
    cuerpo_peticion = request.get_json()
    user=PeticionParaCrearUsuario(
        nombre=cuerpo_peticion["nombre"],
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"], 
        direccion=cuerpo_peticion["direccion"],
        telefono=cuerpo_peticion["telefono"]
    )#controlas las excepciones para crear el usuario y saber si ya esta creado al momento del registro
    try:
        cliente= casos_cli.crear_cliente(user=user)

        return Response(
            response=json.dumps({"usuario_creado": cliente.__dict__}),#se retorna mensaje cuando el usario es creado
            status=201
        )
    except excepciones_cliente.ErrorClienteYaRegistrado:
        return Response(
            response=json.dumps({"error": "El cliente ya exixiste"}),# se retorna un mesaje si el usuario ya esta creado
            status=400
        )
# se crea el servicio de login para cliente en el recurso cliente/login con metodo POST
@app.route("/cliente/login", methods=["POST"])
def login_cliente():
    cuerpo_peticion=request.get_json()
    datos_user=PeticionParaLogin(
        correo=cuerpo_peticion["correo"],
        contraseña=cuerpo_peticion["contraseña"]
    )#controlas las excepciones para validar que ingreso correctamente,si el usuario no esta registrado o si la contraseña es incorrecta.
    try:
        a=casos_cli.login_cliente(datos_user=datos_user)
        return Response(
            response=json.dumps({"ingreso exito":a.__dict__}),#retorna mensaje cuando es correcto el ingreso del usuario.
            status=200

        )
    except excepciones_cliente.ErrorClienteNoEncontrado:
        return Response(
            response=json.dumps({"error": "cliente no registrado con este correo"}), #retorna un errror de cliente no encontrado o no regitrado.
            status=404
        )
    except excepciones_cliente.ContraseñaIncorrecta:
        return Response(
            response=json.dumps({"error":"contraseña incorrecta"}),#retorna mesnaje cuando la contrasena es incorrecta.
            status=404
        )

@app.route("/producto", methods=["POST"])
def crear_producto():
    cuerpo_peticion=request.get_json()
    datos_prod=PeticionParaCrearProducto(
        imagen=cuerpo_peticion["imagen"],
        nombreProducto=cuerpo_peticion["nombre"],
        color=cuerpo_peticion["color"],
        talla=cuerpo_peticion["talla"],
        precio=cuerpo_peticion["precio"],
    )
    producto = casos.crear_producto(datos_prod=datos_prod)
    return Response(
        response=json.dumps({"Prducto creado": producto.__dict__}),
        status=200
    )

@app.route("/producto", methods=["GET"])
def servicio_consultar_productos():
    lista_respuesta = []
    for producto in casos.consultar_productos():
        lista_respuesta.append(producto.__dict__)

    return Response(
        response=json.dumps({"Productos": lista_respuesta}),
        status=201
    )


