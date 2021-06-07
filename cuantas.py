#uno
def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total = 0.0
    for i in lista:
        total += round((i - x) ** 2,2)
    y = total / (len(lista))
    y= round(y**(1/2),3)
    return x,y


#dos
def color_frecuente(lista):
    contador = {}
    prioridad = ["azul","rojo","verde","amarillo"]
    for color in lista:
        if color in contador:
            contador[color] += 1 
        else:
            contador[color] = 1 
    m = max(contador.values()) 
    print(contador)
    color_seleccionado = [key for key, value in contador.items() if value == m] 
    if len(color_seleccionado) > 1: 
        color_seleccionado = min(color_seleccionado, key= lambda x: prioridad.index(x)) 
    else:
         color_seleccionado = color_seleccionado[0]
    return color_seleccionado, m

prioridad = ["azul","rojo","verde","amarillo"]
colores = ['rojo', 'rojo', 'azul', 'azul','verde','amarillo']
print(obtener_color_frecuente(lista))


#tres
def buscaminas(tablero, i, j):
    minas=0
    for h in range(i-1, i+2):
        for v in range(j-1, j+2):
            if h<0 or h>len(tablero[0])-1 or v<0 or v>len(tablero)-1:
                continue
            minas = minas+1 if tablero[h][v]=="x" else minas
    return minas


''''''

def buscaminas(tablero, i, j):
    minas=0
    for h in range(i-1, i+2):
        for v in range(j-1, j+2):
            if h<0 or h>len(tablero[0])-1 or v<0 or v>len(tablero)-1:
                continue
            minas = minas+1 if tablero[h][v]=="X" else minas
    return minas
#lista = [10, 6, 9, 28, 42, 47, 32, 7, 73, 78, 32]
tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
print(buscaminas(tablero, 1, 1))

def color_frecuente(lista):
    contador = {}
    prioridad = ["azul","rojo","verde","amarillo"]
    for color in lista:
        if color in contador:
            contador[color] += 1 
        else:
            contador[color] = 1 
    m = max(contador.values()) 
    print(contador)
    color_seleccionado = [key for key, value in contador.items() if value == m] 
    if len(color_seleccionado) > 1: 
        color_seleccionado = min(color_seleccionado, key= lambda x: prioridad.index(x)) 
    else:
         color_seleccionado = color_seleccionado[0]
    return color_seleccionado, m

prioridad = ["azul","rojo","verde","amarillo"]
colores = ['rojo', 'rojo', 'azul', 'azul','verde','amarillo']
print(color_frecuente(colores))

def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total = 0.0
    for i in lista:
        total += round((i - x) ** 2,2)
    y = total / (len(lista))
    y= round(y**(1/2),3)
    return x,y
    
lista=[54, 17, 14, 36, 65, 28, 13, 97, 56, 88, 44, 9, 30, 49, 73, 43]   
print(promedio_std(lista))
