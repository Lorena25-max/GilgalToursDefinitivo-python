import pandas as pd

def limpiar_datos_cliente(data_frame_cliente_sucio):
    data_frame_cliente_limpio=data_frame_cliente_sucio.copy()

    #Procesando los textos del dataframe sucio

    #1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_cliente_limpio["nombre"]=data_frame_cliente_limpio["nombre"].astype("string").str.strip().str.lower()

    data_frame_cliente_limpio["apellido"]=data_frame_cliente_limpio["apellido"].astype("string").str.strip().str.lower()

    data_frame_cliente_limpio["email"]=data_frame_cliente_limpio["email"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados

    valores_esperados_nombres=["lorena", "daniel", "mateo", "alejandra", "lucas"]

    data_frame_cliente_limpio["nombre"]=data_frame_cliente_limpio["nombre"].where(
        data_frame_cliente_limpio["nombre"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_apellidos=["ruiz", "tirado", "pérez", "diaz", "toro"]

    data_frame_cliente_limpio["apellido"]=data_frame_cliente_limpio["apellido"].where(
        data_frame_cliente_limpio["apellido"].isin(valores_esperados_apellidos),
        pd.NA
    )

    valores_esperados_emails=["ruiz@gmail.com", "tira@gmail.com", "mate@gmailo.com", "aleja@gmail.com", "luca@gmail.com"]

    data_frame_cliente_limpio["email"]=data_frame_cliente_limpio["email"].where(
        data_frame_cliente_limpio["email"].isin(valores_esperados_emails),
        pd.NA
    )

    #Limpieza de datos numéricos

    #1.Verificar que los números sí sean números
    data_frame_cliente_limpio["telefono"]=pd.to_numeric(data_frame_cliente_limpio["telefono"])

    data_frame_cliente_limpio["id_cliente"]=pd.to_numeric(data_frame_cliente_limpio["id_cliente"])

    #2.Verifiquemos los valores numéricos esperados
    data_frame_cliente_limpio=data_frame_cliente_limpio[data_frame_cliente_limpio["telefono"]>0]

    data_frame_cliente_limpio=data_frame_cliente_limpio[data_frame_cliente_limpio["id_cliente"]>0]

    #Rutina para evaluar fechas
    #Evaluar que una fecha si es una fecha
    data_frame_cliente_limpio["fecha_registro"]=pd.to_datetime(data_frame_cliente_limpio["fecha_registro"])

    #Reemplazar una fecha por defecto si el campo llega vacío
    fecha_default=pd.to_datetime("1990-06-28")
    data_frame_cliente_limpio["fecha_registro"]=data_frame_cliente_limpio["fecha_registro"].fillna(fecha_default)

    #Rutina para evaluar novedades
    #Rutina para evaluar campos obligatorios que vienen vacíos
    columnas_obligatorias=["id_cliente", "nombre", "apellido", "documento"]
    data_frame_cliente_limpio=data_frame_cliente_limpio.dropna(subset=columnas_obligatorias)

    data_frame_cliente_limpio=data_frame_cliente_limpio.drop_duplicates()

    return data_frame_cliente_limpio



