import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from src.model_predict.Micro.get_data import get_metales 

def prediction_metales(prediction_days:int):

    #Crear un dataframe
    data_tip = get_metales()
    df_tip = pd.DataFrame(data_tip)
    df_tip['date'] = pd.to_datetime(df_tip['date'])

    #Convertir la columna 'year_month_day' en el indice del dataFrame
    df_tip.set_index('date', inplace=True)
    print(df_tip)

    #Ordenamos los valores por año
    df_tip = df_tip.sort_values(by=['date'])


    def apply_arima(metal, price_type):

        data = df_tip[metal].apply(lambda x: x[price_type])
        model = ARIMA(data, order=(1, 0, 2))
        model_fit = model.fit()
        days_for_prediction =prediction_days

        #hacer prediciones
        predictions:float = model_fit.forecast(steps=days_for_prediction)

        return predictions
    


    metals = ['gold', 'silver', 'platinum']
    price_types = ["purchase_price", "sales_price"]

    merged_data = {}
    for metal in metals:
        merged_data[metal] = {}

        for price_type in price_types:
            predictions = apply_arima(metal, price_type)
            last_date = df_tip.index[-1]
            date_range = pd.date_range(start=last_date, periods=prediction_days)

            predicted_dict = {str(date.date()) : value for date, value in zip(date_range, predictions) }
            merged_data[metal][price_type] = predicted_dict

    return merged_data
    
 

if __name__ == '__main__':
    prediction_metales(12)