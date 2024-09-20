

class Maestro:
    numeroControl: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, numeroControl:str, nombre:str, apellido:str, rfc:str, sueldo:float,ano_nacimiento:int ):
        self.numeroControl= numeroControl 
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo
        self.ano_nacimiento= ano_nacimiento

    