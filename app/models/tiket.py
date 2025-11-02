import tkinter as tk
from tkinter import ttk
from app.controlers import ticketControlers
from tkinter import messagebox

class GuiTicket:

    def guiTiket(sector_bool):
        root = tk.Tk()
        root.title("Tickets")
        root.configure(bg="#f0f0f0")
       

        ancho = root.winfo_screenwidth()
        alto = root.winfo_screenheight()
        root.geometry(f"{ancho}x{alto}")

        tk.Label(root, text="Tickets", font=("Arial", 24, "bold"), bg="#f0f0f0").pack(pady=15)

        frame_buttons = tk.Frame(root, bg="#dbeafe")
        frame_buttons.pack(side="top", fill="x", padx=20, pady=5)

        buttons = ["Tickets", "Configuraciones"]
        for x in buttons:
            button = tk.Button(frame_buttons, text=x, font=("Arial", 12), bg="#1e3a8a", fg="white")
            button.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        frame_principal = tk.Frame(root, bg="#f0f0f0")
        frame_principal.pack(fill="both", expand=True)

        frame_form = tk.Frame(frame_principal, bg="#ffffff", padx=12, pady=12, bd=2, relief="groove")
        frame_form.pack(fill="both", padx=10, pady=10)

        def user_soporte():
            frame_form_s_one = tk.Frame(frame_form, bg="#ffffff", padx=3, pady=3)
            frame_form_s_one.pack(fill="x", expand=True)
            
            #.........................sector----------------
            frmae_form_sector = tk.Frame(frame_form_s_one, bg="#e0ecff")
            frmae_form_sector.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frmae_form_sector, text="Sector", font=("Arial", 11), bg="#e0ecff").pack()
            sector = ttk.Combobox(frmae_form_sector, values=["Erno", "Tick"])
            sector.pack(pady=3)
            
            #-------------------------descripcion------------
            frame_form_descripcion = tk.Frame(frame_form_s_one, bg="#e0ecff")
            frame_form_descripcion.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_form_descripcion, text="Descripción", font=("Arial", 11), bg="#e0ecff").pack()
            descripcion = tk.Text(frame_form_descripcion, height=2, width=40)
            descripcion.pack(pady=3)
            
            #--------------------------estado--------------
            frame_from_estado = tk.Frame(frame_form_s_one, bg="#e0ecff")
            frame_from_estado.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_estado, text="Estado", font=("Arial", 11), bg="#e0ecff").pack()
            estado = tk.Entry(frame_from_estado)
            estado.pack(pady=3)
            
            #--------------------------fecha_resolucion--------
            frame_from_fecha_resolucion = tk.Frame(frame_form_s_one, bg="#e0ecff")
            frame_from_fecha_resolucion.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_fecha_resolucion, text="Fecha resolución", font=("Arial", 11), bg="#e0ecff").pack()
            fecha_resolucion = tk.Entry(frame_from_fecha_resolucion)
            fecha_resolucion.pack(pady=3)

            #---------------------frame dos--------------
            frame_form_S_two = tk.Frame(frame_form, bg="#ffffff")
            frame_form_S_two.pack(padx=3, pady=3, expand=True, fill="x")
            
            #----------------------prioridad----------------
            frame_from_prioridad = tk.Frame(frame_form_S_two, bg="#e0ecff")
            frame_from_prioridad.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_prioridad, text="Prioridad", font=("Arial", 11), bg="#e0ecff").pack()
            prioridad = tk.Entry(frame_from_prioridad)
            prioridad.pack(pady=3)

            #--------------------asignado a------------------
            frame_from_asignado_a = tk.Frame(frame_form_S_two, bg="#e0ecff")
            frame_from_asignado_a.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_asignado_a, text="Asignado a", font=("Arial", 11), bg="#e0ecff").pack()
            asignado_a = tk.Entry(frame_from_asignado_a)
            asignado_a.pack(pady=3)

            #--------------------cliente----------------------
            frame_from_cliente = tk.Frame(frame_form_S_two, bg="#e0ecff")
            frame_from_cliente.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_cliente, text="Cliente", font=("Arial", 11), bg="#e0ecff").pack()
            cliente = tk.Entry(frame_from_cliente)
            cliente.pack(pady=3)
            
            #---------------------tipo----------------------
            frame_from_tipo = tk.Frame(frame_form_S_two, bg="#e0ecff")
            frame_from_tipo.pack(padx=3, pady=3, side="left", fill="both", expand=True)
            tk.Label(frame_from_tipo, text="Tipo", font=("Arial", 11), bg="#e0ecff").pack()
            tipo = tk.Entry(frame_from_tipo)
            tipo.pack(pady=3)

            # Botón insertar para soporte
            frame_botones = tk.Frame(frame_form_S_two, bg="#ffffff")
            frame_botones.pack(pady=10, expand=True, fill="both")

            boton_modificar = tk.Button(frame_botones, text="modificar", font=("Arial", 12), bg="#1e3a8a", fg="white", command= lambda: cambiar_registro() )
            boton_modificar.pack(fill="x", padx=3, pady=3)

            boton_eliminar = tk.Button(frame_botones, text="eiminar", font=("Arial", 12), bg="#1e3a8a", fg="white", command= lambda: eliminar()  )
            boton_eliminar.pack(fill="x", padx=3, pady=3)

            def eliminar():
                if sector_bool == "soporte":

                    ticketControlers.eliminar(False, tree)
                    ticketControlers.mostrar(tree)
                
                else:

                    messagebox.showinfo("estado", "esta opcion solo esta disponible para los soprtes ")

            def cambiar_registro():

                if sector_bool == "soporte":

                    ticketControlers.modificar(False, 
                                           sector.get(), 
                                           descripcion.get("1.0", "end-1c"), 
                                           estado.get(), 
                                           fecha_resolucion.get(), 
                                           prioridad.get(), 
                                           asignado_a.get(),
                                           cliente.get(),
                                           tipo.get(),
                                           tree)
                          
                    ticketControlers.mostrar(tree)
                
                else:

                    messagebox.showinfo("estado","esta funcion solo esta disponible para los soportes")

                    


                



        def user_general():
            frame_form_ns = tk.Frame(frame_form, bg="#ffffff")
            frame_form_ns.pack(fill="x", expand=True)

            frame_form_tipo = tk.Frame(frame_form_ns, bg="#e0ecff")
            frame_form_tipo.pack(side="left", fill="both", expand=True, padx=3, pady=3)
            tk.Label(frame_form_tipo, text="Tipo", font=("Arial", 11), bg="#e0ecff").pack()
            entry_tipo = tk.Entry(frame_form_tipo)
            entry_tipo.pack(pady=3)

            frame_form_descripcion = tk.Frame(frame_form_ns, bg="#e0ecff")
            frame_form_descripcion.pack(side="left", fill="both", expand=True, padx=3, pady=3)
            tk.Label(frame_form_descripcion, text="Descripción", font=("Arial", 11), bg="#e0ecff").pack()
            text_descripcion = tk.Text(frame_form_descripcion, height=2, width=40)
            text_descripcion.pack(pady=3)

            frame_form_two = tk.Frame(frame_form, bg="#ffffff")
            frame_form_two.pack(fill="x", expand=True)

            frame_from_cliente = tk.Frame(frame_form_two, bg="#e0ecff")
            frame_from_cliente.pack(side="left", fill="both", expand=True, padx=3, pady=3)
            tk.Label(frame_from_cliente, text="Cliente", font=("Arial", 11), bg="#e0ecff").pack()
            entry_cliente = tk.Entry(frame_from_cliente)
            entry_cliente.pack(pady=3)

            frame_from_sector = tk.Frame(frame_form_two, bg="#e0ecff")
            frame_from_sector.pack(side="left", fill="both", expand=True, padx=2, pady=2)
            tk.Label(frame_from_sector, text="Sector", font=("Arial", 11), bg="#e0ecff").pack()
            combobox_sector = ttk.Combobox(frame_from_sector, values=["RECURSOS HUMANOS", "ADMINISTRACION", "SOPORTE"])
            combobox_sector.pack(pady=3)
            combobox_sector.insert(0, "Ingresa tu sector")

            frame_form_insertar = tk.Frame(frame_form_two, bg="#ffffff")
            frame_form_insertar.pack(fill="both", expand=True, padx=4, pady=4, side="left")
            button_insrtar = tk.Button(frame_form_insertar, text="Insertar", font=("Arial", 12), bg="#1e3a8a", fg="white", command=lambda: insertar())
            button_insrtar.pack(fill="both", anchor="center")

            def insertar():
                ticketControlers.insertar(
                    entry_tipo.get(),
                    text_descripcion.get("1.0", "end").strip(),
                    entry_cliente.get(),
                    combobox_sector.get()
                )
                ticketControlers.mostrar(tree)

        user_general()

        

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="white", background="#1e3a8a")
        style.configure("Treeview", font=("Arial", 11), rowheight=25)

        frame_tree = tk.Frame(frame_principal, bg="#f0f0f0")
        frame_tree.pack(fill="both", padx=10, pady=10, expand=True)

        tree = ttk.Treeview(frame_tree, columns=("id","sector", "descripcion", "estado",
                                                 "fecha_Creacion", "fecha_De_Resolucion",
                                                 "prioridad", "asignado_a", "cliente", "tipo"), show="headings")
        tree.pack(fill="both", expand=True)

      



        tree.heading("id", text="ID")
        tree.heading("sector", text="Sector")
        tree.heading("descripcion", text="Descripción")
        tree.heading("estado", text="Estado")
        tree.heading("fecha_Creacion", text="Fecha Creación")
        tree.heading("fecha_De_Resolucion", text="Fecha Resolución")
        tree.heading("prioridad", text="Prioridad")
        tree.heading("asignado_a", text="Asignado a")
        tree.heading("cliente", text="Cliente")
        tree.heading("tipo", text="Tipo")

        tree.column("id", anchor="center", width=50)
        tree.column("sector", anchor="center", width=120)
        tree.column("descripcion", anchor="center", width=200)
        tree.column("estado", anchor="center", width=100)
        tree.column("fecha_Creacion", anchor="center", width=120)
        tree.column("fecha_De_Resolucion", anchor="center", width=140)
        tree.column("prioridad", anchor="center", width=100)
        tree.column("asignado_a", anchor="center", width=120)
        tree.column("cliente", anchor="center", width=120)
        tree.column("tipo", anchor="center", width=100)

        ticketControlers.mostrar(tree)

        # Scroll horizontal
        scroll_x = ttk.Scrollbar(frame_tree, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scroll_x.set)
        scroll_x.pack(side="bottom", fill="x")

        ultima_seleccion = None  # Variable global o externa a la función


        def elementoTreeSeleccionado(event):
    
          global ultima_seleccion

          seleccion = tree.selection()
          if not seleccion or seleccion == ultima_seleccion:
                return  # No hacer nada si no hay selección o es la misma que antes


          ultima_seleccion = seleccion

          # Limpiar cualquier interfaz previa
          for widget in frame_form.winfo_children():
            widget.destroy()

          # Cargar interfaz de soporte
          user_soporte()

        def deseleccionar(event):
       
           global ultima_seleccion

           region = tree.identify_region(event.x, event.y)

           # Solo si el clic fue fuera de una fila
           if region not in ("cell", "tree"):
             # Quitar selección
             tree.selection_remove(tree.selection())

             # Resetear última selección
             ultima_seleccion = None

             # Limpiar interfaz
             for widget in frame_form.winfo_children():
                widget.destroy()

             # Volver a interfaz general
             user_general()


        # --- Enlaces de eventos ---
        tree.bind("<<TreeviewSelect>>", elementoTreeSeleccionado)
        tree.bind("<Button-1>", deseleccionar, add="+")


        root.mainloop()

        