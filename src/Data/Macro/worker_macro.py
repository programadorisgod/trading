import threading
import time
import os


from src.Data.Macro.fetch import get_dolar

data_dolar= None
data_dolar_lock = threading.Lock()

def get_data_dolar():
    global data_dolar
    with data_dolar_lock:
        return data_dolar

def set_data_dolar(new_data):
    global data_dolar
    with data_dolar_lock:
        data_dolar = new_data

def worker_fetch():
    while True:
        new_data_dolar = get_dolar()
        set_data_dolar(new_data_dolar)
       
        time.sleep(30 * 60)
        




