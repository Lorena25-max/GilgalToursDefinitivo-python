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
""" import pandas as pd
from utils.clientesGilgalSimulados import simular_clientes_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
clientesGilgalSimulados=simular_clientes_gilgal(10)

#Convertir los datos simulados en dataframe
clientes_ordenados=pd.DataFrame(clientesGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/clientesGilgal.json")
crear_csv(clientes_ordenados,"data/clientesGilgal.csv") """

#------------------------------------------------------------
#Destinos Gilgal
""" import pandas as pd
from utils.destinosGilgalSimulador import simular_destinos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
destinosGilgalSimulados=simular_destinos_gilgal(10)

#Convertir los datos simulados en dataframe
destinos_ordenados=pd.DataFrame(destinosGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(destinos_ordenados,"data/destinosGilgal.json")
crear_csv(destinos_ordenados,"data/destinosGilgal.csv") """

#-------------------------------------------------------------
#Pagos Gilgal
""" import pandas as pd
from utils.pagosGilgalSimulados import simular_pagos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
pagosGilgalSimulados=simular_pagos_gilgal(10)

#Convertir los datos simulados en dataframe
pagos_ordenados=pd.DataFrame(pagosGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(pagos_ordenados,"data/pagosGilgal.json")
crear_csv(pagos_ordenados,"data/pagosGilgal.csv") """

#-------------------------------------------------------------
#Paquetes turísticos Gilgal
""" import pandas as pd
from utils.paquetesTuristicosGilgalSimulados import simular_paquetes_turisticos_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
paquetesGilgalSimulados=simular_paquetes_turisticos_gilgal(1000)

#Convertir los datos simulados en dataframe
paquetes_ordenados=pd.DataFrame(paquetesGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/paquetesGilgal.json")
crear_csv(clientes_ordenados,"data/paquetesGilgal.csv") """


#------------------------------------------------------------
#Reservas Gilgal
""" import pandas as pd
from utils.reservasGilgalSimulados import simular_reservas_gilgal

from notebook.generador import crear_json,crear_csv

#Simulo los datos
reservasGilgalSimulados=simular_reservas_gilgal(1000)

#Convertir los datos simulados en dataframe
reservas_ordenadas=pd.DataFrame(reservasGilgalSimulados)

#Convierto el dataframe en csv y en json
crear_json(clientes_ordenados,"data/reservasGilgal.json")
crear_csv(clientes_ordenados,"data/reservasGilgal.csv") """

#---------------------------------
#Ensayo limpieza cliente

""" import pandas as pd

from utils.clientesGilgalSimulados import simular_clientes_gilgal

from notebook.limpiezaClientes import limpiar_datos_cliente

clientesGilgalSimulados=simular_clientes_gilgal(10)
clientes_ordenados=pd.DataFrame(clientesGilgalSimulados)

clientesGilgalSimuladosLimpios=limpiar_datos_cliente(clientes_ordenados)
print(clientesGilgalSimuladosLimpios)  """

#---------------------------------------------------
#Ensayo limpieza destinos

""" import pandas as pd

from utils.destinosGilgalSimulador import simular_destinos_gilgal

from notebook.limpiezaDestinos import limpiar_datos_destino

destinosGilgalSimulados=simular_destinos_gilgal(10)
destinos_ordenados=pd.DataFrame(destinosGilgalSimulados)

destinosGilgalSimuladosLimpios=limpiar_datos_destino(destinos_ordenados)
print(destinosGilgalSimuladosLimpios)
 """

#--------------------------------------------------
#Ensayo limpieza pagos

""" import pandas as pd

from utils.pagosGilgalSimulados import simular_pagos_gilgal
from notebook.limpiezaPagos import limpiar_datos_pago

pagosGilgalSimulados = simular_pagos_gilgal(10)


pagos_ordenados = pd.DataFrame(pagosGilgalSimulados)

pagosGilgalSimuladosLimpios = limpiar_datos_pago(pagos_ordenados)

print(pagosGilgalSimuladosLimpios) """

#Transformación Clientes
import pandas as pd

# IMPORTAR FUNCIONES
from notebook.consumoClientes import consumir_api_clientes
from notebook.limpiezaClientes import limpiar_datos_cliente
from notebook.transformacionClientes import transformar_clientes


# 1. CONSUMIR DATOS DESDE LA API

clientes = consumir_api_clientes()
# print(clientes)

# 2. CONVERTIR LOS DATOS A DATAFRAME

dataFrameClientes = pd.DataFrame(clientes)
# print(dataFrameClientes)


# 3. LIMPIAR LOS DATOS

dataFrameClientesLimpio = limpiar_datos_cliente(dataFrameClientes)

# print(dataFrameClientesLimpio)


# 4. TRANSFORMAR LOS DATOS

resultadoTransformacion = transformar_clientes(dataFrameClientesLimpio)

print(resultadoTransformacion)


# 5. MOSTRAR CADA AGRUPACIÓN

print("\n--- CLIENTES POR FECHA ---")
print(resultadoTransformacion["clientesPorFecha"])

print("\n--- CLIENTES CON DOCUMENTO ALTO ---")
print(resultadoTransformacion["clientesDocumentoAlto"])

print("\n--- PROMEDIO DOCUMENTO POR NOMBRE ---")
print(resultadoTransformacion["promedioDocumentoNombre"])

print("\n--- CLIENTES GMAIL POR APELLIDO ---")
print(resultadoTransformacion["clientesGmailApellido"])

print("\n--- CLIENTES POR NOMBRE ---")
print(resultadoTransformacion["clientesPorNombre"])

#Transformación Destinos
import pandas as pd

# IMPORTAR FUNCIONES
from notebook.consumoDestinos import consumir_api_destinos
from notebook.limpiezaDestinos import limpiar_datos_destino
from notebook.transformacionDestinos import transformar_datos



# 1. CONSUMIR DATOS DESDE LA API

destinos = consumir_api_destinos()

# print(destinos)


# 2. CONVERTIR LOS DATOS A DATAFRAME

dataFrameDestinos = pd.DataFrame(destinos)

# print(dataFrameDestinos)


# 3. LIMPIAR LOS DATOS

dataFrameDestinosLimpio = limpiar_datos_destino(dataFrameDestinos)

# print(dataFrameDestinosLimpio)


# 4. TRANSFORMAR LOS DATOS

resultadoTransformacion = transformar_datos(dataFrameDestinosLimpio)

print(resultadoTransformacion)


# 5. MOSTRAR CADA AGRUPACIÓN

print("\n--- DESTINOS ACTIVOS POR CIUDAD ---")
print(resultadoTransformacion["destinosActivosPorCiudad"])

print("\n--- PROMEDIO PRECIO POR DESTINO ---")
print(resultadoTransformacion["promedioPrecioDestino"])

print("\n--- DESTINOS ECONÓMICOS POR CIUDAD ---")
print(resultadoTransformacion["destinosEconomicosCiudad"])

print("\n--- DESTINOS INACTIVOS POR CIUDAD ---")
print(resultadoTransformacion["destinosInactivosCiudad"])

print("\n--- TOTAL PRECIOS POR CIUDAD ---")
print(resultadoTransformacion["totalPreciosCiudad"])

#Transformación Pagos
import pandas as pd

# IMPORTAR FUNCIONES
from notebook.consumoPagos import consumir_api_pagos
from notebook.limpiezaPagos import limpiar_datos_pago
from notebook.transformacionPagos import transformar_pagos


# 1. CONSUMIR DATOS DESDE LA API

pagos = consumir_api_pagos()
# print(pagos)


# 2. CONVERTIR LOS DATOS A DATAFRAME

dataFramePagos = pd.DataFrame(pagos)
# print(dataFramePagos)


# 3. LIMPIAR LOS DATOS

dataFramePagosLimpio = limpiar_datos_pago(dataFramePagos)
# print(dataFramePagosLimpio)


# 4. TRANSFORMAR LOS DATOS

resultadoTransformacion = transformar_pagos(dataFramePagosLimpio)

print(resultadoTransformacion)


# 5. MOSTRAR CADA AGRUPACIÓN

print("\n--- PAGOS APROBADOS POR FECHA ---")
print(resultadoTransformacion["pagosAprobadosFecha"])

print("\n--- MONTO POR MÉTODO DE PAGO ---")
print(resultadoTransformacion["montoPorMetodoPago"])

print("\n--- PAGOS PENDIENTES POR MÉTODO ---")
print(resultadoTransformacion["pagosPendientesMetodo"])

print("\n--- PAGOS RECHAZADOS POR FECHA ---")
print(resultadoTransformacion["pagosRechazadosFecha"])

print("\n--- PROMEDIO MONTO POR MÉTODO ---")
print(resultadoTransformacion["promedioMontoMetodo"])