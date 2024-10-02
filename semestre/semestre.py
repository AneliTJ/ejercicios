from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id_semestre: str
    numero: int
    id_carrera: str 
    materias: List [Materia]
    grupos: List [Grupo]

    def __init__(self, numero:int, id_carrera:str):
        self.id_semestre= self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero =numero


    def generar_id(self, numero_semestre:int)-> str:
        return f"{numero_semestre}-{randint(0,100000)}-{randint(0, 100000)}"

    def registrar_grupo_en_semestre(self,grupo:Grupo):
        self.grupos.append(grupo)

    def mostrar_info_semestre(self):
        print(f"ID: {self.id_semestre}, Numero del semestre: {self.numero}, ID de la carrera: {self.id_carrera}")
