import pwinput
import os

estudiantes = [['']*9 for n in range(8)]

moderadores = [['']*9 for n in range(4)]

estudiantes[0][0] = "1"                                         #Tanto el ID de cada estudiante como de cada moderador va a ser siempre un número entero auto-incremental, que comienza en 0.
estudiantes[0][1] = "estudiante1@ayed.com"
estudiantes[0][2] = "111222"
estudiantes[0][3] = "Pedro Castillo"
estudiantes[0][4] = "Estudiante"
estudiantes[0][5] = "date(1994, 6, 20)"
estudiantes[0][6] = "Hola esta es mi biografia"
estudiantes[0][7] = "Andar a caballo es mi hobbie"
estudiantes[0][8] = "s"

estudiantes[1][0] = "2"
estudiantes[1][1] = "estudiante2@ayed.com"
estudiantes[1][2] = "333444"
estudiantes[1][3] = "Florencia Abascal"
estudiantes[1][4] = "Estudiante"
estudiantes[1][5] = "date(2000, 4, 20)"
estudiantes[1][6] = "Hola esta es mi biografia"
estudiantes[1][7] = "Andar a caballo es mi hobbie"
estudiantes[1][8] = "s"

estudiantes[2][0] = "3"
estudiantes[2][1] = "estudiante3@ayed.com"
estudiantes[2][2] = "555666"
estudiantes[2][3] = "Raul Gimenez"
estudiantes[2][4] = "Estudiante"
estudiantes[2][5] = "date(2002, 10, 9)"
estudiantes[2][6] = "Hola esta es mi biografia"
estudiantes[2][7] = "Andar a caballo es mi hobbie"
estudiantes[2][8] = "s"

moderadores[0][0] = "1"
moderadores[0][1] = "moderador1@ayed.com"
moderadores[0][2] = "111222"
moderadores[0][3] = "Pedro Castillo"
moderadores[0][4] = "Moderador"
moderadores[0][5] = "date(1994, 6, 20)"
moderadores[0][6] = "Hola esta es mi biografia"
moderadores[0][7] = "Andar a caballo es mi hobbie"
moderadores[0][8] = "s"

moderadores[1][0] = "2"
moderadores[1][1] = "moderador2@ayed.com"
moderadores[1][2] = "333444"
moderadores[1][3] = "Florencia Abascal"
moderadores[1][4] = "Moderador"
moderadores[1][5] = "date(2000, 4, 20)"
moderadores[1][6] = "Hola esta es mi biografia"
moderadores[1][7] = "Andar a caballo es mi hobbie"
moderadores[1][8] = "s"

# -------------------------------------------
# Funcion obtenerPassword (para que en vez de la password aparezcan asteriscos)
# VARIABLES - TIPO DE DATOS:
# password - STRING

#Funcion limpiarConsola (Funcion dedicada a limpiar la consola para no saturar la pantalla de informacion)
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password


def login(usuario_logueado, estudiantes):
    intentos = 0
    # Mientras el contador sea menor o igual a 3 y no este logeado
    print('LOGIN')
    print('--------------------')
    while (intentos < 3 and usuario_logueado[0] == ''):
        print(intentos)
        # Pedir al usuario igresar usuario y contraseña
        email = input("Ingresar email: ")
        resultadoBusqueda = buscarUsuario(estudiantes, email)

        if (resultadoBusqueda != -1):
            while (intentos < 3 and usuario_logueado[0] == ''):
                password = obtenerPassword()
                if (estudiantes[resultadoBusqueda][2] == password):
                    for i in range(len(estudiantes[0])):
                        usuario_logueado[i] = estudiantes[resultadoBusqueda][i]
                    print(estudiantes[resultadoBusqueda])
                    print(usuario_logueado)
                    print("login exitoso! usuario")
                else:
                    intentos = intentos + 1
        else:
            resultadoBusqueda = buscarUsuario(moderadores, email)

            if (resultadoBusqueda != -1):
                while (intentos < 3 and usuario_logueado[0] == ''):
                    password = obtenerPassword()
                    if (moderadores[resultadoBusqueda][2] == password):
                        for i in range(len(moderadores[0])):
                            usuario_logueado[i] = moderadores[resultadoBusqueda][i]
                        print(moderadores[resultadoBusqueda])
                        print(usuario_logueado)
                        print("login exitoso! moderador")
                    else:
                        intentos = intentos + 1
            else:
                password = obtenerPassword()
                intentos = intentos + 1


def buscarUsuario(array, usuario):
    contadorPosicion = 0

    while ((array[contadorPosicion][1] != usuario) and contadorPosicion <= (len(array)-2)):
        contadorPosicion += 1

    if (array[contadorPosicion][1] == usuario):
        return contadorPosicion
    else:
        return -1


def buscarEspacioVacio(a):
    i = 0
    while (i < (len(a)) and a[i][0] != ''):
        i = i+1
    if (i== (len(a))):
            return -1
    else:
        return i


def registro(array):

    i = buscarEspacioVacio(array)
    print("espacio vacio: ", i)
    if (i == (-1)):
        print("No hay mas espacio para registros.")
    else:
        array[i][0] = i+1
        print("Ingrese email:")
        array[i][1] = input()
        print("Ingrese contraseña:")
        array[i][2] = input()
        print("Ingrese nombre y apellido:")
        array[i][3] = input()
        array[i][4] = "Estudiante"
        array[i][8] = "s"

    for j in range(8):
        print(array[i][j])

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

#-------------------------------------------
#Función menu (funcion dedicada al funcionamiento del menu principal)
#VARIBLES - TIPOS DE DATOS
#num_op, menu_principal - STRING
def menuEstudiante():
    num_op = ''

    while num_op != '0':
        menu_principal = "MENU PRINCIPAL ESTUDIANTE \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenu(num_op)

def menuModerador():
    num_op = ''

    while num_op != '0':
        menu_principal = "MENU PRINCIPAL MODERADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuModerador(num_op)

def opMenuModerador(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar ususarios \n--------------- \na. Desactivar usuario \nb. Volver")
            letra_op = input("Ingrese a, b: ")
            limpiarConsola()
            if letra_op == "a":
                print("desactivarUsuario()")
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
        print('Se cerro correctamente.')
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')



# PROGRAMA PRINCIPAL
usuario_logueado = ['']*9
print("1. Login")
print("2. Registro")
print("0. Salir")
opc = int(input())
while (opc != 0 and usuario_logueado[0] == ''):
    if (opc == 1):
        login(usuario_logueado, estudiantes)                #En el login faltaria: 
                                                                #Para acceder a la sección de logueo, deberá haber aunque sea 1 moderador y 4 estudiantes cargados.
                                                                #Tener en cuenta que, además de ingresar un par usuario / contraseña correctos, también se debe chequear que el estado del usuario sea “ACTIVO” (string). Caso contrario, el login NO será correcto.
        if (usuario_logueado[4] == "Estudiante"):
            menuEstudiante()
        elif (usuario_logueado[4] == "Moderador"):
            menuModerador()
    elif (opc == 2):
        registro(estudiantes)
    if (usuario_logueado[0] == ''):
        print("1. Login")
        print("2. Registro")
        print("0. Salir")
        opc = int(input())
