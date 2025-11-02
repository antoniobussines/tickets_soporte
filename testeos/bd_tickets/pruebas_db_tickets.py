from app.controlers import ticketControlers


def agregar_ticket():

    ticketControlers.insertar("falla mecanica", "error en la engrapadora", "juan", "administracion")

def modificar():

    print(ticketControlers.modificar(True, "administracion", "esta mal", "reparaciones", "20", "33", "3", "carlso", "ses"))

def eliminar():

    ticketControlers.eliminar(True)