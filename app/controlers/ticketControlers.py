from config.database import SessionLocal
from app.models.personal import Tickets
from tkinter import messagebox
from tkinter import simpledialog

def insertar ( tipo, descripcion, cliente, sector):

    try:
        sesion = SessionLocal()

        nuevo = Tickets(

             sector=sector,
             descripcion=descripcion,
             estado="en proceso",
             tipo=tipo,
             fecha_resolucion=None,
             prioridad="sin asignar",
             cliente=cliente,
             asignado_a= 3
             # fecha_creacion se genera automáticamente
        )
    
        sesion.add(nuevo)
        sesion.commit()
    
    except Exception as error:

        messagebox.showerror("error inesperado codigo de error" + str(error))

    finally:

        sesion.close()

def eliminar (modo, tree = None):

    try:

        sesion =SessionLocal()

      
        if modo:

            id_elemento = simpledialog.askinteger("estado","ingresa el registro a eliminar")
                  
        else:
            elemento = tree.selection()
            for x in elemento:

             valores = tree.item(x, "values")

             id_elemento = valores[0]
            
            
        ticket = sesion.query(Tickets).filter_by(id = id_elemento).first()

        if ticket:

            sesion.delete(ticket)
            sesion.commit()
            messagebox.showinfo("estado", "registro eliminado con exito")
        
        else:

            messagebox.showinfo("estado", "el registro no eiste")


    except Exception as error :

        messagebox.showerror("estado", "error inesperado codigo de error" + str(error))

    finally:

        sesion.close()

    

def mostrar (tree):

    try:
        sesion = SessionLocal()

        registros =sesion.query(Tickets).all()

        ids = tree.get_children()

        for y in ids:

           tree.delete(y)

        for x in registros:

           tree.insert("", "end", values=(x.id, 
                                          x.sector, 
                                          x.descripcion, 
                                          x.estado, 
                                          x.fecha_creacion, 
                                          x.fecha_resolucion, 
                                          x.prioridad, 
                                          x.asignado_a, 
                                          x.cliente, 
                                          x.tipo))
    
    except Exception as error:

        messagebox.showerror("error inesperado codigo de error" + str(error))

    finally:

        sesion.close()

def modificar (modo, sector, descripcion, estado, fecha_Resolucion, prioridad, asignado_a, cliente, tipo, tree =None):
    

    sesion = SessionLocal()

    if modo:
        id = simpledialog.askinteger("estado","ingresa id que deseas eliminar")
    else:
        elemento = tree.selection()

        if not elemento:

            messagebox.showinfo("estado"," selecciona un registro")
            return 
         
        for x in elemento:

            valores = tree.item(x, "values")
            id = valores[0]
        
        
    registro = sesion.query(Tickets).filter_by(id = id).first()
    if sector:

        registro.sector = sector
    
    if descripcion:

        registro.descripcion = descripcion
    
    if estado:

        registro.estado = estado

    if fecha_Resolucion:

        registro.fecha_resolucion = fecha_Resolucion

    if prioridad:

        registro.asignado_a = asignado_a

    if cliente:

        registro.cliente = cliente

    if tipo:

        registro.tipo = tipo

    if registro:

        sesion.commit()
    
    if modo:

        txt1 =f"ID: {registro.id} SECTOR: {registro.sector}, DESCRIPCION: { registro.descripcion} ESTADO: {registro.fecha_resolucion}"
        txt2= f"PRIORIDAD: {registro.prioridad} ASIGNADO_A: {registro.asignado_a} CLIENTE: {registro.cliente} TIPO: {registro.tipo}"

        texto_completo=txt1 + txt2

        return texto_completo


         
         


   
    

   
    
   


    



   
