from pydantic import BaseModel

class Ipc (BaseModel):
    indice: float
    inflacion_anual: float
    inflacion_mensual: float
    inflacion_corriente_anual: float


class Metales (BaseModel):
    
    oro: dict
    plata: dict
    platino: dict


#ahora viene la parte de acciones y tiene el formato de 


class Acciones (BaseModel):
    ultimo_precio: float
    variacion_porcentual: float
    volumenes: float
    cantidad: float
    variacion_absoluta: float
    precio_apertura: float
    precio_maximo: float
    precio_minimo: float
    precio_promedio: float
    emisor: float
    nombre: str
    codigo: str




