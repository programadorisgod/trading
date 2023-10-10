import pandas as pd 
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from src.model_predict.Micro.get_data import get_data

def prediccion_ipc(months):
    #Obtener los datos
    data_ipc = get_data()

    #Crear un dataframe
    df_ipc = pd.DataFrame(data_ipc)

    df_ipc['date'] = pd.to_datetime(df_ipc['date'])

    #Convertir la columna 'date' en el indice del dataFrame
    df_ipc.set_index('date', inplace=True)

    #Ordenamos los valores por año
    df_ipc = df_ipc.sort_values(by=['date'])
    print(df_ipc)
    #Ajustar el modelo ARIMA
    model = ARIMA(df_ipc['indice'], order=(1, 1, 1))
    model_fit = model.fit()

    months_for_prediction = months

    #hacer prediciones
    
    predictions:float = model_fit.forecast(steps=months_for_prediction)
    data= []
    for ipc in data_ipc:
        data.append({
            'date': ipc['date'],
            'indice': ipc['indice']
        })
     
    for year, ipc in predictions.items():
        data.append({
            'date': year.strftime('%Y-%m'),
            'indice': round(ipc,2)
        })

    data = sorted(data, key=lambda x: x['date'])
    return  data

if __name__ == '__main__':
    prediccion_ipc(12)
