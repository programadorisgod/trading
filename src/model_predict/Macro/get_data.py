import requests

def get_pib_current():
    url = 'http://localhost:3000/API/Macro/PibCorriente/Colombia'
    response = requests.get(url)
    data = response.json()
    data_pib = data['pibCurrentData']
    data_pib_current=[]

    for pib in data_pib:
        if int(pib['year']) < 2019:
            continue
        data_pib_current.append({
            'year': pib['year'],
            'pib': pib['pib']
        })
      
    return data_pib_current 
    


def get_pib_const():
    url = 'http://localhost:3000/API/Macro/PibConstante/Colombia'
    response = requests.get(url)
    data = response.json()    
    
    data_pib = data['pibConstData']
    data_pib_const=[]

    for pib in data_pib:
        if int(pib['year']) < 2020:
            print(pib['year'])
            continue
      
        data_pib_const.append({
            'year': pib['year'],
            'pib': pib['pib']
        }) 

    return data_pib_const



def get_inflation():
    url = 'http://localhost:3000/API/Macro/Inflacion/Colombia'
    
    response =  requests.get(url)

    data = response.json()

    data_inflation = data['inflationData']

      
    data = []

    for pib in data_inflation:
        year = pib['year_month'].split('-')[0]

        if int(year) < 2020:
            continue

        data.append({
            'year_month': pib['year_month'],
            'inflation': pib['inflation']
        })


        
    return data



def get_unemployment():
    url = 'http://localhost:3000/API/Macro/Desempleo/Colombia'
    response = requests.get(url)
    data = response.json()
    data_unemployment = data['unemploymentData']
    data_unemployment_data = []

    for unemployment in data_unemployment:
        year = unemployment['year_month'].split('-')[0]
        if int(year) < 2021:
            continue
        data_unemployment_data.append({
            'year_month': unemployment['year_month'],
            'unemployment': unemployment['unemployment']
        })


      
    return data_unemployment_data



def get_tip():
    url = 'http://localhost:3000/API/Macro/Tip/Colombia'
    response = requests.get(url)
    data = response.json() 
    data_tip = data['tipData']

    data = []
    for tip in data_tip:
        year = tip['year_month_day'].split('-')[0]
        if int(year) < 2021:
            continue

        data.append({
            'year_month_day': tip['year_month_day'],
            'tip': tip['tip']
        })

    print(data)

    return data






if __name__ == '__main__':
    get_tip()
    


  

