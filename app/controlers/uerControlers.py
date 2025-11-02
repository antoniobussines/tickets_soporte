from config.database import SessionLocal
from app.models.personal import Personal
from tkinter import messagebox
from sqlalchemy import and_


def crear_usuario(nombre, correo, contraseña, sector, rol):

    try :
        session = SessionLocal()

        nuevo  = Personal(

           nombre = nombre,
           correo = correo,
           password = contraseña,
           sector = sector,
           rol = rol
        )

        session.add(nuevo)
        session.commit()
        comprobante = session.query(Personal).all()

        print(comprobante)
    
    except Exception as error:

        messagebox.showerror("error inesperado codigo de error" + str(error))

    finally:

        session.close()

def buscar_usuario (nombre, contraseña, pruebas = None):

    session = SessionLocal()

    try:

        usuario = session.query(Personal).filter(and_(Personal.nombre == nombre,
                                                       Personal.password == contraseña)
                                                       ).first()
        
        if  usuario:

            if pruebas:

                text =f"ID: {usuario.id} NOMBRE: {usuario.nombre} CORREO: {usuario.correo} "
                text_dos =f"CONTRASEÑA {usuario.password} SECTOR: {usuario.sector} ROL: {usuario.rol}"
                text_completo = text + text_dos

                return[True, text_completo]        
             
            else:
                
               messagebox.showinfo("estado", f" bienvenido {usuario.nombre} del sector{ usuario.sector} ")

               return [True, usuario.sector]
        

        else:
   
            return [ False]
        
    except Exception as error:

        messagebox.showerror("error inesperado codigo de error" + str(error) )



   
   