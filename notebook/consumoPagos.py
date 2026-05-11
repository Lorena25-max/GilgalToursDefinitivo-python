import requests

def consumir_api_pagos():

    url = "http://localhost:8080/pagos"

    respuesta = requests.get(url)

    respuesta.raise_for_status()

    datos = respuesta.json()

    print("PAGOS:")
    print(datos)

consumir_api_pagos()