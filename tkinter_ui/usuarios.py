import tkinter
class app:

    def __init__(self):
        self.root =None

    def inicioSesion(self):
        
        self.root = tkinter.Tk()

        self.root.geometry("532x250")
    
        framePrincipal = tkinter.Frame(self.root, relief="raised", bd=3, padx=6, pady=5)
        framePrincipal.pack(pady=40)
        
        tkinter.Label(framePrincipal, text="usuario", font=20).pack()
        self.entryUser = tkinter.Entry(framePrincipal)
        self.entryUser.pack(pady=2)
        self.entryUser.insert(0, "ingresa el nombre")

        tkinter.Label(framePrincipal, text="contraseña", font=20).pack()
        self.EntryPassword = tkinter.Entry(framePrincipal)
        self.EntryPassword.pack(pady=2)
        self.EntryPassword.insert(0, "ingresa la contraseña")
        
        buttonInicioSesion = tkinter.Button(framePrincipal, text= "iniciar")
        buttonInicioSesion.pack(pady=2, fill="x")
        
#----------------- campo usuario --------------------------------------
        def entryUserPlaceholder(event):
            if self.entryUser.get() == "ingresa el nombre":
               self.entryUser.delete(0, "end")
               self.entryUser.config(fg="black")

      

        def outUsuariosPlaceholder(event):
            if self.entryUser.get() == "":
                self.entryUser.insert(0,"ingresa el nombre")
                self.entryUser.config(fg="black")

        self.entryUser.bind('<FocusIn>', entryUserPlaceholder)
        self.entryUser.bind('<FocusOut>', outUsuariosPlaceholder)

#--------------------- campo password --------------------
        
        def entryContraseñaPlaceholder(event):
            
            if self.EntryPassword.get() == "ingresa la contraseña":

                self.EntryPassword.delete(0, "end")
                self.EntryPassword.config(fg= "black")

        def outContraseñaPlaceholder(event):
            if self.EntryPassword.get() == "":

                self.EntryPassword.insert(0, "ingresa la contraseña")
                self.EntryPassword.config(fg= "black")

        self.EntryPassword.bind('<FocusIn>', entryContraseñaPlaceholder)
        self.EntryPassword.bind('<FocusOut>', outContraseñaPlaceholder)

        self.root.mainloop()

objecto = app()

objecto.inicioSesion()

