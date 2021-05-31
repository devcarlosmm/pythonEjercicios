s="hast"
n=3
def remover_enesimo(s, n):
    if len(s) == n+1:
        substring=slice(n)
        resultado = s[substring]
        print(resultado)
    return resultado

remover_enesimo(s,n)
