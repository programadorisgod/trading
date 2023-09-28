import pandas as pd
import os 



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
        data[year_month] = {'indice': index, 'inflacion_anual': inflation_annual,'inflacion_mensual': inflation_monthly, 'inflacion_corriente_anual': current_year_inflation}
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

def get_path_file():
     source_dir = '/home/camilo/Descargas/'
     files = os.listdir(source_dir)

     for file in files:
         if file.startswith('RVLocal_') and file.endswith('.csv'):
                return source_dir + file
         
def normalize_data(data):
    for key, value in data.items():
        if value['ultimo_precio'] == '-':
            value['ultimo_precio'] = '0'
        if value['variacion_porcentual'] == '-':
            value['variacion_porcentual'] = '0'
        if value['volumenes'] == '-':
            value['volumenes'] = '0'
        if value['cantidad'] == '-':
            value['cantidad'] = '0'
        if value['variacion_absoluta'] == '-':
            value['variacion_absoluta'] = '0'
        if value['precio_apertura'] == '-':
            value['precio_apertura'] = '0'
        if value['precio_maximo'] == '-':
            value['precio_maximo'] = '0'
        if value['precio_minimo'] == '-':
            value['precio_minimo'] = '0'
        if value['precio_promedio'] == '-':
            value['precio_promedio'] = '0'                           
       
    return data

             

def read_acciones():
    file_path = get_path_file()
    try:
        df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
        data = {}
        for index, row in df.iterrows():
          
          nemotecnico = str (row['Nemotécnico'])
          ultimo_precio = str (row['Último precio'])
          variacion_porcentual = str (row['Variación porcentual'])
          volumenes = str (row['Volúmenes'])
          cantidad = str (row['Cantidad'])
          variacion_absoluta = str (row['Variación absoluta'])
          precio_apertura = str (row['Precio apertura'])
          precio_maximo = str (row['Precio máximo'])
          precio_minimo = str (row['Precio mínimo'])
          precio_promedio = str (row['Precio promedio'])
          emisor = str (row['Emisor'])
          nombre = str (row['Nombre'] )
          codigo =str ( row['Codigo'])

          data[nemotecnico] = {
            'ultimo_precio': ultimo_precio,
            'variacion_porcentual': variacion_porcentual,
            'volumenes': volumenes,
            'cantidad': cantidad,
            'variacion_absoluta': variacion_absoluta,
            'precio_apertura': precio_apertura,
            'precio_maximo': precio_maximo,
            'precio_minimo': precio_minimo,
            'precio_promedio': precio_promedio,
            'emisor': emisor,
            'nombre': nombre,
            'codigo': codigo
        }
        
        dataNormalized = normalize_data(data)
       
        print(dataNormalized)
        return dataNormalized
    except Exception as e:
        print(f'Erorr: {e}')








if __name__ == '__main__':
   print(read_acciones())

  