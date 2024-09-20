from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro


class Materia: 
    id: str #MT {ultimos 2 digitos del nombre}{semestre}{cantidadCreditos}{numero random del 1-1000}
    instructor: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__ (self, id: int, instructor: str, descripcion: str, semestre:int, creditos: int):
        self.id = id 
        self.instructor = instructor 
