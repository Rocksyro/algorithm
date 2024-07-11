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

# -------------------------------------------
# Funcion obtenerPassword (para que en vez de la password aparezcan asteriscos)
# VARIABLES - TIPO DE DATOS:
# password - STRING


def obtenerPassword():
   password = pwinput.pwinput('Introduce tu contraseña: ')
   return password





def login(estudiante_logueado, estudiantes):
    intentos = 1
    # Mientras el contador sea menor o igual a 3 y no este logeado
    print('LOGIN')
    print('--------------------')
    # Pedir al usuario igresar usuario y contraseña
    email = input("Ingresar email: ")
    password = obtenerPassword()
    resultadoBusqueda = buscarUsuario(estudiantes, email)
    print(resultadoBusqueda)
    if (resultadoBusqueda != (-1)):
        while (intentos < 3 and estudiante_logueado == ''):
            if(estudiantes[resultadoBusqueda][2] == password):
                 estudiante_logueado = estudiantes[resultadoBusqueda][1]
                 print("login exitoso!")
            else:
                 intentos+=1
                 password = obtenerPassword()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Si el dato de usuario concuerda con el mail, y el de password con contraseña,
        #almacenar a ese estudiante específico en la variable estudiante y asignarle ese mismo rol.
      #  for i in range (len(estudiantes)-1):
  #          if(estudiantes[i][3] == email and estudiantes[i][4] == password):
         #       estudiante_logueado = estudiantes[i]
        #    else:
                #Si no se pudo logear sumar uno al contador de intentos
                #Si no se pudo logear sumar uno al contador de intentos
                #Si no se pudo logear sumar uno al contador de intentos
     #             intentos = intentos + 1
     #         if (intentos < 3):
                #Se le muestra que los datos ingresados fueron incorrectos
          #        print("Datos incorrectos, vuelva a intentar.")
        #          print('--------------------')


def buscarUsuario(array, usuario):
            contadorPosicion = 0
            print(len(array))
            while ((array[contadorPosicion][1] != usuario) and contadorPosicion<=(len(array)-1)  ):
                contadorPosicion+=1
            if (array[contadorPosicion][1] == usuario):
                return contadorPosicion
            else:
                return -1
                


#PROGRAMA PRINCIPAL
login('', estudiantes)