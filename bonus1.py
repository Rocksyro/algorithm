# Definimos y dimensionamos el arreglo edades
# VARIABLES - TIPO DE DATOS:
# edades - ARRAY of INTEGER
edades = [0]*6
edades = [21, 18, 26, 19, 23, 28]

# Procedimiento para mostrar los elementos de un arreglo
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY of INTEGER
def mostrarBonus1(z):
    s = len(z)
    for i in range(s):
        print(z[i])

# Procedimiento para ordenar los elementos de un arreglo con el método de la burbuja
# VARIABLES - TIPO DE DATOS:
# s, aux - INTEGER
# z - ARRAY of INTEGER
def ordenarBonus1(z):
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
# z - ARRAY of INTEGER
def contarhuecosBonus1(z):
    s = len(z)
    h = 0
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            h = h+1
    return h

# Función que crea un arreglo con los elementos que faltan para completar la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z, g - ARRAY of INTEGER
def faltantesBonus1(z):
    s = len(z)
    g = [0]*(s-1)
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            g[i] = z[i]+1
        else:
            g[i] = 0
    return g

# Procedimiento para mostrar los elementos que faltan en la secuencia
# VARIABLES - TIPO DE DATOS:
# s - INTEGER
# z - ARRAY of INTEGER
def mostrarfaltantesBonus1(z):
    s = len(z)
    for i in range(s):
        if z[i] != 0:
            print(z[i])

# PRINCIPAL
# VARIABLES - TIPO DE DATOS:
# huecos - INTEGER
# edadesFaltantes - ARRAY of INTEGER
print("Reporte de edades:")
mostrarBonus1(edades)

ordenarBonus1(edades)
print("Reporte de edades ordenadas de forma creciente:")
mostrarBonus1(edades)

huecos = contarhuecosBonus1(edades)
print("Cantidad de huecos en la secuencia: ", huecos)

edadesFaltantes = faltantesBonus1(edades)
print("El/los elemento/s faltante/s para tener una secuencia autoincremental es/son:")
mostrarfaltantesBonus1(edadesFaltantes)