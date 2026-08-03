from statistics import variance

import numpy as np


# Operaciones Básicas con Arrays
# Instrucción: Crea dos arrays de 1D con valores enteros y realiza las operaciones de suma, resta, multiplicación, y división entre ellos.
A = np.random.randint(10,50,4)
B = np.random.randint(51,100,4)
suma = A + B
resta = A - B
multiplicacion = A * B
division = A / B
print(f"""Suma de Array: {suma}
Resta de Array: {resta}
Multiplicaion de Array: {multiplicacion}
Divicion de Array: {division}""")


# Cálculos Estadísticos en Arrays
# Instrucción: Dado un array de datos, calcula la media, mediana, varianza, 
# y desviación estándar.
C = np.random.randint(10,20,15)
media = np.mean(C)
mediana = np.median(C)
varianza = np.var(C)
dEstandar = np.std(C)
print(f"""Media: {media}
Mediana: {mediana}
Varianza: {varianza}
Desviacion Estandar: {dEstandar}""")



# Operaciones Matriciales
# Instrucción: Crea dos matrices de 2x2 y realiza las operaciones de suma, resta, 
# multiplicación (producto matricial) y cálculo de la inversa de una de ellas.
D = np.random.randint(10,20, size=(2,2))
E = np.random.randint(20,30, size=(2,2))
sumaM = D + E
restaM = D -E
multiplicacionM = np.dot(D,E)
inversaD = np.linalg.inv(D)
print(f"""Suma de Matriz: {sumaM}
Resta de Matriz: {restaM}
Multiplicaion de Matriz: {multiplicacionM}
Inversa de Matriz D: {inversaD}""")



# Resolución de un Sistema de Ecuaciones Lineales
# Instrucción: Resuelve el sistema de ecuaciones lineales dado por Ax=b, donde A es una matriz 2x2 y b es un vector de 2 elementos.
# Ax=bAx = b
b = np.array([15,23])
x = np.linalg.solve(D, b)
print("Solucion al sistema de ecuacion es: ", x)



# Simulación de Datos
# Instrucción: Genera un array de 1000 números aleatorios que sigan una distribución 
# normal con media 0 y desviación estándar 1. Calcula la media y desviación estándar del 
# array generado.
datos_simulados = np.random.normal(0,1,1000)
media_simulacion = np.mean(datos_simulados)
desviacion_simulacion = np.std(datos_simulados)
print(f"""Media: {media_simulacion}
Desviacion Estandar: {desviacion_simulacion}""")