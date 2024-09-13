class Hospital:
    pacientes = []
    medicos = []
    consultas = []

    def registrar_consulta(self):
        self.validar_cantidad_usuarios()
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes)==0:
            print("No puedes registrar una consulta, no hay pacientes")
            return
        
        if len(self.medico)==0:
            print("No puedes registrar una consulta, no hay medicos")
            return 
        
        