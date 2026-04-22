#función para generar N clientes de Gilgal Tours
#En springboot el modelo de un cliente es:
#id_cliente(Integer)
#nombres(String)
#apellidos(String)
#email(String)
#telefono(String)
#documento(Integer)
#fecha_registro(LocalDate)

import random
from datetime import datetime, timedelta
def simular_clientes_gilgal(numeroClientes):

    #defino atributos base, todos los string
    nombres=["Lorena", "Daniel", "Mateo", "Alejandra", "Lucas"]
    apellidos=["Ruiz", "Tirado", "Pérez", "Diaz", "Toro"]
    emails=["ruiz@gmail.com", "tira@gmail.com", "mate@gmailo.com", "aleja@gmail.com", "luca@gmail.com"]
    telefonos=["3214545", "3224354", "2345665", "1234567", "2341234"]

    #Para simular un rango de fechas, debo introducir una fecha inicial
    fechaInicial=datetime(2026,1,1)
    fechaBase=fechaInicial+timedelta(days=random.randint(0,20))
    
    #Ciclo para generar N registros de la tabla clientes
    clientes=[]
    for _ in range(numeroClientes):
        cliente={
            "id_cliente":random.randint(1,1000),
            "nombre":random.choice(nombres),
            "apellido":random.choice(apellidos),
            "email":random.choice(emails),
            "telefono":random.choice(telefonos),
            "documento":random.randint(800,3000),
            "fecha_registro":fechaBase.strftime("%Y-%m-%d"),
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            cliente["id_cliente"]=None
        elif(probabilidadError<0.4):
            cliente["nombre"]=random.choice(["abc","dfc"])
        elif(probabilidadError<0.5):
            cliente["apellido"]=random.choice(["hola","bye"])
        elif(probabilidadError<0.8):
            cliente["email"]=None
        elif(probabilidadError<0.5):
            cliente["telefono"]=random.choice(["pera","uva"])
        elif(probabilidadError<0.5):
            cliente["documento"]=random.choice(["xxx","yyy"])
        elif(probabilidadError<0.9):
            cliente["fecha_registro"]=None

        clientes.append(cliente)
    return clientes
