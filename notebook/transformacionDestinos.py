import pandas as pd

def transformar_datos(data_frame_limpio):

    # FILTRO 1
    # Destinos activos agrupados por ciudad
    filtro1 = data_frame_limpio.query("activo == True")
    agrupacion1 = filtro1.groupby("ciudad")["id_destino"] \
        .count() \
        .reset_index(name="cantidad_destinos")

    # FILTRO 2
    # Destinos con precio alto agrupados por nombre del destino
    filtro2 = data_frame_limpio.query("precio_base >= 500000")
    agrupacion2 = filtro2.groupby("nombre_destino")["precio_base"] \
        .mean() \
        .reset_index(name="promedio_precio")

    # FILTRO 3
    # Destinos económicos agrupados por ciudad
    filtro3 = data_frame_limpio.query("precio_base <= 300000")
    agrupacion3 = filtro3.groupby("ciudad")["id_destino"] \
        .count() \
        .reset_index(name="cantidad_economicos")

    # FILTRO 4
    # Destinos inactivos agrupados por ciudad
    filtro4 = data_frame_limpio.query("activo == False")
    agrupacion4 = filtro4.groupby("ciudad")["id_destino"] \
        .count() \
        .reset_index(name="cantidad_inactivos")

    # FILTRO 5
    # Suma total de precios por ciudad para destinos activos
    filtro5 = data_frame_limpio.query("activo == True")
    agrupacion5 = filtro5.groupby("ciudad")["precio_base"] \
        .sum() \
        .reset_index(name="total_precios")

    resultado = {
        "destinosActivosPorCiudad": agrupacion1,
        "promedioPrecioDestino": agrupacion2,
        "destinosEconomicosCiudad": agrupacion3,
        "destinosInactivosCiudad": agrupacion4,
        "totalPreciosCiudad": agrupacion5
    }

    return resultado