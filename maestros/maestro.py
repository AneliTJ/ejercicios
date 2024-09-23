

class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, numero_control:str, nombre:str, apellido:str, rfc:str, sueldo:float,ano_nacimiento:int ):
        self.numero_control= numero_control 
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo
        self.ano_nacimiento= ano_nacimiento

    