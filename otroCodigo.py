import pwinput

# Inicialización de arrays de estudiantes y moderadores
estudiantes = [['']*9 for n in range(8)]
moderadores = [['']*9 for n in range(4)]

# Datos iniciales de prueba
estudiantes[0] = ["1", "estudiante1@ayed.com", "111222", "Pedro Castillo", "Estudiante", "date(1994, 6, 20)", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
estudiantes[1] = ["2", "estudiante2@ayed.com", "333444", "Florencia Abascal", "Estudiante", "date(2000, 4, 20)", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
estudiantes[2] = ["3", "estudiante3@ayed.com", "555666", "Raul Gimenez", "Estudiante", "date(2002, 10, 9)", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]

moderadores[0] = ["1", "moderador1@ayed.com", "111222", "Pedro Castillo", "Moderador", "date(1994, 6, 20)", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]
moderadores[1] = ["2", "moderador2@ayed.com", "333444", "Florencia Abascal", "Moderador", "date(2000, 4, 20)", "Hola esta es mi biografia", "Andar a caballo es mi hobbie", "s"]

def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password

def login(usuario_logueado, estudiantes, moderadores):
    intentos = 0
    # Mientras el contador sea menor o igual a 3 y no este logueado
    print('LOGIN')
    print('--------------------')
    while (intentos < 3 and usuario_logueado[0] == ''):
        print(intentos)
        # Pedir al usuario ingresar usuario y contraseña
        email = input("Ingresar email: ")
        resultadoBusqueda = buscarUsuario(estudiantes, email)

        if (resultadoBusqueda != -1):
            while (intentos < 3 and usuario_logueado[0] == ''):
                password = obtenerPassword()
                if (estudiantes[resultadoBusqueda][2] == password):
                    for i in range(9):
                        usuario_logueado[i] = estudiantes[resultadoBusqueda][i]  # Actualiza el usuario_logueado
                    print("login exitoso! usuario")
                else:
                    intentos += 1
        else:
            resultadoBusqueda = buscarUsuario(moderadores, email)

            if (resultadoBusqueda != -1):
                while (intentos < 3 and usuario_logueado[0] == ''):
                    password = obtenerPassword()
                    if (moderadores[resultadoBusqueda][2] == password):
                        for i in range(9):
                            usuario_logueado[i] = moderadores[resultadoBusqueda][i]  # Actualiza el usuario_logueado
                        print("login exitoso! moderador")
                    else:
                        intentos += 1
            else:
                password = obtenerPassword()
                intentos += 1

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
        if (i == 7 and a[i][0] != ''):
            return -1
    return i

def registro(array):
    i = buscarEspacioVacio(array)
    print("espacio vacio: ", i)
    if (i == -1):
        print("No hay mas espacio para registros.")
    else:
        array[i][0] = str(i + 1)
        print("Ingrese email:")
        array[i][1] = input()
        print("Ingrese contraseña:")
        array[i][2] = input()
        print("Ingrese nombre y apellido:")
        array[i][3] = input()
        array[i][4] = "Estudiante"
        array[i][8] = "s"

    for j in range(9):
        print(array[i][j])

# PROGRAMA PRINCIPAL
usuario_logueado = ['']*9 
print("1. Login")
print("2. Registro")
print("0. Salir")
opc = int(input())
while (opc != 0):
    if (opc == 1):
        login(usuario_logueado, estudiantes, moderadores)
        print(usuario_logueado)
        if(usuario_logueado[4] == "Estudiante"):
            print("menuEstudiante")
        elif(usuario_logueado[4] == "Moderador"):
            print("menuModerador")
    elif (opc == 2):
        registro(estudiantes)
    print("1. Login")
    print("2. Registro")
    print("0. Salir")
    opc = int(input())
