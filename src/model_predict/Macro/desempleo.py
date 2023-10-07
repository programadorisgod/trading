import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

from src.model_predict.Macro.get_data import get_unemployment

def prediction_desempleo(months_prediction:int):
    #Obtener los datos 
    desempleo = get_unemployment()

    #Crear un dataframe
    df_desempleo = pd.DataFrame(desempleo)

    df_desempleo['year_month'] = pd.to_datetime(df_desempleo['year_month'])

    #Convertir la columna 'year_month' en el indice del dataFrame
    df_desempleo.set_index('year_month', inplace=True)

    #Ordenamos los valores por año
    df_desempleo = df_desempleo.sort_values(by=['year_month'])

    #Visualizar los datos
    '''
    plt.figure(figsize=(12, 6))
    plt.plot(df_desempleo.index, df_desempleo['unemployment'], label='Desempleo')
    plt.xlabel('Año')
    plt.ylabel('Desempleo en %')
    plt.title('Desempleo Colombia')
    plt.legend()
    plt.show()
    '''

    #Ajustar el modelo ARIMA
    model = ARIMA(df_desempleo['unemployment'], order=(1, 1, 1))
    model_fit = model.fit()

    months_for_prediction = months_prediction

    #hacer prediciones
    predictions = model_fit.forecast(steps=months_for_prediction)
    
    #Calcular  el error cuadratico medie (MSE)
    mse = mean_squared_error(df_desempleo['unemployment'][-months_for_prediction:], predictions)
    

    data = []

    for unemployment in  desempleo:
        data.append({
            'year_month': unemployment['year_month'],
            'unemployment': unemployment['unemployment']
        })
    
    for year, unemployment in predictions.items():
        data.append({
            'year_month': year.strftime('%Y-%m'),
            'unemployment': round(unemployment, 2)
        })

    data_sorted = sorted(data, key=lambda x: int(x['year_month'].split('-')[0]))

    return data_sorted



if __name__ == '__main__':
    prediction_desempleo()