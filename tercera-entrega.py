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

global ArFiEstudiantes, ArFiAdministradores, ArFiModeradores,ArFiLikes,ArFiReportes, usuario_logueado

ArFiEstudiantes = "./archivos/estudiantes.txt"
ArFiAdministradores = "./archivos/administradores.txt"
ArFiModeradores = "./archivos/moderadores.txt"
ArFiLikes = "./archivos/likes.txt"
ArFiReportes = "./archivos/reportes.txt"

# ID del usuario - Tipo de usuario (0 = estudiantes, 1 = moderador, 2 = administrador)
usuario_logueado = [-1, -1]

# Función para inicializar los archivos
def inicializarArchivos():
    global arLoAdministradores, arLoEstudiantes, arLoModeradores, arLoLikes, arLoReportes

    if not (os.path.exists(ArFiEstudiantes)):
        arLoEstudiantes = open(ArFiEstudiantes, "w+b")
        inicializarEstudiantes()
    else:
        arLoEstudiantes = open(ArFiEstudiantes, "r+b")
    if not (os.path.exists(ArFiAdministradores)):
        arLoAdministradores = open(ArFiAdministradores, "w+b")
        inicializarAdministradores()
    else:
        arLoAdministradores = open(ArFiAdministradores, "r+b")
    if not (os.path.exists(ArFiModeradores)):
        arLoModeradores = open(ArFiModeradores, "w+b")
        inicializarModeradores()
    else:
        arLoModeradores = open(ArFiModeradores, "r+b")
    if not (os.path.exists(ArFiLikes)):
        arLoLikes = open(ArFiLikes, "w+b")
    else:
        arLoLikes = open(ArFiLikes, "r+b")
    if not (os.path.exists(ArFiReportes)):
        arLoReportes = open(ArFiReportes, "w+b")
    else:
        arLoReportes = open(ArFiReportes, "r+b")

# Función para formatear los registros de estudiantes    
def formatearRegistroEstudiante(registro):
    registro.email = registro.email.ljust(30," ")
    registro.password = registro.password.ljust(30," ")
    registro.nombre = registro.nombre.ljust(30," ")
    registro.rol = registro.rol.ljust(30," ")
    registro.bio = registro.bio.ljust(30," ")
    registro.hobbies = registro.hobbies.ljust(30," ")
    registro.materia_favorita = registro.materia_favorita.ljust(30," ")
    registro.deporte_favorito = registro.deporte_favorito.ljust(30," ")
    registro.materia_fuerte = registro.materia_fuerte.ljust(30," ")
    registro.materia_debil = registro.materia_debil.ljust(30," ")
    registro.pais = registro.pais.ljust(30," ")
    registro.ciudad = registro.ciudad.ljust(30," ")
    
# Función para formatear los registros de moderadores
def formateoModerador(registro):
    registro.email = registro.email.ljust(30," ")
    registro.password = registro.password.ljust(30," ")
    registro.nombre = registro.nombre.ljust(30," ")
    registro.rol = registro.rol.ljust(30," ")

# Función para formatear los registros de administradores
def formateoAdministrador(registro):
    registro.email = registro.email.ljust(30," ")
    registro.password = registro.password.ljust(30," ")
    registro.nombre = registro.nombre.ljust(30," ")
    registro.rol = registro.rol.ljust(30," ")
        
def persistirRegistroEstudiante(registro, varibleLogica):
    varibleLogica.seek(0,2)
    formatearRegistroEstudiante(registro)
    pickle.dump(registro, varibleLogica)
    varibleLogica.flush()

def persistirAdministrador(registro, variableLogica):
    variableLogica.seek(0,2)
    formateoAdministrador(registro)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()

def persistirModerador(registro, variableLogica):
    variableLogica.seek(0,2)
    formateoModerador(registro)
    pickle.dump(registro, variableLogica)
    variableLogica.flush()

# Función para precargar los datos de un moderador
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

# Función para precargar los datos de un administrador
def inicializarAdministradores():
    global arLoAdministradores

    administrador1 = Admin()
    administrador1.id_admin = 1
    administrador1.email = "a1@ayed.com"
    administrador1.password = "a123"
    administrador1.nombre = "nombreadministrador"
    administrador1.rol = "administrador"

    persistirAdministrador(administrador1, arLoAdministradores)

#Función para precargar los datos de los 4 estudiantes
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

    estudiante4 = Estudiante()
    estudiante4.email = "estudiante4@ayed.com"
    estudiante4.password = "777888"
    estudiante4.nombre = "Pedro"
    estudiante4.rol = "Estudiante"
    estudiante4.fecha_nacimiento = "1994-06-20"
    estudiante4.bio = "Hola esta es mi biografia"
    estudiante4.hobbies = "Andar a caballo es mi hobbie"
    estudiante4.activo = "s"
    estudiante4.sexo = "m"
    estudiante4.ciudad = "Rosario"
    estudiante4.deporte_favorito = "basket"
    estudiante4.id_est = 111
    estudiante4.materia_debil = "matematica"
    estudiante4.materia_favorita = "historia"
    estudiante4.materia_fuerte = "biologia"
    estudiante4.pais = "argentina"

    persistirRegistroEstudiante(estudiante4, arLoEstudiantes)

# Función para limpiar la consola
def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para que aparezcan asteriscos en la contraseña
def obtenerPassword():
    password = pwinput.pwinput('Introduce tu contraseña: ')
    return password

#esta funcion se utiliza en el login
def calcularCantidadRegistros(archLogico, archFisico):
    tamArch = os.path.getsize(archFisico)
    cantReg = 0
    if (tamArch != 0):
        archLogico.seek(0,0)
        pickle.load(archLogico)
        tamReg = archLogico.tell()
        cantReg = int(tamArch/tamReg)
    return cantReg

# Función para buscar estudiante por mail y contraseña
def buscarEstudiantePorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    tamArchivo = os.path.getsize(ArFiEstudiantes)  # Tamaño del archivo
    pos = 0  # Posición inicial

    # Mover el puntero al inicio del archivo
    arLoEstudiantes.seek(0, 0)

    while pos < tamArchivo:
        if arLoEstudiantes.tell() < tamArchivo:
            estudiante = pickle.load(arLoEstudiantes)
            if estudiante.email == email and estudiante.password == password:
                return arLoEstudiantes.tell()  # Retorna la posición si hay coincidencia
        pos = arLoEstudiantes.tell()  # Actualizar la posición
    return -1  # Si no encuentra coincidencias

# Función para buscar moderador por mail y contraseña
def buscarModeradorPorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    tamArchivo = os.path.getsize(ArFiModeradores)
    pos = 0

    arLoModeradores.seek(0, 0)

    while pos < tamArchivo:
        if arLoModeradores.tell() < tamArchivo:
            moderador = pickle.load(arLoModeradores)
            if moderador.email == email and moderador.password == password:
                return arLoModeradores.tell()
        pos = arLoModeradores.tell()

    return -1

# Función para buscar administrador por mail y contraseña
def buscarAdministradorPorEmailYPassword(email, password):
    email = email.ljust(30, " ")
    password = password.ljust(30, " ")
    tamArchivo = os.path.getsize(ArFiAdministradores)
    pos = 0

    arLoAdministradores.seek(0, 0)

    while pos < tamArchivo:
        if arLoAdministradores.tell() < tamArchivo:
            administrador = pickle.load(arLoAdministradores)
            if administrador.email == email and administrador.password == password:
                return arLoAdministradores.tell()
        pos = arLoAdministradores.tell()

    return -1

# Función para calcular el tamaño de un registro
def tamanioRegistro(archivo):
    archivo.seek(0,0)
    aux = pickle.load(archivo)
    tamanioRegistro = archivo.tell() 
    return tamanioRegistro

# Inicio del Login
def login():
    intentos = 0
    cantidadEstudiantes = calcularCantidadRegistros(arLoEstudiantes, ArFiEstudiantes)
    cantidadModeradores = calcularCantidadRegistros(arLoModeradores, ArFiModeradores)
    cantidadAdministradores = calcularCantidadRegistros(arLoAdministradores, ArFiAdministradores)
    
    print(f"Cantidad de Estudiantes: {cantidadEstudiantes}")
    print(f"Cantidad de Moderadores: {cantidadModeradores}")
    print(f"Cantidad de Administradores: {cantidadAdministradores}")

    if ((cantidadEstudiantes != -1 and cantidadEstudiantes >= 4) and (cantidadModeradores != -1 and cantidadModeradores >= 1) and (cantidadAdministradores != -1 and cantidadAdministradores >= 1)):
        # Mientras el contador sea menor o igual a 4 y no este logeado
        print('LOGIN')
        print('--------------------')
        while (intentos < 3 and usuario_logueado[0] == -1):
            # Pedir al usuario igresar usuario y contraseña
            email = input("Ingresar email: ")
            #password = input("Ingresar password: ")
            password = obtenerPassword()
            administradorBusqueda = buscarAdministradorPorEmailYPassword(email,password)
            moderadorBusqueda = buscarModeradorPorEmailYPassword(email,password)
            estudianteBusqueda = buscarEstudiantePorEmailYPassword(email,password)
            print("busqueda del estudiante: ", estudianteBusqueda)
            print("busqueda del moderador: ", moderadorBusqueda)
            print("busqueda del administrador: ", administradorBusqueda)
            tamRegEstudiante = tamanioRegistro(arLoEstudiantes)
            tamRegModerador = tamanioRegistro(arLoModeradores)
            tamRegAdministrador = tamanioRegistro(arLoAdministradores)
            print("est: ",tamRegEstudiante)
            print("mod: ",tamRegModerador)
            print("adm: ", tamRegAdministrador)
            if (estudianteBusqueda != -1):
                arLoEstudiantes.seek((estudianteBusqueda - tamRegEstudiante),0)
                registroEstudiante = pickle.load(arLoEstudiantes) 
                usuario_logueado[0] = registroEstudiante.id_est
                usuario_logueado[1] = 0
                print("usuario logueado: ",usuario_logueado)
            elif(moderadorBusqueda != -1):
                arLoModeradores.seek((moderadorBusqueda - tamRegModerador),0)
                registroModerador = pickle.load(arLoModeradores) 
                usuario_logueado[0] = registroModerador.id_mod
                usuario_logueado[1] = 1
                print("usuario logueado: ",usuario_logueado)
            elif(administradorBusqueda != -1):
                arLoAdministradores.seek((administradorBusqueda- tamRegAdministrador),0)
                registroAdministradores = pickle.load(arLoAdministradores) 
                usuario_logueado[0] = registroAdministradores.id_admin
                usuario_logueado[1] = 2
                print("usuario logueado: ",usuario_logueado)
            else:
                intentos=intentos+1
                print("Inicio de sesion incorrecto. Quedan ", (3-intentos), " intentos")
            #limpiarConsola()  
    else:
        print('No hay suficientes usuarios creados para el logueo')


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
        print("En construcción")
        print('---------------')
        volver_principal = True
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

def menuEstudiante():
    num_op = ''
    while (num_op != '0'):
        menu_principal = "MENU ESTUDIANTE \n------------------ \n1.Gestionar mi perfil \n2.Gestionar candidatos \n3.Matcheos \n4.Reportes estadísticos \n0.Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 4, 0): ")
        limpiarConsola()
        opMenuEstudiante(num_op)


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

def menuModerador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU MODERADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuModerador(num_op)

def menuAdministrador():
    num_op = ''
    while num_op != '0':
        menu_principal = "MENU ADMINISTRADOR \n------------------ \n1. Gestionar usuarios \n2. Gestionar reportes \n3. Reportes estadísticos \n0. Salir"
        print(menu_principal)
        num_op  = input("Ingresar número de opción (1, 2, 3, 0): ")
        limpiarConsola()
        opMenuAdministrador(num_op)

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
                altaModerador()
            elif letra_op == "c":
                desactivarUsuario()
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

# PROGRAMA PRINCIPAL
# Inicialización de los archivos
inicializarArchivos()
#cargaUsuario()
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
    elif (opc == '0'):
        print('Saliendo del programa...')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')
