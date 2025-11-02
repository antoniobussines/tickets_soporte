import tkinter as tk
from app.models import tiket
from app.controlers import uerControlers
from tkinter import messagebox

class GuiInicioSesion:

    def ejecutar(self):
        root =tk.Tk()
        root.title("inicioSesion")
        root.geometry("500x235")

        framePrincipal = tk.Frame(root, padx=2, pady=3, border=3, relief="raised")
        framePrincipal.pack(padx=10, pady=20)

        tk.Label(framePrincipal, text="nombre", font=12).pack()
        entry_nombre =tk.Entry(framePrincipal)
        entry_nombre.pack(fill="both")
        entry_nombre.insert(0, "ingresa el nombre")

        entry_password =tk.Label(framePrincipal, text="nombre", font=12).pack()
        entry_password= tk.Entry(framePrincipal)
        entry_password.pack(fill="both",pady=2)

        button_iniciar_sesion = tk.Button(framePrincipal, text="iniciar", command= lambda:funcion_general())
        button_iniciar_sesion.pack(fill="x")

        def funcion_general():

            bool = uerControlers.buscar_usuario(entry_nombre.get(), entry_password.get())



            if bool[0]:
                root.destroy()
                tiket.GuiTicket.guiTiket(bool[1])
            else:

                messagebox.showinfo("estado", "usuario no encontrado")

                
        
        entry_password.insert(0, "ingresa la contraseña")

        def entryPlaceholderName(event):
            if entry_nombre.get() == "ingresa el nombre":
                entry_nombre.delete(0,tk.END)
                entry_nombre.config(fg="black")
        
        def outPlaceholderName(event):
            if entry_nombre.get() == "":
                entry_nombre.insert(0,"ingresa el nombre")
                entry_nombre.config(fg="black")

        entry_nombre.bind('<FocusIn>', entryPlaceholderName)
        entry_nombre.bind('<FocusOut>', outPlaceholderName)

        
        def entryPlaceholderContraseña(event):
            if entry_password.get() == "ingresa la contraseña":
                entry_password.delete(0, tk.END)
                
        def outPlaceholderContraseña(event):
            if entry_password.get() == "":
                entry_password.insert(0, "ingresa la contraseña")
                entry_password.config(fg="black")

        entry_password.bind('<FocusIn>', entryPlaceholderContraseña)
        entry_password.bind('<FocusOut>', outPlaceholderContraseña)





    
        root.mainloop()




