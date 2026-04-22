#función para generar N paquetes turísticos de Gilgal Tours
#En springboot el modelo de un cliente es:
#id_paquete(Integer)
#nombre_paquete(String)
#id_destino(Integer)
#duracion_dias(Integer)
#incluye(String)
#precio(Float)
#cupos_disponibles(Integer)

import random

def simular_paquetes_turisticos_gilgal(paquetesTuristicos):

    #defino atributos base, todos los string
    nombre_paquete=["Guatapé", "Comuna 13", "Santa fe de Antioquia", "Oriente", "Aeropuerto"]
    incluye=["Traslados, guía", "Traslados, guía", "Traslados, guía", "Traslados, guía", "Traslados, guía"]

    
    #Ciclo para generar N registros de la tabla clientes
    paquetes=[]
    for _ in range(paquetesTuristicos):
        paquete={
            "id_paquete":random.randint(1,1000),
            "nombre_paquete":random.choice(nombre_paquete),
            "id_destino":random.randint(1,1000),
            "duracion_dias":random.randint(1,5),
            "incluye":random.choice(incluye),
            "precio":random.uniform(150000, 900000),
            "cupos_disponibles":random.randint(1, 4),
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            paquete["id_paquete"]=None
        elif(probabilidadError<0.4):
            paquete["nombre_paquete"]=random.choice(["Amazonas","Cocora"])
        elif(probabilidadError<0.5):
            paquete["id_destino"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            paquete["duracion_dias"]=None
        elif(probabilidadError<0.9):
            paquete["incluye"]=None
        elif(probabilidadError<0.4):
            paquete["precio"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.5):
            paquete["cupos_disponibles"]=None
        

        paquetes.append(paquete)
    return paquetes