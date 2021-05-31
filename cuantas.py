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
def cuantas(conjunto):
    i=0
    contadorAzul=0
    contadorRojo=0
    contadorVerde=0
    contadorAmarillo=0
    for i in range(len(conjunto)):
        if conjunto[i] == "azul":
            contadorAzul=contadorAzul + 1
        elif conjunto[i] == "rojo":
            contadorRojo+=1
        elif conjunto[i] == "verde":
            contadorVerde+=1
        elif conjunto[i] == "amarillo":
            contadorAmarillo+=1
    contadores=[[contadorAzul,"Azul"],[contadorRojo, "Rojo"],[contadorVerde, "Verde"],[contadorAmarillo, "Amarillo"]]
    contadores.sort(reverse=True)
    print(contadores)
    mayor=contadores[0]
    
  
conjunto = ['azul', 'rojo', 'rojo', 'azul', 'verde', 'verde']
cuantas(conjunto)


#tres
def buscaminas(tablero, i, j):
    minas=0
    for h in range(i-1, i+2):
        for v in range(j-1, j+2):
            if h<0 or h>len(tablero[0])-1 or v<0 or v>len(tablero)-1:
                continue
            minas = minas+1 if tablero[h][v]=="x" else minas
    return minas
