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
    
    
        
    


  

