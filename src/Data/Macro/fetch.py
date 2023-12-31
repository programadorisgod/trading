import requests

def get_dolar():
    resp = requests.get('https://www.datos.gov.co/resource/32sa-8pi3.json?$query=SELECT%20%60valor%60%2C%20%60unidad%60%2C%20%60vigenciadesde%60%2C%20%60vigenciahasta%60%0AORDER%20BY%20%60unidad%60%20ASC%20NULL%20LAST%2C%20%60vigenciadesde%60%20DESC%20NULL%20FIRST')
    data = resp.json()
    price_dolar = {}
    for item in data:
        item['vigenciadesde'] = item['vigenciadesde'][:10]
        if item['vigenciadesde'] < '2022-01-01':
            break
        
        price_dolar[item['vigenciadesde']] = {
            'valor': item['valor'],
            'vigenciahasta': item['vigenciahasta'],
            'vigenciadesde': item['vigenciadesde']
        }
    return price_dolar


if __name__ == "__main__":
   get_dolar()
   