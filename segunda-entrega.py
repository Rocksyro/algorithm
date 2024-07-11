#CATEDRA: ALGORITMOS Y ESTRUCTURAS DE DATOS
#TRABAJO PRACTICO N° 1
#INTEGRANTES DEL GRUPO: Battocchio, Leandro
#                       Carle, Rocio
#                       Kopp, Brenda
#                       Urquiza, Juan
#------------------------------------------------
#Es necesario instalar esta libreria con: 'pip install pwinput' 
#Importamos el módulo que hará que la contraseña no se vea
import pwinput
#Importamos el modulo para poder limpiar la consola
import os
#Importar el modulo para manejar fechas
from datetime import date, datetime
#Importar random para la ruleta
import random
#Los siguientes datos precargados son todos de tipo STRING
#Datos estudiante uno
estudiante1_mail = "estudiante1@ayed.com"
estudiante1_contrasenia = "111222"
estudiante1_nombre = "Pedro Castillo"
estudiante1_rol = ""
estudiante1_fecha = date(1994, 6, 20)
estudiante1_bio ="Hola"
estudiante1_hobbies = "Andar a caballo"
estudiante1_megusta = 'fdhgsdfg'
#Datos estudiante dos
estudiante2_mail = "estudiante2@ayed.com"
estudiante2_contrasenia = "333444"
estudiante2_nombre = "Florencia Abascal"
estudiante2_rol = ""
estudiante2_fecha = date(2000, 4, 20)
estudiante2_bio = "Acá con sueño"
estudiante2_hobbies = "Hacer deporte"
estudiante2_megusta = ''
#Datos estudiante tres
estudiante3_mail = "estudiante3@ayed.com"
estudiante3_contrasenia = "555666"
estudiante3_nombre = "Raul Gimenez"
estudiante3_rol = ""
estudiante3_fecha = date(2002, 10, 9)
estudiante3_bio = "Empezando la carrera"
estudiante3_hobbies ="Jugar Lol"
estudiante3_megusta = ''
#Datos estudiante cuatro
estudiante4_nombre = "Mario Sandas"
estudiante4_rol = ""
estudiante4_fecha = date(1995, 12, 5)
estudiante4_bio = "Programando"
estudiante4_hobbies ="Pescar"
estudiante4_megusta = ''
#rol, estudiante_logueado - tipo STRING
rol = "Desconocido"
estudiante_logueado = ""
#FUNCIONES
#-------------------------
#Funcion pedirFecha (en esta funcion se pediran los datos de la fecha de nacimiento)
#VARIABLES - TIPO DE DATOS:
#anio, mes, dia - INTEGER
#fecha_actual, fecha - DATE
def pedirFecha():
    fecha_actual = date.today()

    anio = int(input("Ingrese el año de nacimiento (YYYY): "))
    while( anio < 1920 or anio > fecha_actual.year):
        print("El formato es incorrecto. Vuelva a ingresar: \n")
        anio = int(input("Ingrese el año de nacimiento (YYYY): "))
    
    mes = int(input("Ingrese el mes de nacimiento (MM): "))
    while( mes < 1 or mes > 12):
        print("El formato es incorrecto. Vuelva a ingresar: \n")
        mes = int(input("Ingrese el mes de nacimiento (MM): "))

    dia = int(input("Ingrese el día de nacimiento (DD): "))
    while( dia < 1 or dia > 31):
        print("El formato es incorrecto. Vuelva a ingresar: \n")
        dia = int(input("Ingrese el día de nacimiento (DD): "))

    fecha = date(anio, mes, dia)
    return fecha
#---------------------------------------------
#Funcion calcularEdad (en esta funcion se ingresara una fecha, y devolvera la edad actual)
#VARIABLES - TIPO DE DATOS:
#fecha_actual, fecha_nacimiento - DATE
#edad - INTEGER
def calcularEdad(fecha_nacimiento):
    #Obtener el año actual
    fecha_actual = datetime.now()
    #Calcula la edad  
    if ((fecha_actual.month < fecha_nacimiento.month) or ((fecha_actual.month == fecha_nacimiento.month) and (fecha_actual.day < fecha_nacimiento.day))):
        edad = fecha_actual.year - fecha_nacimiento.year - 1
    else:
        edad = fecha_actual.year - fecha_nacimiento.year
    #Devuelve la edad
    return edad
#-------------------------------------------
#Función login (en esta funcion el usuario intentera iniciar sesion)
#VARIABLES - TIPO DE DATOS:
#estudiante_logueado, rol, user, password - STRING
#estudiante1_mail, estudiante2_mail, estudiante3_mail - STRING
#estudiante1_contrasenia, estudiante2_contrasenia, estudiante3_contrasenia - STRING
def login():
    global estudiante_logueado, rol
    intentos = 0 
    #Mientras el contador sea menor o igual a 3 y no este logeado
    while(intentos < 3 and estudiante_logueado == ''):
        print('LOGIN')
        print('--------------------')
        #Pedir al usuario igresar usuario y contraseña
        user = input("Ingresar email: ")
        password = obtenerPassword()
        #Si el dato de usuario concuerda con el mail, y el de password con contraseña,
        #almacenar a ese estudiante específico en la variable estudiante y asignarle ese mismo rol.
        if ((user == estudiante1_mail) and (password == estudiante1_contrasenia)):
            estudiante_logueado = user
            rol = "Estudiante"
            limpiarConsola()
        elif((user == estudiante2_mail) and (password== estudiante2_contrasenia)):
            estudiante_logueado = user
            rol = "Estudiante"
            limpiarConsola()
        elif((user == estudiante3_mail) and (password == estudiante3_contrasenia)):
            estudiante_logueado = user
            rol = "Estudiante"
            limpiarConsola()
        else:
            #Si no se pudo logear sumar uno al contador de intentos
            limpiarConsola()
            intentos = intentos + 1
            if (intentos < 3):
                #Se le muestra que los datos ingresados fueron incorrectos
                print("Datos incorrectos, vuelva a intentar.")
                print('--------------------')
#-------------------------------------------
#Funcion obtenerPassword (para que en vez de la password aparezcan asteriscos)
#VARIABLES - TIPO DE DATOS:
#password - STRING
def obtenerPassword():
   password = pwinput.pwinput('Introduce tu contraseña: ')
   return password
#-------------------------------------------
#Función editarPerfil (aqui se manejara la edicion del perfil del usuario logueado)
#VARIABLES - TIPO DE DATOS:
#estudiante1_mail, estudiante2_mail, estudiante3_mail - STRING
#estudiante1_fecha, estudiante2_fecha, estudiante3_fecha - STRING
#estudiante1_bio, estudiante2_bio, estudiante3_bio - STRING
#estudiante1_hobbies, estudiante2_hobbies, estudiante3_hobbies - STRING
#toEdit, estudiante_logueado - STRING
def editarPerfil():
    global estudiante1_fecha, estudiante1_bio, estudiante1_hobbies, estudiante2_fecha, estudiante2_bio, estudiante2_hobbies, estudiante3_fecha, estudiante3_bio, estudiante3_hobbies

    if (estudiante_logueado == estudiante1_mail):

        print("Datos personales \n---------------\nFecha: ", estudiante1_fecha,"\nBiografía: ", estudiante1_bio,"\nHobbies: ", estudiante1_hobbies, '\n---------------')
        toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()

        while(toEdit != '0'):
            if (toEdit == "1"):
                estudiante1_fecha = pedirFecha()
                limpiarConsola()
            elif (toEdit == "2"):
                estudiante1_bio = input("Nueva biografía: ")
                limpiarConsola()
            elif (toEdit == '3'):
                estudiante1_hobbies = input("Agregar nuevo Hobby: ")
                limpiarConsola()
            else:
                print('No has elegido una opcion valida.')
                print('------------------------')
            
            print("Datos personales \n---------------\nFecha: ", estudiante1_fecha,"\nBiografía: ", estudiante1_bio,"\nHobbies: ", estudiante1_hobbies, '\n---------------')
            toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
            limpiarConsola()              
    elif(estudiante_logueado == estudiante2_mail):
        print("Datos personales \n---------------\nFecha: ", estudiante2_fecha,"\nBiografía: ", estudiante2_bio,"\nHobbies: ", estudiante2_hobbies, '\n---------------')
        toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()

        while(toEdit != '0'):
            
            if (toEdit == "1"):
                estudiante2_fecha = pedirFecha()
                limpiarConsola()
            elif (toEdit =="2"):
                estudiante2_bio = input("Nueva biografía: ")
                limpiarConsola()
            elif (toEdit =="3"):
                estudiante2_hobbies = input("Agregar nuevo Hobby: ")
                limpiarConsola()
            else:
                print('No has elegido una opcion valida.')
                print('------------------------')

            print("Datos personales \n---------------\nFecha: ", estudiante2_fecha,"\nBiografía: ", estudiante2_bio,"\nHobbies: ", estudiante2_hobbies, '\n---------------')
            toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
            limpiarConsola()    
    elif(estudiante_logueado == estudiante3_mail):
        print("Datos personales \n---------------\nFecha: ", estudiante3_fecha,"\nBiografía: ", estudiante3_bio,"\nHobbies: ", estudiante3_hobbies, '\n---------------')
        toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()
        
        while(toEdit != '0'):
            
            if (toEdit == "1"):
                estudiante3_fecha = pedirFecha()
                limpiarConsola()
            elif (toEdit =="2"):
                estudiante3_bio = input("Nueva biografía: ")
                limpiarConsola()
            elif (toEdit =="3"):
                estudiante3_hobbies = input("Agregar nuevo Hobby: ")
                limpiarConsola()
            else:
                print('No has elegido una opcion valida.')
                print('------------------------')

            print("Datos personales \n---------------\nFecha: ", estudiante3_fecha,"\nBiografía: ", estudiante3_bio,"\nHobbies: ", estudiante3_hobbies, '\n---------------')
            toEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
            limpiarConsola()
#-------------------------------------------
#Funcion verCandidatos (funcion para ver todos los candidatos, y poder darle me gusta a uno)
#VARIBLES - TIPOS DE DATOS
#calcularEdad - FUNCTION
#estudiante1_info, estudiante2_info, estudiante3_info - STRING
#estudiante1_fecha, estudiante2_fecha, estudiante3_fecha - STRING
#estudiante1_bio, estudiante2_bio, estudiante3_bio - STRING
#estudiante1_hobbies, estudiante2_hobbies, estudiante3_hobbies - STRING
#estudiante1_nombre, estudiante2_nombre, estudiante3_nombre - STRING
#estudiante1_mail, estudiante2_mail, estudiante3_mail, estudiante_logueado, matchear, me_gusta - STRING
#estudiante1_megusta, estudiante2_megusta, estudiante3_megusta - STRING
def verCandidatos():
    estudiante1_info = f"Nombre: {estudiante1_nombre} \n Fecha de nacimiento: {estudiante1_fecha} \n Biografia: {estudiante1_bio}  \n Hobbies: {estudiante1_hobbies}"
    estudiante2_info = f"Nombre: {estudiante2_nombre} \n Fecha de nacimiento: {estudiante2_fecha} \n Biografia: {estudiante2_bio}  \n Hobbies: {estudiante2_hobbies}"
    estudiante3_info = f"Nombre: {estudiante3_nombre} \n Fecha de nacimiento: {estudiante3_fecha} \n Biografia: {estudiante3_bio}  \n Hobbies: {estudiante3_hobbies}"
    
    if(estudiante_logueado == estudiante1_mail):
        print("Lista de candidatos \n---------------")
        print(f'2do estudiante: \n {estudiante2_info} \n Edad: {calcularEdad(estudiante2_fecha)}')
        print(f'3er estudiante: \n {estudiante3_info} \n Edad: {calcularEdad(estudiante3_fecha)}')
    elif(estudiante_logueado == estudiante2_mail):
        print("Lista de candidatos \n---------------")
        print(f'1er estudiante: \n {estudiante1_info} \n Edad: {calcularEdad(estudiante1_fecha)}')
        print(f'3er estudiante: \n {estudiante3_info} \n Edad: {calcularEdad(estudiante3_fecha)}')
    else:
        print("Lista de candidatos \n---------------")
        print(f'1er estudiante: \n {estudiante1_info} \n Edad: {calcularEdad(estudiante1_fecha)}')
        print(f'2do estudiante: \n {estudiante2_info} \n Edad: {calcularEdad(estudiante2_fecha)}')

    matchear = input('\nQuiere matchear con algun candidato? Ingrese "S/N": ')

    while(matchear != 'S' and matchear != 'N'):
        print('---------------')
        print('No ha ingresado una opcion valida!')
        print('---------------')
        matchear = input('Quiere matchear con algun candidato? Ingrese "S/N": ')

    if(matchear == 'S'):
        me_gusta = input('--------------- \nIngrese el nombre de la persona con la que le gustaria matchear: ')
        limpiarConsola()    
        if((me_gusta == estudiante1_nombre) or (me_gusta == estudiante2_nombre) or (me_gusta == estudiante3_nombre)):
            print(f'Estudiante ({me_gusta}) agregado a tus preferibles futuros matcheos. \n---------------')
            if(estudiante_logueado == estudiante1_mail):
                estudiante1_megusta = me_gusta
            elif(estudiante_logueado == estudiante2_mail):
                estudiante2_megusta = me_gusta
            else:
                estudiante3_megusta = me_gusta
        else:
            print('No se ha ingresado un nombre de estudiante valido. \n---------------')              
#-------------------------------------------
#Función menu (funcion dedicada al funcionamiento del menu principal)
#VARIBLES - TIPOS DE DATOS
#num_op, menu_principal - STRING
def menu():
    num_op = ''

    while num_op != '0':
        menu_principal = "MENU PRINCIPAL \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenu(num_op)
#-------------------------------------------
#Funcion pedirPorcentaje (para pedir y verificar el ingreso del porcentaje)
#VARIABLES - TIPOS DE DATOS
#porcentaje - INTEGER
def pedirPorcentaje():
    porcentaje = int(input("Ingrese un porcentaje de compatibilidad (sin el %, de 1 a 100) con el estudiante mostrado: "))

    while(porcentaje < 0 or porcentaje > 100):
        print('------------------')
        print('Valor invalido, vuelta a intentar.')
        print('------------------')
        porcentaje = int(input("Ingrese un porcentaje de compatibilidad (sin el %, de 1 a 100) con el estudiante mostrado: "))

    return porcentaje
#-------------------------------------------
#Funcion ruleta (funcion encargada del funcionamiento de la ruleta)
#VARIABLES - TIPOS DE DATOS: 
#participante_A, participante_B, participante_C, repetir_ruleta - STRING
#estudiante1_mail, estudiante2_mail, estudiante1_nombre, estudiante2_nombre, estudiante3_nombre - STRING
#estudiante1_fecha, estudiante2_fecha, estudiante3_fecha - STRING
#estudiante1_bio, estudiante2_bio, estudiante3_bio - STRING
#estudiante1_hobbies, estudiante2_hobbies, estudiante3_hobbies - STRING
#compatibilidad_participante_A, compatibilidad_participante_B, compatibilidad_participante_C, comprobacion_suma, ruleta - INTEGER
def ruleta():
    
    if(estudiante_logueado == estudiante1_mail):
        participante_A = f"Nombre: {estudiante2_nombre} \n Fecha de nacimiento: {estudiante2_fecha} \n Biografia: {estudiante2_bio}  \n Hobbies: {estudiante2_hobbies}"
        participante_B = f"Nombre: {estudiante3_nombre} \n Fecha de nacimiento: {estudiante3_fecha} \n Biografia: {estudiante3_bio}  \n Hobbies: {estudiante3_hobbies}"        
    elif(estudiante_logueado == estudiante2_mail):
        participante_A = f"Nombre: {estudiante1_nombre} \n Fecha de nacimiento: {estudiante1_fecha} \n Biografia: {estudiante1_bio}  \n Hobbies: {estudiante1_hobbies}"
        participante_B = f"Nombre: {estudiante3_nombre} \n Fecha de nacimiento: {estudiante3_fecha} \n Biografia: {estudiante3_bio}  \n Hobbies: {estudiante3_hobbies}"    
    else:
        participante_A = f"Nombre: {estudiante1_nombre} \n Fecha de nacimiento: {estudiante1_fecha} \n Biografia: {estudiante1_bio}  \n Hobbies: {estudiante1_hobbies}"
        participante_B = f"Nombre: {estudiante2_nombre} \n Fecha de nacimiento: {estudiante2_fecha} \n Biografia: {estudiante2_bio}  \n Hobbies: {estudiante2_hobbies}"

    participante_C = f"Nombre: {estudiante4_nombre} \n Fecha de nacimiento: {estudiante4_fecha} \n Biografia: {estudiante4_bio}  \n Hobbies: {estudiante4_hobbies}"
    
    repetir_ruleta = ''

    while(repetir_ruleta != 'N'):
        comprobacion_suma = 0  # Reiniciar la comprobación de suma al inicio de cada iteración principal

        while comprobacion_suma != 100:
            print('REGLAS DE LA RULETA \n--------------------- \nLos porcentajes de todos los alumnos deben sumar el 100% \n---------------------')
            print(f'Datos estudiante 1 \n------------------------ \n {participante_A} \n------------------------')
            compatibilidad_participante_A = pedirPorcentaje()
            limpiarConsola()
            
            print(f'Datos estudiante 2 \n------------------------ \n {participante_B} \n------------------------')
            compatibilidad_participante_B = pedirPorcentaje()
            limpiarConsola()

            print(f'Datos estudiante 3 \n------------------------ \n {participante_C} \n------------------------')
            compatibilidad_participante_C = pedirPorcentaje()
            limpiarConsola()

            comprobacion_suma = compatibilidad_participante_A + compatibilidad_participante_B + compatibilidad_participante_C

            if comprobacion_suma != 100:
                print(f"La suma de los porcentajes no es 100%. Ingrese nuevamente. \n------------------------")

        ruleta = random.randint(1, 100)

        if ruleta <= compatibilidad_participante_A:
            print(f'------------------------ \nLa ruleta seleccionó al Estudiante 1 \n------------------------\n{participante_A} \n------------------------')
        elif ruleta <= (compatibilidad_participante_A + compatibilidad_participante_B):
            print(f'------------------------ \nLa ruleta seleccionó al Estudiante 2 \n------------------------\n{participante_B} \n------------------------')
        else:
            print(f'------------------------ \nLa ruleta seleccionó al Estudiante 3 \n------------------------\n{participante_C} \n------------------------')

        repetir_ruleta = input("Desea volver a girar la ruleta? S/N: ")
        limpiarConsola()

        while( repetir_ruleta != 'S' and repetir_ruleta != 'N'):
            print('---------------')
            print('No ha ingresado una opcion valida!')
            print('---------------')
            repetir_ruleta = input("Desea volver a girar la ruleta? S/N: ")
            limpiarConsola()

    print('Cerrando programa...')
#-------------------------------------------
#Funcion limpiarConsola (Funcion dedicada a limpiar la consola para no saturar la pantalla de informacion)
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')
#-------------------------------------------
#Función opMenu (Funcion encargada de manejar las opciones del menu principal)
#VARIABLES - TIPOS DE DATOS
#volver_principal - BOOLEANO
#num_op,letra_op - STRING
def opMenu(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar mi perfil \n--------------- \na.Editar mis datos personales \nb.Eliminar mi perfil \nc.Volver")
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == "a":
                editarPerfil()
            elif letra_op == "b":
                print("Eliminar perfil (En construcción)")
                print('---------------')
            elif letra_op == "c":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "2":
        while (not volver_principal):
            print("Gestionar candidatos \n--------------- \na.Ver candidatos \nb.Reportar candidatos \nc.Volver")
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == "a":
                verCandidatos()
            elif letra_op == "b":
                print("Reportar candidatos (En construcción)")
                print('---------------')
            elif letra_op == "c":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "3":
        while (not volver_principal):
            print("Matcheos \n--------------- \na.Ver matcheos \nb.Eliminar un matcheo \nc.Volver")
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == "a":
                print("Ver matcheos (En construcción)")
                print('---------------')
            elif letra_op == "b":
                print("Eliminar un matcheo (En construcción)")
                print('---------------')
            elif letra_op == "c":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "4":
        while (not volver_principal):
            print("4- Reportes estadisticos \n--------------- \na.(En construcción) \nb.(En construcción) \nc.Volver")
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == 'c': 
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------') 
    elif num_op == "0":
        print('Se cerro correctamente.')
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')
#----------------------
#INCIO DEL PROGRAMA
#----------------------
#Se loguea el usuario
login()
#Se determina si esta logueado o no
if (estudiante_logueado != ''):
    print(f'Logueado con exito! \n------------------------ \n1- Menu \n2- Ruleta \n------------------------')
    eleccion = input('Elige la opcion a la que quieras ingresar (1 o 2): ')
    limpiarConsola()
    #Nos aseguramos de que elija el menu o la ruleta
    while (eleccion != '1' and eleccion != '2'):
        print('No has ingresado una opcion valida!')
        print('---------------')
        print(f'1- Menu \n2- Ruleta \n------------------------')
        eleccion = input('Elige la opcion a la que quieras ingresar (1 o 2): ')
        limpiarConsola()
    #Se ejecuta el menu o la ruleta
    if(eleccion == '1'):
        menu()        
    else:
        ruleta()      
else:
    print("Error de acceso. No se permiten mas intentos")

