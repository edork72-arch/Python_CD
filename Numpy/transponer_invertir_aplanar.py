import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Transposición de Matrices
# La transposición de una matriz es una operación que intercambia sus filas y columnas, esencial en el álgebra lineal y la manipulación de datos científicos. En NumPy, se puede transponer una matriz usando matrix.T, lo que convierte las filas en columnas y viceversa.
transpuesta_matrix = matrix.T
print(matrix)
print(transpuesta_matrix)


# Cambiar la Forma (Reshape) de un Array
# La función reshape permite cambiar la forma de un array sin cambiar sus datos. Es importante asegurarse de que el número total de elementos permanezca constante.
array = np.arange(1,13)
reshaped_array = array.reshape(3,4)
print(array)
print(reshaped_array)


# ¿Cómo se invierte un array en NumPy?
# En el procesamiento de señales y en algoritmos de inversión de datos, es muy común invertir un array, lo que implica cambiar el orden de sus elementos de forma que el primer elemento se convierta en el último y viceversa.
reversed_array = array[::-1]
print(array)
print(reversed_array)


# Flattening de Arrays Multidimensionales
# El aplanamiento de arrays es el proceso de convertir un array multidimensional en un array unidimensional, es útil en algoritmos que requieren una entrada lineal o para operaciones de agregación. En NumPy, se puede aplanar un array usando flatten().
flattened_array = matrix.flatten()
print(matrix)
print(flattened_array)
