from fastapi import FastAPI

from src.model_predict.Micro.metales import prediction_metales
from src.model_predict.Micro.ipc import prediccion_ipc
from src.model_predict.Macro.dolar import prediction_dolar
from src.model_predict.Macro.tip import prediction_tip
from src.model_predict.Macro.desempleo import prediction_desempleo
from src.model_predict.Macro.inflation import prediction_inflation
from src.model_predict.Macro.pib_constante import prediction_pib_const
from src.model_predict.Macro.pib_correinte  import prediction_pib_current
from src.models.Micro.Micro import Acciones, Ipc, Metales
from src.models.Macro.Macro import Desempleo, Dolar, Inflation, Pib_constantes, Pib_corrientes,  Tip
from src.Data.Macro.readMacroEconomicas import read_xls_tip, read_xlsx_tib,read_xlsx_inflacion, pib_anual_precios_corrientes, pib_anual_precios_constantes, desempleo
from src.Data.Macro.fech import get_dolar
from src.Data.Micro.readMicroEconomicas import ipc_anual, metales_preciosos, read_acciones



app = FastAPI()


@app.get("/")
def index():
    return {"message": "Monitor Financiero API"}

@app.get("/tip", response_model=Tip)
def tip():
    return read_xls_tip()


@app.get("/inflacion", response_model=Inflation)
def inflacion():
    return read_xlsx_inflacion()

@app.get("/pib_corrientes", response_model=Pib_corrientes)
def pib_corrientes():
    return pib_anual_precios_corrientes()

@app.get("/pib_constantes", response_model=Pib_constantes)
def pib_constantes():
    return pib_anual_precios_constantes()

@app.get("/desempleo", response_model=Desempleo)
def desempleoGet():
    return desempleo()

@app.get("/dolar")
def dolar():
    return get_dolar()



 #VARIABLES MICROECONOMICAS   
   
@app.get("/ipc", response_model=Ipc)
def ipc():
    return ipc_anual()

@app.get("/metales")
def metales():
    return metales_preciosos()
      
@app.get("/acciones")
def acciones():
    return read_acciones()


#VARIABLES MACROECONOMICAS PREDICCIONES
@app.get("/predicciones/macroeconomicas/pib_corriente/{start_year}/{end_year}")
def predicciones(start_year:int, end_year:int):
        return prediction_pib_current(start_year, end_year)

@app.get("/predicciones/macroeconomicas/pib_constante/{start_year}/{end_year}")
def predicciones(start_year:int, end_year:int):
        return prediction_pib_const(start_year, end_year)

@app.get("/predicciones/macroeconomicas/inflacion/{months_prediction}")
def predicciones(months_prediction:int):
        return prediction_inflation(months_prediction)


@app.get("/predicciones/macroeconomicas/desempleo/{months_prediction}")
def predicciones(months_prediction:int):
        return prediction_desempleo(months_prediction)

@app.get("/predicciones/macroeconomicas/tip/{months_prediction}")
def predicciones(months_prediction:int):
        return prediction_tip(months_prediction)

@app.get("/predicciones/macroeconomicas/dolar/{day}")
def predicciones(day:int):
        return prediction_dolar(day=day)


#VARIABLES MICROECONOMICAS PREDICCIONES

@app.get("/predicciones/microeconomicas/ipc/{months_prediction}")
def predicciones(months_prediction:int):
        return prediccion_ipc(months_prediction)

@app.get("/predicciones/microeconomicas/metales/{months_prediction}")
def predicciones(months_prediction:int):
        return prediction_metales(months_prediction)
