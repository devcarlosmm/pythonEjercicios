s="hast"
n=0
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
        
    return resultado

remover_enesimo(s,n)
