import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from src.model_predict.Macro.get_data import get_tip 


def prediction_tip(months_prediction:int):
    #Obtener datos
    data_tip = get_tip()

    #Crear un dataframe
    df_tip = pd.DataFrame(data_tip)

    df_tip['year_month_day'] = pd.to_datetime(df_tip['year_month_day'])

    #Convertir la columna 'year_month_day' en el indice del dataFrame

    df_tip.set_index('year_month_day', inplace=True)

    #Ordenamos los valores por año

    df_tip = df_tip.sort_values(by=['year_month_day'])


    #Ajusatar el modelo ARIMA
    model = ARIMA(df_tip['tip'], order=(1, 1, 1))
    model_fit = model.fit()

    months_for_prediction = months_prediction

    #hacer prediciones

    predictions:float = model_fit.forecast(steps=months_for_prediction)
    data = []
    last_date = df_tip.index[-1]

    for i in range(1, months_for_prediction+1):
        next_date = last_date + pd.DateOffset(months=i)
        data.append({
            'year_month_day': next_date.strftime('%Y-%m-%d'),
            'tip': predictions[i+989-1]
        })

    data = sorted(data, key=lambda x: x['year_month_day'])

    return data
    

    
if __name__ == '__main__':
    prediction_tip(12)