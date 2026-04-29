#función para generar N pagos de Gilgal Tours
#En springboot el modelo de un cliente es:
#id_pago(Integer)
#id_reserva(Integer)
#fecha_pago(LocalDate)
#monto(Float)
#metodo_pago(String)
#estado_pago(String)


import random
from datetime import datetime, timedelta
def simular_pagos_gilgal(numeroPagos):

    #defino atributos base, todos los string
    metodo_pago=["Efectivo", "PSE", "Transferencia"]
    estado_pago=["Pendiente", "Aprobado", "Cancelado"]
    

    #Para simular un rango de fechas, debo introducir una fecha inicial
    fechaInicial=datetime(2026,1,1)
    fechaBase=fechaInicial+timedelta(days=random.randint(0,20))
    
    #Ciclo para generar N registros de la tabla clientes
    pagos=[]
    for _ in range(numeroPagos):
        pago={
            "id_pago":random.randint(1,1000),
            "id_reserva":random.randint(1,1000),
            "fecha_pago":fechaBase.strftime("%Y-%m-%d"),
            "monto":random.uniform(150000, 900000),
            "metodo_pago":random.choice(metodo_pago),
            "estado_pago":random.choice(estado_pago),
        }
        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            pago["id_pago"]=None
        elif(probabilidadError<0.4):
            pago["id_reserva"]=random.choice(["1234","567"])
        elif(probabilidadError<0.5):
            pago["monto"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            pago["fecha_pago"]=None
        elif(probabilidadError<0.9):
            pago["metodo_pago"]=None
        elif(probabilidadError<0.9):
            pago["estado_pago"]=None

        pagos.append(pago)
    return pagos
