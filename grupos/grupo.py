from typing import List
from random import randint
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia 

class Grupo:
    id:str
    id_semestre: str
    estudiantes: List [Estudiante] = []
    maestros: List[Maestro] = []
    materias : List [Materia]=[]
    tipo: chr # chr caracter (un elemento o una letra)
    
    def __init__ (self, tipo: chr, id_semestre:str):
        self.id= self.generar_id()
        self.tipo=tipo
        self.id_semestre= id_semestre

    def generar_id(self, tipo: chr)-> str:
        return f"{tipo}-{randint(0,100000)}-{randint(0, 100000)}"
    
    def mostrar_info_grupo(self):
        print(f"ID del grupo: {self.generar_id}, Tipo: {self.tipo}, ID del semestre: {self.id_semestre}")

# mostrar  id_grupo, tipo y id_semestre