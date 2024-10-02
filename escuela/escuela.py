from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante]=[]
    lista_maestros: List [Maestro]=[]
    lista_grupos: List[Grupo]=[]
    lista_materias: List[Materia]=[]
    lista_carreras: List [Carrera] = []
    lista_semestres : List[Semestre] =[]

    def registrar_estudiante(self,estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro (self, maestro:Maestro):
        self.lista_maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def registrar_carrera(self, carrera:Carrera):
        self.lista_carreras.append (carrera)

    def registrar_semestre(self, semestre:Semestre):
        id_carrera =semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestres.append (semestre)

    def registrar_grupo(self, grupo:Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id_semestre:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        self.lista_grupos.append(grupo) 


    def generar_numero_control(self):
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"
        return numero_control
    
    def generar_numero_control_maestro(self, maestro: Maestro):
        ano_nacimiento = maestro.ano_nacimiento
        dia =datetime.now().day
        random = randint (500,5000)
        letra_nombre = maestro.nombre[:2].upper()
        letra_rfc = maestro.rfc[-2:].upper()
        longitud_maestros = len(self.lista_maestros) + 1
        numero_control = f"M{ano_nacimiento}{dia}{random}{letra_nombre}{letra_rfc}{longitud_maestros}"
        return numero_control
    
    def generar_id_materia(self,materia: Materia):
        nombre_materia= materia.nombre_materia [-2:].upper()
        numero_semestre= materia.semestre 
        cant_creditos = materia.creditos
        aleatorio= randint(1,1000)
        id_materia= f"MT{nombre_materia}{numero_semestre}{cant_creditos}{aleatorio}"
        return id_materia
    
    
    def listar_estudiantes(self):
        print("**Estudiantes**")
        for estudiante in self.lista_estudiantes:
            print (estudiante.mostrar_info_estudiante())

    def listar_maestros(self):
        print("**Maestros**")
        for maestro in self.lista_maestros:
            print (maestro.mostrar_info_maestro())

    def listar_materias(self):
        print ("****Materias****")
        for materia in self.lista_materias:
            print(materia.mostrar_materias())

    def listar_carreras(self):
        print("****Carreras****")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())

    def listar_semestres(self):
        print("****Semestres****")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())

    def listar_grupos(self):
        print("****Grupos*****")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())


    def eliminar_estudiante(self, numero_control:str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return #si no se encuentra el estudiante, te da el print de abajo por eso tambien esta al nivel del for :'D
        print (f"No se encontro el estudiante con el id: {numero_control}")

    def eliminar_maestro(self, numero_control:str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return 
        print (f"No se encontro el maestro con el id: {numero_control}")

    def eliminar_materia(self, id_materia:str):
        for materia in self.lista_materias:
            if materia.id_materia==id_materia:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
            return
        print(f"No se encontro la materia con el ID: {id_materia}")

    