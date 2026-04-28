import pandas as pd

def limpiar_datos_pago(data_frame_pago_sucio):
    data_frame_pago_limpio=data_frame_pago_sucio.copy()

    #Procesando los textos del dataframe sucio

    #1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_pago_limpio["metodo_pago"]=data_frame_pago_limpio["metodo_pago"].astype("string").str.strip().str.lower()

    data_frame_pago_limpio["estado_pago"]=data_frame_pago_limpio["estado_pago"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados

    valores_esperados_metodo_pago=["efectivo", "pse", "transferencia"]

    data_frame_pago_limpio["metodo_pago"]=data_frame_pago_limpio["metodo_pago"].where(
        data_frame_pago_limpio["metodo_pago"].isin(valores_esperados_metodo_pago),
        pd.NA
    )

    valores_esperados_estado_pago=["ruiz", "tirado", "pérez", "diaz", "toro"]

    data_frame_pago_limpio["estado_pago"]=data_frame_pago_limpio["estado_pago"].where(
        data_frame_pago_limpio["estado_pago"].isin(valores_esperados_estado_pago),
        pd.NA
    )

    #Limpieza de datos numéricos

    #1.Verificar que los números sí sean números
    data_frame_pago_limpio["id_pago"]=pd.to_numeric(data_frame_pago_limpio["id_pago"])

    """ data_frame_pago_limpio["id_reserva"]=pd.to_numeric(data_frame_pago_limpio["id_reserva"]) """
    # Convertir a numérico (sin romper)
    
    data_frame_pago_limpio["id_reserva"] = pd.to_numeric(data_frame_pago_limpio["id_reserva"], errors="coerce")#TENGO DUDAS AQUÍ

    # Eliminar los inválidos TENGO DUDAS CON ESTO
    data_frame_pago_limpio = data_frame_pago_limpio.dropna(subset=["id_reserva"])

    data_frame_pago_limpio["monto"]=pd.to_numeric(data_frame_pago_limpio["monto"])

    #2.Verifiquemos los valores numéricos esperados
    data_frame_pago_limpio=data_frame_pago_limpio[data_frame_pago_limpio["id_pago"]>0]

    data_frame_pago_limpio=data_frame_pago_limpio[data_frame_pago_limpio["id_reserva"]>0]

    data_frame_pago_limpio=data_frame_pago_limpio[data_frame_pago_limpio["id_pago"]>150000]

    #Rutina para evaluar fechas
    #Evaluar que una fecha si es una fecha
    data_frame_pago_limpio["fecha_pago"]=pd.to_datetime(data_frame_pago_limpio["fecha_pago"])

    #Reemplazar una fecha por defecto si el campo llega vacío
    fecha_default=pd.to_datetime("1990-06-28")
    data_frame_pago_limpio["fecha_pago"]=data_frame_pago_limpio["fecha_pago"].fillna(fecha_default)

    #Rutina para evaluar novedades
    #Rutina para evaluar campos obligatorios que vienen vacíos
    columnas_obligatorias=["id_pago", "id_reserva"]
    data_frame_pago_limpio=data_frame_pago_limpio.dropna(subset=columnas_obligatorias)

    data_frame_pago_limpio=data_frame_pago_limpio.drop_duplicates()

    return data_frame_pago_limpio
    