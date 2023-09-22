import pandas as pd

def read_xlsx_ipc(filepath='./Datos/1.2.5.IPC_Serie_variaciones.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año(aaaa)-Mes(mm)')

    data = {}

    for idx, row in df.iterrows():
        year = str(idx)[:4]
        if int(year) < 2015:
            break
        month = str(idx)[4:]
        year_month = f'{year}-{month}'
        index = row['Índice']
        inflation_annual = row['Inflación anual %']
        inflation_monthly = row['Inflación mensual %']
        current_year_inflation = row['Inflación año corrido %']
        data[year_month] = {'indice': index, 'inflacion_anual': inflation_annual,'inflacion_mensual': inflation_monthly, 'inflacion_conrriente_anual': current_year_inflation}
   
    return data
    

def read_xlsx_ipp_mensual(filepath='./Datos/IPP_Según actividad económica_mensual.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1', index_col='Año(aaaa)-Mes(mm)')
    data ={}

    for idx, row in df.iterrows():
        year = str(idx)[:4]
        if int(year) < 2015:
            break

        month = str(idx)[4:]
        year_month = f'{year}-{month}'
        agriculture=row['Agricultura, ganadería, caza, silvicultura y pesca']
        mines=row['Explotación de minas y canteras']
        industry=row['Industrias manufactureras']
        total=row['Total']
        data[year_month]={'agricultura':agriculture, 'mineria':mines,'industrias': industry, 'total':total}

    return data






if __name__ == '__main__':
    data1 = read_xlsx_ipc()
    print(data1)
    print(read_xlsx_ipp_mensual())
  