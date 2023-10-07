from fastapi import FastAPI

#from typing import Union
from src.model_predict.Macro.pib_correinte  import prediction_pib_current
from src.models.Micro.Micro import Acciones, Ipc, Metales
from src.models.Macro.Macro import Desempleo, Dolar, Inflation, Pib_constantes, Pib_corrientes, Tip
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

@app.get("/dolar", response_model=Dolar)
def dolar():
    return get_dolar()



 #VARIABLES MICROECONOMICAS   
   
@app.get("/ipc", response_model=Ipc)
def ipc():
    return ipc_anual()

@app.get("/metales",response_model= Metales)
def metales():
    return metales_preciosos()
      
@app.get("/acciones")
def acciones():
    return read_acciones()


#PREDICCIONES
@app.get("/predicciones")
def predicciones():
        return prediction_pib_current()