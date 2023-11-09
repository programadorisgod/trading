import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from src.model_predict.Micro.get_data import get_actions

def prediccion_action(minuts, name):
    data_action = get_actions(name)
    
    #Creación del dataframe
    df= pd.DataFrame(data_action)

    #Acomodar el dataframe
    df['last'] = df['data'].apply(lambda x: float(x['data']['last'].replace('.', '').replace(',', '.')))

    current_year = pd.Timestamp.now().year
    df['hour'] = pd.to_datetime(df['data'].apply(lambda x: f"{current_year}/{x['data']['hour']} 00:00"), format='%Y/%d/%m %H:%M')
    ##df['hour'] = pd.to_datetime(df['data'].apply(lambda x: x['data']['hour'] + ' 00:00'), format='%d/%m %H:%M')

    df = df.sort_values(by='hour')
    df = df.set_index('hour')

    
    #Entrenamiento del modelo
    model = ARIMA(df['last'], order=(0, 0, 0))

    model_fit = model.fit()

    time = minuts.split('-')[2]

    minuts = minuts.replace('-', '/')

    print(minuts, 'minuts')

    hour_pred = pd.to_datetime(minuts, format='%d/%m/%H:%M')
    print(hour_pred, 'hour_pred')


    hour_pred_timestamp = hour_pred.timestamp()
    print(hour_pred_timestamp, 'hour_pred_timestamp')
    #Predicción
    price_pred = model_fit.forecast(steps=1)

    print(price_pred, 'price_pred')

    print(f'Predicción del precio a las {hour_pred_timestamp}: {price_pred}')

    data = {
        'time':time,
        'value':price_pred.values[0]
    }
    return data