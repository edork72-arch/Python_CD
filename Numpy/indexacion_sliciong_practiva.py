import numpy as np

array = np.random.randint(1,20,10)
print(f"Array: {array}")
print(f"cuarta posicion: {array[4]} y penultima posicion {array[-2]}")

print(f"Datos entre las pociciones 3 y 7: {array[3:7]} y las ultimas 5 posiciones: {array[-5:]}")

array = np.random.randint(0,100,30)
bool_array = array > 50
print(f"Nuevo Arreglo: {array}")
print(f"Arreglo con los numeros mayores a 50: {array[bool_array]}")

list_index = [1,4,6]
array = np.random.randint(0,100,8)
print(f"Nuevo Arreglo: {array}")
print(f"Datos de los indices: {array[list_index]}")

matriz = np.random.randint(10,50, size=(4,4))
print(f"Matriz: {matriz}")
print(f"Matriz 2x2 de la esquina inferior derecha: \n{matriz[2:,2:]}")