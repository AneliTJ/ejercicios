import random
class Medico:
    id_medico = int
    nombre = str
    ano_nacimiento= int
    direccion = str
    rfc = str

    def __init__(self,id_medico: int, nombre: str, ano_nacimiento: int, rfc:str , direccion:str ):
        self.id_medico = id_medico
        self.nombre =nombre 
        self.ano_nacimiento = ano_nacimiento
        self.rfc= rfc
        self.direccion = direccion

    def mostrar_informacion_medicos(self):
          print("Nombre: ",self.nombre,"Año de nacimiento: ",self.ano_nacimiento,"Direccion: ", self.direccion, "RFC: ", self.rfc,"ID:", self.id_medico)