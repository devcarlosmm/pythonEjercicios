#uno
def promedio_std(lista):
    x = 0
    y = 0
    x = sum(lista) / len(lista)
    total = 0.0
    for i in lista:
        total += round((i - x) ** 2,2)
    y = total / (len(lista) -1)
    y= round(y**(1/2),2)
    return (x,y)


#dos
def obtener_color_frecuente(colores):
    contador = {}
    prioridad = ["azul","rojo","verde","amarillo"]
    for color in colores:
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
print(obtener_color_frecuente(colores))


#tres
def buscaminas(tablero, i, j):
    minas=0
    for h in range(i-1, i+2):
        for v in range(j-1, j+2):
            if h<0 or h>len(tablero[0])-1 or v<0 or v>len(tablero)-1:
                continue
            minas = minas+1 if tablero[h][v]=="x" else minas
    return minas
