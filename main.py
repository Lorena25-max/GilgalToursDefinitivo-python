""" from utils.clientesGilgalSimulados import simular_clientes_gilgal
print(simular_clientes_gilgal(5)) """

""" from utils.paquetesTuristicosGilgalSimulados import simular_paquetes_turisticos_gilgal
print(simular_paquetes_turisticos_gilgal(2)) """

""" from utils.pagosGilgalSimulados import simular_pagos_gilgal
print(simular_pagos_gilgal(2)) """

""" from utils.destinosGilgalSimulador import simular_destinos_gilgal
print(simular_destinos_gilgal(3)) """

#------------------------------------------------------------
#Clientes Gilgal
import pandas as pd
from utils.clientesGilgalSimulados import simular_clientes_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
clientesGilgalSimulados=simular_clientes_gilgal(1000)

#Convertir los datos simulados en dataframe
clientes_ordenados=pd.DataFrame(clientesGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/clientesGilgal.json")
crear_csv(clientes_ordenados,"data/clientesGilgal.csv")

#------------------------------------------------------------
#Destinos Gilgal
import pandas as pd
from utils.destinosGilgalSimulador import simular_destinos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
destinosGilgalSimulados=simular_destinos_gilgal(1000)

#Convertir los datos simulados en dataframe
clientes_ordenados=pd.DataFrame(destinosGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/destinosGilgal.json")
crear_csv(clientes_ordenados,"data/destinosGilgal.csv")

#-------------------------------------------------------------
#Pagos Gilgal
import pandas as pd
from utils.pagosGilgalSimulados import simular_pagos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
pagosGilgalSimulados=simular_pagos_gilgal(1000)

#Convertir los datos simulados en dataframe
pagos_ordenados=pd.DataFrame(pagosGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/pagosGilgal.json")
crear_csv(clientes_ordenados,"data/pagosGilgal.csv")

#-------------------------------------------------------------
#Paquetes turísticos Gilgal
import pandas as pd
from utils.paquetesTuristicosGilgalSimulados import simular_paquetes_turisticos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
paquetesGilgalSimulados=simular_paquetes_turisticos_gilgal(1000)

#Convertir los datos simulados en dataframe
paquetes_ordenados=pd.DataFrame(paquetesGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/paquetesGilgal.json")
crear_csv(clientes_ordenados,"data/paquetesGilgal.csv")


#------------------------------------------------------------
#Reservas Gilgal
import pandas as pd
from utils.reservasGilgalSimulados import simular_reservas_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
reservasGilgalSimulados=simular_reservas_gilgal(1000)

#Convertir los datos simulados en dataframe
reservas_ordenadas=pd.DataFrame(reservasGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/reservasGilgal.json")
crear_csv(clientes_ordenados,"data/reservasGilgal.csv")


