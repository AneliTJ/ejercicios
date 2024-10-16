from typing import List
from random import randint
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia 

class Grupo:
    id_grupo:str
    id_semestre: str
    estudiantes: List [Estudiante] 
    materias : List [Materia]
    tipo: chr # chr caracter (un elemento o una letra)
    
    def __init__ (self, tipo: chr, id_semestre:str):
        self.id_grupo= self.generar_id(tipo)
        self.tipo=tipo
        self.id_semestre= id_semestre

    def generar_id(self, tipo: chr)-> str:
        return f"{tipo}{randint(0,100000)}{randint(0, 100000)}"
    
    def mostrar_info_grupo(self):
        print(f"ID del grupo: {self.id_grupo}, Tipo: {self.tipo}, ID del semestre: {self.id_semestre}")

    def registrar_estudiante(self, estrudiante:Estudiante):
        self.estudiantes.append(estrudiante)

    def registrar_materia(self, materia:Materia):
        self.materias.append(materia)

    def registrar_maestro(self, maestro:Maestro):
        self.maestros.append(maestro)

    def mostrar_info_grupo_para_estudiante(self,):
        print(f"Informacion del grupo {self.tipo}, del semestre {self.id_semestre}")
        for materia in self.materias:
            materia.mostrar_materias()

# mostrar  id_grupo, tipo y id_semestre