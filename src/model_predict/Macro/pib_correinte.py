import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from src.model_predict.Macro.get_data import get_pib_current

def prediction_pib_current (start_year:int, end_year:int):
   
    pib_current_data = get_pib_current()

    #Crear un dataFrame
    df_pib = pd.DataFrame(pib_current_data)

    #Convertir la columna a formato numerico
    df_pib['pib'] = df_pib['pib'].str.replace(',', '').astype(float)
    #convertir la columna 'year' a tipo int 
    df_pib['year'] = df_pib['year'].astype(int).round(0)
    df_pib = df_pib.sort_values(by=['year'])

    #Convertir la columna 'year' en el indice del dataFrame
    df_pib.set_index('year', inplace=True)


    #Visualizar los datos
    '''
    plt.figure(figsize=(12, 6))
    plt.plot(df_pib['pib'], label='PIB corriente')
    plt.xlabel('Año')
    plt.ylabel('PIB corriente en Millones de dolares')
    plt.title('PIB corriente Colombia')
    plt.legend()
    plt.show()
    '''


    #Ajustar el modelo ARIMA

    order = (1, 1, 1) #p, d, q
    model = ARIMA(df_pib['pib'], order=order)
    model_fit = model.fit()


    start_year_prediction = start_year
    end_year_prediction = end_year

    year_prediction = range(start_year_prediction, end_year_prediction+1)
    
    #hacer prediciones 
    predictions:float = model_fit.forecast(steps=len(year_prediction))

    #Calcular  el error cuadratico medie (MSE)

    mse = mean_squared_error(df_pib['pib'][-len(year_prediction):], predictions)


    year_alls = list(df_pib.index) + list(year_prediction)

    #Visualizar las predicciones
    '''
    plt.figure(figsize=(12, 6))
    plt.plot(df_pib['pib'], label='PIB corriente REAL ')
    #print(range(df_pib.index[-1]+1 , df_pib.index[-1] + 5))
    plt.plot(year_prediction, predictions, label='PIB corriente PREDICCIONES')

    #Establecer las marcas del eje x para incluir tanto los años reales como los predichos
    print(year_alls)

    plt.xticks(year_alls)


    plt.xlabel('Año')
    plt.ylabel('PIB corriente en Millones de dolares')
    plt.title('PIB corriente Colombia predicciones')
    plt.legend()
    plt.show() 
    '''
    #Guardar las predicciones en formato json
   

    data=[]

    
    for pib in pib_current_data:
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
    prediction_pib_current(2021, 2025)



    



    

