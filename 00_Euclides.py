"""
ALGORITMO DE EUCLIDES
- Este algoritmo sirve para encontrar el Maximo Comun Divisor (MCD) de dos numeros
Pasos:
[1] Mientras (b) sea diferente de "0" se continua iterando
[2] Se calcula el residuo de (a) % (b) 
[3] Pasa a tener el valor de (b) y (b) pasa a tener el valor del residuo obtenido anteriormente
[4] Si (b) llega a ser "0" el maximo comun divisor estara en (a)
[5] Devuelve (a)

"""
#Manera larga  
a = 15
b = 25
while b != 0:
    r = a % b
    a = b
    b = r
    if b == 0:
        print(f"El Maximo Comun Divisor de los numeros es: {a}") 

#Manera corta

a = 15
b = 25
while b != 0:
    r = a % b
    a , b = b , r
print(f"El Maximo Comun Divisor de los 2 numeros es: {a}") 

#Metodo Funcion

def Algoritmo_Euclides(a,b):
    while b != 0:
        r = a % b
        a , b = b , r
    return f"El MCD de los 2 numeros es: {a}" 

print(Algoritmo_Euclides(15,25))
