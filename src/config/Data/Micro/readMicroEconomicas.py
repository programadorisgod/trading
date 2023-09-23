import pandas as pd




def ipc_anual(filepath='./Datos/1.2.5.IPC_Serie_variaciones.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año(aaaa)-Mes(mm)')
    data ={}

    for idx, row in df.iterrows():
        year = str(idx)[:4]
        if int(year) < 2015:
            continue
        month = str(idx)[4:]
        year_month = f'{year}-{month}'
        index = row['Índice']
        inflation_annual = row['Inflación anual %']
        inflation_monthly = row['Inflación mensual %']
        current_year_inflation = row['Inflación año corrido %']
        data[year_month] = {'indice': index, 'inflacion_anual': inflation_annual,'inflacion_mensual': inflation_monthly, 'inflacion_conrriente_anual': current_year_inflation}
    return data







def metales_preciosos(filepath='./Datos/metalespreciosos.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Fecha (dd/mm/aaaa)')
    data ={}

    for idx, row in df.iterrows():
        date = str(idx)[:10]
        gold={'compra': row['Compra Oro'], 'venta': row['Venta Oro']}
        silver={'compra': row['Compra Plata'], 'venta': row['Venta Plata']}
        platinum={'compra': row['Compra Platino'], 'venta': row['Venta Platino']}
        data[date]={'oro':gold, 'plata':silver,'platino': platinum}
    

  
    return data







if __name__ == '__main__':
   print(ipc_anual())

  