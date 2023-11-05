import requests

def get_data():
    try:
        url = 'http://localhost:4000/API/Micro/ipc/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
    

def get_metales():
    try:
        url = 'http://localhost:4000/API/Micro/metales/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
    

def get_actions(name):
    try: 
        url = f'http://localhost:4000/API/Micro/acciones/{name}'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(e)
        return "Error"


if __name__ == '__main__':
    get_actions('Cemargos')