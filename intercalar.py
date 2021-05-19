'''
Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, 
pero con el segundo string intercalado entre cada letra del primero.
'''
def intercalar(string_a, string_b):
    if type(string_a) == str and type(string_b) == str:
        i=0;
        for i in range(len(string_a)):
            if i==0:
                resultado=string_a[i]+string_b
            else:
                resultado=resultado+string_a[i]+string_b
            i=+1
        return resultado
    else:
        while type(string_a) != str or type(string_b)!= str:
            print("Las cadenas proporcionadas no son cadenas... \nPor favor, introduce unas nuevas.")
            string_a=input("Dame una cadena: ")
            string_b=input("Dame la otra cadena: ")
        i=0;
        for i in range(len(string_a)):
            if i==0:
                resultado=string_a[i]+string_b
            else:
                resultado=resultado+string_a[i]+string_b
            i=+1
        return resultado

print(intercalar("familia",0))
