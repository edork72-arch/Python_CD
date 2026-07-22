import numpy as np

#  Mis apuntes y ejercicios de la clase:
# Indexación
# Forma de acceder a los elementos de un array por medio de su índice.
#📢 Los indices empiezan a partir del 0 que representa el primer elemento del array.
array = np.random.randint(5, 30, 20) 
print(array)

print("Elemento en la posición 5:", array[4])
print("Elemento en la primer posición:", array[0])
print("Elemento en la última posición", array[-1])
print("Elemento en la ante última posición", array[-2])


# Indexación booleana
# Forma de obtener datos a partir de una condición.
# 📢 Todos los elementos que cumplan con la condición serán “devueltos”.
bool_index = array > 15
print("Array booleano:", bool_index)
print("Elementos mayortes a 15:", array[bool_index])
print("Elementos entre 15 y 20:", array[(array >= 15 ) & (array <= 20)])


# Indexación por listas
# Permite obtener multiples elementos de un array con una lista de indices.
# 📢 Al mandarle indices “desordenados” el array resultante obtiene los elementos en el orden en que se pasó el índice centro de la lista.
index_list = [3,8,5,0]
print("Elementos en las posiciones 3,8,5 y 0:", array[index_list])
print("Elementos en las posiciones -1, 2,3 y 5:", array[[-1,2,3, 5]])


# ```**Indexación de arrays multidimensionales**
# Para acceder a un elemento de un array bidimensional, le indicamos 2 indices.&#x20;
# 📢 `[indice_fila, indice_columna]`
# ```python
matrix = np.random.randint(5, 30, size=(5,5))
print("Elemento de la fila 2, columna 2:", matrix[2,2]) # Elemento especifio
print("Elementos de las fila 1 y 2, columna 2:", matrix[[1,2],2]) # Indexaciónb por lista (1)
print("Elementos en la fila 1 , columna 2, y fila 3, columna 2:", matrix[[1,2],[3,2]]) # Indexaciónb por lista (2)
print("Elementos mayores a 18:", matrix[matrix > 18])


# Indexación booleana
# Slicing
# Selección de sub-arrays, donde le indicamos el índice inicial e índice final del conjunto original.
# 📢 También se se pueden agregar “saltos”.
print("*"*5, "Array", "*"*5)
print("Elementos desde el incio hasta la posición 3:", array[:3])
print("Elementos desde la posición 5 hasta el final:", array[5:])
print("Elementos desde la posición 5 hasta la posición 10:", array[5:10])
print("Elementos desde la posición hasta la penultima posición dando 2 saltos:", array[3:-2:2])

print("*"*5, "Matriz", "*"*5)
print("Elementos a partir de la fila uno, y columnas a partir de la fila 2:\n", matrix[1:, 2:])
print("Elementos hasta la fila 3, y hasta la columna 2:\n", matrix[:3, :2])
print("Elementos a partir de la fila 1 dando 2 saltos, hasta la columna 1 dando 2 saltos\n",matrix[1::2, :1:2])