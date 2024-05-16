"""
ALGORITMO DE ORDENAMIENTO RAPIDO (QUICKSORT)

[1] Selección del pivote: Se elige un elemento de la lista llamado pivote. El pivote es un valor alrededor del cual se dividirá la lista en dos subgrupos, el primero elemento sera el pivote
[2] Particionamiento: Se reorganiza la lista de manera que todos los elementos menores que el pivote estén a su izquierda, y todos los elementos mayores que el pivote estén a su derecha. Al final de este paso, el pivote está en su posición final en la lista ordenada.
[3] Recursión: Se aplica el algoritmo de forma recursiva a las dos sublistas generadas en el paso anterior. Esto se hace hasta que todas las sublistas sean de tamaño 0 o 1, lo que significa que la lista está ordenada.
[4] Combinación: No se requiere un paso explícito de combinación en el algoritmo de quicksort, ya que la reorganización de elementos en el paso de particionamiento coloca automáticamente todos los elementos en su posición final en la lista ordenada.

"""


# Manera larga (Mejora el Entendimiento Terciario)
def QuickSort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    menores = []
    mayores = []
    for x in lista[1:]:
        if x <= pivote:
            menores.append(x)
        else:
            mayores.append(x)

    return QuickSort(menores) + [pivote] + QuickSort(mayores)

lista = [7,5,4,2,0,8,6,1,3,9,10]
print(QuickSort(lista))

# Manera mas corta
def QuickSort2(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x >= pivote]
    return QuickSort2(menores) + [pivote] + QuickSort2(mayores)

lista2 = [17,15,14,12,10,18,16,11,13,19,20]
print(QuickSort2(lista2))