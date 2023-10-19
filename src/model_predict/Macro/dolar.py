import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from src.model_predict.Macro.get_data import get_dolar,get_inflation,get_pib_const,get_unemployment

def prediction_dolar(day:int):
    if day > 2:
        return "Error"
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

    model = ARIMA(df_dolar['dolar'], order=(0,0,1)) #p, d, q
    model_fit = model.fit()

    predicitons = model_fit.forecast(steps= days_prediction)

    data = []
    
    for dolar in data_dolar:
         data.append(dolar)


    for i in range(1, days_prediction +1):
        next_date = df_dolar.index[-1] + pd.DateOffset(days=i) 
  
        data.append({
            'year_month_day': next_date.strftime('%Y-%m-%d'),
            'dolar': round(predicitons[i+420-1], 2)
        })


    data_sorted = sorted(data, key=lambda x: x['year_month_day'])

    return data_sorted

if __name__ == "__main__":
    prediction_dolar(2)