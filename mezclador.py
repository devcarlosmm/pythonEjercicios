def mezclador(string_a, string_b):
 if type(string_a) == str and type(string_b) == str:
    print("son strings")
    if len(string_a)>2 and len(string_b)>2:
        print("son strings y mayores de 2")
        resultado=string_a[0:2] + string_b[0:2]
        return resultado
    else:
        print("son strings pero menos que 2")
        cond1=False
        cond2=False
        while cond1 == False or cond2 == False:
            string_a=input("Dame un string: ")
            string_b=input("Dame otro string: ")
            if type(string_a) == str and type(string_b) == str:
                cond1=True
            if len(string_a)>2 and len(string_b)>2:
                cond2=True
        print("son strings y mayores de 2")
        resultado=string_a[0:2] + string_b[0:2]
        return resultado
 else:
    print("no son strings")
    cond1=False
    cond2=False
    while cond1 == False or cond2 == False:
        string_a=input("Dame un string: ")
        string_b=input("Dame otro string: ")
        if type(string_a) == str and type(string_b) == str:
            cond1=True
        if len(string_a)>2 and len(string_b)>2:
            cond2=True
    print("son strings y mayores de 2")
    resultado=string_a[0:2] + string_b[0:2]
    return resultado
  
mezclador("penas","q")
