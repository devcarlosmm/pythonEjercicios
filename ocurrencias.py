'''
Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
'''

string = "11000110101"
def ocurrencias(string):
    i=0;
    unos=0;
    ceros=0;
    for i in range(len(string)):
        if string[i] == "1":
            unos+=1
        elif string[i] =="0":
            ceros+=1
        resultado = unos - ceros
    return resultado
    
    
ocurrencias(string)
