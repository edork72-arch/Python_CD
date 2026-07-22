import numpy as np

# Código en NumPy para la suma de matrices:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

suma = A + B
print("Suma de matrices:\n", suma)


#Código en NumPy para la multiplicación de matrices:
producto = np.dot(A, B)
print("Producto de matrices:\n", producto)


# Transposición de Matrices
# La transposición de una matriz intercambia sus filas y columnas. Por ejemplo, la transposición de la matriz A es:
transpuesta = A.T
print(transpuesta)


# Determinante de una matriz
# El determinante es un valor único que puede calcularse a partir de una matriz cuadrada. Por ejemplo, el determinante de la matriz AAA es:
determinante = np.linalg.det(A)
print("Determinante de A:", determinante)


# Inversa de una matriz
# La matriz inversa de A:
inversa = np.linalg.inv(A)
print("Inversa de A:\n", inversa)


# Valores y vectores propios
# Los valores propios y los vectores propios son fundamentales en muchas aplicaciones, como en la compresión de datos y el análisis de sistemas dinámicos.
valores_propios, vectores_propios = np.linalg.eig(A)
print("Valores propios de A:\n", valores_propios)
print("Vectores propios de A:\n", vectores_propios)


# Resolución de sistemas de ecuaciones lineales
# Para resolver un sistema de ecuaciones lineales AX=BAX = BAX=B:
B = np.array([1, 2])
X = np.linalg.solve(A, B)
print("Solución del sistema AX = B:\n", X)