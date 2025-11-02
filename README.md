
#  Gestor de Tickets de Soporte

Aplicación de escritorio para gestionar tickets de soporte técnico. Permite registrar, visualizar y administrar solicitudes con interfaz gráfica en Tkinter y base de datos SQLAlchemy. Ideal para equipos internos que manejan tareas y reportes.

---

##  Funcionalidades principales

- Registro de tickets con campos como sector, descripción, estado, prioridad, cliente y tipo
- Visualización en tabla interactiva con scroll horizontal
- Validación de campos y manejo de errores
- Interfaz gráfica clara y adaptable a pantalla completa
- Estructura modular para futuras mejoras

---

##  Tecnologías usadas

- Python 3.x
- Tkinter
- SQLAlchemy
- SQLite

---

## ventanas del sisitema

aqui los empleados de la empresa podran iniciar sesion para acceder a la pagina de tickets

![inicio sesion](./img_proyect/inicio_sesion.png)

aqui es donde los empleados podran realizar un ingreso de ticket donde pondran el sector o otro diferente al suyo 
una descripcion para tener nocion del problema etc

![tickets general](./img_proyect/tickets_general.png)

esta se despliega al momento de seleccionar un registro en la tabla pero estas opciones solo estan disponibles para los encargados de soportes o mantencion
![ticket especificos](./img_proyect/ticket_especific.png)

## mer(entidad relacion)

<img width="710" height="143" alt="image" src="https://github.com/user-attachments/assets/3368f686-fc7d-45a0-8a98-04822eeccb00" />

personas 1Nm tickets

tickets mN1 personas


##  Instalación

```bash
git clone https://github.com/tu_usuario/tickets_soporte.git
cd nombre_del_repo
pip install -r requirements.txt
python main.py

