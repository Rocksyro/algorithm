import os
import pickle
from datetime import date, datetime
import random
import os.path
import io


class Estudiante:
    def __init__(self):
        self.id_est = 0
        self.email = ""
        self.password = ""
        self.nombre = ""
        self.sexo = ""
        self.rol = ""
        self.fecha_nacimiento = ""
        self.bio = ""
        self.hobbies = ""
        self.materia_favorita = ""
        self.deporte_favorito = ""
        self.materia_fuerte = ""
        self.materia_debil = ""
        self.pais = ""
        self.ciudad = ""
        self.activo = bool


class Moderador:
    def __init__(self):
        self.id_mod = 0
        self.email = ""
        self.password = ""
        self.activo = bool
        # Estos no están en el modelo pero los dejo por las dudas los necesitemos
        self.nombre = ""
        self.rol = ""


class Admin:
    def __init__(self):
        self.id_admin = 0
        self.email = ""
        self.password = ""
        # Estos no están en el modelo pero los dejo por las dudas los necesitemos
        self.nombre = ""
        self.rol = ""


class Likes:
    def __init__(self):
        self.remitente = 0
        self.destinatario = 0


class Reportes:
    def __init__(self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = ""
        self.estado = 0


global ArFiEstudiantes, ArFiAdministradores, ArFiModeradores, ArFiLikes, ArFiReportes, usuario_logueado

ArFiEstudiantes = "./archivos/estudiantes.txt"
ArFiAdministradores = "./archivos/administradores.txt"
ArFiModeradores = "./archivos/moderadores.txt"
ArFiLikes = "./archivos/likes.txt"
ArFiReportes = "./archivos/reportes.txt"

# ID del usuario - Tipo de usuario (0 = estudiantes, 1 = moderador, 2 = administrador)
usuario_logueado = [-1, -1]


def inicializarArchivos():
    global arLoAdministradores, arLoEstudiantes, arLoModeradores, arLoLikes, arLoReportes

    if (os.path.exists(ArFiEstudiantes)) == False:
        arLoEstudiantes = open(ArFiEstudiantes, "w+b")
        inicializarEstudiantes()
    else:
        arLoEstudiantes = open(ArFiEstudiantes, "r+b")

    if (os.path.exists(ArFiAdministradores)) == False:
        arLoAdministradores = open(ArFiAdministradores, "w+b")
        inicializarAdministradores()
    else:
        arLoAdministradores = open(ArFiAdministradores, "r+b")

    if (os.path.exists(ArFiModeradores)) == False:
        arLoModeradores = open(ArFiModeradores, "w+b")
        inicializarModeradores()
    else:
        arLoModeradores = open(ArFiModeradores, "r+b")

    if (os.path.exists(ArFiLikes)) == False:
        arLoLikes = open(ArFiLikes, "w+b")
    else:
        arLoLikes = open(ArFiLikes, "r+b")

    if (os.path.exists(ArFiReportes)) == False:
        arLoReportes = open(ArFiReportes, "w+b")
    else:
        arLoReportes = open(ArFiReportes, "r+b")


def formatearRegistroEstudiante(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")
    registro.bio = registro.bio.ljust(30, " ")
    registro.hobbies = registro.hobbies.ljust(30, " ")
    registro.materia_favorita = registro.materia_favorita.ljust(30, " ")
    registro.deporte_favorito = registro.deporte_favorito.ljust(30, " ")
    registro.materia_fuerte = registro.materia_fuerte.ljust(30, " ")
    registro.materia_debil = registro.materia_debil.ljust(30, " ")
    registro.pais = registro.pais.ljust(30, " ")
    registro.ciudad = registro.ciudad.ljust(30, " ")


def formateoModerador(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")


def formateoAdministrador(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")


def persistirRegistroEstudiante(registro, varibleLogica):
    formatearRegistroEstudiante(registro)
    varibleLogica.seek(0, 2)
    pickle.dump(registro, varibleLogica)
    varibleLogica.flush()


def persistirAdministrador(registro, variableLogica):
    formateoAdministrador(registro)
    variableLogica.seek(0, 2)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()


def persistirModerador(registro, variableLogica):
    formateoModerador(registro)
    variableLogica.seek(0, 2)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()


def inicializarModeradores():

    global arLoModeradores

    moderador1 = Moderador()
    moderador1.id_mod = 1
    moderador1.email = "m1@ayed.com"
    moderador1.password = "m123"
    moderador1.activo = "s"
    moderador1.nombre = "moderadornombre"
    moderador1.rol = "moderador"

    persistirModerador(moderador1, arLoModeradores)


def inicializarAdministradores():
    global arLoAdministradores

    administrador1 = Admin()
    administrador1.id_admin = 1
    administrador1.email = "a1@ayed.com"
    administrador1.password = "a123"
    administrador1.nombre = "nombreadministrador"
    administrador1.rol = "administrador"

    persistirAdministrador(administrador1, arLoAdministradores)


def inicializarEstudiantes():

    global arLoEstudiantes

    estudiante1 = Estudiante()
    estudiante1.email = "estudiante1@ayed.com"
    estudiante1.password = "111222"
    estudiante1.nombre = "Pedro"
    estudiante1.rol = "Estudiante"
    estudiante1.fecha_nacimiento = "1994-06-20"
    estudiante1.bio = "Hola esta es mi biografia"
    estudiante1.hobbies = "Andar a caballo es mi hobbie"
    estudiante1.activo = "s"
    estudiante1.sexo = "m"
    estudiante1.ciudad = "Rosario"
    estudiante1.deporte_favorito = "basket"
    estudiante1.id_est = 111
    estudiante1.materia_debil = "matematica"
    estudiante1.materia_favorita = "historia"
    estudiante1.materia_fuerte = "biologia"
    estudiante1.pais = "Argentina"

    persistirRegistroEstudiante(estudiante1, arLoEstudiantes)

    estudiante2 = Estudiante()
    estudiante2.email = "estudiante2@ayed.com"
    estudiante2.password = "333444"
    estudiante2.nombre = "Pedro"
    estudiante2.rol = "Estudiante"
    estudiante2.fecha_nacimiento = "1994-06-20"
    estudiante2.bio = "Hola esta es mi biografia"
    estudiante2.hobbies = "Andar a caballo es mi hobbie"
    estudiante2.activo = "s"
    estudiante2.sexo = "m"
    estudiante2.ciudad = "Rosario"
    estudiante2.deporte_favorito = "basket"
    estudiante2.id_est = 111
    estudiante2.materia_debil = "matematica"
    estudiante2.materia_favorita = "historia"
    estudiante2.materia_fuerte = "biologia"
    estudiante2.pais = "argentina"

    persistirRegistroEstudiante(estudiante2, arLoEstudiantes)

    estudiante3 = Estudiante()
    estudiante3.email = "estudiante3@ayed.com"
    estudiante3.password = "555666"
    estudiante3.nombre = "Pedro"
    estudiante3.rol = "Estudiante"
    estudiante3.fecha_nacimiento = "1994-06-20"
    estudiante3.bio = "Hola esta es mi biografia"
    estudiante3.hobbies = "Andar a caballo es mi hobbie"
    estudiante3.activo = "s"
    estudiante3.sexo = "m"
    estudiante3.ciudad = "Rosario"
    estudiante3.deporte_favorito = "basket"
    estudiante3.id_est = 111
    estudiante3.materia_debil = "matematica"
    estudiante3.materia_favorita = "historia"
    estudiante3.materia_fuerte = "biologia"
    estudiante3.pais = "argentina"

    persistirRegistroEstudiante(estudiante3, arLoEstudiantes)


def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# esta funcion se utiliza en el login


def calcularCantidadRegistros(archLogico, archFisico):
    tamArch = os.path.getsize(archFisico)
    cantReg = 0
    if (tamArch != 0):
        archLogico.seek(0, 0)
        pickle.load(archLogico)
        tamReg = archLogico.tell()
        cantReg = int(tamArch/tamReg)
    return cantReg

# esta funcion se utiliza en el login


def buscarUsuarioPorEmailyContrasenia(email, password, archLogico, archFisico):
    tamArchivo = os.path.getsize(archFisico)
    if (tamArchivo != 0):
        pos = 0
        archLogico.seek(0, 0)
        registro = pickle.load(archLogico)
        print("Email ingresado: ", email)
        print("Password ingresada: ", password)
        while ((archLogico.tell() < tamArchivo) and (registro.email != email)):
            print("Email en el archivo: ", registro.email)
            print("Password en el archivo: ", registro.password)
            pos = archLogico.tell()
            registro = pickle.load(archLogico)
            pos += 1
        if ((registro.email == email) and (registro.password == password) and (registro.activo == True)):
            return pos
        else:
            return -1

# Inicio del Login


def login():
    intentos = 0
    cantidadEstudiantes = calcularCantidadRegistros(
        arLoEstudiantes, ArFiEstudiantes)
    cantidadModeradores = calcularCantidadRegistros(
        arLoModeradores, ArFiModeradores)
    cantidadAdministradores = calcularCantidadRegistros(
        arLoAdministradores, ArFiAdministradores)

    print(f"Cantidad de Estudiantes: {cantidadEstudiantes}")
    print(f"Cantidad de Moderadores: {cantidadModeradores}")
    print(f"Cantidad de Administradores: {cantidadAdministradores}")

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 3) and (cantidadModeradores != -1 and cantidadModeradores >= 1) and (cantidadAdministradores != -1 and cantidadAdministradores >= 1)):
        # Mientras el contador sea menor o igual a 3 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == -1):
            # Pedir al usuario igresar usuario y contraseña
            email = input("Ingresar email: ")
            password = input("Ingresar password: ")
        #  password = obtenerPassword()
        estudianteBusqueda = buscarUsuarioPorEmailyContrasenia(
            email, password, arLoEstudiantes, ArFiEstudiantes)
        moderadorBusqueda = buscarUsuarioPorEmailyContrasenia(
            email, password, arLoModeradores, ArFiModeradores)
        administradorBusqueda = buscarUsuarioPorEmailyContrasenia(
            email, password, arLoAdministradores, ArFiAdministradores)
        estudianteBusqueda = buscarUsuarioPorEmailyContrasenia(email, password)

        if (estudianteBusqueda != -1):
            arLoEstudiantes.seek(estudianteBusqueda, 0)
            registroEstudiante = pickle.load(arLoEstudiantes)
            usuario_logueado[0] = registroEstudiante.id_est
            usuario_logueado[1] = 0
        elif (moderadorBusqueda != -1):
            arLoModeradores.seek(moderadorBusqueda, 0)
            registroModerador = pickle.load(arLoModeradores)
            usuario_logueado[0] = registroModerador.id_mod
            usuario_logueado[1] = 1
        elif (administradorBusqueda != -1):
            arLoAdministradores.seek(administradorBusqueda, 0)
            registroAdministradores = pickle.load(arLoAdministradores)
            usuario_logueado[0] = registroAdministradores.id_admin
            usuario_logueado[1] = 2
        else:
            intentos = intentos+1
            print("Inicio de sesion incorrecto. Quedan ",
                (3-intentos), " intentos")
            # limpiarConsola()
    else:
        print('No hay suficientes usuarios creados para el logueo')


# INICIO DEL PROGRAMA

inicializarArchivos()
# cargaUsuario()
opc = '*'
while (opc != '0'):
    print('MENU PRINCIPAL')
    print("---------------------------------------")
    print("1. Login")
    print("2. Registro")
    print("0. Salir")
    opc = input('Ingrese una opcion: ')
    limpiarConsola()
    if (opc == '1'):
        login()
#        if (usuario_logueado[1] == 0):
#            menuEstudiante()
#        elif (usuario_logueado[1] == 1):
#            menuModerador()
#    elif (opc == '2'):
#        registro(estudiantes)
    elif (opc == '0'):
        print('Saliendo del programa...')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')








def buscarDisfraz(numero):
	global arFiDisfraz
	global arLoDisfraz
	d = Disfraz()
	t = os.path.getsize(arFiDisfraz)
	pos = 0
	arLoDisfraz.seek(pos,0) 
	if t>0:
		d = pickle.load(arLoDisfraz)

	while (arLoDisfraz.tell()<t) and (int(numero) != int(d.numero)):
		pos = arLoDisfraz.tell()
		d = pickle.load(arLoDisfraz)
	if int(d.numero) == int(numero):		
		return pos
	else:
		return -1








def buscarEstudiantePorEmailYPassword(email,password):
    email=email.ljust(30," ")
    password=password.ljust(30," ")
    estudianteB = Estudiante()
    tamArchivo = os.path.getsize(ArFiEstudiantes)
    pos = 0
    arLoEstudiantes.seek(pos,0)
    #p = arLoEstudiantes.tell()
    if (tamArchivo>0):
        estudianteB = pickle.load(arLoEstudiantes)
    while ((pos < tamArchivo) and (estudianteB.email != email) and (estudianteB.password != password) ):
        print(estudianteB.email)
        print(estudianteB.password)
        pos = arLoEstudiantes.tell()
        estudianteB = pickle.load(arLoEstudiantes)
    if((estudianteB.email == email) and (estudianteB.password == password)):
        return pos
    else:
        return -1