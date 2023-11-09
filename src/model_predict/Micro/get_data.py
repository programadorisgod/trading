import requests

def get_data():
    try:
        url = 'https://api-node-motor-finaciero-production.up.railway.app/API/Micro/ipc/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
    

def get_metales():
    try:
        url = 'https://api-node-motor-finaciero-production.up.railway.app/API/Micro/metales/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
    

def get_actions(name):
    try: 
        url = f'https://api-node-motor-finaciero-production.up.railway.app/API/Micro/acciones/{name}'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(e)
        return "Error"


if __name__ == '__main__':
    get_actions('Cemargos')