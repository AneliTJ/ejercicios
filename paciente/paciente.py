import random

class Paciente:
    id_paciente: int
    nombre= str
    ano_nacimiento= int
    peso = float
    estatura = float
    direccion = str
    menor = []
    mayor = []


    def __init__(self, nombre:str , peso: float, ano_nacimiento: int, estatura: float, direccion: str):
        self.id_paciente = random.randint(1,10000)
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion_pacientes(self):
        print( "Nombre: ",self.nombre,"Año de nacimiento: ",self.ano_nacimiento,"Peso: ",self.peso,"Estatura: ", self.estatura,  "Direccion: ", self.direccion, "ID:", self.id_paciente)

    def clasificar_pacientes_edad(self):
        if self.ano_nacimiento < 2006:
            return "mayor"
        else:
            return "menor"