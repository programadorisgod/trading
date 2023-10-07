import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from src.model_predict.Macro.get_data import get_pib_const
def prediction_pib_const(start_year:int, end_year:int):

    #Obtener los datos
    pib_consta_data = get_pib_const()

    #Crear un dataFrame
    df_pib = pd.DataFrame(pib_consta_data)

    #Convertir la columna a formato numerico
    df_pib['pib'] = df_pib['pib'].str.replace(',', '').astype(float)
    #convertir la columna 'year' a tipo int
    df_pib['year'] = df_pib['year'].astype(int)
    #Ordenamos los valores por año
    df_pib = df_pib.sort_values(by=['year'])

    #Convertir la columna 'year' en el indice del dataFrame
    df_pib.set_index('year', inplace=True)

    print(df_pib)
    
    #Visualizar los datos
    '''
    plt.figure(figsize=(12, 6))
    plt.plot( df_pib['year'], df_pib['pib'], label='PIB constante')
    plt.xlabel('Año')
    plt.ylabel('PIB constante en Millones de dolares')
    plt.title('PIB constante Colombia')
    plt.legend()
    plt.show()
    '''

    #Ajustar el modelo ARIMA
    order = (1, 1, 1) #p, d, q
    model = ARIMA(df_pib['pib'], order=order)
    model_fit = model.fit()

    #print(model_fit.summary())

    start_year_prediction = start_year
    end_year_prediction = end_year

    year_prediction = range(start_year_prediction, end_year_prediction+1)
    print(year_prediction)
    #hacer prediciones
    predictions:float = model_fit.forecast(steps=len(year_prediction))
    print(predictions)
    #Calcular  el error cuadratico medie (MSE)
    mse = mean_squared_error(df_pib['pib'][-len(year_prediction):], predictions)


    year_alls = list(df_pib.index) + list(year_prediction)

    #Visualizar las predicciones
    '''

    plt.figure(figsize=(12, 6))
    plt.plot(df_pib['pib'], label='PIB constante')
    plt.plot(year_prediction, predictions, label='Predicciones')
    plt.xlabel('Año')
    plt.ylabel('PIB constante en Millones de dolares')
    plt.title('PIB constante Colombia - Predicciones')
    plt.legend()
    plt.show()
    '''
    data = []

    for pib in pib_consta_data:
        data.append({
            'year': pib['year'],
            'pib': pib['pib']
        })

    for year, prediction in zip(year_prediction, list(predictions)):
        data.append({
            'year': year.__str__(),
            'pib': round(prediction, 2).__str__()
        })

    data_sort = sorted(data, key=lambda x: int(x['year']))
    
    return data_sort


if __name__ == '__main__':
    prediction_pib_const(2023, 2024)