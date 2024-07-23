import pwinput
import os
from datetime import date, datetime
import random

# PRIMERO COLUMNAS, SEGUNDO FILAS
matrizLikes = [[-1]*8 for n in range(8)]
estudiantes = [['']*9 for n in range(8)]
moderadores = [['']*9 for n in range(4)]
reportes = [[''] * 4 for n in range(49)]

# Tanto el ID de cada estudiante como de cada moderador va a ser siempre un número entero auto-incremental, que comienza en 0.
estudiantes[0] = ["0", "estudiante1@ayed.com", "111222", "Pedro Castillo", "Estudiante", "1994-06-20", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
estudiantes[1] = ["1", "estudiante2@ayed.com", "333444", "Florencia Abascal", "Estudiante", "2000-04-20", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
estudiantes[2] = ["2", "estudiante3@ayed.com", "555666", "Raul Gimenez", "Estudiante", "2002-10-9", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]

moderadores[0] = ["0", "moderador1@ayed.com", "111222", "Pedro Castillo", "Moderador", "2000-07-12", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
moderadores[1] = ["1", "moderador2@ayed.com", "333444", "Florencia Abascal", "Moderador", "2000-07-12", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]

usuario_logueado = ['']*9

# Funcion obtenerPassword (para que en vez de la password aparezcan asteriscos)
# VARIABLES - TIPO DE DATOS:
# password - STRING
# Funcion limpiarConsola (Funcion dedicada a limpiar la consola para no saturar la pantalla de informacion)
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password

def login(usuario_logueado, estudiantes):
    intentos = 0
    cantidadEstudiantes = buscarEspacioVacioPorPosicion(estudiantes)
    cantidadModeradores = buscarEspacioVacioPorPosicion(moderadores)

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 3) and (cantidadModeradores != -1 and cantidadModeradores >= 1)):
        # Mientras el contador sea menor o igual a 3 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == ''):
            # Pedir al usuario igresar usuario y contraseña
            email = input("Ingresar email: ")
            resultadoBusqueda = buscarUsuarioPorEmail(estudiantes, email)

            if (resultadoBusqueda != -1):
                if (estudiantes[resultadoBusqueda][8] == 'n'):
                    print('Tu usuario esta desactivado, no puedes loguearte.')
                    intentos = 3

                while (intentos < 3 and usuario_logueado[0] == ''):
                    password = obtenerPassword()
                    if (estudiantes[resultadoBusqueda][2] == password):
                        for i in range(len(estudiantes[0])):
                            usuario_logueado[i] = estudiantes[resultadoBusqueda][i]
                        limpiarConsola()
                        print("Login exitoso! bienvenido usuario", usuario_logueado[3], '.')
                        print('--------------------')
                    else:
                        intentos = intentos + 1
            else:
                resultadoBusqueda = buscarUsuarioPorEmail(moderadores, email)

                if (resultadoBusqueda != -1):
                    while (intentos < 3 and usuario_logueado[0] == ''):
                        password = obtenerPassword()
                        if (moderadores[resultadoBusqueda][2] == password):
                            for i in range(len(moderadores[0])):
                                usuario_logueado[i] = moderadores[resultadoBusqueda][i]
                            limpiarConsola()
                            print("Login exitoso! bienvenido moderador ", usuario_logueado[3])
                        else:
                            intentos = intentos + 1
                else:
                    password = obtenerPassword()
                    intentos = intentos + 1
    else:
        print('No hay suficientes usuario creados para el logueo')

def buscarEspacioVacioPorPosicion(a):
    i = 0
    while (i < (len(a) - 1) and a[i][0] != ''):
        i = i+1
    if (i == (len(a))):
        return -1
    else:
        return i

def buscarUsuarioPorEmail(array, email):
    contadorPosicion = 0
    while (contadorPosicion < (len(array) - 1) and (array[contadorPosicion][1] != email)):
        contadorPosicion += 1

    if (array[contadorPosicion][1] == email):
        return contadorPosicion
    else:
        return -1

def buscarUsuarioPorNombre(array, nombre):
    contadorPosicion = 0
    while (contadorPosicion < (len(array) - 1) and (array[contadorPosicion][3] != nombre)):
        contadorPosicion += 1

    if (array[contadorPosicion][3] == nombre):
        return contadorPosicion
    else:
        return -1

def buscarUsuarioPorId(array, id):
    contadorPosicion = 0
    while (contadorPosicion < (len(array) - 1) and (array[contadorPosicion][0] != id)):
        contadorPosicion += 1

    if (array[contadorPosicion][0] == id):
        return contadorPosicion
    else:
        return -1

def registro(array):
    i = buscarEspacioVacioPorPosicion(array)
    if (i == (-1)):
        print("No hay mas espacio para registros.")
    else:
        array[i][0] = i
        print('REGISTRO')
        print('------------')
        email = input('Ingrese el email:')
        encontrado = buscarUsuarioPorEmail(array, email)

        while (encontrado != -1):
            print('Usuario ya creado, por favor ingrese otro email.')
            email = input('Ingrese el email:')
            encontrado = buscarUsuarioPorEmail(array, email)

        array[i][1] = email
        array[i][2] = obtenerPassword()
        array[i][3] = input("Ingrese nombre y apellido: ")
        array[i][4] = "Estudiante"
        array[i][8] = "s"
        limpiarConsola()
        espacio_vacio = buscarEspacioVacioPorPosicion(estudiantes) - 1

        for i in range(espacio_vacio):
            matrizLikes[espacio_vacio][i] = random.randint(0, 1)
            matrizLikes[i][espacio_vacio] = random.randint(0, 1)
    matrizLikes[espacio_vacio][espacio_vacio] = 0

def calcularEdad(fecha_nacimiento):
    # Convertir el string de fecha de nacimiento a un objeto datetime
    fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

    # Obtener la fecha actual
    hoy = datetime.today()

    # Calcular la diferencia de años
    edad = hoy.year - fecha_nac.year

    # Ajustar si no ha cumplido años este año
    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
    return edad

def pedirFecha():
    fecha_actual = date.today()
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

def editarPerfil(usuario_logueado):
    print("Datos personales \n---------------\nFecha: ", usuario_logueado[5], "\nBiografía: ", usuario_logueado[6], "\nHobbies: ", usuario_logueado[7], '\n---------------')

    opEdit = input(
        "1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
    limpiarConsola()

    while (opEdit != '0'):
        if (opEdit == "1"):
            usuario_logueado[5] = pedirFecha()
            limpiarConsola()
        elif (opEdit == "2"):
            usuario_logueado[6] = input("Nueva biografía: ")
            limpiarConsola()
        elif (opEdit == '3'):
            usuario_logueado[7] = input("Agregar nuevo Hobby: ")
            limpiarConsola()
        else:
            print('No has elegido una opcion valida.')
            print('------------------------')

        print("Datos personales \n---------------\nFecha: ", usuario_logueado[5], "\nBiografía: ", usuario_logueado[6], "\nHobbies: ", usuario_logueado[7], '\n---------------')
        opEdit = input(
            "1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()

    estudiantes[int(usuario_logueado[0])][5] = usuario_logueado[5]
    estudiantes[int(usuario_logueado[0])][6] = usuario_logueado[6]
    estudiantes[int(usuario_logueado[0])][7] = usuario_logueado[7]

def mostrar(a):
    ultimo = buscarEspacioVacioPorPosicion(a)
    if ultimo == -1:
        ultimo = len(a) - 1

    for i in range(ultimo):
        if (usuario_logueado[0] != a[i][0]):
            print('Nombre: ', a[i][3], '- ♡' if matrizLikes[int(
                usuario_logueado[0])][i] == 1 else '')
            print('Edad: ', calcularEdad(a[i][5]))
            print('Biografia: ', a[i][6])
            print('Hobbies: ', a[i][7])
            print('-------------------------')

def verCandidatos():
    mostrar(estudiantes)
    matchear = input(
        '\nQuieres darle like a algun candidato? Ingrese "S/N": ').capitalize()
    while (matchear != 'S' and matchear != 'N'):
        print('---------------')
        print('No ha ingresado una opcion valida!')
        print('---------------')
        matchear = input(
            'Quieres darle like a algun candidato? Ingrese "S/N": ').capitalize()

    if (matchear == 'S'):
        me_gusta = input(
            '--------------- \nIngrese el nombre de la persona con la que le gustaria matchear: ')
        limpiarConsola()
        idEstudianteMeGusta = buscarUsuarioPorNombre(estudiantes, me_gusta)
        if (idEstudianteMeGusta != -1):

            if (matrizLikes[int(usuario_logueado[0])][idEstudianteMeGusta] == 1):
                matrizLikes[int(usuario_logueado[0])][idEstudianteMeGusta] = 0
                print('Le has quitado el me gusta al usuario: ', estudiantes[idEstudianteMeGusta][3])
            else:
                matrizLikes[int(usuario_logueado[0])][idEstudianteMeGusta] = 1
                print('Le has dado un me gusta al usuario: ', estudiantes[idEstudianteMeGusta][3])
        else:
            print('No se ha ingresado un nombre de estudiante valido. \n---------------')

def desactivarPerfil(usuario_logueado):
    opc = ''
    while (opc != 'S' and opc != 'N'):
        print('ATENCION')
        print('--------------------')
        opc = input(
            'Esta apunto de inhabilitar su perfil, esta seguro de esta accion? S/N').capitalize()

        if (opc != 'S' and opc != 'N'):
            print('No ha ingresado una opcion valida, vuelva a intentar!')

    if (opc == 'S'):
        estudiantes[int(usuario_logueado[0])][8] = 'n'
        usuario_logueado[0] = ''
        usuario_logueado[1] = ''
        usuario_logueado[2] = ''
        usuario_logueado[3] = ''
        usuario_logueado[4] = ''
        usuario_logueado[5] = ''
        usuario_logueado[6] = ''
        usuario_logueado[7] = ''
        usuario_logueado[8] = 'n'
        limpiarConsola()
        print('Usuario desactivado')

def reportarCandidatos():
    estudiante_reportado = input('Ingrese el nombre o la ID del estudiante a reportar: ')

    if (estudiante_reportado == usuario_logueado[0]):
        print('No podes reportarte a vos mismo.')
    else:
        usuario_encontrado = buscarUsuarioPorNombre(
            estudiantes, estudiante_reportado)
        if (usuario_encontrado == -1):
            usuario_encontrado = buscarUsuarioPorId(
                estudiantes, estudiante_reportado)

        while (usuario_encontrado == -1):
            print('Usuario a reportar no encontrado, vuelva a intentar!')
            print('--------------------------')
            estudiante_reportado = input(
                'Ingrese el nombre o la ID del estudiante a reportar: ')

            usuario_encontrado = buscarUsuarioPorNombre(
                estudiantes, estudiante_reportado)
            if (usuario_encontrado == -1):
                usuario_encontrado = buscarUsuarioPorId(
                    estudiantes, estudiante_reportado)

        motivo = input('Ingrese el motivo del reporte: ')
        posicionReporteNuevo = buscarEspacioVacioPorPosicion(reportes)

        if (posicionReporteNuevo != -1):
            # ID DEL REPORTANTE
            reportes[posicionReporteNuevo][0] = usuario_logueado[0]
            # ID DEL USUARIO A REPORTAR
            reportes[posicionReporteNuevo][1] = estudiantes[usuario_encontrado][0]
            # MOTIVO
            reportes[posicionReporteNuevo][2] = motivo
            # ESTADO INICIAL DEL REPORTE
            reportes[posicionReporteNuevo][3] = '0'
            print('Usuario reportado con exito!')
        else:
            print('No hay mas memoria para reportes!')

def limpiarUsuarioLogueado(usuario):
    usuario[0] = ''
    usuario[1] = ''
    usuario[2] = ''
    usuario[3] = ''
    usuario[4] = ''
    usuario[5] = ''
    usuario[6] = ''
    usuario[7] = ''
    usuario[8] = ''

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
                print("Eliminar perfil")
                desactivarPerfil(usuario_logueado)
            elif letra_op == "C":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')

            if (usuario_logueado[8] == 'n'):
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
        limpiarUsuarioLogueado(usuario_logueado)
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')

def menuEstudiante():
    num_op = ''
    while (num_op != '0'):
        menu_principal = "MENU PRINCIPAL ESTUDIANTE \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenuEstudiante(num_op)

        if (usuario_logueado[8] == 'n'):
            num_op = '0'

def menuModerador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU PRINCIPAL MODERADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuModerador(num_op)

def desactivarEstudiante():
    print('ESTUDIANTES')
    print('---------------')
    ultimo_estudiante = buscarEspacioVacioPorPosicion(estudiantes)
    if (ultimo_estudiante == -1):
        ultimo_estudiante = len(estudiantes)

    for i in range(ultimo_estudiante):
        print('ID: ', estudiantes[i][0])
        print('Nombre: ', estudiantes[i][3])
        activo = 'Si' if estudiantes[i][8] == 's' else 'No'
        print('Usuario activo: ', activo)
        print('-------------------')

    estudiante = input(
        'Ingrese la ID o nombre del usuario que desea activar/desactivar: ')
    estudiante_encontrado = buscarUsuarioPorNombre(
        estudiantes, estudiante)
    if (estudiante_encontrado == -1):
        estudiante_encontrado = buscarUsuarioPorId(
            estudiantes, estudiante)

    while (estudiante_encontrado == -1):
        print('Estudiante no encontrado, vuelva a intentar!')
        print('--------------------------')
        estudiante = input('Ingrese la ID o nombre del usuario que desea activar/desactivar: ')
        estudiante_encontrado = buscarUsuarioPorNombre(
            estudiantes, estudiante)
        if (estudiante_encontrado == -1):
            estudiante_encontrado = buscarUsuarioPorId(
                estudiantes, estudiante)

    confirmacion = input(
        'Esta seguro que desea continuar con la accion? S/N: ').capitalize()
    while (confirmacion != 'S' and confirmacion != 'N'):
        print('No ha ingresado una opcion valida, vuelta a intentar!')
        confirmacion = input(
            'Esta seguro que desea continuar con la accion? S/N: ').capitalize()

    if (confirmacion == 'S'):
        if (estudiantes[estudiante_encontrado][8] == 'n'):
            estudiantes[estudiante_encontrado][8] = 's'
            print('Estudiante activado con exito!')
        else:
            estudiantes[estudiante_encontrado][8] = 'n'
            print('Estudiante desactivado con exito!')
    else:
        print('Accion abortada.')

def verReportes():
    reportes_contador = 0
    ultimo_reporte = buscarEspacioVacioPorPosicion(reportes)

    if (ultimo_reporte == -1):
        ultimo_reporte = len(reportes)

    for i in range(ultimo_reporte):
        estadoReportante = estudiantes[int(reportes[i][0])][8]
        estadoReportado = estudiantes[int(reportes[i][1])][8]
        estadoReporte = reportes[i][3]
        if (estadoReportante == 's' and estadoReportado == "s" and estadoReporte == '0'):
            reportes_contador = + 1
            print('Reporte numero: ', i+1)
            print('Estado del reporte: ', reportes[i][3])
            print('-----------------')
    if (reportes_contador == 0):
        print('No hay reportes para analizar.')
    else:
        eleccion = int(
            input('Ingrese el numero de reporte que desea ver o presione 0 para salir'))

        while (eleccion < 0 or eleccion > 50):
            eleccion = int(
                input('Ingrese el numero de reporte que desea ver. Presione 0 para salir'))

        estadoReportanteEleccion = estudiantes[int(reportes[eleccion-1][0])][8]
        estadoReportadoEleccion = estudiantes[int(reportes[eleccion-1][1])][8]
        estadoReporteEleccion = reportes[eleccion-1][3]

        if (eleccion != 0 and estadoReportanteEleccion == 's' and estadoReportadoEleccion == "s" and estadoReporteEleccion == '0'):
            print('ID usuario reportante: ', reportes[eleccion-1][0])
            print('ID usuario reportado: ', reportes[eleccion-1][1])
            print('Motivo del reporte: ', reportes[eleccion-1][2])

            accion = input('Ignorar reporte (I) o dar de baja al reportado (B)?').capitalize()
            if (accion == 'I'):
                reportes[eleccion-1][3] = '2'
                print("Has ignorado la solicitud")
            elif (accion == 'B'):
                reportes[eleccion-1][3] = '1'
                estudiantes[int(reportes[eleccion-1][1])][8] = 'n'
                print("Has aceptado la solicitud. El usuario ha sido dado de baja")
            else:
                print('No has elegido una opcion valida!')
        else:
            print('El reporte no se encuentra')

def opMenuModerador(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print(
                "Gestionar ususarios \n--------------- \na. Desactivar usuario \nb. Volver")
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
        limpiarUsuarioLogueado(usuario_logueado)
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')

def matcheosMutuos():
    acumMeGustaMutuos = 0
    i = int(usuario_logueado[0])
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 1):
                if (matrizLikes[j][i] == 1):
                    acumMeGustaMutuos = acumMeGustaMutuos+1
        j = j+1

    porcentaje = acumMeGustaMutuos/(j-1)*100
    return porcentaje

def meGustaNoDevueltos():
    acumMeGustaNoDevueltos = 0
    i = int(usuario_logueado[0])
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 1):
                if (matrizLikes[j][i] == 0):
                    acumMeGustaNoDevueltos = acumMeGustaNoDevueltos+1
        j = j+1
    return acumMeGustaNoDevueltos

def leGustoYNoMeGusta():
    acum = 0
    i = int(usuario_logueado[0])
    j = 0
    while (matrizLikes[i][j] != -1):
        if (i != j):
            if (matrizLikes[i][j] == 0):
                if (matrizLikes[j][i] == 1):
                    acum = acum+1
        j = j+1
    return acum

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

def cantidadMatcheosPosibles(estudiantes):
    cantidadEstudiantes = buscarEspacioVacioPorPosicion(estudiantes)
    cantidadMatcheosPosiblesTotales = cantidadEstudiantes * \
        (cantidadEstudiantes - 1)
    print('La cantidad de matcheos posibles entre todos los estudiantes es de: ', cantidadMatcheosPosiblesTotales)

###Bonus Track 1 Inicio
# Definimos y dimensionamos el arreglo edades
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
###Bonus Track 1 Fin



# INICIALIZAMOS MATRIZ DE LIKES CON 0s y 1s DE MANERA RANDOM.
generarInteracciones()
# PROGRAMA PRINCIPAL
opc = ''
while (opc != '0'):
    print("---------------------------------------")
    print("1. Login")
    print("2. Registro")
    print("3. Cantidad de matcheos posibles") #Bonus Track 2
    print("4. Reporte de edades") #Bonus Track 1
    print("0. Salir")
    opc = input('Ingrese una opcion: ')
    limpiarConsola()
    if (opc == '1'):
        login(usuario_logueado, estudiantes)
        if (usuario_logueado[4] == "Estudiante"):
            menuEstudiante()
        elif (usuario_logueado[4] == "Moderador"):
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