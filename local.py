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
estudiantes[0][0] = "0"
estudiantes[0][1] = "estudiante1@ayed.com"
estudiantes[0][2] = "111222"
estudiantes[0][3] = "Pedro Castillo"
estudiantes[0][4] = "Estudiante"
estudiantes[0][5] = "2000-04-23"
estudiantes[0][6] = "Hola esta es mi biografia"
estudiantes[0][7] = "Andar a caballo es mi hobbie"
estudiantes[0][8] = "s"

estudiantes[1][0] = "1"
estudiantes[1][1] = "estudiante2@ayed.com"
estudiantes[1][2] = "333444"
estudiantes[1][3] = "Florencia Abascal"
estudiantes[1][4] = "Estudiante"
estudiantes[1][5] = "2000-07-13"
estudiantes[1][6] = "Hola esta es mi biografia"
estudiantes[1][7] = "Andar a caballo es mi hobbie"
estudiantes[1][8] = "s"

estudiantes[2][0] = "2"
estudiantes[2][1] = "estudiante3@ayed.com"
estudiantes[2][2] = "555666"
estudiantes[2][3] = "Raul Gimenez"
estudiantes[2][4] = "Estudiante"
estudiantes[2][5] = "2000-07-14"
estudiantes[2][6] = "Hola esta es mi biografia"
estudiantes[2][7] = "Andar a caballo es mi hobbie"
estudiantes[2][8] = "s"


moderadores[0][0] = "0"
moderadores[0][1] = "moderador1@ayed.com"
moderadores[0][2] = "111222"
moderadores[0][3] = "Pedro Castillo"
moderadores[0][4] = "Moderador"
moderadores[0][5] = "2000-07-12"
moderadores[0][6] = "Hola esta es mi biografia"
moderadores[0][7] = "Andar a caballo es mi hobbie"
moderadores[0][8] = "s"

moderadores[1][0] = "1"
moderadores[1][1] = "moderador2@ayed.com"
moderadores[1][2] = "333444"
moderadores[1][3] = "Florencia Abascal"
moderadores[1][4] = "Moderador"
moderadores[1][5] = "2000-07-12"
moderadores[1][6] = "Hola esta es mi biografia"
moderadores[1][7] = "Andar a caballo es mi hobbie"
moderadores[1][8] = "s"

usuario_logueado = ['']*9
# -------------------------------------------
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

    cantidadEstudiantes = buscarEspacioVacio(estudiantes)
    cantidadModeradores = buscarEspacioVacio(moderadores)

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 3) and (cantidadModeradores != -1 and cantidadModeradores >= 1)):
        # Mientras el contador sea menor o igual a 3 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == ''):
            print(intentos)
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
                        print("login exitoso! usuario")
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
                            print("login exitoso! moderador")
                        else:
                            intentos = intentos + 1
                else:
                    password = obtenerPassword()
                    intentos = intentos + 1
    else:
        print('No hay suficientes usuario creados para el logueo')


def buscarEspacioVacio(a):
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

    i = buscarEspacioVacio(array)
    print("espacio vacio: ", i)
    if (i == (-1)):
        print("No hay mas espacio para registros.")
    else:
        array[i][0] = i

        email = input('Ingrese el email:')
        encontrado = buscarUsuarioPorEmail(array, email)

        while (encontrado != -1):
            print('Usuario ya creado, por favor ingrese otro email.')
            email = input('Ingrese el email:')
            encontrado = buscarUsuarioPorEmail(array, email)

        array[i][1] = email

        print("Ingrese contraseña:")
        array[i][2] = input()
        print("Ingrese nombre y apellido:")
        array[i][3] = input()
        array[i][4] = "Estudiante"
        array[i][8] = "s"

    for j in range(8):
        print(array[i][j])


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
    print("Datos personales \n---------------\nFecha: ", usuario_logueado[5], "\nBiografía: ",
          usuario_logueado[6], "\nHobbies: ", usuario_logueado[7], '\n---------------')

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

        print("Datos personales \n---------------\nFecha: ", usuario_logueado[5], "\nBiografía: ",
              usuario_logueado[6], "\nHobbies: ", usuario_logueado[7], '\n---------------')

        opEdit = input(
            "1.Fecha \n2.Biografía \n3.Hobbies \n0.Volver\nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()

    estudiantes[int(usuario_logueado[0])][5] = usuario_logueado[5]
    estudiantes[int(usuario_logueado[0])][6] = usuario_logueado[6]
    estudiantes[int(usuario_logueado[0])][7] = usuario_logueado[7]


def mostrar(a):
    ultimo = buscarEspacioVacio(a)
    if ultimo == -1:
        ultimo = len(a) - 1

    for i in range(ultimo):
        if (usuario_logueado[0] != a[i][0]):
            print('Nombre: ', a[i][3])
            print('Edad: ', calcularEdad(a[i][5]))
            print('Biografia: ', a[i][6])
            print('Hobbies: ', a[i][7])
            print('-------------------------')


def verCandidatos():
    mostrar(estudiantes)


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
    estudiante_reportado = input(
        'Ingrese el nombre o la ID del estudiante a reportar.')

    usuario_encontrado = buscarUsuarioPorNombre(
        estudiantes, estudiante_reportado)
    if (usuario_encontrado == -1):
        usuario_encontrado = buscarUsuarioPorId(
            estudiantes, estudiante_reportado)

    while (usuario_encontrado == -1):
        print('Usuario a reportar no encontrado, vuelva a intentar!')
        print('--------------------------')
        estudiante_reportado = input(
            'Ingrese el nombre o la ID del estudiante a reportar.')

        usuario_encontrado = buscarUsuarioPorNombre(
            estudiantes, estudiante_reportado)
        if (usuario_encontrado == -1):
            usuario_encontrado = buscarUsuarioPorId(
                estudiantes, estudiante_reportado)

    motivo = input('Ingrese el motivo del reporte: ')

    posicionReporteNuevo = buscarEspacioVacio(reportes)

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
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == "a":
                editarPerfil(usuario_logueado)
            elif letra_op == "b":
                print("Eliminar perfil")
                desactivarPerfil(usuario_logueado)
            elif letra_op == "c":
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
            letra_op = input("Ingrese a, b o c: ")
            limpiarConsola()
            if letra_op == "a":
                verCandidatos()
            elif letra_op == "b":
                print("Reportar candidatos")
                print('---------------')
                reportarCandidatos()
            elif letra_op == "c":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
    elif num_op == "3":
        while (not volver_principal):
            print(
                "Matcheos \n--------------- \na.Ver matcheos \nb.Eliminar un matcheo \nc.Volver")
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

    ultimo_estudiante = buscarEspacioVacio(estudiantes)
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
        estudiante = input(
            'Ingrese la ID o nombre del usuario que desea activar/desactivar: ')

        estudiante_encontrado = buscarUsuarioPorNombre(
            estudiantes, estudiante)
        if (estudiante_encontrado == -1):
            estudiante_encontrado = buscarUsuarioPorId(
                estudiantes, estudiante)

    if (estudiantes[estudiante_encontrado][8] == 'n'):
        estudiantes[estudiante_encontrado][8] = 's'
        print('Estudiante activado con exito!')
    else:
        estudiantes[estudiante_encontrado][8] = 'n'
        print('Estudiante desactivado con exito!')


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
                print("verReportes()")
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


def generarInteracciones():

    ultimo = buscarEspacioVacio(estudiantes)

    if (ultimo == -1):
        ultimo = len(estudiantes)

    for i in range(ultimo):
        for j in range(ultimo):
            if (i != j):
                matrizLikes[i][j] = random.randint(0, 1)
            else:
                matrizLikes[i][j] = 0


# INICIALIZAMOS MATRIZ DE LIKES CON 0s y 1s DE MANERA RANDOM.
generarInteracciones()
# PROGRAMA PRINCIPAL
opc = ''

while (opc != '0'):

    print("1. Login")
    print("2. Registro")
    print("0. Salir")
    opc = input('Ingrese una opcion: ')

    if (opc == '1'):
        login(usuario_logueado, estudiantes)
        if (usuario_logueado[4] == "Estudiante"):
            menuEstudiante()
        elif (usuario_logueado[4] == "Moderador"):
            menuModerador()
    elif (opc == '2'):
        registro(estudiantes)
    elif (opc == '0'):
        print('Saliendo del programa...')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')
        print("1. Login")
        print("2. Registro")
        print("0. Salir")
        opc = input('Ingrese una opcion: ')
