# CATEDRA: ALGORITMOS Y ESTRUCTURAS DE DATOS
# TRABAJO PRACTICO N° 3
# INTEGRANTES DEL GRUPO: Battocchio, Leandro
#                        Carle, Rocio
#                        Kopp, Brenda
#                        Urquiza, Juan
#----------------------------------------------------------------
# Es necesario instalar esta libreria con: 'pip install pwinput' 
import pwinput
import os
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
        #Estos no están en el modelo pero los dejo por las dudas los necesitemos
        self.nombre = ""
        self.rol = ""
        
class Admin:
    def __init__(self):
        self.id_admin = 0
        self.email = ""
        self.password = ""
        #Estos no están en el modelo pero los dejo por las dudas los necesitemos
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

ArFiEstudiantes = "./archivos/estudiantes.txt"
ArFiAdministradores = "./archivos/administradores.txt"
ArFiModeradores = "./archivos/moderadores.txt"
ArFiLikes = "./archivos/likes.txt"
ArFiReportes = "./archivos/reportes.txt"


def inicializar():
    estudiante1 = Estudiante()
    estudiante1.email = "estudiante1@ayed.com"
    estudiante1.password = "111222"
    estudiante1.nombre = "Pedro Castillo"
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
    estudiante1.pais = "argentina"
    estudiante2 = Estudiante()
    estudiante2.email = "estudiante2@ayed.com"
    estudiante2.password = "333444"
    estudiante2.nombre = "Florencia Abascal"
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
    estudiante3 = Estudiante()
    estudiante3.email = "estudiante3@ayed.com"
    estudiante3.password = "555666"
    estudiante3.nombre = "Raul Gimenez"
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
    moderador1 = Moderador()
    moderador1.activo = "s"
    moderador1.email = "m1@ayed.com"
    moderador1.id_mod = 1
    moderador1.nombre = "moderadornombre"
    moderador1.password = "m123"
    moderador1.rol = "moderador"
    administrador1 = Admin()
    administrador1.email = "a1@ayed.com"
    administrador1.id_admin = 1
    administrador1.nombre = "nombreadministrador"
    administrador1.password = "a123"
    administrador1.rol = "administrador"
