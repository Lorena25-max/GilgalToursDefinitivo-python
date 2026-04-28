import pandas as pd

def limpiar_datos_destino(data_frame_destino_sucio):
    data_frame_destino_limpio=data_frame_destino_sucio.copy()

    #Procesando los textos del dataframe sucio

    #1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_destino_limpio["nombre_destino"]=data_frame_destino_limpio["nombre_destino"].astype("string").str.strip().str.lower()

    data_frame_destino_limpio["ciudad"]=data_frame_destino_limpio["ciudad"].astype("string").str.strip().str.lower()

    data_frame_destino_limpio["descripcion"]=data_frame_destino_limpio["descripcion"].astype("string").str.strip().str.lower()

    data_frame_destino_limpio["activo"]=data_frame_destino_limpio["activo"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados

    valores_esperados_nombre_destino=["guatapé", "comuna 13", "santa fe de antioquia", "oriente", "aeropuerto"]

    data_frame_destino_limpio["nombre_destino"]=data_frame_destino_limpio["nombre_destino"].where(
        data_frame_destino_limpio["nombre_destino"].isin(valores_esperados_nombre_destino),
        pd.NA
    )

    valores_esperados_ciudad=["medellín"]

    data_frame_destino_limpio["ciudad"]=data_frame_destino_limpio["ciudad"].where(
        data_frame_destino_limpio["ciudad"].isin(valores_esperados_ciudad),
        pd.NA
    )

    valores_esperados_descripcion=["visita piedra del peñol,pueblo de colores,replica" ,"visita grafitour, escaleras electricas","visita puente colgante, centro historico","visita el retiro, la ceja, san antonio de pereira, rionegro","traslados desde y hacia el aeropuerto jmc"]

    data_frame_destino_limpio["descripcion"]=data_frame_destino_limpio["descripcion"].where(
        data_frame_destino_limpio["descripcion"].isin(valores_esperados_descripcion),
        pd.NA
    )

    valores_esperados_activo=["si","no"]

    data_frame_destino_limpio["activo"]=data_frame_destino_limpio["activo"].where(
        data_frame_destino_limpio["activo"].isin(valores_esperados_activo),
        pd.NA
    )

    #Limpieza de datos numéricos

    #1.Verificar que los números sí sean números
    data_frame_destino_limpio["id_destino"]=pd.to_numeric(data_frame_destino_limpio["id_destino"])

    data_frame_destino_limpio["precio_base"]=pd.to_numeric(data_frame_destino_limpio["precio_base"])

    #2.Verifiquemos los valores numéricos esperados
    data_frame_destino_limpio=data_frame_destino_limpio[data_frame_destino_limpio["id_destino"]>0]

    data_frame_destino_limpio=data_frame_destino_limpio[data_frame_destino_limpio["precio_base"]>150000]

    #No hay fechas en destino

    #Rutina para evaluar novedades
    #Rutina para evaluar campos obligatorios que vienen vacíos
    columnas_obligatorias=["id_destino", "nombre_destino", "precio_base"]
    data_frame_destino_limpio=data_frame_destino_limpio.dropna(subset=columnas_obligatorias)

    data_frame_destino_limpio=data_frame_destino_limpio.drop_duplicates()

    return data_frame_destino_limpio

