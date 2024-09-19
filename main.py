from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
escuela = Escuela()

while True: 
    print("** Mindbox**")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")

    opcion = input("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print("Seleccionaste la opcion para registrar un estudiante")
        numero_control= escuela.generar_numero_control()
        print (numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el curp del estudiante: ")
        ano = int(input("Ingresa el año nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

    elif opcion =="2":
        pass


    elif opcion =="3":
        pass


    elif opcion =="4":
        pass


    elif opcion =="5":
        pass


    elif opcion =="6":
        print ("\nHasta luego")
        break