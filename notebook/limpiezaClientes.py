import pandas as pd

def limpiar_datos_cliente(data_frame_cliente_sucio):
    data_frame_cliente_limpio=data_frame_cliente_sucio.copy()

    #Procesando los textos del dataframe sucio

    #1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_cliente_limpio["nombres"]=data_frame_cliente_limpio["nombres"].astype("string").str.strip().str.lower()

    data_frame_cliente_limpio["apellidos"]=data_frame_cliente_limpio["apellidos"].astype("string").str.strip().str.lower()

    data_frame_cliente_limpio["emails"]=data_frame_cliente_limpio["emails"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados

    valores_esperados_nombres=["Lorena", "Daniel", "Mateo", "Alejandra", "Lucas"]

    data_frame_cliente_limpio["nombres"]=data_frame_cliente_limpio["nombres"].where(
        data_frame_cliente_limpio["nombres"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_apellidos=["Ruiz", "Tirado", "Pérez", "Diaz", "Toro"]

    data_frame_cliente_limpio["apellidos"]=data_frame_cliente_limpio["apellidos"].where(
        data_frame_cliente_limpio["apellidos"].isin(valores_esperados_apellidos),
        pd.NA
    )

    valores_esperados_emails=["ruiz@gmail.com", "tira@gmail.com", "mate@gmailo.com", "aleja@gmail.com", "luca@gmail.com"]

    data_frame_cliente_limpio["emails"]=data_frame_cliente_limpio["emails"].where(
        data_frame_cliente_limpio["emails"].isin(valores_esperados_emails),
        pd.NA
    )

    #Limpieza de datos numéricos

    #1.Verificar que los números sí sean números
    data_frame_limpio=["telefonos"]=pd.to_numeric(data_frame_limpio["telefonos"])

    #2.Verifiquemos los valores numéricos esperados
    data_frame_limpio=data_frame_limpio[data_frame_limpio["telefonos"]>0]



