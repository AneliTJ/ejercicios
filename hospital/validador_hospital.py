from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico

class ValidadorHospital:
    def validar_existencia_paciente(self,id_paciente: int , lista_pacientes: List[Paciente]):
        for paciente in lista_pacientes:
            if paciente.id_paciente == id_paciente:
                return True
        return False

    def validar_cantidad_usuarios(self, lista_pacientes: List[Paciente], lista_medicos:List[Medico]):
        if len(lista_pacientes)==0:
            print("No puedes registrar una consulta, no hay pacientes")
            return False

        if len(self.medicos)==0:
            print("No puedes registrar una consulta, no hay medicos")
            return
    
    def validar_existencia_medico(self, id_medico: int, lista_medicos: List [Medico]):
        for medico in lista_medicos:
            if medico.id_medico ==id_medico:
                return True
        return False