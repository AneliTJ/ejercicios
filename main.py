from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico
hospital = Hospital()

while True:
    print("BIENVENIDO AL SISTEMA DEL HOSPITAL")
    print("1. registar paciente")
    print("2. registar medico")
    print("3. mostrar pacientes")
    print("4. mostrar medicos")
    print("5. eliminar paciente")
    print("6. eliminar medico")
    print("7. mostrar pacientes menores de edad")
    print("8. mostrar pacientes mayores de edad")
    print("9. salir")

    opcion_usuario=input("selecciona la opcion deseada: ")
    if opcion_usuario == "1":
        print ("Seleccionaste la opcion para registrar un paciente ~~~~~~~~~~")
        id_paciente=input("Ingresa el ID del paciente: ")
        nombre = input ("Ingresa el nombre: ")
        ano_nacimiento = input ("Ingresa el año de nacimiento: ")
        peso = input ("Ingresa el peso: ")
        estatura = input ("Ingresa el estatura: ")
        direccion = input ("Ingresa el direccion: ")

        paciente = Paciente (id_paciente=id_paciente, nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente= paciente)
        print("paciente registrado correctamente")


    elif opcion_usuario=="2":
        print ("Seleccionaste la opcion para registrar un medico ~~~~~~~~~~")
        id_medico= input ("Ingresa el id del medico: ")
        nombre = input ("Ingresa el nombre: ")
        ano_nacimiento = input ("Ingresa el año de nacimiento: ")
        rfc = input ("Ingresa el rfc: ")
        direccion = input ("Ingresa el direccion: ")

        medico = Medico(id_medico=id_medico, nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico= medico)
        print("paciente registrado correctamente")

    elif opcion_usuario=="3":
        print ("~~~~~~~~~~~~~Mostrar Pacientes~~~~~~~~~~~")
        hospital.mostrar_pacientes()


    elif opcion_usuario=="4":
        print ("~~~~~~~~~~~~~Mostrar Medicos~~~~~~~~~~~")
        hospital.mostrar_medicos()

#5. eliminar paciente
    elif opcion_usuario=="5":
        print ("Seleccionaste la opcion para eliminar un paciente ~~~~~~~~~~")
        id_paciente = input("Ingrese el id del paciente que desea eliminar: ")
        hospital.eliminar_paciente(id_paciente) 


#6. eliminar medico
    elif opcion_usuario=="6":
        print ("Seleccionaste la opcion para eliminar un medico ~~~~~~~~~~")
        id_medico = input("Ingresa el id del medico que desees eliminar: ")
        hospital.eliminar_medico(id_medico)

#7. mostrar pacientes menores de edad
    elif opcion_usuario=="7":
        print ("~~~~~~~~~~~~~Mostrar pacientes menores de edad~~~~~~~~~~~")
        menores, _ = hospital.clasificar_pacientes()
        print("Pacientes menores de edad:")
        for paciente in menores:
            paciente.mostrar_informacion_pacientes()

#8. mostrar pacientes mayores de edad
    elif opcion_usuario=="8":
        print ("~~~~~~~~~~~~~Mostrar pacientes mayores de edad~~~~~~~~~~~")
        _,mayores = hospital.clasificar_pacientes()
        for paciente in menores:
            paciente.mostrar_informacion_pacientes()
    else:
        break

    