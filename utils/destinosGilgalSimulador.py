#función para generar N clientes de Gilgal Tours
#En springboot el modelo de un cliente es:
#id_destino(Integer)
#nombre_destino(String)
#ciudad(String)
#descripcion(String)
#precio_base(Float)
#activo(String)

import random

def simular_destinos_gilgal(numeroDestinos):

    #defino atributos base, todos los string
    nombre_destino=["Guatapé", "Comuna 13", "Santa fe de Antioquia", "Oriente", "Aeropuerto"]
    ciudad=["Medellín"]
    descripcion=["Visita piedra del peñol,Pueblo de colores,Replica" ,"Visita grafitour, escaleras electricas","Visita puente colgante,Centro historico","Visita el Retiro, la Ceja,San antonio de pereira, rionegro","Traslados desde y hacia el Aeropuerto JMC"]
    activo=["Si","No"]

    #Ciclo para generar N registros de la tabla Destino
    destinos=[]
    for _ in range(numeroDestinos):
        destino={
            "id_destino":random.randint(1,1000),
            "nombre_destino":random.choice(nombre_destino),
            "ciudad":random.choice(ciudad),
            "descripcion":random.choice(descripcion),
            "precio_base":random.uniform(150000, 900000),
            "activo":random.choice(activo)
        }
        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            destino["id_destino"]=None
        elif(probabilidadError<0.4):
            destino["nombre_destino"]=random.choice(["Perú","Cartagena"])
        elif(probabilidadError<0.5):
            destino["ciudad"]=random.choice(["Portugal","España"])
        elif(probabilidadError<0.5):
            destino["descripcion"]=random.choice(["Pasadía","Bono"])
        elif(probabilidadError<0.5):
            destino["precio_base"]=None
        elif(probabilidadError<0.9):
            destino["activo"]=None

        destinos.append(destino)
    return destinos



