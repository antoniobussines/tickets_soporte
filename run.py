from config.database import Base,engine
from app.models import iniciarsesion
from testeos.bd_personal import busqueda_personal, pruebas_bd_personal
from testeos.bd_tickets import pruebas_db_tickets


class funciones_generales:

 def crear_tablas():
    Base.metadata.create_all(bind=engine)
    print("tabla creada")

 def ejecutar_programa():
 
    instacnia = iniciarsesion.GuiInicioSesion()
    instacnia.ejecutar()

 def insertar_usuario():

    pruebas_bd_personal.insertar_usuario()
 
 def buscar_usuario():

    busqueda_personal.buscar_usuario()
 def modificar_ticket():
    
    pruebas_db_tickets.modificar()
 
 def eliminar_ticket():
    
    pruebas_db_tickets.eliminar()


funciones_generales.ejecutar_programa()









