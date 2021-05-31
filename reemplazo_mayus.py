'''
Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.

Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".
'''

string="Viva la Vida"
def reemplazo(string):
    i=0
    resultado=""
    for i in range(len(string)):
        if string[i].isupper():
            print("es mayus")
            resultado = resultado+"$"
        else:
            print("no mayus")
            resultado=resultado+string[i]
    print(resultado)
    return resultado

reemplazo(string)
