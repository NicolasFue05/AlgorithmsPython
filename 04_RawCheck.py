"""
ALGORITMO DE COMPROBACION PRIMA

-SIRVE PARA COMPROBAR SI UN NUMERO ENTERO POSITIVO INTRODUCCIDO POR EL USUARIO ES PRIMO O NO
"""

n = int(input("Ingresa un numero: "))

if n < 2:
    es_primo = False
else:
    es_primo = True
    for i in range(2,int(n**0.05) + 1):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El numero {n} es primo")
else:
    print(f"El numero {n} no es primo") 


# METODO FUNCION

def es_primo(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.05) +1):
            if n % i == 0:
                return False
        return True
    

if es_primo(5):
    print(f"El numero es primo")
else:
    print(f"El numero no es primo") 