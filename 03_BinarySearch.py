"""
ALGORITMO DE BUSQUEDA BINARIA

- SIRVE PARA ENCONTRAR UN ELEMENTO EN UNA LISTA ORDENADA

[1] SE COMIENZA CON UNA LISTA ORDENADA
[2] CALCULAMOS EL PUNTO MEDIO DEL INTERVALO
[3] VERIFICAMOS SI EL PUNTO MEDIO ES EL ELEMENTO QUE ESTAMOS BUSCANDO
[4] SI EL PUNTO MEDIO NO ES EL ELEMENTO QUE ESTAMOS BUSCANDO, VERIFICAMOS SI ES MAYOR O MENOR AL ELEMENTO QUE ESTAMOS BUSCANDO
[5] SI EL ELEMENTO EN EL PUNTO MEDIO ES MAYOR PODEMOS DESCARTAR LOS ELEMENTOS DE LA DERECHA SIGUEINTE AL ELEMENTO DEL PUNTO MEDIO
[6] SI EL ELEMENTO EN EL PUTNO MEDIO ES MENOR SE DESCARTA LA MITAD DE LA IZQUIERDA
"""


def busqueda_binaria(lista,valor):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio 
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio -1
    return -1

 


# Binary Search
def BinarySearch(array,value):
    left = 0
    right = len(array) - 1

    while left <= right:
        medium = (left + right) // 2
        if array[medium] == value:
            return medium
        elif array[medium] < value:
            left = medium + 1
        else:
            right = medium - 1
    return -1


array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
value = 35
result = BinarySearch(array, value)
if result != -1:
    print(f"El elemento {value} se encuentra en la lista")
else:
    print(f"El elemento {value} no se encuentra en la lista")