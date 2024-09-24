from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from datetime import datetime
from materias.materia import Materia
escuela = Escuela()


while True: 
    print("** Mindbox**")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros") 
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Salir")

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
        estudiante= Estudiante(numero_control= "", nombre = nombre, apellido=apellido,curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante)

    elif opcion =="2":
        print("Seleccionaste la opcion para registrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        letra_nombre = nombre[0:1]
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el rfc del maestro: ")
        letra_rfc = rfc [-2:0]
        sueldo = input("Ingresa el sueldo del maestro: ")
        ano_nacimiento = int(input("Ingresa el año nacimiento del maestro: "))
        maestro= Maestro(numero_control= "", nombre = nombre, ano_nacimiento =ano_nacimiento, apellido=apellido, rfc=rfc, sueldo=sueldo)
        generar_numero_control_maestro = escuela.generar_numero_control_maestro(maestro)
        maestro.numero_control=generar_numero_control_maestro
        escuela.registrar_maestro(maestro)
        print (generar_numero_control_maestro)


    elif opcion =="3":
        print("Seleccionaste la opcion para registrar una materia")
        instructor= input ("Ingresa el nombre del instructor: ")
        descripcion= input ("Ingresa la descipcion de la materia: ")
        semestre= int(input("Ingresa el semestre correspondiente a la materia: "))
        creditos= int (input("Ingresa los creditos de la materia: "))
        materia = Materia(id_materia= "", instructor= instructor, descripcion=descripcion, semestre=semestre,creditos=creditos)
        generar_numero_control_materia=escuela.generar_id_materia(materia)
        materia.id_materia=generar_numero_control_materia
        escuela.registrar_materia(materia)
        print(generar_numero_control_materia)


    elif opcion =="4":
        pass


    elif opcion =="5":
        pass

    elif opcion =="6":
        escuela.listar_estudiantes()

    elif opcion =="7":
        escuela.listar_maestros()

    elif opcion =="8":
        escuela.listar_materias()

    elif opcion =="9":
        pass

    elif opcion =="10":
        print ("Seleccionaste la opcion para eliminar un estudiante")
        numero_control = input ("Ingresa el numero de control del estudiante que quieras eliminar: ")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion =="11":
        print("Seleccionaste eliminar a un maestro")
        numero_control=input("Ingresa el ID del maestro que quieras eliminar: ")
        escuela.eliminar_maestro(numero_control=numero_control)

    elif opcion =="12":
        print("Seleccionaste eliminar materia")
        id_materia=input ("Ingresa el ID de la materia que desees eliminar: ")
        escuela.eliminar_materia(id_materia=id_materia)

    elif opcion =="13":
        print ("\nHasta luego")
        break