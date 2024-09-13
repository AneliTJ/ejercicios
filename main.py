from paciente import Paciente
from hospital import Hospital
from medico import Medico
hospital = Hospital()
paciente = Paciente("Juan",2004, 76, 1.78, "Av. Madero")
paciente_dos = Paciente("Jonathan",2005, 70, 1.90, "Av. Madero")

medico = Medico("Alberto",1900, "hncbuiwasdbhjk","Av. Periodismo")

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)

hospital.registrar_medico(medico=medico)
#hospital.registrar_consulta(id_paciente=1, id_medico=2)
hospital.mostrar_pacientes()
