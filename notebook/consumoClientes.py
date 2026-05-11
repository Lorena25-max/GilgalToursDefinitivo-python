""" import requests

def consumir_api_servicios():

    url = "http://localhost:8080/clientes"

    respuesta = requests.get(url)

    respuesta.raise_for_status  # valida errores HTTP

    datos = respuesta.json  # convierte JSON a Python

    print(datos)

consumir_api_servicios() """

import requests

def consumir_api_clientes():

    url = "http://localhost:8080/clientes"

    respuesta = requests.get(url)

    print(respuesta.status_code)

    datos = respuesta.json()

    print(datos)

consumir_api_clientes()