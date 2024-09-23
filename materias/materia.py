from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro


class Materia: 
    id_materia: str #MT {ultimos 2 digitos del nombre}{semestre}{cantidadCreditos}{numero random del 1-1000}
    instructor: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__ (self, id_materia: int, instructor: str, descripcion: str, semestre:int, creditos: int):
        self.id_materia = id_materia
        self.instructor = instructor 
        self.descripcion = descripcion
        self.semestre=semestre
        self.creditos=creditos

