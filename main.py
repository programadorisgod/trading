from fastapi import FastAPI
from typing import Union

from src.config.Data.Macro.readMacroEconomicas import read_xls_tip, read_xlsx_tib,read_xlsx_inflacion, pib_anual_precios_corrientes, pib_anual_precios_constantes, desempleo
from src.config.Data.Macro.fech import get_dolar
from src.config.Data.Micro.readMicroEconomicas import ipc_anual, metales_preciosos



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
    return get_dolar()



 #VARIABLES MICROECONOMICAS   
   
@app.get("/ipc")
def ipc():
    return ipc_anual()

@app.get("/metales")
def metales():
    return metales_preciosos()
      