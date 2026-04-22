import pandas as pd

def limpiar_datos_pago(data_frame_pago_sucio):
    data_frame_pago_limpio=data_frame_pago_sucio.copy()

    #Procesando los textos del dataframe sucio

    #1. Limpiando los textos para eliminar espacios y mayúsculas
    data_frame_pago_limpio["metodo_pago"]=data_frame_pago_limpio["metodo_pago"].astype("string").str.strip().str.lower()

    data_frame_pago_limpio["estado_pago"]=data_frame_pago_limpio["estado_pago"].astype("string").str.strip().str.lower()

    #2. Limpiando los textos para controlar valores inesperados

    valores_esperados_metodo_pago=["Efectivo", "PSE", "Transferencia"]

    data_frame_pago_limpio["metodo_pago"]=data_frame_pago_limpio["metodo_pago"].where(
        data_frame_pago_limpio["metodo_pago"].isin(valores_esperados_metodo_pago),
        pd.NA
    )

    valores_esperados_estado_pago=["Ruiz", "Tirado", "Pérez", "Diaz", "Toro"]

    data_frame_pago_limpio["estado_pago"]=data_frame_pago_limpio["estado_pago"].where(
        data_frame_pago_limpio["estado_pago"].isin(valores_esperados_estado_pago),
        pd.NA
    )

    #Limpieza de datos numéricos

    #1.Verificar que los números sí sean números
    data_frame_limpio=["id_pago"]=pd.to_numeric(data_frame_limpio["id_pago"])

    data_frame_limpio=["id_reserva"]=pd.to_numeric(data_frame_limpio["id_reserva"])

    data_frame_limpio=["monto"]=pd.to_numeric(data_frame_limpio["monto"])

    #2.Verifiquemos los valores numéricos esperados
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_pago"]>0]

    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_reserva"]>0]

    data_frame_limpio=data_frame_limpio[data_frame_limpio["id_pago"]>150000]

    #Limpieza de fechas
    