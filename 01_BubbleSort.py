"""
ALGORITMO DE ORDENAMIENTO BURBUJA (BUBBLE SORT)
- Sirve para ordenar una lista de elementos comparando cada elemento adyacente(que se encuentra cerca) y cambiandolos de posicion si estan en el orden incorrecto

[1] Comienza con una lista de elementos desordenados
[2] Compara el primero elemento con el segundo, Si el primero elemento es mayor que es segundo, los intercambia
[3] Continua comparando pares de elementos adyacentes a lo largo de toda la lista, moviendo el elemento mas grande al final de de la lista en cada iteracion
[4] Despues de la primera iteracion, el elemento mas grande estara en la ultima posicion
[5] Se repite este proceso para los elementos restantes de la lista, excluyendo el ultimo elemento, que ya esta en su posicion final
[6] Continua este proceso hasta que no se realicen intercambios en una iteracion completa, indicando que la lista esta completamente ordenada

NOTA: Aunque es simple de entender, el ordenamiento burbuja no es eficiente para grandes conjuntos de datos debido a su complejidad de tiempo, para datos mas grandes usa: algoritmo de ordenamiento rapido o algoritmo de ordenamiento por mezcla
"""

# Metodo Convencional
lista = [3,5,4,7,8,9,6,1,2]
n = len(lista)
for i in range(n):
    for j in range(0,n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] #El intercambio se debe de hacer en una sola lista
print(lista)


# Metodo Funcion
def Bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(Bubble_sort([3,5,4,7,8,9,6,1,2])) 
