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






