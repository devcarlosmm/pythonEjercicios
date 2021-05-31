'''
Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.

Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
'''

s="hasta luego"
n=3
def remover_enesimo(s, n):
    if len(s) == n+1:
        substring=slice(n)
        resultado = s[substring]
        print(resultado)
    elif n == 0:
        substring=slice(n+1,len(s))
        resultado = s[substring]
        print(resultado)
    else:
        substring1=slice(n)
        substring2=slice(n+1,len(s))
        resultado=s[substring1]+s[substring2]
        print(resultado)
    return resultado

remover_enesimo(s,n)
