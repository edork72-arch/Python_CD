import numpy as np


escalar = np.array(42)
print(type(escalar))
print(escalar)


#¿Cómo crear un vector?
#Pues bien, si lo que deseas es almacenar datos de toda una semana, entonces necesitas un vector. Un vector es una secuencia ordenada y se representa como una dimensión uno en NumPy:
vector = np.array([30,41,35,38,39,46])
print(vector)

# ¿Cómo se trabaja con matrices en NumPy?
# Las matrices en NumPy se utilizan cuando trabajamos con dos dimensiones, lo cual es común en datos tabulares o imágenes. Almacenar y acceder a datos organizados en filas y columnas puede ser muy eficiente:
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

# ¿Qué es un tensor y cómo se representa?
# Un tensor es una extensión de matrices a más dimensiones, utilizado para representar estructuras de datos más complejas, como imágenes en 3D en las que se trabaja con los canales RGB:
tensor = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(tensor)


# ¿Cuáles son las formas de crear arrays en NumPy?

# NumPy ofrece diversas formas para crear arrays, cada una adaptándose a situaciones específicas:

# Conversión desde otras estructuras de Python, como listas y tuplas.
# Funciones de creación, como np.zeros para matrices de ceros.
# Replicación, unión o mutación de arrays existentes.
# Lectura de arrays desde disco, en formatos estándar o personalizados.
# Creación desde bytes crudos usando cadenas o buffers.
# Funciones especiales de bibliotecas de álgebra lineal.

#Veamos un ejemplo usando arange:
array_range = np.arange(10)
print(array_range)

#Y la creación de una matriz identidad:
eyes_matrix = np.eye(6)
print(eyes_matrix)


# ¿Qué otras funciones matemáticas puedo utilizar con NumPy?

# NumPy ofrece varias funciones matemáticas avanzadas, como diag para crear matrices diagonales y random para generar matrices con valores aleatorios:
diag = np.diag([1,2,3,4,5,6])
print(diag)

random = np.random.random([2,3])
print(random)

# Estos métodos sirven para aplicaciones que van desde álgebra lineal hasta simulaciones estocásticas. Te recomiendo explorar más sobre métodos numéricos y álgebra lineal para sacar el máximo provecho de NumPy.