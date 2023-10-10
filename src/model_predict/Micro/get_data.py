import requests

def get_data():
    try:
        url = 'http://localhost:3000/API/Micro/ipc/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
    

def get_metales():
    try:
        url = 'http://localhost:3000/API/Micro/metales/Colombia'
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return "Error"
