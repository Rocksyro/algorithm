import pwinput

estudiantes = [['']*9 for n in range(8)]

moderadores = [['']*9 for n in range(4)]

estudiantes[0][0] = "1"
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


def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password


def login(usuario_logueado, estudiantes):
    intentos = 0
    # Mientras el contador sea menor o igual a 3 y no este logeado
    print('LOGIN')
    print('--------------------')
    while (intentos < 3 and usuario_logueado == ''):
        print(intentos)
        # Pedir al usuario igresar usuario y contraseña
        email = input("Ingresar email: ")
        resultadoBusqueda = buscarUsuario(estudiantes, email)

        if (resultadoBusqueda != -1):
            while (intentos < 3 and usuario_logueado == ''):
                password = obtenerPassword()
                if (estudiantes[resultadoBusqueda][2] == password):
                    usuario_logueado = estudiantes[resultadoBusqueda][1]
                    print("login exitoso! usuario")
                else:
                    intentos = intentos + 1
        else:
            resultadoBusqueda = buscarUsuario(moderadores, email)

            if (resultadoBusqueda != -1):
                while (intentos < 3 and usuario_logueado == ''):
                    password = obtenerPassword()
                    if (moderadores[resultadoBusqueda][2] == password):
                        usuario_logueado = estudiantes[resultadoBusqueda][1]
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


# PROGRAMA PRINCIPAL
login('', estudiantes)
