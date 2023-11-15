import pandas as pd
import math


def read_xlsx_inflacion(filepath='./Datos/inflacion.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1',  index_col='Año(aaaa)-Mes(mm)')
    data = {}

    for idx, row in df.iterrows():
        # Como el formato viene 202308 vamos a hace que quede 2023-08
        year = str(idx)[:4]
        if int(year) < 2015:
           break
        month = str(idx)[4:]
        year_mount = f'{year}-{month}'
        infltation = row['Inflación total 1']
        data[year_mount] = infltation
    return data


def read_xlsx_tib(filepath='./Datos/TIB.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Fecha(dd/mm/aaaa)')
    data = {}
    for idx, row in df.iterrows():
        year_mounth_day = idx.strftime('%Y-%m-%d')
     
        if int(year_mounth_day[:4]) < 2015:
            break
        tib = row['TIB (Efectiva anual) %']

        if math.isnan(row['Monto']):
            mount = 0
        else:
            mount = row['Monto']

        data[year_mounth_day] = {'TIB': tib, 'Monto': mount}
    
    return data



def read_xls_tip(filepath='./Datos/tip.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1',index_col='Fecha (dd/mm/aaaa)')
    print(df)
    data = {}
    for idx, row in df.iterrows():
        year_mounth_day = idx.strftime('%Y-%m-%d')
        if int(year_mounth_day[:4]) < 2015:
            break
        tip = row['Tasa de intervención de política monetaria (%)']
        data[year_mounth_day] = tip
    print(data)
    return data






def pib_anual_precios_corrientes(filepath='./Datos/1.19 PIB_Total_corrientes.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año(aaaa)')
    data = {}

    for idx, row in df.iterrows():
        year = str(idx)
        number = row['Total en millones de dólares estadounidenses']
        pib = "{:,.0f}".format(number)
        
        data[year] = pib
    
    return data    

def pib_anual_precios_constantes(filepath='./Datos/PIB_Total_constantes.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año(aaaa)')
    data = {}

    for idx, row in df.iterrows():
        year = str(idx)
        number = row['Total en millones de dólares estadounidenses']
        pib = "{:,.0f}".format(number)
        
        data[year] = pib
    
    return data    

def desempleo(filepath='./Datos/desempleo.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año-Mes (AAAA-MM)')
    data = {}

    for idx, row in df.iterrows():
        year = str(idx)[:4]
        if int(year) < 2015:
            break
        month = str(idx)[4:]
        year_month = f'{year}{month}'
        desempleo = row['Tasa de desempleo (%)']
        data[year_month] = desempleo
    
    return data


   
