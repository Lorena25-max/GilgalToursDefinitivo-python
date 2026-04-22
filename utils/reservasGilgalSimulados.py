#función para generar N clientes de Gilgal Tours
#En springboot el modelo de un cliente es:

#id_reserva(integer)
#id_cliente(Integer)
#id_paquete(integer)
#fecha_reserva(localDate)
#cantidad_personas(integer)
#fecha_viaje(localDate)
#estado(string)
#total_pagado(integer)

import random
from datetime import datetime, timedelta
def simular_reservas_gilgal(numeroReservas):

    #defino atributos base, todos los string
    estado=["Reserva Activa","Reserva Cancelada","Reserva pendiente de pago"]


    #Para simular un rango de fechas, debo introducir una fecha inicial
    fechaInicial=datetime(2026,1,1)
    fechaBase=fechaInicial+timedelta(days=random.randint(0,30))

    #Ciclo para generar N registros de la tabla clientes
    reservas=[]
    for _ in range(numeroReservas):
        reserva={
            "id_reserva":random.randint(1,1000),
            "id_cliente":random.randint(1,1000),
            "id_paquete":random.randint(1,5),
            "fecha_reserva":fechaBase.strftime("%Y,$m,%d"),
            "cantidad_personas":random.randint(1,4),
            "fecha_viaje":fechaBase.strftime("%Y,$m,%d"),
            "estado":random.choice(estado),
            "total_pagado":random.randint(180000,900000),
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            reserva["id_reserva"]=None
        elif(probabilidadError<0.4):
            reserva["id_cliente"]=random.choice(["naranja","coco"])
        elif(probabilidadError<0.5):
            reserva["id_paquete"]=None
        elif(probabilidadError<0.8):
            reserva["fecha_reserva"]=None
        elif(probabilidadError<0.9):
            reserva["cantidad_personas"]=random.choice([0,-100,None])
        elif(probabilidadError<0.9):
            reserva["fecha_viaje"]=None
        elif(probabilidadError<0.9):
            reserva["estado"]=None
        elif(probabilidadError<0.9):
            reserva["total_pagado"]=random.choice([0,-10000,None])

        reservas.append(reserva)
    return reservas




