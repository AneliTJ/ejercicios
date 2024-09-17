class Hospital:
    pacientes = []
    medicos = []
    consultas = []

    def registrar_consulta(self,id_paciente, id_medico):
        if self.validar_cantidad_usuarios() == False:
            return
        
        if self.validar_existencia_paciente(id_paciente) ==False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el medico o el paciente")
            return 
        print ("continuamos con el registro")
    

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print ("****Pacientes en el sistema********")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
        


    def validar_existencia_paciente(self,id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id ==id_medico:
                return True
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes)==0:
            print("No puedes registrar una consulta, no hay pacientes")
            return False
        
        if len(self.medicos)==0:
            print("No puedes registrar una consulta, no hay medicos")
            return 

