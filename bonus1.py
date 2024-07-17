edades = ['']*6
edades = [21, 18, 20, 19, 23, 24]

def mostrar(z):
    s = len(z)
    for i in range(s):
        print(z[i])

def ordenar(z):
    s = len(z)
    for i in range(s-1):
        for j in range((i+1),s-2):
            if z[i] > z[j]:
                aux = z[i]
                z[i] = z[j]
                z[j] = aux

def contarhuecos(z):
    s = len(z)
    h = 0
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            h = h+1
    return h

def faltantes(z):
    s = len(z)
    g = ['']*(s-1)
    for i in range(s-1):
        if z[i+1] == (z[i]+2):
            g[i] = z[i]+1
        else:
            g[i] = 0
    return g

def mostrarfaltantes(z):
    s = len(z)
    for i in range(s):
        if z[i] != 0:
            print(z[i])

print("Reporte de edades:")
mostrar(edades)

ordenar(edades)
print("Reporte de edades ordenadas de forma creciente:")
mostrar(edades)

huecos = contarhuecos(edades)
print("Cantidad de huecos en la secuencia: ",huecos)

edadesFaltantes = faltantes(edades)

print("El/los elemento/s faltante/s para tener una secuencia autoincremental es/son:")
mostrarfaltantes(edadesFaltantes)