

class Maestro:
    numeroControl: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, nombre:str, apellido:str, rfc:str, sueldo:float):
        self.numeroControl= "9877890"
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo