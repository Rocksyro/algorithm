# CATEDRA: ALGORITMOS Y ESTRUCTURAS DE DATOS
# TRABAJO PRACTICO N° 2
# INTEGRANTES DEL GRUPO: Battocchio, Leandro
#                        Carle, Rocio
#                        Kopp, Brenda
#                        Urquiza, Juan
#----------------------------------------------------------------
# Es necesario instalar esta libreria con: 'pip install pwinput' 
# Importamos el módulo que hará que la contraseña no se vea
import pwinput
# Importamos el modulo para poder limpiar la consola
import os
#Importamos el modulo para manejar fechas
from datetime import date, datetime
#Importamos el módulo para la ruleta
import random

# VARIABLES - TIPO DE DATOS:
# matrizLikes - ARRAY OF STRING (8x8)
# estudiantes - ARRAY OF STRING (8x8)
# moderadores - ARRAY OF STRING (8x4)
# reportes_motivos - ARRAY OF STRING(2x49)
# reportes_ids - ARRAY OF INTEGER(2x49)
# usuario_logueado - ARRAY OF INTEGER (2x1)

matrizLikes = [[-1]*8 for n in range(8)]
estudiantes = [['']*8 for n in range(8)]
moderadores = [['']*8 for n in range(4)]
reportes_motivos = [[''] * 2 for n in range(49)]
reportes_ids = [[-1] * 2 for n in range(49)]

# Tanto el ID de cada estudiante como de cada moderador va a ser siempre un número entero auto-incremental, que comienza en 0.
estudiantes[0] = ["estudiante1@ayed.com", "111222", "Pedro Castillo", "Estudiante", "1994-06-20", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
estudiantes[1] = ["estudiante2@ayed.com", "333444", "Florencia Abascal", "Estudiante", "2000-04-20", "Hola qué tal", "Hacer deporte", "s"]
estudiantes[2] = ["estudiante3@ayed.com", "555666", "Raul Gimenez", "Estudiante", "2002-10-9", "Soy feli", "Jugar Lol", "s"]

moderadores[0] = ["moderador1@ayed.com", "111222", "Pipo Castillo", "Moderador", "2000-07-12", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
moderadores[1] = ["moderador2@ayed.com", "333444", "Jalan Abascal", "Moderador", "2000-07-12", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]

# ID del usuario - Tipo de usuario (0 = estudiantes, 1 = moderador)
usuario_logueado = [-1, -1]

# VARIABLES - TIPO DE DATOS:
# a - ARRAY OF INTEGER
# i - INTEGER
def buscarEspacioVacioPorPosicion(a):
    i = 0
    while (i < (len(a)) and a[i][0] != ''):
        i = i+1
    else:
        return i

# VARIABLES - TIPO DE DATOS:
# array - ARRAY OF STRING
# email - STRING
# contadorPosicion - INTEGER
def buscarUsuarioPorEmail(array, email):
    contadorPosicion = 0
    while (contadorPosicion < (len(array) - 1) and (array[contadorPosicion][0] != email)):
        contadorPosicion += 1

    if (array[contadorPosicion][0] == email):
        return contadorPosicion
    else:
        return -1

# VARIABLES - TIPO DE DATOS:
# ultimo - INTEGER
# estudiantes - ARRAY OF STRING
# matrizLikes - ARRAY OF INTEGER
def generarInteracciones():
    ultimo = buscarEspacioVacioPorPosicion(estudiantes)
    if (ultimo == -1):
        ultimo = len(estudiantes)

    for i in range(ultimo):
        for j in range(ultimo):
            if (i != j):
                matrizLikes[i][j] = random.randint(0, 1)
            else:
                matrizLikes[i][j] = 0

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# VARIABLES - TIPO DE DATOS:
# password - STRING
def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password

# VARIABLES - TIPO DE DATOS:
# usuario_logueado - ARRAY OF INTEGER
# estudiantes, moderadores - ARRAY OF STRING
# intentos, cantidadEstudiantes, cantidadModeradores, resultadoBusqueda - INTEGER
# email, password - STRING
def login(usuario_logueado, estudiantes, moderadores):
    intentos = 0
    cantidadEstudiantes = buscarEspacioVacioPorPosicion(estudiantes)
    cantidadModeradores = buscarEspacioVacioPorPosicion(moderadores)

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 3) and (cantidadModeradores != -1 and cantidadModeradores >= 1)):
        # Mientras el contador sea menor o igual a 3 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == -1):
            # Pedir al usuario igresar usuario y contraseña
            email = input("Ingresar email: ")
            resultadoBusqueda = buscarUsuarioPorEmail(estudiantes, email)

            if (resultadoBusqueda != -1):
                if (estudiantes[resultadoBusqueda][7] == 'n'):
                    print('Tu usuario esta desactivado, no puedes loguearte.')
                    intentos = 3

                while (intentos < 3 and usuario_logueado[0] == -1):
                    password = obtenerPassword()
                    if (estudiantes[resultadoBusqueda][1] == password):
                        for i in range(len(estudiantes[0])):
                            usuario_logueado[0] = resultadoBusqueda
                        limpiarConsola()
                        print("Login exitoso! bienvenido usuario ", estudiantes[usuario_logueado[0]][2], '.')
                        usuario_logueado[1] = 0
                        print('--------------------')
                    else:
                        intentos = intentos + 1
            else:
                resultadoBusqueda = buscarUsuarioPorEmail(moderadores, email)
                if (resultadoBusqueda != -1):
                    while (intentos < 3 and usuario_logueado[0] == -1):
                        password = obtenerPassword()
                        if (moderadores[resultadoBusqueda][1] == password):
                            for i in range(len(moderadores[0])):
                                usuario_logueado[0] = resultadoBusqueda
                            limpiarConsola()
                            print("Login exitoso! bienvenido moderador ", moderadores[usuario_logueado[0]][2])
                            usuario_logueado[1] = 1
                        else:
                            intentos = intentos + 1
                else:
                    password = obtenerPassword()
                    intentos = intentos + 1
    else:
        print('No hay suficientes usuario creados para el logueo')

# VARIABLES - TIPO DE DATOS:
# num_op, menu_principal - STRING
# estudiantes - ARRAY OF STRING
# usuario_logueado - ARRAY OF INTEGER
def menuEstudiante():
    num_op = ''
    while (num_op != '0'):
        menu_principal = "MENU ESTUDIANTE \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenuEstudiante(num_op)

        if (estudiantes[usuario_logueado[0]][7] == 'n'):
            num_op = '0'
            usuario_logueado[0] = -1
            usuario_logueado[1] = -1

# VARIABLES - TIPO DE DATOS:
# array - ARRAY OF STRING
# nombre - STRING
# contadorPosicion - INTEGER
def buscarUsuarioPorNombre(array, nombre):
    contadorPosicion = 0
    while (contadorPosicion < (len(array) - 1) and (array[contadorPosicion][2] != nombre)):
        contadorPosicion += 1

    if (array[contadorPosicion][2] == nombre and nombre != ""):
        return contadorPosicion
    else:
        return -1

# VARIABLES - TIPO DE DATOS:
#array - array of string
#id - integer
def buscarUsuarioPorId(array, id):
    usuario_buscado = array[id]
    if (usuario_buscado[0] != ''):
        return id
    else:
        return -1

# VARIABLES - TIPO DE DATOS:
#fecha_nac, hoy - datetime
#edad - integer
def calcularEdad(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.today()
    # Calcular la diferencia de años
    edad = hoy.year - fecha_nac.year
    # Ajustar si no ha cumplido años este año
    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
    return edad

# VARIABLES - TIPO DE DATOS:
#anio, mes, dia - integer
#fecha - string
def pedirFecha():
    fecha_actual = date.today()
    try:
        anio = int(input("Ingrese el año de nacimiento (YYYY): "))
        while (anio < 1920 or anio > fecha_actual.year):
            print("El formato es incorrecto. Vuelva a ingresar: \n")
            anio = int(input("Ingrese el año de nacimiento (YYYY): "))

        mes = int(input("Ingrese el mes de nacimiento (MM): "))
        while (mes < 1 or mes > 12):
            print("El formato es incorrecto. Vuelva a ingresar: \n")
            mes = int(input("Ingrese el mes de nacimiento (MM): "))

        dia = int(input("Ingrese el día de nacimiento (DD): "))
        while (dia < 1 or dia > 31):
            print("El formato es incorrecto. Vuelva a ingresar: \n")
            dia = int(input("Ingrese el día de nacimiento (DD): "))

        fecha = f'{anio}-{mes}-{dia}'
        return fecha
    except:
        print("Ingrese un dato correcto por favor.")
# VARIABLES - TIPO DE DATOS:
#opEdit - integer
def editarPerfil(usuario_logueado):
    print("Datos personales \n---------------\nFecha: ", estudiantes[usuario_logueado[0]][4], "\nBiografía: ", estudiantes[usuario_logueado[0]][5], "\nHobbies: ", estudiantes[usuario_logueado[0]][6], '\n---------------')
    opEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
    limpiarConsola()

    while (opEdit != '0'):
        if (opEdit == "1"):
            estudiantes[usuario_logueado[0]][4] = pedirFecha()
            limpiarConsola()
        elif (opEdit == "2"):
            estudiantes[usuario_logueado[0]][5] = input("Nueva biografía: ")
            limpiarConsola()
        elif (opEdit == '3'):
            estudiantes[usuario_logueado[0]][6] = input("Agregar nuevo Hobby: ")
            limpiarConsola()
        else:
            print('No has elegido una opcion valida.')
            print('------------------------')
        print("Datos personales \n---------------\nFecha: ", estudiantes[usuario_logueado[0]][4], "\nBiografía: ", estudiantes[usuario_logueado[0]][5], "\nHobbies: ", estudiantes[usuario_logueado[0]][6], '\n---------------')
        opEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()

# VARIABLES - TIPO DE DATOS:
#ultimo - integer
#a - array of string
def mostrar(a):
    ultimo = buscarEspacioVacioPorPosicion(a)
    if ultimo == -1:
        ultimo = len(a) - 1

    for i in range(ultimo):
        if (usuario_logueado[0] != i and a[i][7] != 'n'):
            print(
                'Nombre: ', a[i][2], '- ♡' if matrizLikes[usuario_logueado[0]][i] == 1 else '')
            print('Edad: ', calcularEdad(a[i][4]))
            print('Biografia: ', a[i][5])
            print('Hobbies: ', a[i][6])
            print('-------------------------')

# VARIABLES - TIPO DE DATOS:
#matchear - char
#me_gusta - string
#idEstudianteMeGusta - integer
def verCandidatos():
    mostrar(estudiantes)
    matchear = input('\nQuieres darle like a algun candidato? Ingrese "S/N": ').capitalize()
    while (matchear != 'S' and matchear != 'N'):
        print('---------------')
        print('No ha ingresado una opcion valida!')
        print('---------------')
        matchear = input('Quieres darle like a algun candidato? Ingrese "S/N": ').capitalize()

    if (matchear == 'S'):
        me_gusta = input('--------------- \nIngrese el nombre de la persona con la que le gustaria matchear: ')
        limpiarConsola()
        idEstudianteMeGusta = buscarUsuarioPorNombre(estudiantes, me_gusta)
        if (idEstudianteMeGusta != -1):
            if (matrizLikes[usuario_logueado[0]][idEstudianteMeGusta] == 1):
                matrizLikes[usuario_logueado[0]][idEstudianteMeGusta] = 0
                print('Le has quitado el me gusta al usuario: ', estudiantes[idEstudianteMeGusta][2])
            else:
                matrizLikes[usuario_logueado[0]][idEstudianteMeGusta] = 1
                print('Le has dado un me gusta al usuario: ', estudiantes[idEstudianteMeGusta][2])
        else:
            print('No se ha ingresado un nombre de estudiante valido. \n---------------')
    else:
        limpiarConsola()

# VARIABLES - TIPO DE DATOS:
#opc - char
def desactivarPerfil(usuario_logueado):
    opc = ''
    while (opc != 'S' and opc != 'N'):
        print('ATENCION')
        print('--------------------')
        opc = input('Esta apunto de inhabilitar su perfil, esta seguro de esta accion? S/N: ').capitalize()

        if (opc != 'S' and opc != 'N'):
            limpiarConsola()
            print('No ha ingresado una opcion valida, vuelva a intentar!')
    if (opc == 'S'):
        estudiantes[usuario_logueado[0]][7] = 'n'
        limpiarConsola()
        print('Usuario desactivado')
    else:
        limpiarConsola()

# VARIABLES - TIPO DE DATOS:
#usuario_encontrado, opc, estudiante_reportado - integer
#estudiante_reportado, motivo - string
def reportarCandidatos():
    print("MENU REPORTAR")
    usuario_encontrado = -1
    opc = input('1. Por ID \n2. Por Nombre \nIngrese la forma que quiere reportar: ')
    while (opc != "1" and opc != "2"):
        opc = input(
            '1. Por ID \n2. Por Nombre \nIngrese la forma que quiere reportar: ')
    if (opc == "1"):
        try:
            estudiante_reportado = int(input('Ingrese la ID del estudiante a reportar: '))
            usuario_encontrado = buscarUsuarioPorId(estudiantes, estudiante_reportado)
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_reportado = input("Ingrese el nombre del estudiante a reportar: ")
        usuario_encontrado = buscarUsuarioPorNombre(estudiantes, estudiante_reportado)

    # Continuacion del reporte
    if (usuario_encontrado == usuario_logueado[0]):
        limpiarConsola()
        print('No podes reportarte a vos mismo.')
    elif (usuario_encontrado == -1):
        limpiarConsola()
        print("Usuario no encontrado o Ingresaste dato inválido")
    else:
        motivo = input('Ingrese el motivo del reporte: ')
        posicionReporteNuevo = buscarEspacioVacioPorPosicion(reportes_motivos)
        if (posicionReporteNuevo != -1):
            # ID DEL REPORTANTE
            reportes_ids[posicionReporteNuevo][0] = usuario_logueado[0]
            # ID DEL USUARIO A REPORTAR
            reportes_ids[posicionReporteNuevo][1] = usuario_encontrado
            # MOTIVO
            reportes_motivos[posicionReporteNuevo][0] = motivo
            # ESTADO INICIAL DEL REPORTE
            reportes_motivos[posicionReporteNuevo][1] = '0'
            limpiarConsola()
            print('Usuario reportado con exito!')
        else:
            limpiarConsola()
            print('No hay mas memoria para reportes!')

# VARIABLES - TIPO DE DATOS:
#ultimo_estudiante, i, estudiante_desactivado, opc - integer
#activo - string
#confirmacion - char
def desactivarEstudiante():
    print('ESTUDIANTES')
    print('---------------')
    ultimo_estudiante = buscarEspacioVacioPorPosicion(estudiantes)
    if (ultimo_estudiante == -1):
        ultimo_estudiante = len(estudiantes)

    for i in range(ultimo_estudiante):
        print('ID: ', i)
        print('Nombre: ', estudiantes[i][2])
        activo = 'Si' if estudiantes[i][7] == 's' else 'No'
        print('Usuario activo: ', activo)
        print('-------------------')

    estudiante_desactivado = -1
    opc = input('1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere desactivar: ')
    while (opc != "1" and opc != "2"):
        opc = input('1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere desactivar: ')
    if (opc == "1"):
        try:
            estudiante_desactivado = buscarUsuarioPorId(estudiantes, int(
                input('Ingrese la ID del estudiante a desactivar: ')))
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_desactivado = buscarUsuarioPorNombre(estudiantes, input("Ingrese el nombre del estudiante a desactivar: "))
    if (estudiante_desactivado != -1):
        confirmacion = input('Esta seguro que desea continuar con la accion? S/N: ').capitalize()
        while (confirmacion != 'S' and confirmacion != 'N'):
            print('No ha ingresado una opcion valida, vuelta a intentar!')
            confirmacion = input(
                'Esta seguro que desea continuar con la accion? S/N: ').capitalize()

        if (confirmacion == 'S'):
            if (estudiantes[estudiante_desactivado][7] == 'n'):
                estudiantes[estudiante_desactivado][7] = 's'
                print('Estudiante activado con exito!')
            else:
                estudiantes[estudiante_desactivado][7] = 'n'
                print('Estudiante desactivado con exito!')
        else:
            print('Accion abortada.')
    else:
        print("El usuario no se encontró. Ingrese opción válida.")

# VARIABLES - TIPO DE DATOS:
#reportes_contador, ultimo_reporte, i,  estadoReporte, reportes_contador, eleccion, estadoReporteEleccion - integer
#estadoReportante, estadoReportado, estadoReportadoEleccion, estadoReportanteEleccion, accion - char
def verReportes():
    reportes_contador = 0
    ultimo_reporte = buscarEspacioVacioPorPosicion(reportes_motivos)
    if (ultimo_reporte == -1):
        ultimo_reporte = len(reportes_motivos)

    for i in range(ultimo_reporte):
        estadoReportante = estudiantes[reportes_ids[i][0]][7]
        estadoReportado = estudiantes[reportes_ids[i][1]][7]
        estadoReporte = reportes_motivos[i][1]
        if (estadoReportante == 's' and estadoReportado == "s" and estadoReporte == '0'):
            reportes_contador = + 1
            print('Reporte numero: ', i+1)
            print('Estado del reporte: ', reportes_motivos[i][1])
            print('-----------------')
    if (reportes_contador == 0):
        print('No hay reportes para analizar.')
    else:
        eleccion = int(input('Ingrese el numero de reporte que desea ver o presione 0 para salir'))
        while (eleccion < 0 or eleccion > 50):
            eleccion = int(
                input('Ingrese el numero de reporte que desea ver. Presione 0 para salir'))

        estadoReportanteEleccion = estudiantes[reportes_ids[eleccion-1][0]][7]
        estadoReportadoEleccion = estudiantes[reportes_ids[eleccion-1][1]][7]
        estadoReporteEleccion = reportes_motivos[eleccion-1][1]

        if (eleccion != 0 and estadoReportanteEleccion == 's' and estadoReportadoEleccion == "s" and estadoReporteEleccion == '0'):
            print('ID usuario reportante: ', reportes_ids[eleccion-1][0])
            print('ID usuario reportado: ', reportes_ids[eleccion-1][1])
            print('Motivo del reporte: ', reportes_motivos[eleccion-1][0])

            accion = input('Ignorar reporte (I) o dar de baja al reportado (B)?').capitalize()
            if (accion == 'I'):
                reportes_motivos[eleccion-1][1] = '2'
                print("Has ignorado la solicitud")
            elif (accion == 'B'):
                reportes_motivos[eleccion-1][1] = '1'
                estudiantes[reportes_ids[eleccion-1][1]][7] = 'n'
                print("Has aceptado la solicitud. El usuario ha sido dado de baja")
            else:
                print('No has elegido una opcion valida!')
        else:
            print('El reporte no se encuentra')

# Reportes Estadisticos inicio
# VARIABLES - TIPO DE DATOS:
#acumMeGustaMutuos, i, j - integer
#porcentaje - float
def matcheosMutuos():
    acumMeGustaMutuos = 0
    i = usuario_logueado[0]
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 1):
                if (matrizLikes[j][i] == 1):
                    if (estudiantes[i][7] != "n" and estudiantes[j][7] != "n"):
                        acumMeGustaMutuos = acumMeGustaMutuos+1
        j = j+1
    porcentaje = acumMeGustaMutuos/(j-1)*100
    return porcentaje

# VARIABLES - TIPO DE DATOS:
#acumMeGustaNoDevueltos, i, j - integer
def meGustaNoDevueltos():
    acumMeGustaNoDevueltos = 0
    i = usuario_logueado[0]
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 1):
                if (matrizLikes[j][i] == 0):
                    if (estudiantes[i][7] != "n" and estudiantes[j][7] != "n"):
                        acumMeGustaNoDevueltos = acumMeGustaNoDevueltos+1
        j = j+1
    return acumMeGustaNoDevueltos

# VARIABLES - TIPO DE DATOS:
#acum, i, j - integer
def leGustoYNoMeGusta():
    acum = 0
    i = usuario_logueado[0]
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 0):
                if (matrizLikes[j][i] == 1):
                    if (estudiantes[i][7] != "n" and estudiantes[j][7] != "n"):
                        acum = acum+1
        j = j+1
    return acum
# Reportes Estadisticos fin

# VARIABLES - TIPO DE DATOS:
#volver_principal - boolean
#num_op, letra_op - char

def opMenuEstudiante(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar mi perfil \n--------------- \na.Editar mis datos personales \nb.Eliminar mi perfil \nc.Volver")
            letra_op = input("Ingrese a, b o c: ").capitalize()
            limpiarConsola()
            if letra_op == "A":
                editarPerfil(usuario_logueado)
            elif letra_op == "B":
                desactivarPerfil(usuario_logueado)
            elif letra_op == "C":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
            if (estudiantes[usuario_logueado[0]][7] == 'n'):
                volver_principal = True
    elif num_op == "2":
        while (not volver_principal):
            print(
                "Gestionar candidatos \n--------------- \na.Ver candidatos \nb.Reportar candidatos \nc.Volver")
            letra_op = input("Ingrese a, b o c: ").capitalize()
            limpiarConsola()
            if letra_op == "A":
                verCandidatos()
            elif letra_op == "B":
                print("Reportar candidatos")
                print('---------------')
                reportarCandidatos()
            elif letra_op == "C":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "3":
        while (not volver_principal):
            print(
                "Matcheos \n--------------- \na.Ver matcheos \nb.Eliminar un matcheo \nc.Volver")
            letra_op = input("Ingrese a, b o c: ").capitalize()
            limpiarConsola()
            if letra_op == "A":
                print("Ver matcheos (En construcción)")
                print('---------------')
            elif letra_op == "B":
                print("Eliminar un matcheo (En construcción)")
                print('---------------')
            elif letra_op == "C":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "4":
        while (not volver_principal):
            print("REPORTES ESTADISTICOS")
            print('-------------------')
            ver = matcheosMutuos()
            print("Porcentaje de matcheos mutuos: ", ver, "%")
            ver2 = meGustaNoDevueltos()
            print("Cantidad de me gusta no devueltos: ", ver2)
            ver3 = leGustoYNoMeGusta()
            print("Cantidad de le gusto y no me gusta: ", ver3)
            print('---------------------')
            num_subOp = int(input("Presione 0 para volver: "))
            if num_subOp == 0:
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
            limpiarConsola()
    elif num_op == "0":
        print('Se deslogueo correctamente.')
        usuario_logueado[0] = -1
        usuario_logueado[1] = -1
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')

# VARIABLES - TIPO DE DATOS:
#volver_principal - boolean
#num_op, letra_op - char
def opMenuModerador(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar ususarios \n--------------- \na. Desactivar usuario \nb. Volver")
            letra_op = input("Ingrese a, b: ")
            limpiarConsola()
            if letra_op == "a":
                desactivarEstudiante()
            elif letra_op == "b":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "2":
        while (not volver_principal):
            print("Gestionar reportes \n--------------- \na. Ver reportes \nb. Volver")
            letra_op = input("Ingrese a, b: ")
            limpiarConsola()
            if letra_op == "a":
                verReportes()
            elif letra_op == "b":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "3":
        while (not volver_principal):
            print("Reportes Estadisticos \n--------------- \na. ? \nb. Volver")
            letra_op = input("Ingrese a, b: ")
            limpiarConsola()
            if letra_op == "a":
                print("?")
            elif letra_op == "b":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "0":
        print('Se deslogueo correctamente.')
        usuario_logueado[0] = -1
        usuario_logueado[1] = -1
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')

# VARIABLES - TIPO DE DATOS:
#num_op - char
#menu_principal - string
def menuModerador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU MODERADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuModerador(num_op)

# VARIABLES - TIPO DE DATOS:
#i, encontrado, posicion_registrado - int
#email - string
def registro(array):
    i = buscarEspacioVacioPorPosicion(array)
    if (i == 8):
        print("No hay mas espacio para registros.")
    else:
        print('REGISTRO')
        print('------------')
        email = input('Ingrese el email:')
        encontrado = buscarUsuarioPorEmail(array, email)
        
        while (encontrado != -1):
            print('Usuario ya creado, por favor ingrese otro email.')
            email = input('Ingrese el email:')
            encontrado = buscarUsuarioPorEmail(array, email)

        array[i][0] = email
        array[i][1] = obtenerPassword()
        array[i][2] = input("Ingrese nombre y apellido: ")
        array[i][3] = "Estudiante"
        array[i][4] = pedirFecha()
        array[i][7] = "s"
        limpiarConsola()
        posicion_registrado = buscarEspacioVacioPorPosicion(estudiantes) - 1
        for i in range(posicion_registrado+1):
            matrizLikes[posicion_registrado][i] = random.randint(0, 1)
            matrizLikes[i][posicion_registrado] = random.randint(0, 1)
        matrizLikes[posicion_registrado][posicion_registrado] = 0

# VARIABLES - TIPO DE DATOS:
#cantidadEstudiantes, cantidadMatcheosPosiblesTotales - integer
def cantidadMatcheosPosibles(estudiantes):
    cantidadEstudiantes = buscarEspacioVacioPorPosicion(estudiantes)
    cantidadMatcheosPosiblesTotales = cantidadEstudiantes * \
        (cantidadEstudiantes - 1)
    print('La cantidad de matcheos posibles entre todos los estudiantes es de: ', cantidadMatcheosPosiblesTotales)

# BONUS TRACK 1 - INICIO
# VARIABLES - TIPO DE DATOS:
# edades - ARRAY of INTEGER
edades = [0]*6
edades = [21, 18, 26, 19, 23, 28]

# Procedimiento para mostrar los elementos de un arreglo
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY of INTEGER
def mostrarBonus1(z):
    s = len(z)
    for i in range(s):
        print(z[i])

# Procedimiento para ordenar los elementos de un arreglo con el método de la burbuja
# VARIABLES - TIPO DE DATOS:
# s, aux - INTEGER
# z - ARRAY of INTEGER
def ordenarBonus1(z):
    s = len(z)
    for i in range(s-1):
        for j in range((i+1), s):
            if z[i] > z[j]:
                aux = z[i]
                z[i] = z[j]
                z[j] = aux
# Función para contar la cantidad de "huecos" que hay en la secuencia
# VARIABLES - TIPO DE DATOS:
# s, h - INTEGER
# z - ARRAY of INTEGER
def contarhuecosBonus1(z):
    s = len(z)
    h = 0
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            h = h+1
    return h
# Función que crea un arreglo con los elementos que faltan para completar la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z, g - ARRAY of INTEGER
def faltantesBonus1(z):
    s = len(z)
    g = [0]*(s-1)
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            g[i] = z[i]+1
        else:
            g[i] = 0
    return g
# Procedimiento para mostrar los elementos que faltan en la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY of INTEGER
def mostrarfaltantesBonus1(z):
    s = len(z)
    for i in range(s):
        if z[i] != 0:
            print(z[i])
# BONUS TRACK 1 - FIN

# INICIALIZAMOS MATRIZ DE LIKES CON 0s y 1s DE MANERA RANDOM.
generarInteracciones()
# PROGRAMA PRINCIPAL
# VARIABLES - TIPO DE DATOS:
#opc - char
#huecos - integer
#edadesFaltantes - array of integers
opc = ''
while (opc != '0'):
    print('MENU PRINCIPAL')
    print("---------------------------------------")
    print("1. Login")
    print("2. Registro")
    print("3. Cantidad de matcheos posibles")  # Bonus Track 2
    print("4. Reporte de edades")  # Bonus Track 1
    print("0. Salir")
    opc = input('Ingrese una opcion: ')
    limpiarConsola()
    if (opc == '1'):
        login(usuario_logueado, estudiantes, moderadores)
        if (usuario_logueado[1] == 0):
            menuEstudiante()
        elif (usuario_logueado[1] == 1):
            menuModerador()
    elif (opc == '2'):
        registro(estudiantes)
    elif (opc == '3'):
        cantidadMatcheosPosibles(estudiantes)
    elif (opc == '4'):
        print("Reporte de edades:")
        mostrarBonus1(edades)
        ordenarBonus1(edades)
        print("Reporte de edades ordenadas de forma creciente:")
        mostrarBonus1(edades)
        huecos = contarhuecosBonus1(edades)
        print("Cantidad de huecos en la secuencia: ", huecos)
        edadesFaltantes = faltantesBonus1(edades)
        print("El/los elemento/s faltante/s para tener una secuencia autoincremental es/son:")
        mostrarfaltantesBonus1(edadesFaltantes)
    elif (opc == '0'):
        print('Saliendo del programa...')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')