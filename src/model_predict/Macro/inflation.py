import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from src.model_predict.Macro.get_data import get_inflation

def prediction_inflation(months_prediction:int):
    #Obtener los datos
    inflation_data = get_inflation()

    #Crear un dataframe 
    df_inflation = pd.DataFrame(inflation_data)

    df_inflation['year_month'] = pd.to_datetime(df_inflation['year_month'])

    #Convertir la columna 'year_month' en el indice del dataFrame

    df_inflation.set_index('year_month', inplace=True)

    #Ordenamos los valores por año

    df_inflation = df_inflation.sort_values(by=['year_month'])


    #Ajustar el modelo ARIMA
    model = ARIMA(df_inflation['inflation'], order=(1, 1, 1)) 
    model_fit = model.fit()

    months_for_prediction = months_prediction

    #hacer prediciones
    predictions:float = model_fit.forecast(steps=months_for_prediction)
    

    #Calcular  el error cuadratico medie (MSE)
    mse = mean_squared_error(df_inflation['inflation'][-months_for_prediction:], predictions)
    
    last_date = df_inflation.index[-1]
  
    prediction_dates = [last_date + pd.DateOffset(months=1) for i in range(1, months_for_prediction+1)]
    

    
    data = []


    for year, inflation in predictions.items():
        data.append({
            'year_month': year.strftime('%Y-%m'),
            'inflation': round(inflation, 2)
        })

    data_sort = sorted(data, key= lambda x: int(x['year_month'].split('-')[0]))

    return data_sort





if __name__ == '__main__':
    prediction_inflation()