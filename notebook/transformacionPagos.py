import pandas as pd

def transformar_pagos(data_frame_limpio):

    # FILTRO 1
    # Pagos aprobados agrupados por fecha
    filtro1 = data_frame_limpio.query("estado_pago == 'aprobado'")
    agrupacion1 = filtro1.groupby("fecha_pago")["id_pago"] \
        .count() \
        .reset_index(name="cantidad_pagos")

    # FILTRO 2
    # Pagos mayores a 500000 agrupados por método de pago
    filtro2 = data_frame_limpio.query("monto >= 500000")
    agrupacion2 = filtro2.groupby("metodo_pago")["monto"] \
        .sum() \
        .reset_index(name="total_monto")

    # FILTRO 3
    # Pagos pendientes agrupados por método de pago
    filtro3 = data_frame_limpio.query("estado_pago == 'pendiente'")
    agrupacion3 = filtro3.groupby("metodo_pago")["id_pago"] \
        .count() \
        .reset_index(name="cantidad_pendientes")

    # FILTRO 4
    # Pagos rechazados agrupados por fecha
    filtro4 = data_frame_limpio.query("estado_pago == 'rechazado'")
    agrupacion4 = filtro4.groupby("fecha_pago")["id_pago"] \
        .count() \
        .reset_index(name="cantidad_rechazados")

    # FILTRO 5
    # Promedio de monto por método de pago
    filtro5 = data_frame_limpio.copy()
    agrupacion5 = filtro5.groupby("metodo_pago")["monto"] \
        .mean() \
        .reset_index(name="promedio_monto")

    resultado = {
        "pagosAprobadosFecha": agrupacion1,
        "montoPorMetodoPago": agrupacion2,
        "pagosPendientesMetodo": agrupacion3,
        "pagosRechazadosFecha": agrupacion4,
        "promedioMontoMetodo": agrupacion5
    }

    return resultado