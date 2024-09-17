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
        nombre = input ("Ingresa el nombre: ")
        ano_nacimiento = input ("Ingresa el año de nacimiento: ")
        peso = input ("Ingresa el peso: ")
        estatura = input ("Ingresa el estatura: ")
        direccion = input ("Ingresa el direccion: ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente= paciente)
        print("paciente registrado correctamente")
        break



    elif opcion_usuario=="2":
        pass




    elif opcion_usuario=="3":
        hospital.mostrar_pacientes()


    elif opcion_usuario=="4":
        hospital.mostrar_medicos()