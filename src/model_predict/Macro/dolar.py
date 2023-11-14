import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import datetime
import pytz

from src.model_predict.Macro.get_data import get_dolar,get_inflation,get_pib_const,get_unemployment

def prediction_dolar(day:int):
   
    #Obtener datos de PIB, inflacion, desempleo y dolar
    data_dolar = get_dolar()
   #Crear un dataframe
    df_dolar = pd.DataFrame(data_dolar)
    df_dolar['year_month_day'] = pd.to_datetime(df_dolar['year_month_day'])
    
    #Convertir la columna 'year_month_day' en el indice del dataFrame
    df_dolar.set_index('year_month_day', inplace=True)
    #Ordenamos los valores por año
    df_dolar.sort_values(by=['year_month_day'], inplace=True, ascending=True)


    #Ajustar el modelo ARIMA

    days_prediction = day

    model = ARIMA(df_dolar['dolar'], order=(1,0,2)) #p, d, q (p=0, d=0, q=1)
    model_fit = model.fit()

    predicitons = model_fit.forecast(steps= days_prediction)
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()

    lats_index_prediction = df_dolar.index.get_loc(df_dolar.index[-1])
    data = []
    

    # Obtén la hora y fecha actual en Miami
    current_datetime_miami = datetime.datetime.now(pytz.timezone('America/New_York'))

    # Establece la zona horaria de Colombia
    colombia_tz = pytz.timezone('America/Bogota')

    # Convierte el datetime de Miami a la zona horaria de Colombia
    current_datetime_colombia = current_datetime_miami.astimezone(colombia_tz)

    # Extrae la fecha de Colombia
    current_date_colombia = current_datetime_colombia.date()



    for i in range(1, days_prediction +1):
        next_date = current_date_colombia + pd.DateOffset(days=i) 
        dolar_value = round (predicitons[i+lats_index_prediction],2)
        data.append({
            'year_month_day': next_date.strftime('%Y-%m-%d'),
            'dolar': dolar_value
        })


    data_sorted = sorted(data, key=lambda x: x['year_month_day'])

    return data_sorted

if __name__ == "__main__":
    prediction_dolar(2)