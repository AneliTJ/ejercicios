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

    def generar_numero_control_maestro(self, maestro: Maestro):
        ano_nacimiento = maestro.ano_nacimiento
        dia =datetime.now().day
        random = randint (500,5000)
        letra_nombre = maestro.nombre[:2].upper()
        letra_rfc = maestro.rfc[-2:].upper()
        longitud_maestros = len(self.lista_maestros) + 1
        numero_control = f"M{ano_nacimiento}{dia}{random}{letra_nombre}{letra_rfc}{longitud_maestros}"
        return numero_control

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def generar_id_materia(self,materia: Materia):
        letra_instructor= materia.instructor [-2:].upper()
        numero_semestre= materia.semestre 
        cant_creditos = materia.creditos
        aleatorio= randint(1,1000)
        id_materia= f"MT{letra_instructor}{numero_semestre}{cant_creditos}{aleatorio}"
        return id_materia

    