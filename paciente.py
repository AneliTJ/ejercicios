import random

class Paciente:
    id = 0
    nombre =""
    ano_nacimiento= 0
    peso =0
    estatura =0
    direccion = ""


    def __init__(self, nombre, peso, ano_nacimiento, estatura, direccion):
        self.id = random.randint(1,10000)
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"\nId:{self.id}")
        print(f"\nnombre:{self.nombre}")
        print(f"\nano_nacimiento:{self.ano_nacimiento}")
        print(f"\npeso:{self.peso}")
        print(f"\nestatura:{self.estatura}")
        print(f"\ndireccion:{self.direccion}")


    #getters
    #@property
    #def id(self):
     #   return self.id
    
    # @property
    # def nombre(self):
    #     return self.nombre
    
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def peso(self):
    #     return self.peso
    
    # @property
    # def estatura(self):
    #     return self.estatura
    
    # @property
    # def direccion(self):
    #     return self.direccion
    