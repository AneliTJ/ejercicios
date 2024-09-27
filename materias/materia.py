from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro


class Materia: 
    id_materia: str #MT {ultimos 2 digitos del nombre}{semestre}{cantidadCreditos}{numero random del 1-1000}
    nombre_materia: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__ (self, id_materia: int, nombre_materia: str, descripcion: str, semestre:int, creditos: int):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia 
        self.descripcion = descripcion
        self.semestre=semestre
        self.creditos=creditos

    def mostrar_materias(self):
        print(f"ID de la materia: {self.id_materia}, Materia: {self.nombre_materia}, Descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditos}")
        