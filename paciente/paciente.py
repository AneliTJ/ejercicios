import random

class Paciente:
    id_paciente: int
    nombre= str
    ano_nacimiento= int
    peso = float
    estatura = float
    direccion = str



    def __init__(self,id_paciente: int, nombre:str , peso: float, ano_nacimiento: int, estatura: float, direccion: str,):
        self.id_paciente = id_paciente
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion_pacientes(self):
        print( "Nombre: ",self.nombre,"Año de nacimiento: ",self.ano_nacimiento,"Peso: ",self.peso,"Estatura: ", self.estatura,  "Direccion: ", self.direccion, "ID:", self.id_paciente)
    
    
    