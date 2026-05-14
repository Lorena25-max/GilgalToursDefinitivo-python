import pandas as pd

def transformar_clientes(data_frame_limpio):

    # FILTRO 1
    # Clientes registrados después de 2024
    filtro1 = data_frame_limpio.query("fecha_registro >= '2024-01-01'")
    agrupacion1 = filtro1.groupby("fecha_registro")["id_cliente"] \
        .count() \
        .reset_index(name="cantidad_registros")

    # FILTRO 2
    # Clientes con documento mayor a 2000
    filtro2 = data_frame_limpio.query("documento >= 2000")
    agrupacion2 = filtro2.groupby("apellido")["id_cliente"] \
        .count() \
        .reset_index(name="cantidad_clientes")

    # FILTRO 3
    # Clientes con documento menor a 1500
    filtro3 = data_frame_limpio.query("documento <= 1500")
    agrupacion3 = filtro3.groupby("nombre")["documento"] \
        .mean() \
        .reset_index(name="promedio_documento")

    # FILTRO 4
    # Clientes cuyo email contiene gmail
    filtro4 = data_frame_limpio[
        data_frame_limpio["email"].str.contains("gmail", na=False)
    ]

    agrupacion4 = filtro4.groupby("apellido")["id_cliente"] \
        .count() \
        .reset_index(name="cantidad_gmail")

    # FILTRO 5
    # Cantidad de clientes por nombre
    filtro5 = data_frame_limpio.copy()

    agrupacion5 = filtro5.groupby("nombre")["id_cliente"] \
        .count() \
        .reset_index(name="cantidad_clientes")

    resultado = {
        "clientesPorFecha": agrupacion1,
        "clientesDocumentoAlto": agrupacion2,
        "promedioDocumentoNombre": agrupacion3,
        "clientesGmailApellido": agrupacion4,
        "clientesPorNombre": agrupacion5
    }

    return resultado