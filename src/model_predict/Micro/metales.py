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
    metals_spanish = ['oro', 'plata', 'platino']
    last_date = df_tip.index[-1]

    date_range = pd.date_range(start=last_date, periods=prediction_days)

    merged_data = []

    for  date in date_range:
        date_data = []
      
        for metal, metal_spanish in zip(metals, metals_spanish):

            metal_data = {metal_spanish: {}}
          
            predictions = apply_arima(metal, 'purchase_price')
            predicted_purchase = predictions[date_range.get_loc(date)]
            metal_data[metal_spanish]['compra'] = predicted_purchase


            predictions = apply_arima(metal, 'sales_price')
            predicted_sales = predictions[date_range.get_loc(date)]
            metal_data[metal_spanish]['venta'] = predicted_sales

            
            date_data.append(metal_data)
        merged_data.append([str(date.date()),date_data])    

    return merged_data
