import pandas as pd 
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from src.model_predict.Micro.get_data import get_metales 


def prediction_metales(months_prediction:int):
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
        print(metal, price_type)
        data = df_tip[metal].apply(lambda x: x[price_type])
        model = ARIMA(data, order=(1, 0, 2))
        model_fit = model.fit()
        months_for_prediction = months_prediction
        #hacer prediciones
        predictions:float = model_fit.forecast(steps=months_for_prediction)

        return predictions
    
    predicted_gold_purchase = apply_arima('gold', 'purchase_price')
    
    predicted_gold_sale = apply_arima('gold', 'sales_price')

    predicted_silver_purchase = apply_arima('silver', 'purchase_price')
    predicted_silver_sale = apply_arima('silver', 'sales_price')

    predicted_platinum_purchase = apply_arima('platinum', 'purchase_price')
    predicted_platinum_sale = apply_arima('platinum', 'sales_price')

    print(predicted_gold_purchase, 'predicted_gold_purchase')
    print(predicted_gold_sale, 'predicted_gold_sale')
    print(predicted_silver_purchase, 'predicted_silver_purchase')
    print(predicted_silver_sale, 'predicted_silver_sale')
    print(predicted_platinum_purchase, 'predicted_platinum_purchase')
    print(predicted_platinum_sale, 'predicted_platinum_sale')

    # Convertir las series de predicciones a diccionarios con el formato deseado
    predicted_gold_purchase_dict = {str(date.date()): value for date, value in predicted_gold_purchase.items()}
    predicted_gold_sale_dict = {str(date.date()): value for date, value in predicted_gold_sale.items()}
    predicted_silver_purchase_dict = {str(date.date()): value for date, value in predicted_silver_purchase.items()}
    predicted_silver_sale_dict = {str(date.date()): value for date, value in predicted_silver_sale.items()}
    predicted_platinum_purchase_dict = {str(date.date()): value for date, value in predicted_platinum_purchase.items()}
    predicted_platinum_sale_dict = {str(date.date()): value for date, value in predicted_platinum_sale.items()}


    merged_data = {
    "gold": {
        "purchase_price": None,
        "sales_price": None
    },
    "silver": {
        "purchase_price": None,
        "sales_price": None
    },
    "platinum": {
        "purchase_price": None,
        "sales_price": None
    }

    }
    

        # Actualizar el nuevo objeto con las predicciones
    merged_data["gold"]["purchase_price"] = predicted_gold_purchase_dict
    merged_data["gold"]["sales_price"] = predicted_gold_sale_dict

    merged_data["silver"]["purchase_price"] = predicted_silver_purchase_dict
    merged_data["silver"]["sales_price"] = predicted_silver_sale_dict

    merged_data["platinum"]["purchase_price"] = predicted_platinum_purchase_dict
    merged_data["platinum"]["sales_price"] = predicted_platinum_sale_dict
   

    return merged_data
    
 

if __name__ == '__main__':
    prediction_metales(12)