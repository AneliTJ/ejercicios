import random
class Medico:
    id = 0
    nombre =""
    ano_nacimiento= 0
    direccion = ""
    rfc = ""

    def __init__(self, nombre, rfc, ano_nacimiento, direccion):
        self.id = random.randint(1,10000)
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.rfc= rfc
        self.direccion = direccion


    #getters
@property
def id(self):
    return self.id
    
@property
def nombre(self):
    return self.nombre
    
@property
def ano_nacimiento(self):
    return self.ano_nacimiento
    
@property
def direccion(self):
    return self.direccion
    
@property
def rfc(self):
    return self.rfc 