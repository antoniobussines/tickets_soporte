from app.controlers import uerControlers

#ejecutar esta funcion en el run

def  insertar_usuario ():

    sectores =["administracion","soporte","recepcion"]

    uerControlers.crear_usuario("luis","luiscoman@gmail.com","123",sectores[0],"recepcionista")

def buscar_usuario ():

    uerControlers.buscar_usuario("antonio","123",True)