from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante]=[]
    lista_maestros: List [Maestro]=[]
    lista_grupos: List[Grupo]=[]
    lista_materias: List[Materia]=[]

    def registrar_estudiante(self,estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"
        return numero_control
    
    def registrar_maestro (self, maestro:Maestro):
        self.lista_maestros.append(maestro)

    

    def generar_numero_control_maestro(self):
        numeroControl = f"M{datetime.now().year}{datetime.now().day}{randint(500,5000)}{[1]}{print(letra_nombre[0:1])}{rfc[-2:0]}{len(self.lista_maestros)+1}"