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
    contadores=[["Azul",contadorAzul],["Rojo",contadorRojo],["Verde",contadorVerde],["Amarillo",contadorAmarillo]]
    mayor=contadores[0]
    for i in range(len(contadores)):
        if contadores[i][1] >
    print(contadores)
  
conjunto = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
cuantas(conjunto)
