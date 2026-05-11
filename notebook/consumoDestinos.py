import requests

def consumir_api_destinos():

    url = "http://localhost:8080/destinos"

    respuesta = requests.get(url)

    respuesta.raise_for_status()

    datos = respuesta.json()

    print("DESTINOS:")
    print(datos)

consumir_api_destinos()