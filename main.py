from fastapi import FastAPI
import threading
import os




from src.model_predict.Micro.metales import prediction_metales
from src.model_predict.Micro.ipc import prediccion_ipc
from src.model_predict.Macro.dolar import prediction_dolar
from src.model_predict.Macro.tip import prediction_tip
from src.model_predict.Macro.desempleo import prediction_desempleo
from src.model_predict.Macro.inflation import prediction_inflation
from src.model_predict.Macro.pib_constante import prediction_pib_const
from src.model_predict.Macro.pib_correinte  import prediction_pib_current
from src.Data.Macro.readMacroEconomicas import read_xls_tip, read_xlsx_tib,read_xlsx_inflacion, pib_anual_precios_corrientes, pib_anual_precios_constantes, desempleo
from src.Data.Micro.readMicroEconomicas import ipc_anual, metales_preciosos
from src.Data.Macro.worker_macro import worker_fetch, get_data_dolar


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Monitor Financiero API"}

@app.get("/tip")
def tip():
    return read_xls_tip()


@app.get("/inflacion")
def inflacion():
    return read_xlsx_inflacion()

@app.get("/pib_corrientes")
def pib_corrientes():
    return pib_anual_precios_corrientes()

@app.get("/pib_constantes")
def pib_constantes():
    return pib_anual_precios_constantes()

@app.get("/desempleo")
def desempleoGet():
    return desempleo()

@app.get("/dolar")
def dolar():
    data_dolar = get_data_dolar()
    if data_dolar:
        return data_dolar
    else: 
          return {"message": "No data aviable"}
    
     



 #VARIABLES MICROECONOMICAS   
   
@app.get("/ipc")
def ipc():
    return ipc_anual()

@app.get("/metales")
def metales():
    return metales_preciosos()
      


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

@app.get("/predicciones/microeconomicas/metales/{prediction_days}")
def predicciones(prediction_days:int):
        return prediction_metales(prediction_days)


print("procces id main:", os.getpid())
print("procces parent id main:", os.getppid())
print("______________________________")
worker_thread  = threading.Thread(target=worker_fetch)
worker_thread.daemon = True
worker_thread.start()

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)