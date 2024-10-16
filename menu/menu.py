from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from usuario.utils.roles import Rol
from datetime import datetime


class Menu:
    escuela: Escuela =Escuela()

    def login(self):
        intentos = 0
        while intentos <5:
            print("*********Bienvenido*******")
            print("Inicia sesion para continuar")
            numero_control = input ("Ingresa tu numero de control de usuario: ")
            contrasena_usuario = input ("Ingresa tu contraseña de usuario: ")
            
            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contrasena=contrasena_usuario)
            if usuario is None:
                intentos=self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            else:
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudiante(usuario)
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro(usuario)
                    intentos = 0
                else:
                    self.mostrar_menu()
                    intentos = 0
                 
             


        print("Maximos intentos alcanzados. Adios")

    def mostrar_intento_sesion_fallido(self,intentos_usuario):
        print ("Usuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1

    def mostrar_menu_estudiante(self, usuario):
        opcion =0
        while opcion != 9:
            print ("\n *****Mindbox*****")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materia")
            print("4. Ver semestre")
            print("5. Ver carrera")
            print("6. Ver profesores")
            print("7. Ver mi informacion")
            print("8. Registrar horario")
            print("9. Salir")
            opcion = int (input("Ingresa una opcion: "))

            if opcion==2:
                self.escuela.ver_grupos_asignados_a_estudiante()

            elif opcion == 7:
                print(usuario.mostrar_info_estudiante())

            elif opcion == 9:
                break

    def mostrar_menu_maestro(self, usuario):
        opcion =0
        while opcion != 9:
            print ("\n *****Mindbox*****")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materia")
            print("4. Ver semestre")
            print("5. Ver carreras")
            print("6. Ver alumnos")
            print("7. Ver mi informacion")
            print("8. Registrar horario")
            print("9. Salir")

            opcion = int (input("Ingresa una opcion: "))

            if opcion == 7:
                print(usuario.mostrar_info_maestro())

            if opcion == 9:
                break

    def mostrar_menu_coordinador(self, usuario):
        opcion =0
        while opcion != 9:
            print ("\n *****Mindbox*****")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materia")
            print("4. Ver semestre")
            print("5. Ver carrera")
            print("6. Ver profesores")
            print("7. Ver mi informacion")
            print("8. Registrar horario")
            print("9. Salir")
            opcion = int (input("Ingresa una opcion: "))

            if opcion == 7:
                print(usuario.mostrar_info_coordinador())

            if opcion == 9:
                break


    def mostrar_menu(self):
        
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
            print("13. Registrar carrera")
            print("14. Registrar semestre")
            print("15. Mostrar carreras")
            print("16. Mostrar semestres")
            print("17. Salir")

            opcion = input("Ingresa una opcion para continuar: ")

            if opcion == "1":
                print("Seleccionaste la opcion para registrar un estudiante")
                numero_control= self.escuela.generar_numero_control()
                print (numero_control)
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa el curp del estudiante: ")
                ano = int(input("Ingresa el año nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)

                contrasena= input("Ingresa la contraseña: ")

                estudiante= Estudiante(numero_control=numero_control, nombre = nombre, apellido=apellido,curp=curp, fecha_nacimiento=fecha_nacimiento, contrasena=contrasena)
                self.escuela.registrar_estudiante(estudiante)

            elif opcion =="2":
                print("Seleccionaste la opcion para registrar un maestro")
                nombre = input("Ingresa el nombre del maestro: ")
                letra_nombre = nombre[0:1]
                apellido = input("Ingresa el apellido del maestro: ")
                rfc = input("Ingresa el rfc del maestro: ")
                letra_rfc = rfc [-2:0]
                sueldo = input("Ingresa el sueldo del maestro: ")
                ano_nacimiento = int(input("Ingresa el año nacimiento del maestro: "))
                contrasena= input("Ingresa la contraseña: ")
                maestro= Maestro(numero_control= "", nombre = nombre, ano_nacimiento =ano_nacimiento, apellido=apellido, rfc=rfc, sueldo=sueldo,contrasena=contrasena)
                generar_numero_control_maestro = self.escuela.generar_numero_control_maestro(maestro)
                maestro.numero_control=generar_numero_control_maestro
                self.escuela.registrar_maestro(maestro)
                print (generar_numero_control_maestro)

            elif opcion =="3":
                print("Seleccionaste la opcion para registrar una materia")
                nombre_materia= input ("Ingresa el nombre de la materia: ")
                descripcion= input ("Ingresa la descipcion de la materia: ")
                semestre= int(input("Ingresa el semestre correspondiente a la materia: "))
                creditos= int (input("Ingresa los creditos de la materia: "))
                id_maestro= input("Ingresa el ID del maestro asignado a esta meteria: ")

                maestro=self.escuela.buscar_maestro_por_numero_control(numero_control_maestro=id_maestro)
                if maestro is None:
                    print("No existe un maestro con ese numero de control")
                    return

                materia = Materia(id_materia= "", nombre_materia=nombre_materia, descripcion=descripcion, semestre=semestre,creditos=creditos)
                generar_numero_control_materia=self.escuela.generar_id_materia(materia)
                materia.id_materia=generar_numero_control_materia
                self.escuela.registrar_materia(materia)
                print(generar_numero_control_materia)

            elif opcion =="4":
                print("Seleccionaste la opcion de agregar un grupo")
                tipo= input("Ingresa el tipo de grupo: (A/B): ")
                id_semestre= input ("Ingresa el ID del semestre al que pertenece: ")
                grupo=Grupo(tipo=tipo,id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion =="5":
                pass

            elif opcion =="6":
                self.escuela.listar_estudiantes()

            elif opcion =="7":
                self.escuela.listar_maestros()

            elif opcion =="8":
                self.escuela.listar_materias()

            elif opcion =="9":
                self.escuela.listar_grupos()

            elif opcion =="10":
                print ("Seleccionaste la opcion para eliminar un estudiante")
                numero_control = input ("Ingresa el numero de control del estudiante que quieras eliminar: ")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion =="11":
                print("Seleccionaste eliminar a un maestro")
                numero_control=input("Ingresa el ID del maestro que quieras eliminar: ")
                self.escuela.eliminar_maestro(numero_control=numero_control)

            elif opcion =="12":
                print("Seleccionaste eliminar materia")
                id_materia=input ("Ingresa el ID de la materia que desees eliminar: ")
                self.escuela.eliminar_materia(id_materia=id_materia)

            elif opcion =="13":
                print ("\nSeleccionaste la opcion para registrar una carrera")
                nombre = input("Ingresa el nombre de la carrera:  ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera=carrera)

            elif opcion =="14":
                print ("Seleccionaste la opcion de registrar un semestre")
                numero=input("Ingresa el numero del semestre: ")
                id_carrera = input ("Ingresa el ID de la carrera: ")
                semestre=Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion =="15":
                self.escuela.listar_carreras()


            elif opcion =="16":
                self.escuela.listar_semestres()
                
            elif opcion =="18":
                print ("\nHasta luego")
                break