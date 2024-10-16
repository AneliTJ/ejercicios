from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from coordinador.coordinador import Coordinador
from usuario.usuario import Usuario
from datetime import datetime
from random import randint

class Escuela:
    lista_usuarios: List [Usuario]=[]
    lista_estudiantes: List[Estudiante]=[]
    lista_maestros: List [Maestro]=[]
    lista_coordinadores: List [Coordinador]=[]
    lista_grupos: List[Grupo]=[]
    lista_materias: List[Materia]=[]
    lista_carreras: List [Carrera] = []
    lista_semestres : List[Semestre] =[]

    def __init__ (self):
        coordinador=Coordinador(
        numero_control = "12345",
        nombre="Edson",
        apellido="Medina",
        rfc = "MEDINA123",
        sueldo=10000,
        antiguedad= 10,
        contrasena="123*",
        )
        self.lista_coordinadores.append(coordinador)

    def registrar_estudiante(self,estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro (self, maestro:Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)

    def registrar_coordinador (self, coordinador:Coordinador):
        self.lista_usuarios.append(coordinador)
        self.lista_coordinadores.append(coordinador)

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
    
    def validar_inicio_sesion(self, numero_control: str, contrasena: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contrasena == contrasena:
                    return usuario
        return None
    
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

    def buscar_estudiante_por_numero_control(self,id_estudiante:str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                return estudiante
        return None
    
    def buscar_grupo_por_id(self,id_grupo:str):
        for grupo in self.lista_grupos:
            if grupo.id_grupo=id_grupo:
                return grupo
            return None
        

    def buscar_maestro_por_numero_control(self,numero_control_maestro:str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control_maestro:
                return maestro
        return None


    def registrar_estudiante_en_grupo(self, id_estudiante:str ):
        estudiante=self.buscar_estudiante_por_numero_control(
            numero_control_estudiante=numero_control)

        if estudiante is None:
            print("No se encontro un estudiante con el numero de control proporcionado")
            return #para la ejecucion
        grupo=self.buscar_grupo_por_id(id_grupo=id_grupo)

        if grupo is None:
            print("No se encontro un grupo con ese ID proporcionado")
            return 
        
        grupo.registrar_estudiante(estudiante=estudiante)
        print("Estudiante asignado al grupo correctamente")

    def ver_grupos_asignados_a_estudiante(self):
        estudiante=self.buscar_estudiante_por_numero_control(
            numero_control_estudiante=numero_control)

        if estudiante is None:
            print("No se encontro un estudiante con el numero de control proporcionado")
            return #para la ejecucion
        grupo=self.buscar_grupo_por_id(id_grupo=id_grupo)

        if grupo is None:
            print("No se encontro un grupo con ese ID proporcionado")
            return
        

        
    