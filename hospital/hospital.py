from paciente.paciente import Paciente
from typing import List
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes : List[Paciente] = []
    medicos : List[Medico] = []
    consultas : List[Consulta] = []

    def registrar_consulta(self,id_paciente, id_medico):
        if self.validar_cantidad_usuarios() == False:
            return
        
        if self.validar_existencia_paciente(id_paciente) ==False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el medico o el paciente")
            return 
        print ("continuamos con el registro")
    

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def mostrar_pacientes(self):
        print ("****Pacientes en el sistema********")
        for paciente in self.pacientes:
            paciente.mostrar_informacion_pacientes()
        
    def clasificar_pacientes(self):
        menores = []
        mayores = []
        for paciente in self.pacientes:
            if paciente.ano_nacimiento < 2006:
                menores.append(paciente)
            else:
                mayores.append(paciente)
        return menores, mayores


    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos(self):
        print ("****Medicos en el sistema********")
        for medico in self.medicos:
            medico.mostrar_informacion_medicos()
        
    def buscar_paciente_id(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id_paciente == id_paciente:
                return paciente
        return None

    def buscar_medico_id(self, id_medico):
        for medico in self.medicos:
            if medico.id_medico == id_medico:
                return medico
        return None
    
    def eliminar_paciente(self, id_paciente):
        paciente = self.buscar_paciente_id(id_paciente)
        if paciente:
            self.pacientes.remove(paciente)
            print("Paciente eliminado")
        else:
            print("Paciente no encontrado")

    def eliminar_medico(self, id_medico):
        medico = self.buscar_medico_id(id_medico)
        if medico:
            self.medicos.remove(medico)
            print("Médico eliminado")
        else:
            print("Médico no encontrado")


        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes)==0:
            print("No puedes registrar una consulta, no hay pacientes")
            return False
        
        if len(self.medicos)==0:
            print("No puedes registrar una consulta, no hay medicos")
            return 
        