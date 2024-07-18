# Definimos y dimensionamos el arreglo edades
# VARIABLES - TIPO DE DATOS:
# edades - ARRAY
edades = [0]*6
edades = [21, 18, 26, 19, 23, 28]

# Procedimiento para mostrar los elementos de un arreglo
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY


def mostrar(z):
    s = len(z)
    for i in range(s):
        print(z[i])

# Procedimiento para ordenar los elementos de un arreglo con el método de la burbuja
# VARIABLES - TIPO DE DATOS:
# s, aux - INTEGER
# z - ARRAY


def ordenar(z):
    s = len(z)
    for i in range(s-1):
        for j in range((i+1), s):
            if z[i] > z[j]:
                aux = z[i]
                z[i] = z[j]
                z[j] = aux


# Función para contar la cantidad de "huecos" que hay en la secuencia
# VARIABLES - TIPO DE DATOS:
# s, h - INTEGER
# z - ARRAY

def contarhuecos(z):
    s = len(z)
    h = 0
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            h = h+1
    return h

# Función que crea un arreglo con los elementos que faltan para completar la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z, g - ARRAY

# COMENTARIO PARA NOSOTROS, DESPUÉS BORRAR: JUSTO EN ESTE EJEMPLO HAY SÓLO 1 HUECO CON UN ELEMENTO FALTANTE, PERO QUISE
# GENERALIZARLO POR SI LLEGASE A HABER MÁS DE UN HUECO CON ELEMENTOS FALTANTES. TUVE QUE HACER FUNCIONES POR SEPARADAS
# PORQUE NO SÉ SI TENEMOS PERMITIDO QUE LA FUNCIÓN DEVUELVA MÁS DE UN VALOR, MÁS SI SON TIPOS DE DATOS DIFERENTES, COMO
# LOS HUECOS UN DATO SIMPLE O LOS ELEMENTOS FALTANTES EN UN ARREGLO. COMO ES UN BONUS, YO NO LE DARÍA MUCHA VUELTA. LO
# PROBÉ Y FUNCIONAR, FUNCIONA


def faltantes(z):
    s = len(z)
    g = ['']*(s-1)
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            g[i] = z[i]+1
        else:
            g[i] = 0
    return g

# Procedimiento para mostrar los elementos que faltan en la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY


def mostrarfaltantes(z):
    s = len(z)
    for i in range(s):
        if z[i] != 0:
            print(z[i])


# PRINCIPAL
# VARIABLES - TIPO DE DATOS:
# huecos - INTEGER
# edadesFaltantes - ARRAY
print("Reporte de edades:")
mostrar(edades)

ordenar(edades)
print("Reporte de edades ordenadas de forma creciente:")
mostrar(edades)

huecos = contarhuecos(edades)
print("Cantidad de huecos en la secuencia: ", huecos)

edadesFaltantes = faltantes(edades)
print("El/los elemento/s faltante/s para tener una secuencia autoincremental es/son:")
mostrarfaltantes(edadesFaltantes)
