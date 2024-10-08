# CATEDRA: ALGORITMOS Y ESTRUCTURAS DE DATOS
# TRABAJO PRACTICO N° 3
# INTEGRANTES DEL GRUPO: Battocchio, Leandro
#                        Carle, Rocio
#                        Kopp, Brenda
#                        Urquiza, Juan
# ----------------------------------------------------------------

#import pwinput # Es necesario instalar esta libreria con: 'pip install pwinput'
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
        self.estado = 0

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

# ID del usuario - Tipo de usuario (0 = estudiantes, 1 = moderador, 2 = administrador) - Estado (0 = desactivado, 1 = activado)
usuario_logueado = [-1, -1, -1]

def inicializarArchivos():
    global arLoAdministradores, arLoEstudiantes, arLoModeradores, arLoLikes, arLoReportes

    #INICIALIZACION ESTUDIANTES
    if not (os.path.exists(ArFiEstudiantes)):
        arLoEstudiantes = open(ArFiEstudiantes, "w+b")
        inicializarEstudiantes()
    else:
        arLoEstudiantes = open(ArFiEstudiantes, "r+b")

    #INICIALIZACION ADMINISTRADORES
    if not (os.path.exists(ArFiAdministradores)):
        arLoAdministradores = open(ArFiAdministradores, "w+b")
        inicializarAdministradores()
    else:
        arLoAdministradores = open(ArFiAdministradores, "r+b")

    #INICIALIZACION MODERADORES
    if not (os.path.exists(ArFiModeradores)):
        arLoModeradores = open(ArFiModeradores, "w+b")
        inicializarModeradores()
    else:
        arLoModeradores = open(ArFiModeradores, "r+b")

    #INICIALIZACION LIKES
    if not (os.path.exists(ArFiLikes)):
        arLoLikes = open(ArFiLikes, "w+b")
        inicializarInteracciones()
    else:
        arLoLikes = open(ArFiLikes, "r+b")

    #INICIALIZACION REPORTES
    if not (os.path.exists(ArFiReportes)):
        arLoReportes = open(ArFiReportes, "w+b")
    else:
        arLoReportes = open(ArFiReportes, "r+b")
    
def formatearRegistroEstudiante(registro):
    registro.email = registro.email.ljust(30," ")
    registro.password = registro.password.ljust(30," ")
    registro.nombre = registro.nombre.ljust(30," ")
    registro.sexo = registro.sexo.ljust(30," ")
    registro.rol = registro.rol.ljust(30," ")
    registro.fecha_nacimiento = registro.fecha_nacimiento.ljust(30," ")
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

def inicializarModeradores():
    global arLoModeradores

    moderador1 = Moderador()
    moderador1.id_mod = 1
    moderador1.email = "m1@ayed.com"
    moderador1.password = "m1"
    moderador1.activo = True
    moderador1.nombre = "moderadornombre"
    moderador1.rol = "moderador"

    persistirModerador(moderador1, arLoModeradores)

    moderador2 = Moderador()
    moderador2.id_mod = 2
    moderador2.email = "m2@ayed.com"
    moderador2.password = "m2"
    moderador2.activo = True
    moderador2.nombre = "moderadornombre2"
    moderador2.rol = "moderador"

    persistirModerador(moderador2, arLoModeradores)

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
    estudiante1.bio = "Soy estudiante avanzado"
    estudiante1.hobbies = "Me gusta el rock! Tengo una banda con amigos"
    estudiante1.activo = True
    estudiante1.sexo = "m"
    estudiante1.ciudad = "Rosario"
    estudiante1.deporte_favorito = "Futbol"
    estudiante1.id_est = 1
    estudiante1.materia_debil = "Biologia"
    estudiante1.materia_favorita = "Lengua"
    estudiante1.materia_fuerte = "Ciencias Sociales"
    estudiante1.pais = "Argentina"

    persistirRegistroEstudiante(estudiante1, arLoEstudiantes)

    estudiante2 = Estudiante()
    estudiante2.email = "estudiante2@ayed.com"
    estudiante2.password = "333444"
    estudiante2.nombre = "Laura"
    estudiante2.rol = "Estudiante"
    estudiante2.fecha_nacimiento = "1994-06-20"
    estudiante2.bio = "Soy estudiante y me gusta leer"
    estudiante2.hobbies = "Correr, leerr novelas y comer con amigos"
    estudiante2.activo = True
    estudiante2.sexo = "m"
    estudiante2.ciudad = "Rosario"
    estudiante2.deporte_favorito = "basket"
    estudiante2.id_est = 2
    estudiante2.materia_debil = "matematica"
    estudiante2.materia_favorita = "historia"
    estudiante2.materia_fuerte = "biologia"
    estudiante2.pais = "argentina"

    persistirRegistroEstudiante(estudiante2, arLoEstudiantes)

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

    persistirRegistroEstudiante(estudiante3, arLoEstudiantes)

    estudiante4 = Estudiante()
    estudiante4.email = "estudiante4@ayed.com"
    estudiante4.password = "777888"
    estudiante4.nombre = "Jose"
    estudiante4.rol = "Estudiante"
    estudiante4.fecha_nacimiento = "1994-06-20"
    estudiante4.bio = "Soy estudiante intermedio, y trabajo en un bar"
    estudiante4.hobbies = "Andar en moto. Comer asado con amigos"
    estudiante4.activo = True
    estudiante4.sexo = "m"
    estudiante4.ciudad = "San nicolas"
    estudiante4.deporte_favorito = "Basket"
    estudiante4.id_est = 4
    estudiante4.materia_debil = "Lengua"
    estudiante4.materia_favorita = "Ed fisica"
    estudiante4.materia_fuerte = "Ed fisica"
    estudiante4.pais = "Argentina"

    persistirRegistroEstudiante(estudiante4, arLoEstudiantes)

    estudiante5 = Estudiante()
    estudiante5.email = "estudiante4@ayed.com"
    estudiante5.password = "777888"
    estudiante5.nombre = "KIKO"
    estudiante5.rol = "Estudiante"
    estudiante5.fecha_nacimiento = "1994-06-20"
    estudiante5.bio = "Soy estudiante intermedio, y trabajo en un bar"
    estudiante5.hobbies = "Andar en moto. Comer asado con amigos"
    estudiante5.activo = True
    estudiante5.sexo = "m"
    estudiante5.ciudad = "San nicolas"
    estudiante5.deporte_favorito = "Basket"
    estudiante5.id_est = 5
    estudiante5.materia_debil = "Lengua"
    estudiante5.materia_favorita = "Ed fisica"
    estudiante5.materia_fuerte = "Ed fisica"
    estudiante5.pais = "Argentina"

    persistirRegistroEstudiante(estudiante5, arLoEstudiantes)

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# def obtenerPassword():
#     password = pwinput.pwinput('Introduce tu contraseña: ')
#     return password

def calcularCantidadRegistros(archLogico, archFisico):
    tamArch = os.path.getsize(archFisico)
    cantReg = 0
    if (tamArch != 0):
        archLogico.seek(0,0)
        aux = pickle.load(archLogico)
        tamReg = archLogico.tell()
        cantReg = int(tamArch/tamReg)
    return cantReg

def buscarEstudiantePorEmailYPassword(email, password):
    email = email.ljust(30," ")
    password = password.ljust(30," ")
    regEstudiante = Estudiante()
    arLoEstudiantes.seek(0, 0)
    pos = arLoEstudiantes.tell()
    regEstudiante = pickle.load(arLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)    

    while ((email != regEstudiante.email) and (password != regEstudiante.password) and (arLoEstudiantes.tell() < tamArchivo)):
        pos = arLoEstudiantes.tell()
        regEstudiante = pickle.load(arLoEstudiantes)

    if (email == regEstudiante.email) and (password == regEstudiante.password):
        return pos
    else:
        return -1
    
def buscarUsuarioPorNombre(nombre):
    regEstudiante = Estudiante()
    arLoEstudiantes.seek(0, 0)
    pos = arLoEstudiantes.tell()
    regEstudiante = pickle.load(arLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)    
    print(nombre)
    while ((nombre != regEstudiante.nombre) and (arLoEstudiantes.tell() < tamArchivo)):
        print("while: ", regEstudiante.nombre)
        pos = arLoEstudiantes.tell()
        regEstudiante = pickle.load(arLoEstudiantes)

    if nombre == regEstudiante.nombre:
        return (pos)
    else:
        return -1
    


def mostrarLikes():
    e=Likes()
    arLoLikes.seek(0,0)
    tamArch=os.path.getsize(ArFiLikes)
    print("tamaño archivo likes: ", tamArch)
    print("LIKES")
    print("----------------------------")
    while(arLoLikes.tell()<tamArch):
        e = pickle.load(arLoLikes)
        print("Destinatario: ", e.destinatario)
        print("Remitente: ", e.remitente)
        print("Estado: ", e.estado)



def inicializarInteracciones():
    cantidadEstudiantes = calcularCantidadRegistros(arLoEstudiantes, ArFiEstudiantes)
    
    arLoLikes.seek(0,0)

    for i in range(1, cantidadEstudiantes + 1):
        for j in range(1, cantidadEstudiantes + 1):
            registroLike =  Likes()

            daLike = random.randint(0, 1)

            if i != j:
                registroLike.destinatario = j
                registroLike.remitente = i
                registroLike.estado = daLike            
                pickle.dump(registroLike, arLoLikes)
                arLoLikes.flush()
    

            

def buscarUsuarioPorNombreYDevolverID(nombre):
    regEstudiante = Estudiante()
    arLoEstudiantes.seek(0, 0)
    pos = arLoEstudiantes.tell()
    regEstudiante = pickle.load(arLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)    
    print(nombre)
    while ((nombre != regEstudiante.nombre) and (arLoEstudiantes.tell() < tamArchivo)):
        print("while: ", regEstudiante.nombre)
        pos = arLoEstudiantes.tell()
        regEstudiante = pickle.load(arLoEstudiantes)

    if nombre == regEstudiante.nombre:
        return (regEstudiante.id_est)
    else:
        return -1

def buscarModeradorPorEmailYPassword(email, password):
    email = email.ljust(30," ")
    password = password.ljust(30," ")
    regModerador = Moderador()
    arLoModeradores.seek(0, 0)
    pos = arLoModeradores.tell()
    regModerador = pickle.load(arLoModeradores)
    tamArchivo = os.path.getsize(ArFiModeradores)    

    while ((email != regModerador.email) and (password != regModerador.password) and (arLoModeradores.tell() < tamArchivo)):
        pos = arLoModeradores.tell()
        regModerador = pickle.load(arLoModeradores)

    if (email == regModerador.email) and (password == regModerador.password):
        return pos
    else:
        return -1

def buscarAdministradorPorEmailYPassword(email, password):
    email = email.ljust(30," ")
    password = password.ljust(30," ")
    regAdministrador = Admin()
    arLoAdministradores.seek(0, 0)
    pos = arLoAdministradores.tell()
    regAdministrador = pickle.load(arLoAdministradores)
    tamArchivo = os.path.getsize(ArFiAdministradores)    

    while ((email != regAdministrador.email) and (password != regAdministrador.password) and (arLoAdministradores.tell() < tamArchivo)):
        pos = arLoAdministradores.tell()
        regAdministrador = pickle.load(arLoAdministradores)

    if (email == regAdministrador.email) and (password == regAdministrador.password):
        return pos
    else:
        return -1

def tamanioRegistro(archivo):
    archivo.seek(0,0)
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
            email = input("Ingresar email: ")
            password = input("Ingresar password: ")
            #password = obtenerPassword()
            administradorBusqueda = buscarAdministradorPorEmailYPassword(email,password)
            moderadorBusqueda = buscarModeradorPorEmailYPassword(email,password)
            estudianteBusqueda = buscarEstudiantePorEmailYPassword(email,password)
            print("busqueda del estudiante: ", estudianteBusqueda)
            print("busqueda del moderador: ", moderadorBusqueda)
            print("busqueda del administrador: ", administradorBusqueda)
         
            print("puntero: ", estudianteBusqueda)
            if (estudianteBusqueda != -1):
                arLoEstudiantes.seek(estudianteBusqueda,0)
                registroEstudiante = pickle.load(arLoEstudiantes)
                print(registroEstudiante.activo)
                if(registroEstudiante.activo == False):
                    intentos = 3
                    usuario_logueado[1] = -2
                    print ("Usuario desactivado.")
                else:
                    usuario_logueado[0] = registroEstudiante.id_est
                    usuario_logueado[1] = 0
                print("usuario logueado: ",usuario_logueado)
            elif(moderadorBusqueda != -1):
                arLoModeradores.seek(moderadorBusqueda,0)
                registroModerador = pickle.load(arLoModeradores) 
                usuario_logueado[0] = registroModerador.id_mod
                usuario_logueado[1] = 1
                print("usuario logueado: ",usuario_logueado)
            elif(administradorBusqueda != -1):
                arLoAdministradores.seek(administradorBusqueda,0)
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
            usuario_encontrado = buscarEstudiantePorId(estudiante_reportado)
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_reportado = input("Ingrese el nombre del estudiante a reportar: ")
        estudiante_reportado = estudiante_reportado.ljust(30," ")
        usuario_encontrado = buscarUsuarioPorNombre(estudiante_reportado)

    if(usuario_encontrado != -1):
        arLoEstudiantes.seek(usuario_encontrado, 0)
        registroUsuarioEncontrado = pickle.load(arLoEstudiantes)
        
        if (registroUsuarioEncontrado.id_est == usuario_logueado[0]):
            limpiarConsola()
            print('No podes reportarte a vos mismo.')
        else:
            motivo = input('Ingrese el motivo del reporte: ')
            registroReporte = Reportes()

            registroReporte.estado = 0
            
            registroReporte.razon_reporte = motivo
            registroReporte.razon_reporte = registroReporte.razon_reporte.ljust(30," ")

            registroReporte.id_reportado = registroUsuarioEncontrado.id_est
            registroReporte.id_reportante = usuario_logueado[0]

    
            arLoReportes.seek(0,2)
            pickle.dump(registroReporte, arLoReportes)
            arLoReportes.flush()
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
    arLoLikes.seek(0,0)
    bandera = False

    registroLike = Likes()
    registroLike = pickle.load(arLoLikes)
    
    while (bandera == False) and (arLoLikes.tell() < tamArchvoLikes):
        if((id == registroLike.destinatario) and (usuario_logueado[0] == registroLike.remitente) and (registroLike.estado == 1)):
            bandera = True
        registroLike = pickle.load(arLoLikes)
    
    return bandera
    

def mostrarEstudiantes():
    e=Estudiante()
    arLoEstudiantes.seek(0,0)
    tamArch=os.path.getsize(ArFiEstudiantes)
    print("ESTUDIANTES")
    print("----------------------------")
    while(arLoEstudiantes.tell()<tamArch):
        e = pickle.load(arLoEstudiantes)
        if((e.activo==True) and (e.id_est != usuario_logueado[0])):
            like = meGusta(e.id_est)
            print("like: ", like)
            print("Nombre: ", e.nombre, '- ♡' if like else '')
            print("Fecha de Nacimiento: ", e.fecha_nacimiento)
            print("Edad", calcularEdad(e.fecha_nacimiento))
            print("Biografia: ", e.bio)
            print("Hobbies: ", e.hobbies)
            print("----------------------------")

def buscarLike(remitente, destinatario):
    print("destinatario por parametro: ", destinatario)
    registro = Likes()
    tamArch=os.path.getsize(ArFiLikes)
    arLoLikes.seek(0,0)
    pos = arLoLikes.tell()
    registro=pickle.load(arLoLikes)
    tamReg = arLoLikes.tell()
    cantReg = tamArch // tamReg
    
    for i in range(cantReg):
        for j in range(cantReg):
            if(registro.remitente == remitente and registro.destinatario == destinatario):
                pos = arLoLikes.tell()
            else:
                registro = pickle.load(arLoLikes)

    
    
    # while ((registro.destinatario != destinatario) and (arLoLikes.tell()<tamArch)):
    #     pos = arLoLikes.tell()
    #     registro = pickle.load(arLoLikes)
    print("registro del like encontrado - remitente: ", registro.remitente)
    print("registro del like encontrado - destinatario: ", registro.destinatario)
    print("pos " , pos)
    print((registro.remitente == usuario_logueado[0]) and (registro.destinatario == destinatario))
    return (pos-tamReg)


def verCandidatos():
    mostrarLikes()      
    mostrarEstudiantes()
    matchear = input('\nQuieres darle like a algun candidato? Ingrese "S/N": ').capitalize()
    while (matchear != 'S' and matchear != 'N'):
        print('---------------')
        print('No ha ingresado una opcion valida!')
        print('---------------')
        matchear = input('Quieres darle like a algun candidato? Ingrese "S/N": ').capitalize()

    if (matchear == 'S'):
        me_gusta = input('--------------- \nIngrese el nombre de la persona con la que le gustaria matchear: ')
        me_gusta = me_gusta.ljust(30," ")
        idDestinatario = buscarUsuarioPorNombreYDevolverID(me_gusta)
        print("idDestinatario: ", idDestinatario)

        if (idDestinatario != -1):
            posLike = buscarLike(usuario_logueado[0], idDestinatario)
            print("Like encontrado: ", posLike)
            like = Likes()
            arLoLikes.seek(posLike, 0)
            like = pickle.load(arLoLikes)

            if like.estado == 0:
                like.estado = 1
            else:
                like.estado = 0
            
            arLoLikes.seek(posLike, 0)
            pickle.dump(like,arLoLikes)
            arLoLikes.flush


        else: 
            print('No se ha ingresado un nombre de estudiante valido. \n---------------')
    else:
        limpiarConsola()

def matcheosMutuos():
    # registro = Likes()
    # tamArch=os.path.getsize(ArFiLikes)
    # arLoLikes.seek(0,0)
    # pos=arLoLikes.tell()
    # registro=pickle.load(arLoLikes)
    # tamReg = arLoLikes.tell()
    # cantReg = tamArch // tamReg
    # acum=0
    # for i in range(cantReg):
    #         if(registro.remitente == usuario_logueado[0] and registro.estado == 1):
                
    #             posInvertida=buscarLike(registro.destinatario, usuario_logueado[0])
    #             arLoLikes.seek(posInvertida,0)
    #             registro=pickle.load(arLoLikes)
    #             if(registro.estado == 1):
    #                 acum=acum+1
    #         arLoLikes.seek(pos,0)
    #         pos=arLoLikes.tell()
    #         registro=pickle.load(arLoLikes)
            
    # return acum
    


    registro = Likes()
    arLoLikes.seek(0, 0)
    pos = arLoLikes.tell()
    registro = pickle.load(arLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)    
    acum=0

    while (arLoLikes.tell() < tamArchivo):
        if(registro.remitente == usuario_logueado[0] and registro.estado == 1):
                 posInvertida=buscarLike(registro.destinatario, usuario_logueado[0])
                 arLoLikes.seek(posInvertida,0)
                 registro=pickle.load(arLoLikes)
                 if(registro.estado == 1):
                     acum=acum+1
        arLoLikes.seek(pos,0)
        
        registro=pickle.load(arLoLikes)
        pos=arLoLikes.tell()
    
    cantidadEstudiantes = calcularCantidadRegistros(arLoEstudiantes, ArFiEstudiantes)
    
    return (acum*100/cantidadEstudiantes)

def meGustaNoDevueltos():
    registro = Likes()
    arLoLikes.seek(0, 0)
    pos = arLoLikes.tell()
    registro = pickle.load(arLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)    
    acum=0

    while (arLoLikes.tell() < tamArchivo):
        if(registro.remitente == usuario_logueado[0] and registro.estado == 1):
                 posInvertida=buscarLike(registro.destinatario, usuario_logueado[0])
                 arLoLikes.seek(posInvertida,0)
                 registro=pickle.load(arLoLikes)
                 if(registro.estado == 0):
                     acum=acum+1
        arLoLikes.seek(pos,0)
        
        registro=pickle.load(arLoLikes)
        pos=arLoLikes.tell()

    return acum

def leGustoYNoMeGusta():
    registro = Likes()
    arLoLikes.seek(0, 0)
    pos = arLoLikes.tell()
    registro = pickle.load(arLoLikes)
    tamArchivo = os.path.getsize(ArFiLikes)    
    acum=0

    while (arLoLikes.tell() < tamArchivo):
        if(registro.remitente == usuario_logueado[0] and registro.estado == 0):
                 posInvertida=buscarLike(registro.destinatario, usuario_logueado[0])
                 arLoLikes.seek(posInvertida,0)
                 registro=pickle.load(arLoLikes)
                 if(registro.estado == 1):
                     acum=acum+1
        arLoLikes.seek(pos,0)
        
        registro=pickle.load(arLoLikes)
        pos=arLoLikes.tell()

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

        if (usuario_logueado[2] == 0):
            num_op = '0'
            usuario_logueado[0] = -1
            usuario_logueado[1] = -1

def buscarEstudiantePorId(id):
    regEstudiante = Estudiante()
    arLoEstudiantes.seek(0, 0)
    pos = arLoEstudiantes.tell()
    regEstudiante = pickle.load(arLoEstudiantes)
    tamArchivo = os.path.getsize(ArFiEstudiantes)    
    
    while ((id != regEstudiante.id_est) and (arLoEstudiantes.tell() < tamArchivo)):
        pos = arLoEstudiantes.tell()
        regEstudiante = pickle.load(arLoEstudiantes)

    if id == regEstudiante.id_est:
        return (pos)
    else:
        return -1

def editarPerfil():
    print("Editar perfil")
    print('----------------')
    #el estudiante logueado deberá poder modificar la información ingresada para su fecha de nacimiento, biografía, hobbies y cualquier otro campo que crean relevante.
    opEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n4.Materia favorita \n5.Deporte favorito \n0.Volver \nIngresar qué dato quiere editar (sólo número): ")
    limpiarConsola()
    registroAlumno = Estudiante()
    
    while (opEdit != '0'):
        if (opEdit == "1"):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno = pickle.load(arLoEstudiantes)
                registroAlumno.fecha_nacimiento = pedirFecha()
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno.fecha_nacimiento = registroAlumno.fecha_nacimiento.ljust(30," ")
                print(registroAlumno.fecha_nacimiento)
                pickle.dump(registroAlumno, arLoEstudiantes)
                arLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == "2"):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno = pickle.load(arLoEstudiantes)
                registroAlumno.bio = input("Agregar nueva Biografia: ")
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno.bio = registroAlumno.bio.ljust(30," ")
                pickle.dump(registroAlumno, arLoEstudiantes)
                arLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == '3'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno = pickle.load(arLoEstudiantes)
                registroAlumno.hobbies = input("Agregar nuevos hobbies: ")
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno.hobbies = registroAlumno.hobbies.ljust(30," ")
                pickle.dump(registroAlumno, arLoEstudiantes)
                arLoEstudiantes.flush()
        elif (opEdit == '4'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno = pickle.load(arLoEstudiantes)
                registroAlumno.materia_favorita = input("Agregar nueva materia favorita: ")
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno.materia_favorita = registroAlumno.materia_favorita.ljust(30," ")
                pickle.dump(registroAlumno, arLoEstudiantes)
                arLoEstudiantes.flush()
            limpiarConsola()
        elif (opEdit == '5'):
            posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
            if posEstudiante != -1:
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno = pickle.load(arLoEstudiantes)
                registroAlumno.deporte_favorito = input("Agregar nuevo deporte favorito: ")
                arLoEstudiantes.seek(posEstudiante,0)
                registroAlumno.deporte_favorito = registroAlumno.deporte_favorito.ljust(30," ")
                pickle.dump(registroAlumno, arLoEstudiantes)
                arLoEstudiantes.flush()
            limpiarConsola()
        else:
            print('No has elegido una opcion valida.')
            print('------------------------')
        print("Datos personales \n---------------\nFecha: ", registroAlumno.fecha_nacimiento, "\nBiografía: ", registroAlumno.bio, "\nHobbies: ", registroAlumno.hobbies,"\nMateria favorita: ", registroAlumno.materia_favorita,"\nDeporte favorito: ", registroAlumno.deporte_favorito, '\n---------------')
        opEdit = input("1.Fecha \n2.Biografía \n3.Hobbies \n4.Materia favorita \n5.Deporte favorito \n0.Volver \nIngresar qué dato quiere editar (sólo número): ")
        limpiarConsola()
    print("Datos personales \n---------------\nFecha: ", registroAlumno.fecha_nacimiento,  "\nBiografía: ", registroAlumno.bio, "\nHobbies: ", registroAlumno.hobbies,"\nMateria favorita: ", registroAlumno.materia_favorita, "\nDeporte favorito: ", registroAlumno.deporte_favorito)

def desactivarPerfil():
    opc = ''
    while (opc != 'S' and opc != 'N'):
        print('ATENCION')
        print('--------------------')
        opc = input('Esta apunto de inhabilitar su perfil, esta seguro de esta accion? S/N: ').capitalize()

        if (opc != 'S' and opc != 'N'):
            limpiarConsola()
            print('No ha ingresado una opcion valida, vuelva a intentar!')
    if (opc == 'S'):
        registroEstudiante = Estudiante()
        posEstudiante = buscarEstudiantePorId(usuario_logueado[0])
        print("pos estudiante", posEstudiante)
        arLoEstudiantes.seek(posEstudiante, 0)
        registroEstudiante = pickle.load(arLoEstudiantes)
        registroEstudiante.activo = False
        print(registroEstudiante.activo)
        arLoEstudiantes.seek(posEstudiante, 0)
        pickle.dump(registroEstudiante, arLoEstudiantes)
        arLoEstudiantes.flush()
        #limpiarConsola()
        print('Usuario desactivado')
        usuario_logueado[2] = 0
    else:
        limpiarConsola()

def desactivarEstudiante():
    usuario_encontrado = -1
    opc = input('1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere desactivar al usuario: ')
    while (opc != "1" and opc != "2"):
        opc = input(
            '1. Por ID \n2. Por Nombre \nIngrese la forma en la que quiere reportar: ')
    if (opc == "1"):
        try:
            estudiante_desactivar = int(input('Ingrese la ID del estudiante a reportar: '))
            usuario_encontrado = buscarEstudiantePorId(estudiante_desactivar)
        except:
            print("Ingrese una opcion válida")
    else:
        estudiante_desactivar = input("Ingrese el nombre del estudiante a reportar: ")
        estudiante_desactivar = estudiante_desactivar.ljust(30," ")
        usuario_encontrado = buscarUsuarioPorNombre(estudiante_desactivar)

    if(usuario_encontrado != -1):
        arLoEstudiantes.seek(usuario_encontrado, 0)
        registroUsuarioEncontrado = pickle.load(arLoEstudiantes)
        registroUsuarioEncontrado.activo = False
        arLoEstudiantes.seek(usuario_encontrado, 0)
        pickle.dump(registroUsuarioEncontrado, arLoEstudiantes)
        arLoEstudiantes.flush()
        print("Estudiante desactivado con exito")
        print("------------")
    else:
        limpiarConsola()
        print("Usuario no encontrado o Ingresaste dato inválido")

def verReportes():
    i=0
    r=Reportes()
    arLoReportes.seek(0,0)
    tamArch=os.path.getsize(ArFiReportes)
    print("REPORTES")
    print("----------------------------")
    while(arLoReportes.tell()<tamArch):
        r = pickle.load(arLoReportes)
        remitente_pos = buscarEstudiantePorId(r.id_reportante)
        destinatario_pos = buscarEstudiantePorId(r.id_reportado)
        
        print("pos remitente", remitente_pos)
        print("pos destin", destinatario_pos)
        
        if(remitente_pos != (-1) and destinatario_pos != (-1)):
            print("entro al primer if")
            arLoEstudiantes.seek(remitente_pos,0)
            remitente = pickle.load(arLoEstudiantes)
            arLoEstudiantes.seek(destinatario_pos,0)
            destinatario = pickle.load(arLoEstudiantes)
            print(remitente.activo)
            print(destinatario.activo)
            print(r.estado)
            print(r.estado == 0 and remitente.activo and destinatario.activo)
            if(r.estado == 0 and remitente.activo and destinatario.activo):
                print("Reporte n° ", i)
                print("Estudiante Reportante - ID ", remitente.id_est, " NOMBRE ", remitente.nombre)
                print("Estudiante Reportado - ID ", destinatario.id_est, " NOMBRE ", destinatario.nombre)
                print("Razon del reporte: ", r.razon_reporte)
                print("----------------------------")

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
    elif (usuario_logueado[1] == -2):
        print('Cuenta desactivada')
    else:
        print('No ha ingresado una opcion valida, vuelva a intentar.')
        print('-------------------')
