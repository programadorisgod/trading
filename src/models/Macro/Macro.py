from pydantic import BaseModel


class Tip(BaseModel):
    date: str
    tip: float


class Inflation(BaseModel):
    date: str
    inflation: float


class Pib_corrientes(BaseModel):
    date: str
    pib: float


class Pib_constantes(BaseModel):
    date: str
    pib: float    

class Desempleo(BaseModel):
    date: str
    desempleo: float


class Dolar(BaseModel):
    date: str
    dolar: float
    

       