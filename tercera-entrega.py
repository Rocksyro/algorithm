# CATEDRA: ALGORITMOS Y ESTRUCTURAS DE DATOS
# TRABAJO PRACTICO N° 3
# INTEGRANTES DEL GRUPO: Battocchio, Leandro
#                        Carle, Rocio
#                        Kopp, Brenda
#                        Urquiza, Juan
# ----------------------------------------------------------------

import pwinput # Es necesario instalar esta libreria con: 'pip install pwinput'
import os
import pickle
from datetime import date, datetime
import random
import os.path
import pwinput
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
        self.super_like = bool


class Moderador:
    def __init__(self):
        self.id_mod = 0
        self.email = ""
        self.password = ""
        self.activo = bool
        # Estos no están en el modelo pero los dejamos por las dudas los necesitemos
        self.nombre = ""
        self.rol = ""
        # Agregamos estos campos para las estadisticas del administrador
        self.ignorados = 0
        self.aceptados = 0


class Admin:
    def __init__(self):
        self.id_admin = 0
        self.email = ""
        self.password = ""
        # Estos no están en el modelo pero los dejamos por las dudas los necesitemos
        self.nombre = ""
        self.rol = ""


class Likes:
    def __init__(self):
        self.remitente = 0
        self.destinatario = 0
        self.estado = 0


class Reportes:
    def __init__(self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = ""
        self.estado = 0


global ArFiEstudiantes, ArFiAdministradores, ArFiModeradores, ArFiLikes, ArFiReportes, usuario_logueado

ArFiEstudiantes = "./estudiantes.txt"
ArFiAdministradores = "./administradores.txt"
ArFiModeradores = "./moderadores.txt"
ArFiLikes = "./likes.txt"
ArFiReportes = "./reportes.txt"

# ID del usuario - Tipo de usuario (0 = estudiantes, 1 = moderador, 2 = administrador) - Estado (0 = desactivado, 1 = activado)
usuario_logueado = [-1, -1, -1]


def cerrarArchivos():
    global ArLoAdministradores, ArLoEstudiantes, ArLoModeradores, ArLoLikes, ArLoReportes
    ArLoEstudiantes.close()
    ArLoAdministradores.close()
    ArLoReportes.close()
    ArLoLikes.close()
    ArLoModeradores.close()


def inicializarArchivos():
    global ArLoAdministradores, ArLoEstudiantes, ArLoModeradores, ArLoLikes, ArLoReportes

    # INICIALIZACION ESTUDIANTES
    if not (os.path.exists(ArFiEstudiantes)):
        ArLoEstudiantes = open(ArFiEstudiantes, "w+b")
        inicializarEstudiantes()
    else:
        ArLoEstudiantes = open(ArFiEstudiantes, "r+b")

    # INICIALIZACION ADMINISTRADORES
    if not (os.path.exists(ArFiAdministradores)):
        ArLoAdministradores = open(ArFiAdministradores, "w+b")
        inicializarAdministradores()
    else:
        ArLoAdministradores = open(ArFiAdministradores, "r+b")

    # INICIALIZACION MODERADORES
    if not (os.path.exists(ArFiModeradores)):
        ArLoModeradores = open(ArFiModeradores, "w+b")
        inicializarModeradores()
    else:
        ArLoModeradores = open(ArFiModeradores, "r+b")

    # INICIALIZACION LIKES
    if not (os.path.exists(ArFiLikes)):
        ArLoLikes = open(ArFiLikes, "w+b")
        inicializarInteracciones()
    else:
        ArLoLikes = open(ArFiLikes, "r+b")

    # INICIALIZACION REPORTES
    if not (os.path.exists(ArFiReportes)):
        ArLoReportes = open(ArFiReportes, "w+b")
    else:
        ArLoReportes = open(ArFiReportes, "r+b")


# Función para formatear los registros de estudiantes
def formatearRegistroEstudiante(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.sexo = registro.sexo.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")
    registro.fecha_nacimiento = registro.fecha_nacimiento.ljust(30, " ")
    registro.bio = registro.bio.ljust(30, " ")
    registro.hobbies = registro.hobbies.ljust(30, " ")
    registro.materia_favorita = registro.materia_favorita.ljust(30, " ")
    registro.deporte_favorito = registro.deporte_favorito.ljust(30, " ")
    registro.materia_fuerte = registro.materia_fuerte.ljust(30, " ")
    registro.materia_debil = registro.materia_debil.ljust(30, " ")
    registro.pais = registro.pais.ljust(30, " ")
    registro.ciudad = registro.ciudad.ljust(30, " ")

    return registro


# Función para formatear los registros de moderadores
def formateoModerador(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")


# Función para formatear los registros de administradores
def formateoAdministrador(registro):
    registro.email = registro.email.ljust(30, " ")
    registro.password = registro.password.ljust(30, " ")
    registro.nombre = registro.nombre.ljust(30, " ")
    registro.rol = registro.rol.ljust(30, " ")


def persistirRegistroEstudiante(registro, varibleLogica):
    registro = formatearRegistroEstudiante(registro)
    varibleLogica.seek(0, 2)
    pickle.dump(registro, varibleLogica)
    varibleLogica.flush()


def persistirAdministrador(registro, variableLogica):
    variableLogica.seek(0, 2)
    formateoAdministrador(registro)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()


def persistirModerador(registro, variableLogica):
    variableLogica.seek(0, 2)
    formateoModerador(registro)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()


def inicializarModeradores():
    global ArLoModeradores

    moderador1 = Moderador()
    moderador1.id_mod = 1
    moderador1.email = "m1@ayed.com"
    moderador1.password = "m1"
    moderador1.activo = True
    moderador1.nombre = "moderadornombre"
    moderador1.rol = "moderador"
    moderador1.ignorados = 0
    moderador1.aceptados = 0

    persistirModerador(moderador1, ArLoModeradores)

    moderador2 = Moderador()
    moderador2.id_mod = 2
    moderador2.email = "m2@ayed.com"
    moderador2.password = "m2"
    moderador2.activo = True
    moderador2.nombre = "moderadornombre2"
    moderador2.rol = "moderador"
    moderador2.ignorados = 0
    moderador2.aceptados = 0

    persistirModerador(moderador2, ArLoModeradores)


def inicializarAdministradores():
    global ArLoAdministradores

    administrador1 = Admin()
    administrador1.id_admin = 1
    administrador1.email = "a1@ayed.com"
    administrador1.password = "a1"
    administrador1.nombre = "nombreadministrador"
    administrador1.rol = "administrador"

    persistirAdministrador(administrador1, ArLoAdministradores)


def inicializarEstudiantes():
    global ArLoEstudiantes

    estudiante1 = Estudiante()
    estudiante1.email = "estudiante1@ayed.com"
    estudiante1.password = "111222"
    estudiante1.nombre = "Pedro"
    estudiante1.rol = "Estudiante"
    estudiante1.fecha_nacimiento = "1994-06-20"
    estudiante1.bio = "Soy estudiante avanzado"
    estudiante1.hobbies = "Me gusta el rock!"
    estudiante1.activo = True
    estudiante1.sexo = "m"
    estudiante1.ciudad = "Rosario"
    estudiante1.deporte_favorito = "Futbol"
    estudiante1.id_est = 1
    estudiante1.materia_debil = "Biologia"
    estudiante1.materia_favorita = "Lengua"
    estudiante1.materia_fuerte = "Ciencias Sociales"
    estudiante1.pais = "Argentina"
    estudiante1.super_like = True

    persistirRegistroEstudiante(estudiante1, ArLoEstudiantes)

    estudiante2 = Estudiante()
    estudiante2.email = "estudiante2@ayed.com"
    estudiante2.password = "333444"
    estudiante2.nombre = "Laura"
    estudiante2.rol = "Estudiante"
    estudiante2.fecha_nacimiento = "1994-06-20"
    estudiante2.bio = "Soy estudiante y me gusta leer"
    estudiante2.hobbies = "Correr, leerr novelas"
    estudiante2.activo = True
    estudiante2.sexo = "m"
    estudiante2.ciudad = "Rosario"
    estudiante2.deporte_favorito = "basket"
    estudiante2.id_est = 2
    estudiante2.materia_debil = "matematica"
    estudiante2.materia_favorita = "historia"
    estudiante2.materia_fuerte = "biologia"
    estudiante2.pais = "argentina"
    estudiante2.super_like = True

    persistirRegistroEstudiante(estudiante2, ArLoEstudiantes)

    estudiante3 = Estudiante()
    estudiante3.email = "estudiante3@ayed.com"
    estudiante3.password = "555666"
    estudiante3.nombre = "Andrea"
    estudiante3.rol = "Estudiante"
    estudiante3.fecha_nacimiento = "1994-06-20"
    estudiante3.bio = "Soy una estudiante ingresante"
    estudiante3.hobbies = "Salir los findes"
    estudiante3.activo = True
    estudiante3.sexo = "m"
    estudiante3.ciudad = "Rosario"
    estudiante3.deporte_favorito = "Ninguno"
    estudiante3.id_est = 3
    estudiante3.materia_debil = "Historia"
    estudiante3.materia_favorita = "MAtematica"
    estudiante3.materia_fuerte = "Economia"
    estudiante3.pais = "argentina"
    estudiante3.super_like = True

    persistirRegistroEstudiante(estudiante3, ArLoEstudiantes)

    estudiante4 = Estudiante()
    estudiante4.email = "estudiante4@ayed.com"
    estudiante4.password = "777888"
    estudiante4.nombre = "Jose"
    estudiante4.rol = "Estudiante"
    estudiante4.fecha_nacimiento = "1994-06-20"
    estudiante4.bio = "Trabajo en un bar"
    estudiante4.hobbies = "Comer asado con amigos"
    estudiante4.activo = True
    estudiante4.sexo = "m"
    estudiante4.ciudad = "San nicolas"
    estudiante4.deporte_favorito = "Basket"
    estudiante4.id_est = 4
    estudiante4.materia_debil = "Lengua"
    estudiante4.materia_favorita = "Ed fisica"
    estudiante4.materia_fuerte = "Ed fisica"
    estudiante4.pais = "Argentina"
    estudiante4.super_like = True

    persistirRegistroEstudiante(estudiante4, ArLoEstudiantes)

    estudiante5 = Estudiante()
    estudiante5.email = "estudiante5@ayed.com"
    estudiante5.password = "999"
    estudiante5.nombre = "KIKO"
    estudiante5.rol = "Estudiante"
    estudiante5.fecha_nacimiento = "1994-06-20"
    estudiante5.bio = "Soy estudiante intermedio"
    estudiante5.hobbies = "Comer asado con amigos"
    estudiante5.activo = True
    estudiante5.sexo = "m"
    estudiante5.ciudad = "San nicolas"
    estudiante5.deporte_favorito = "Basket"
    estudiante5.id_est = 5
    estudiante5.materia_debil = "Lengua"
    estudiante5.materia_favorita = "Ed fisica"
    estudiante5.materia_fuerte = "Ed fisica"
    estudiante5.pais = "Argentina"
    estudiante5.super_like = True

    persistirRegistroEstudiante(estudiante5, ArLoEstudiantes)


def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')


def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password


def calcularCantidadRegistros(archLogico, archFisico):
    tamArch = os.path.getsize(archFisico)
    cantReg = 0
    if (tamArch != 0):
        archLogico.seek(0, 0)
        aux = pickle.load(archLogico)
        tamReg = archLogico.tell()
        cantReg = int(tamArch/tamReg)
    return cantReg


def buscarEstudiantePorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    regEstudiante = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    pos = ArLoEstudiantes.tell()
    regEstudiante = pickle.load(ArLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)

    while ((email != regEstudiante.email) and (password != regEstudiante.password) and (ArLoEstudiantes.tell() < tamArchivo)):
        pos = ArLoEstudiantes.tell()
        regEstudiante = pickle.load(ArLoEstudiantes)

    if (email == regEstudiante.email) and (password == regEstudiante.password):
        return pos
    else:
        return -1


def buscarUsuarioPorNombre(nombre):
    regEstudiante = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    pos = ArLoEstudiantes.tell()
    regEstudiante = pickle.load(ArLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)

    while ((nombre != regEstudiante.nombre) and (ArLoEstudiantes.tell() < tamArchivo)):

        pos = ArLoEstudiantes.tell()
        regEstudiante = pickle.load(ArLoEstudiantes)

    if nombre == regEstudiante.nombre:
        return (pos)
    else:
        return -1


def mostrarLikes():
    e = Likes()
    ArLoLikes.seek(0, 0)
    tamArch = os.path.getsize(ArFiLikes)

    print("LIKES")
    print("----------------------------")
    while (ArLoLikes.tell() < tamArch):
        e = pickle.load(ArLoLikes)
        print("Destinatario: ", e.destinatario)
        print("Remitente: ", e.remitente)
        print("Estado: ", e.estado)


def inicializarInteracciones():
    cantidadEstudiantes = calcularCantidadRegistros(
        ArLoEstudiantes, ArFiEstudiantes)

    ArLoLikes.seek(0, 0)

    for i in range(1, cantidadEstudiantes + 1):
        for j in range(1, cantidadEstudiantes + 1):
            registroLike = Likes()

            daLike = random.randint(0, 1)

            if i != j:
                registroLike.destinatario = j
                registroLike.remitente = i
                registroLike.estado = daLike
                pickle.dump(registroLike, ArLoLikes)
                ArLoLikes.flush()


def buscarUsuarioPorNombreYDevolverID(nombre):
    regEstudiante = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    pos = ArLoEstudiantes.tell()
    regEstudiante = pickle.load(ArLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)

    while ((nombre != regEstudiante.nombre) and (ArLoEstudiantes.tell() < tamArchivo)):
        pos = ArLoEstudiantes.tell()
        regEstudiante = pickle.load(ArLoEstudiantes)

    if nombre == regEstudiante.nombre:
        return (regEstudiante.id_est)
    else:
        return -1


def buscarModeradorPorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    regModerador = Moderador()
    ArLoModeradores.seek(0, 0)
    pos = ArLoModeradores.tell()
    regModerador = pickle.load(ArLoModeradores)
    tamArchivo = os.path.getsize(ArFiModeradores)

    while ((email != regModerador.email) and (password != regModerador.password) and (ArLoModeradores.tell() < tamArchivo)):
        pos = ArLoModeradores.tell()
        regModerador = pickle.load(ArLoModeradores)

    if (email == regModerador.email) and (password == regModerador.password):
        return pos
    else:
        return -1


def buscarAdministradorPorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    regAdministrador = Admin()
    ArLoAdministradores.seek(0, 0)
    pos = ArLoAdministradores.tell()
    regAdministrador = pickle.load(ArLoAdministradores)
    tamArchivo = os.path.getsize(ArFiAdministradores)

    while ((email != regAdministrador.email) and (password != regAdministrador.password) and (ArLoAdministradores.tell() < tamArchivo)):
        pos = ArLoAdministradores.tell()
        regAdministrador = pickle.load(ArLoAdministradores)

    if (email == regAdministrador.email) and (password == regAdministrador.password):
        return pos
    else:
        return -1


def tamanioRegistro(archivo):
    archivo.seek(0, 0)
    aux = pickle.load(archivo)
    tamanioRegistro = archivo.tell()
    return tamanioRegistro


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


# Inicio del Login
def login():
    intentos = 0
    cantidadEstudiantes = calcularCantidadRegistros(
        ArLoEstudiantes, ArFiEstudiantes)
    cantidadModeradores = calcularCantidadRegistros(
        ArLoModeradores, ArFiModeradores)
    cantidadAdministradores = calcularCantidadRegistros(
        ArLoAdministradores, ArFiAdministradores)

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 4) and (cantidadModeradores != -1 and cantidadModeradores >= 1) and (cantidadAdministradores != -1 and cantidadAdministradores >= 1)):
        # Mientras el contador sea menor o igual a 4 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == -1):
            email = input("Ingresar email: ")
            password = obtenerPassword()

            administradorBusqueda = buscarAdministradorPorEmailYPassword(
                email, password)
            moderadorBusqueda = buscarModeradorPorEmailYPassword(
                email, password)
            estudianteBusqueda = buscarEstudiantePorEmailYPassword(
                email, password)

            if (estudianteBusqueda != -1):
                ArLoEstudiantes.seek(estudianteBusqueda, 0)
                registroEstudiante = pickle.load(ArLoEstudiantes)

                if (registroEstudiante.activo == False):
                    intentos = 3
                    usuario_logueado[1] = -2
                    print("Usuario desactivado.")
                else:
                    usuario_logueado[0] = registroEstudiante.id_est
                    usuario_logueado[1] = 0
                    limpiarConsola()
            elif (moderadorBusqueda != -1):
                ArLoModeradores.seek(moderadorBusqueda, 0)
                registroModerador = pickle.load(ArLoModeradores)

                if (registroModerador.activo == False):
                    intentos = 3
                    usuario_logueado[1] = -2
                    print("Usuario desactivado.")
                else:
                    usuario_logueado[0] = registroModerador.id_mod
                    usuario_logueado[1] = 1
                limpiarConsola()
            elif (administradorBusqueda != -1):
                ArLoAdministradores.seek(administradorBusqueda, 0)
                registroAdministradores = pickle.load(ArLoAdministradores)
                usuario_logueado[0] = registroAdministradores.id_admin
                usuario_logueado[1] = 2
                limpiarConsola()
            else:
                intentos = intentos+1
                print("Inicio de sesion incorrecto. Quedan ",
                      (3-intentos), " intentos")
    else:
        print('No hay suficientes usuarios creados para el logueo')


def reportarCandidatos():
    print("MENU REPORTAR")
    usuario_encontrado = -1
    opc = input(
        '1. Por ID \n2. Por Nombre \nIngrese la forma que quiere reportar: ')
    while (opc != "1" and opc != "2"):
        opc = input(
            '1. Por ID \n2. Por Nombre \nIngrese la forma que quiere reportar: ')
    if (opc == "1"):
        try:
            estudiante_reportado = int(
                input('Ingrese la ID del estudiante a reportar: '))
            usuario_encontrado = buscarEstudiantePorId(estudiante_reportado)
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_reportado = input(
            "Ingrese el nombre del estudiante a reportar: ")
        estudiante_reportado = estudiante_reportado.ljust(30, " ")
        usuario_encontrado = buscarUsuarioPorNombre(estudiante_reportado)

    if (usuario_encontrado != -1):
        ArLoEstudiantes.seek(usuario_encontrado, 0)
        registroUsuarioEncontrado = pickle.load(ArLoEstudiantes)

        if (registroUsuarioEncontrado.id_est == usuario_logueado[0]):
            limpiarConsola()
            print('No podes reportarte a vos mismo.')
        else:
            motivo = input('Ingrese el motivo del reporte: ')
            registroReporte = Reportes()

            registroReporte.estado = 0

            registroReporte.razon_reporte = motivo
            registroReporte.razon_reporte = registroReporte.razon_reporte.ljust(
                30, " ")

            registroReporte.id_reportado = registroUsuarioEncontrado.id_est
            registroReporte.id_reportante = usuario_logueado[0]

            ArLoReportes.seek(0, 2)
            pickle.dump(registroReporte, ArLoReportes)
            ArLoReportes.flush()
            limpiarConsola()
    else:
        limpiarConsola()
        print("Usuario no encontrado o Ingresaste dato inválido")


def calcularEdad(fecha_nacimiento):

    fecha_nac = datetime.strptime(fecha_nacimiento.strip(), "%Y-%m-%d")
    hoy = datetime.today()
    # Calcular la diferencia de años
    edad = hoy.year - fecha_nac.year
    # Ajustar si no ha cumplido años este año
    if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
    return edad


def meGusta(id):
    tamArchvoLikes = os.path.getsize(ArFiLikes)
    ArLoLikes.seek(0, 0)
    bandera = False

    registroLike = Likes()
    registroLike = pickle.load(ArLoLikes)

    while (bandera == False) and (ArLoLikes.tell() < tamArchvoLikes):
        if ((id == registroLike.destinatario) and (usuario_logueado[0] == registroLike.remitente) and (registroLike.estado == 1)):
            bandera = True
        registroLike = pickle.load(ArLoLikes)

    return bandera


def mostrarEstudiantes():
    e = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    tamArch = os.path.getsize(ArFiEstudiantes)
    print("ESTUDIANTES")
    print("----------------------------")
    while (ArLoEstudiantes.tell() < tamArch):
        e = pickle.load(ArLoEstudiantes)
        if ((e.activo == True) and (e.id_est != usuario_logueado[0])):
            like = meGusta(e.id_est)
            print("Id: ", e.id_est)
            print("Nombre: ", e.nombre, '- ♡' if like else '')
            print("Fecha de Nacimiento: ", e.fecha_nacimiento)
            print("Edad", calcularEdad(e.fecha_nacimiento))
            print("Biografia: ", e.bio)
            print("Hobbies: ", e.hobbies)
            print("----------------------------")


def mostrarEstudiantesAdministrador():
    e = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    tamArch = os.path.getsize(ArFiEstudiantes)
    print("ESTUDIANTES")
    print("----------------------------")
    while (ArLoEstudiantes.tell() < tamArch):
        e = pickle.load(ArLoEstudiantes)

        if (e.activo):
            print('ID: ', e.id_est)
            print("Nombre: ", e.nombre)
            print("Fecha de Nacimiento: ", e.fecha_nacimiento)
            print("Edad", calcularEdad(e.fecha_nacimiento))
            print("Biografia: ", e.bio)
            print("Hobbies: ", e.hobbies)
            print("----------------------------")


def mostrarModeradoresAdministrador():
    moderador = Moderador()
    ArLoModeradores.seek(0, 0)
    tamArch = os.path.getsize(ArFiModeradores)
    print("MODERADORES")
    print("----------------------------")
    while (ArLoModeradores.tell() < tamArch):
        moderador = pickle.load(ArLoModeradores)

        if (moderador.activo):
            print("ID: ", moderador.id_mod)
            print('Nombre: ', moderador.nombre)
            print("Email: ", moderador.email)
            print("Activo: ", moderador.activo)
            print("----------------------------")


def buscarLike(rem, dest):
    l = Likes()
    ArLoLikes.seek(0, 0)
    tamReg = tamanioRegistro(ArLoLikes)
    pos = -1
    while (ArLoLikes.tell() < os.path.getsize(ArFiLikes)):
        l = pickle.load(ArLoLikes)
        if (l.remitente == rem and l.destinatario == dest):
            pos = ArLoLikes.tell()
    return pos-tamReg


def verCandidatos():
    mostrarEstudiantes()
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
        me_gusta = me_gusta.ljust(30, " ")
        idDestinatario = buscarUsuarioPorNombreYDevolverID(me_gusta)

        if (idDestinatario != -1):
            posLike = buscarLike(usuario_logueado[0], idDestinatario)

            usarSuperLike = False
            posLogueado = buscarEstudiantePorId(usuario_logueado[0])
            ArLoEstudiantes.seek(posLogueado, 0)
            estudianteLogueado = pickle.load(ArLoEstudiantes)

            if (estudianteLogueado.super_like):
                superLike = input(
                    'Desea utilizar el super like S/N? ').capitalize()

                while superLike != 'S' and superLike != 'N':
                    print('No ha ingresado una opcion correcta.')
                    superLike = input(
                        'Desea utilizar el super like S/N? ').capitalize()

                if (superLike == 'S'):
                    usarSuperLike = True

            like = Likes()
            ArLoLikes.seek(posLike, 0)
            like = pickle.load(ArLoLikes)

            if like.estado == 0:

                if (usarSuperLike):
                    like = Likes()
                    ArLoLikes.seek(posLike, 0)
                    like = pickle.load(ArLoLikes)

                    like.estado = 1
                    ArLoLikes.seek(posLike, 0)
                    pickle.dump(like, ArLoLikes)
                    ArLoLikes.flush()

                    posLike = buscarLike(idDestinatario, usuario_logueado[0])
                    ArLoLikes.seek(posLike, 0)
                    like = pickle.load(ArLoLikes)

                    like.estado = 1

                    ArLoLikes.seek(posLike, 0)
                    pickle.dump(like, ArLoLikes)
                    ArLoLikes.flush()

                    estudianteLogueado.super_like = False
                    ArLoEstudiantes.seek(posLogueado, 0)
                    pickle.dump(estudianteLogueado, ArLoEstudiantes)
                    ArLoEstudiantes.flush()

                else:
                    like.estado = 1
                    ArLoLikes.seek(posLike, 0)
                    pickle.dump(like, ArLoLikes)
                    ArLoLikes.flush()
            else:
                like.estado = 0

            ArLoLikes.seek(posLike, 0)
            pickle.dump(like, ArLoLikes)
            ArLoLikes.flush()
            limpiarConsola()
            print('Le has dado like a: ', me_gusta)

        else:
            print('No se ha ingresado un nombre de estudiante valido. \n---------------')
    else:
        limpiarConsola()


def matcheosMutuos():

    registro = Likes()
    ArLoLikes.seek(0, 0)
    pos = ArLoLikes.tell()
    registro = pickle.load(ArLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)
    acum = 0

    while (ArLoLikes.tell() < tamArchivo):
        if (registro.remitente == usuario_logueado[0] and registro.estado == 1):
            posInvertida = buscarLike(
                registro.destinatario, usuario_logueado[0])
            ArLoLikes.seek(posInvertida, 0)
            registro = pickle.load(ArLoLikes)
            if (registro.estado == 1):
                acum = acum+1
        ArLoLikes.seek(pos, 0)

        registro = pickle.load(ArLoLikes)
        pos = ArLoLikes.tell()

    cantidadEstudiantes = calcularCantidadRegistros(
        ArLoEstudiantes, ArFiEstudiantes)

    return (acum*100/cantidadEstudiantes)


def meGustaNoDevueltos():
    registro = Likes()
    ArLoLikes.seek(0, 0)
    pos = ArLoLikes.tell()
    registro = pickle.load(ArLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)
    acum = 0

    while (ArLoLikes.tell() < tamArchivo):
        if (registro.remitente == usuario_logueado[0] and registro.estado == 1):
            posInvertida = buscarLike(
                registro.destinatario, usuario_logueado[0])
            ArLoLikes.seek(posInvertida, 0)
            registro = pickle.load(ArLoLikes)
            if (registro.estado == 0):
                acum = acum+1
        ArLoLikes.seek(pos, 0)

        registro = pickle.load(ArLoLikes)
        pos = ArLoLikes.tell()

    return acum


def leGustoYNoMeGusta():
    registro = Likes()
    ArLoLikes.seek(0, 0)
    pos = ArLoLikes.tell()
    registro = pickle.load(ArLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)
    acum = 0

    while (ArLoLikes.tell() < tamArchivo):
        if (registro.remitente == usuario_logueado[0] and registro.estado == 0):
            posInvertida = buscarLike(
                registro.destinatario, usuario_logueado[0])
            ArLoLikes.seek(posInvertida, 0)
            registro = pickle.load(ArLoLikes)
            if (registro.estado == 1):
                acum = acum+1
        ArLoLikes.seek(pos, 0)

        registro = pickle.load(ArLoLikes)
        pos = ArLoLikes.tell()

    return acum


def opMenuEstudiante(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar mi perfil \n--------------- \na.Editar mis datos personales \nb.Eliminar mi perfil \nc.Volver")
            letra_op = input("Ingrese a, b o c: ").capitalize()
            limpiarConsola()
            if letra_op == "A":
                editarPerfil()
            elif letra_op == "B":
                desactivarPerfil()
            elif letra_op == "C":
                volver_principal = True
            else:
                print('No has ingresado una opcion valida!')
                print('---------------')
            if (usuario_logueado[2] == 0):
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
        print("Matcheos\n--------------- \nEn construcción\n---------------")
        num_subOp = int(input("Presione 0 para volver: "))
        if num_subOp == 0:
            volver_principal = True
        else:
            print('No has ingresado una opcion valida!')
            print('---------------')
            limpiarConsola()
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
            num_subOp = input("Presione S para volver: ")
            if num_subOp == "S":
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


def menuEstudiante():
    num_op = ''
    while (num_op != '0'):
        menu_principal = "MENU ESTUDIANTE \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenuEstudiante(num_op)

        if (usuario_logueado[2] == 0):
            num_op = '0'
            usuario_logueado[0] = -1
            usuario_logueado[1] = -1


def buscarEstudiantePorId(id):
    regEstudiante = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    pos = ArLoEstudiantes.tell()
    regEstudiante = pickle.load(ArLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)

    while ((id != regEstudiante.id_est) and (ArLoEstudiantes.tell() < tamArchivo)):
        pos = ArLoEstudiantes.tell()
        regEstudiante = pickle.load(ArLoEstudiantes)

    if id == regEstudiante.id_est:
        return (pos)
    else:
        return -1


def buscarModeradorPorId(id):
    regModerador = Moderador()
    ArLoModeradores.seek(0, 0)
    pos = ArLoModeradores.tell()
    regModerador = pickle.load(ArLoModeradores)
    tamArchivo = os.path.getsize(ArFiModeradores)

    while ((id != regModerador.id_mod) and (ArLoModeradores.tell() < tamArchivo)):
        pos = ArLoModeradores.tell()
        regModerador = pickle.load(ArLoModeradores)

    if id == regModerador.id_mod:
        return (pos)
    else:
        return -1


def editarPerfil():
    print("Editar perfil")
    print('----------------')
    # el estudiante logueado deberá poder modificar la información ingresada para su fecha de nacimiento, biografía, hobbies y cualquier otro campo que crean relevante.
    opEdit = input(
        "1.Fecha \n2.Biografía \n3.Hobbies \n4.Materia favorita \n5.Deporte favorito \n0.Volver \nIngresar qué dato quiere editar (sólo número): ")
    limpiarConsola()
    registroAlumno = Estudiante()

    while (opEdit != '0'):
        if (opEdit == "1"):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno = pickle.load(ArLoEstudiantes)
                registroAlumno.fecha_nacimiento = pedirFecha()
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno.fecha_nacimiento = registroAlumno.fecha_nacimiento.ljust(
                    30, " ")
                print(registroAlumno.fecha_nacimiento)
                pickle.dump(registroAlumno, ArLoEstudiantes)
                ArLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == "2"):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno = pickle.load(ArLoEstudiantes)
                registroAlumno.bio = input("Agregar nueva Biografia: ")
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno.bio = registroAlumno.bio.ljust(30, " ")
                pickle.dump(registroAlumno, ArLoEstudiantes)
                ArLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == '3'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno = pickle.load(ArLoEstudiantes)
                registroAlumno.hobbies = input("Agregar nuevos hobbies: ")
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno.hobbies = registroAlumno.hobbies.ljust(30, " ")
                pickle.dump(registroAlumno, ArLoEstudiantes)
                ArLoEstudiantes.flush()
        elif (opEdit == '4'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno = pickle.load(ArLoEstudiantes)
                registroAlumno.materia_favorita = input(
                    "Agregar nueva materia favorita: ")
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno.materia_favorita = registroAlumno.materia_favorita.ljust(
                    30, " ")
                pickle.dump(registroAlumno, ArLoEstudiantes)
                ArLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == '5'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno = pickle.load(ArLoEstudiantes)
                registroAlumno.deporte_favorito = input(
                    "Agregar nuevo deporte favorito: ")
                ArLoEstudiantes.seek(posEstudiante, 0)
                registroAlumno.deporte_favorito = registroAlumno.deporte_favorito.ljust(
                    30, " ")
                pickle.dump(registroAlumno, ArLoEstudiantes)
                ArLoEstudiantes.flush()
            limpiarConsola()
        else:
            print('No has elegido una opcion valida.')
            print('------------------------')
        print("Datos personales \n---------------\nFecha: ", registroAlumno.fecha_nacimiento, "\nBiografía: ", registroAlumno.bio, "\nHobbies: ",
              registroAlumno.hobbies, "\nMateria favorita: ", registroAlumno.materia_favorita, "\nDeporte favorito: ", registroAlumno.deporte_favorito, '\n---------------')
        opEdit = input(
            "1.Fecha \n2.Biografía \n3.Hobbies \n4.Materia favorita \n5.Deporte favorito \n0.Volver \nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()
    print("Datos personales \n---------------\nFecha: ", registroAlumno.fecha_nacimiento,  "\nBiografía: ", registroAlumno.bio, "\nHobbies: ",
          registroAlumno.hobbies, "\nMateria favorita: ", registroAlumno.materia_favorita, "\nDeporte favorito: ", registroAlumno.deporte_favorito)


def desactivarPerfil():
    opc = ''
    while (opc != 'S' and opc != 'N'):
        print('ATENCION')
        print('--------------------')
        opc = input(
            'Esta apunto de inhabilitar su perfil, esta seguro de esta accion? S/N: ').capitalize()

        if (opc != 'S' and opc != 'N'):
            limpiarConsola()
            print('No ha ingresado una opcion valida, vuelva a intentar!')
    if (opc == 'S'):
        registroEstudiante = Estudiante()
        posEstudiante = buscarEstudiantePorId(usuario_logueado[0])

        ArLoEstudiantes.seek(posEstudiante, 0)
        registroEstudiante = pickle.load(ArLoEstudiantes)
        registroEstudiante.activo = False

        ArLoEstudiantes.seek(posEstudiante, 0)
        pickle.dump(registroEstudiante, ArLoEstudiantes)
        ArLoEstudiantes.flush()
        # limpiarConsola()
        print('Usuario desactivado')
        usuario_logueado[2] = 0
    else:
        limpiarConsola()


def desactivarEstudiante():
    print('DESACTIVAR ESTUDIANTES')
    print('------------------')
    usuario_encontrado = -1
    opc = input(
        '1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere desactivar al usuario: ')
    while (opc != "1" and opc != "2"):
        opc = input(
            '1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere reportar: ')
    if (opc == "1"):
        try:
            estudiante_desactivar = int(
                input('Ingrese la ID del estudiante a reportar: '))
            usuario_encontrado = buscarEstudiantePorId(estudiante_desactivar)
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_desactivar = input(
            "Ingrese el nombre del estudiante a reportar: ")
        estudiante_desactivar = estudiante_desactivar.ljust(30, " ")
        usuario_encontrado = buscarUsuarioPorNombre(estudiante_desactivar)

    if (usuario_encontrado != -1):
        ArLoEstudiantes.seek(usuario_encontrado, 0)
        registroUsuarioEncontrado = pickle.load(ArLoEstudiantes)
        registroUsuarioEncontrado.activo = False
        ArLoEstudiantes.seek(usuario_encontrado, 0)
        pickle.dump(registroUsuarioEncontrado, ArLoEstudiantes)
        ArLoEstudiantes.flush()
        print("Estudiante desactivado con exito")
        print("------------")
    else:
        limpiarConsola()
        print("Usuario no encontrado o Ingresaste dato inválido")


def buscarModeradorPorId(id):
    m = Moderador()
    ArLoModeradores.seek(0, 0)
    pos = ArLoModeradores.tell()
    m = pickle.load(ArLoModeradores)
    tamArchivo = os.path.getsize(ArFiModeradores)

    while ((id != m.id_mod) and (ArLoModeradores.tell() < tamArchivo)):
        pos = ArLoModeradores.tell()
        m = pickle.load(ArLoModeradores)

    if id == m.id_mod:
        return (pos)
    else:
        return -1


def sumarReporteAceptadoModerador():
    m = Moderador()
    pos = buscarModeradorPorId(usuario_logueado[0])
    ArLoModeradores.seek(pos, 0)
    m = pickle.load(ArLoModeradores)
    m.aceptados = m.aceptados + 1
    ArLoModeradores.seek(pos, 0)

    pickle.dump(m, ArLoModeradores)
    ArLoModeradores.flush()


def sumarReporteIgnoradoModerador():
    m = Moderador()
    pos = buscarModeradorPorId(usuario_logueado[0])
    ArLoModeradores.seek(pos, 0)
    m = pickle.load(ArLoModeradores)
    m.ignorados = m.ignorados + 1
    ArLoModeradores.seek(pos, 0)
    pickle.dump(m, ArLoModeradores)
    ArLoModeradores.flush()


def verReportes():

    ArLoReportes.seek(0, 0)
    aux = pickle.load(ArLoReportes)
    tamReg = ArLoReportes.tell()

    i = 0
    r = Reportes()
    ArLoReportes.seek(0, 0)
    tamArch = os.path.getsize(ArFiReportes)

    hayReportes = False

    while ArLoReportes.tell() < tamArch:
        auxReporte = pickle.load(ArLoReportes)

        remitente_pos = buscarEstudiantePorId(auxReporte.id_reportante)
        destinatario_pos = buscarEstudiantePorId(auxReporte.id_reportado)

        if (remitente_pos != (-1) and destinatario_pos != (-1)):

            ArLoEstudiantes.seek(remitente_pos, 0)
            remitente = pickle.load(ArLoEstudiantes)
            ArLoEstudiantes.seek(destinatario_pos, 0)
            destinatario = pickle.load(ArLoEstudiantes)

        if (auxReporte.estado == 0 and remitente.activo and destinatario.activo):
            hayReportes = True

    ArLoReportes.seek(0, 0)

    if (tamArch != 0 and hayReportes):
        print("REPORTES")
        print("----------------------------")
        while (ArLoReportes.tell() < tamArch):
            r = pickle.load(ArLoReportes)
            remitente_pos = buscarEstudiantePorId(r.id_reportante)
            destinatario_pos = buscarEstudiantePorId(r.id_reportado)

            if (remitente_pos != (-1) and destinatario_pos != (-1)):

                ArLoEstudiantes.seek(remitente_pos, 0)
                remitente = pickle.load(ArLoEstudiantes)
                ArLoEstudiantes.seek(destinatario_pos, 0)
                destinatario = pickle.load(ArLoEstudiantes)

                if (r.estado == 0 and remitente.activo and destinatario.activo):
                    print("Reporte n° ", i + 1)
                    print("Estudiante Reportante - ID ",
                          remitente.id_est, " NOMBRE ", remitente.nombre)
                    print("Estudiante Reportado - ID ",
                          destinatario.id_est, " NOMBRE ", destinatario.nombre)
                    print("Razon del reporte: ", r.razon_reporte)
                    print("----------------------------")
            i += 1
        # El usuario elige el numero de reporte al que desea acceder.
        eleccion = int(
            input('Ingrese el numero de reporte al que desea acceder: '))
        cantidadReportes = calcularCantidadRegistros(
            ArLoReportes, ArFiReportes)

        # Se hace una validacion para que el numero elegido este entre los propuestos.
        while (eleccion < 1 or eleccion > cantidadReportes):
            print('No has ingresado un numero de reporte correcto, vuelve a intentar.')
            eleccion = int(input(
                'Ingrese el numero de reporte al que desea acceder: '))
        # Se verifica que el reporte elegido sea valido, ambos usuarios activos, y reporte no visto.
        posReporteElegido = (eleccion - 1) * tamReg

        ArLoReportes.seek(posReporteElegido, 0)
        reporteElegido = pickle.load(ArLoReportes)

        remitente_pos = buscarEstudiantePorId(reporteElegido.id_reportante)
        destinatario_pos = buscarEstudiantePorId(reporteElegido.id_reportado)

        if (remitente_pos != -1 and destinatario_pos != -1):
            ArLoEstudiantes.seek(remitente_pos, 0)
            remitente = pickle.load(ArLoEstudiantes)
            ArLoEstudiantes.seek(destinatario_pos, 0)
            destinatario = pickle.load(ArLoEstudiantes)

            if (reporteElegido.estado == 0 and remitente.activo and destinatario.activo):
                print("Reporte n° ", eleccion)
                print("Estudiante Reportante - ID ",
                      remitente.id_est, " NOMBRE ", remitente.nombre)
                print("Estudiante Reportado - ID ", destinatario.id_est,
                      " NOMBRE ", destinatario.nombre)
                print("Razon del reporte: ", reporteElegido.razon_reporte)
                print("----------------------------")

                eleccion = input(
                    'Desea actuar sobre el reporte (A) o ignorarlo (I)? A/I: ').capitalize()

                while (eleccion != 'A' and eleccion != 'I'):
                    print('No ha elegido una opcion correcta, vuelva a intentar.')
                    eleccion = input(
                        'Desea actuar sobre el reporte (A) o ignorarlo (I)? A/I: ').capitalize()

                if (eleccion == 'A'):
                    reporteElegido.estado = 1
                    destinatario.activo = False
                    sumarReporteAceptadoModerador()
                    ArLoReportes.seek(posReporteElegido, 0)
                    pickle.dump(reporteElegido, ArLoReportes)

                    ArLoEstudiantes.seek(destinatario_pos, 0)
                    pickle.dump(destinatario, ArLoEstudiantes)

                    ArLoEstudiantes.flush()
                else:
                    reporteElegido.estado = 2
                    sumarReporteIgnoradoModerador()
                    ArLoReportes.seek(posReporteElegido, 0)
                    pickle.dump(reporteElegido, ArLoReportes)

                ArLoReportes.flush()
            else:
                print('Error al ingresar numero de reporte.')
        else:
            print('Error al ingresar numero de reporte.')
    else:
        print('No hay reportes para mostrar.')


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
        print("Reportes estadísticos\n--------------- \nEn construcción\n---------------")
        num_subOp = int(input("Presione 0 para volver: "))
        if num_subOp == 0:
            volver_principal = True
    elif num_op == "0":
        print('Se deslogueo correctamente.')
        usuario_logueado[0] = -1
        usuario_logueado[1] = -1
    else:
        print('No ha ingresado una opcion valida')
        print('------------------------')


def menuModerador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU MODERADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n0. Volver"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 0): ")
        limpiarConsola()
        opMenuModerador(num_op)


def menuAdministrador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU ADMINISTRADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuAdministrador(num_op)


def eliminarUsuario():
    eleccion1 = input(
        'Desea eliminar un estudiante (E) o moderador (M)?').capitalize()

    while (eleccion1 != 'E' and eleccion1 != "M"):
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        eleccion1 = input(
            'Desea eliminar un estudiante (E) o moderador (M)?').capitalize()

    if (eleccion1 == 'E'):

        cantEstudiantes = calcularCantidadRegistros(
            ArLoEstudiantes, ArFiEstudiantes)

        mostrarEstudiantesAdministrador()

        eleccion2 = int(
            input('Ingrese la ID del estudiante que desea eliminar: '))

        while (eleccion2 < 1 or eleccion2 > cantEstudiantes):
            print('No ha ingresado una opcion valida, vuelva a intentar.')
            eleccion2 = int(
                input('Ingrese la ID del estudiante que desea eliminar: '))

        posEstudianteElegido = buscarEstudiantePorId(eleccion2)

        ArLoEstudiantes.seek(posEstudianteElegido, 0)
        estudianteElegido = pickle.load(ArLoEstudiantes)

        estudianteElegido.activo = False

        ArLoEstudiantes.seek(posEstudianteElegido, 0)
        pickle.dump(estudianteElegido, ArLoEstudiantes)
        ArLoEstudiantes.flush()
    else:
        cantModeradores = calcularCantidadRegistros(
            ArLoModeradores, ArFiModeradores)

        mostrarModeradoresAdministrador()

        eleccion2 = int(
            input('Ingrese la ID del moderador que desea eliminar: '))

        while (eleccion2 < 1 or eleccion2 > cantModeradores):
            print('No ha ingresado una opcion valida, vuelva a intentar.')
            eleccion2 = int(
                input('Ingrese la ID del moderador que desea eliminar: '))

        posModeradorElegido = buscarModeradorPorId(eleccion2)

        ArLoModeradores.seek(posModeradorElegido, 0)
        moderadorElegido = pickle.load(ArLoModeradores)

        moderadorElegido.activo = False

        ArLoModeradores.seek(posModeradorElegido, 0)
        pickle.dump(moderadorElegido, ArLoModeradores)
        ArLoModeradores.flush()


def buscarModeradorPorEmail(email):
    m = Moderador()
    ArLoModeradores.seek(0, 0)
    bandera = False
    email = email.ljust(30, " ")
    while (ArLoModeradores.tell() < os.path.getsize(ArFiModeradores)):
        m = pickle.load(ArLoModeradores)
        if (m.email == email):
            bandera = True
    return bandera


def darAltaModerador():
    moderador = Moderador()
    cantidadModerador = calcularCantidadRegistros(
        ArLoModeradores, ArFiModeradores)

    moderador.id_mod = cantidadModerador + 1
    moderador.email = input('Ingrese email del nuevo mod: ')
    while (buscarModeradorPorEmail(moderador.email) == True):
        print("El email ya existe. Vuelva a ingresar otro")
        moderador.email = input('Ingrese email del nuevo mod: ')
    moderador.password = input('Ingrese password del nuevo mod: ')
    moderador.nombre = input('Ingrese nombre del nuevo mod: ')
    moderador.activo = True
    moderador.rol = "moderador"
    moderador.ignorados = 0
    moderador.aceptados = 0

    formateoModerador(moderador)

    ArLoModeradores.seek(0, 2)
    pickle.dump(moderador, ArLoModeradores)
    ArLoModeradores.flush()


def calcularCantidadReportesIgnorados():
    r = Reportes()
    ArLoReportes.seek(0, 0)
    acum = 0
    while (ArLoReportes.tell() < os.path.getsize(ArFiReportes)):
        r = pickle.load(ArLoReportes)
        if (r.estado == 2):
            acum = acum + 1
    return acum


def calcularCantidadReportesAceptados():
    r = Reportes()
    ArLoReportes.seek(0, 0)
    acum = 0
    while (ArLoReportes.tell() < os.path.getsize(ArFiReportes)):
        r = pickle.load(ArLoReportes)
        if (r.estado == 1):
            acum = acum + 1
    return acum


def calcularMayorModeradorIgnorados():
    m = Moderador()
    ArLoModeradores.seek(0, 0)
    mayorCantIgn = 0
    while (ArLoModeradores.tell() < os.path.getsize(ArFiModeradores)):
        m = pickle.load(ArLoModeradores)
        if (m.ignorados > mayorCantIgn):
            mayorCantIgn = m.ignorados
            mayorMod = m.id_mod
    if (mayorCantIgn != 0):
        pos = buscarModeradorPorId(mayorMod)
        ArLoModeradores.seek(pos, 0)
        m = pickle.load(ArLoModeradores)
        email = m.email
        return email
    else:
        return 'No hay gestion de reportes actualmente.'


def calcularMayorModeradorAceptados():
    m = Moderador()
    ArLoModeradores.seek(0, 0)
    mayorCantAcep = 0
    while (ArLoModeradores.tell() < os.path.getsize(ArFiModeradores)):
        m = pickle.load(ArLoModeradores)
        if (m.aceptados > mayorCantAcep):
            mayorCantAcep = m.aceptados
            mayorMod = m.id_mod
    if (mayorCantAcep != 0):
        pos = buscarModeradorPorId(mayorMod)
        ArLoModeradores.seek(pos, 0)
        m = pickle.load(ArLoModeradores)
        email = m.email
        return email
    else:
        return 'No hay gestion de reportes actualmente.'


def calcularMayorModeradorAceptadosIgnorados():
    m = Moderador()
    ArLoModeradores.seek(0, 0)
    mayorCantAcepIgn = 0
    while (ArLoModeradores.tell() < os.path.getsize(ArFiModeradores)):
        m = pickle.load(ArLoModeradores)
        if ((m.aceptados + m.ignorados) > mayorCantAcepIgn):
            mayorCantAcepIgn = m.aceptados + m.ignorados
            mayorMod = m.id_mod
    if (mayorCantAcepIgn != 0):
        pos = buscarModeradorPorId(mayorMod)
        ArLoModeradores.seek(pos, 0)
        m = pickle.load(ArLoModeradores)
        email = m.email
        return email
    else:
        return 'No hay gestion de reportes actualmente.'


def opMenuAdministrador(num_op):
    volver_principal = False
    if num_op == "1":
        while (not volver_principal):
            print("Gestionar ususarios \n--------------- \na. Eliminar usuario (incluyendo moderadores) \nb. Dar de alta un moderador \nc. Desactivar usuario \nd. Volver")
            letra_op = input("Ingrese a, b, c, d: ")
            limpiarConsola()
            if letra_op == "a":
                eliminarUsuario()
            elif letra_op == "b":
                darAltaModerador()
            elif letra_op == "c":
                print("En construcción")
            elif letra_op == "d":
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
            print("Reportes Estadisticos \n---------------")

            cantReportes = calcularCantidadRegistros(
                ArLoReportes, ArFiReportes)
            if (cantReportes != 0):
                cantRepIgnorados = calcularCantidadReportesIgnorados()
                cantRepAceptados = calcularCantidadReportesAceptados()
                mayorModIgn = calcularMayorModeradorIgnorados()
                mayorModAcep = calcularMayorModeradorAceptados()
                mayorModAcepMasIgn = calcularMayorModeradorAceptadosIgnorados()
            else:
                cantRepIgnorados = 0
                cantRepAceptados = 0
                mayorModIgn = 0
                mayorModAcep = 0
                mayorModAcepMasIgn = 0

            print("Cantidad de Reportes: ", cantReportes)
            print("Porcentaje de Reportes Ignorados: ",
                  cantRepIgnorados*100/cantReportes, " %")
            print("Porcentaje de Reportes Aceptados: ",
                  cantRepAceptados*100/cantReportes, " %")
            print(
                "Email del moderador con mayor cantidad de reportes ignorados: ", mayorModIgn)
            print(
                "Email del moderador con mayor cantidad de reportes aceptados: ", mayorModAcep)
            print("Email del moderador con mayor cantidad de reportes aceptados e ignorados: ",
                  mayorModAcepMasIgn)

            letra_op = input("Ingrese s para salir ")
            if letra_op == "s":
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


def buscarEstudiantePorEmail(email):
    e = Estudiante()
    ArLoEstudiantes.seek(0, 0)
    bandera = False
    email = email.ljust(30, " ")
    while (ArLoEstudiantes.tell() < os.path.getsize(ArFiEstudiantes)):
        e = pickle.load(ArLoEstudiantes)
        if (e.email == email):
            bandera = True
    return bandera


def generarLikesNuevoUsuario(id):

    l = Likes()
    ArLoLikes.seek(0, 2)
    cantidadEstudiantes = calcularCantidadRegistros(
        ArLoEstudiantes, ArFiEstudiantes)

    for i in range(1, cantidadEstudiantes + 1):
        if (id != i):
            l.remitente = id
            l.destinatario = i
            l.estado = 0
            pickle.dump(l, ArLoLikes)

        l.remitente = i
        l.destinatario = id
        l.estado = 0
        pickle.dump(l, ArLoLikes)


def registro():
    e_nuevo = Estudiante()
    cantReg = calcularCantidadRegistros(ArLoEstudiantes, ArFiEstudiantes)
    e_nuevo.email = input("Ingrese email: ")
    while (buscarEstudiantePorEmail(e_nuevo.email) == True):
        print("El email ingresado ya existe. Vuelva a ingresar otro.")
        e_nuevo.email = input("Ingrese email: ")
    e_nuevo.password = obtenerPassword()
    e_nuevo.nombre = input("Ingrese nombre: ")
    e_nuevo.rol = "Estudiante"
    e_nuevo.fecha_nacimiento = pedirFecha()
    e_nuevo.bio = "bio"
    e_nuevo.hobbies = "hobbies"
    e_nuevo.activo = True
    e_nuevo.sexo = "sexo"
    e_nuevo.ciudad = "ciudad"
    e_nuevo.deporte_favorito = "deporte favorito"
    e_nuevo.id_est = (cantReg + 1)
    e_nuevo.materia_debil = "materia debil"
    e_nuevo.materia_favorita = "materia favorita"
    e_nuevo.materia_fuerte = "materia fuerte"
    e_nuevo.pais = "pais"
    e_nuevo.ciudad = "ciudad"
    e_nuevo.super_like = True

    e_nuevo = formatearRegistroEstudiante(e_nuevo)
    ArLoEstudiantes.seek(0, 2)
    pickle.dump(e_nuevo, ArLoEstudiantes)
    ArLoEstudiantes.flush()

    generarLikesNuevoUsuario(e_nuevo.id_est)


# PROGRAMA PRINCIPAL
# Inicialización de los archivos
inicializarArchivos()
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
        if (usuario_logueado[1] == 0):
            menuEstudiante()
        elif (usuario_logueado[1] == 1):
            menuModerador()
        elif (usuario_logueado[1] == 2):
            menuAdministrador()
    elif (opc == '2'):
        registro()
    elif (opc == '0'):
        print('Saliendo del programa...')
    elif (usuario_logueado[1] == -2):
        print('Cuenta desactivada')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')