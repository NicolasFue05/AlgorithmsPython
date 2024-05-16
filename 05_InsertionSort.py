"""
ALGORITMO DE ORDENAMIENTO POR INSERCCION

"""

def insertion_sort(lista):
    for i in range(1, len(lista)): # Recorremos desde el segundo elemento hasta el final de la lista
        valor_actual = lista[i] # Elemento actual a insertar en la lista ordenada
        posicion = i
        
        while posicion > 0 and lista[posicion - 1] > valor_actual: # Comparamos el elemento actual con los elementos anteriores en la lista ordenada
            lista[posicion] = lista[posicion - 1] # Movemos los elementos mayores hacia la derecha
            posicion -= 1
        
        lista[posicion] = valor_actual # Insertamos el elemento actual en su lugar correcto en la lista ordenada
        


# Ejemplo de uso del algoritmo de ordenamiento por inserción
# El orden va segun el codigo ASCII 
productos = ["Manzanas", "Bananas", "Peras", "Uvas", "Naranjas", "Papas"]
insertion_sort(productos)

# Mostrar la lista ordenada alfabéticamente
print("Lista de productos ordenada alfabéticamente:")
for producto in productos:
    print(f"- {producto}")