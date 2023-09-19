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


def read_xlsx_tib(filepath='./Datos/TIB_Serie historica.xlsx'):
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
    print(data)


def read_xls_tip(filepath='./Datos/1.2.TIP_Serie histórica diaria IQY.xlsx'):
    df = pd.read_excel(filepath, sheet_name='Sheet1',index_col='Fecha (dd/mm/aaaa)')
    data = {}
    for idx, row in df.iterrows():
        year_mounth_day = idx.strftime('%Y-%m-%d')
        if int(year_mounth_day[:4]) < 2015:
            break
        tip = row['Tasa de intervención de política monetaria (%)']
        data[year_mounth_day] = tip
    print(data)


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

    print(data)


def read_xlsx_ipp_anual(filepath='./Datos/IPP_Según actividad económica_anual.xlsx'):
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

    print(data)


if __name__ == '__main__':
    data = read_xlsx_inflacion()
    #print(data)
    #read_xlsx_tib()
    #read_xls_tip()
    #read_xlsx_ipc()
    #read_xlsx_ipp_mensual()