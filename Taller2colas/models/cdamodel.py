from pydantic import BaseModel


class Tests(BaseModel):
    name: str # Nombre de la prueba tecnica
    result: bool # Resultado de la prueba tecnica True si paso, False si no paso

class Vehicle(BaseModel):
    typ: str 
    tuition: str 
    color: str 
    brand: str 
    kilometric: int 
    tests: list[Tests]

