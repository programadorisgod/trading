import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from get_data import get_pib_current

pib_current_data = get_pib_current()
print(pib_current_data)
#Crear un dataFrame
df_pib = pd.DataFrame(pib_current_data)

#Convertir la columna a formato numerico
df_pib['pib'] = df_pib['pib'].str.replace(',', '').astype(float)
#convertir la columna 'year' a tipo int 
df_pib['year'] = df_pib['year'].astype(int).round(0)
df_pib = df_pib.sort_values(by=['year'])
print(df_pib)
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

print(model_fit.summary())

#hacer prediciones 
predictions = model_fit.forecast(steps=4)
print(predictions)
#Calcular  el error cuadratico medie (MSE)

mse = mean_squared_error(df_pib['pib'][-4:], predictions)
print('MSE: ', mse)


#Visualizar las predicciones

plt.figure(figsize=(12, 6))
plt.plot(df_pib['pib'], label='PIB corriente REAL ')
print(range(df_pib.index[-1]+1 , df_pib.index[-1] + 5))
plt.plot(range(df_pib.index[-1]+1, df_pib.index[-1] + 5), predictions, label='PIB corriente PREDICCIONES')
plt.xlabel('Año')
plt.ylabel('PIB corriente en Millones de dolares')
plt.title('PIB corriente Colombia predicciones')
plt.legend()
plt.show() 