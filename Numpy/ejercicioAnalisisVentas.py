import numpy as np

# Paso 1: Crear arrays con datos de ventas mensuales
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])


# Paso 2: Estadísticas Básicas
# Calcula la media y la suma de ventas para los productos A, B y C usando las funciones de NumPy.
media_A = np.mean(ventas_A)
media_B = np.mean(ventas_B)
media_C = np.mean(ventas_C)

suma_A = np.sum(ventas_A)
suma_B = np.sum(ventas_B)
suma_C = np.sum(ventas_C)

print(f"""La Media y Suma de ventas: 
Producto A: Media = {media_A:.2f} -- Suma = {suma_A}
Producto B: Media = {media_B:.2f} -- Suma = {suma_B}
Producto C: Media = {media_C:.2f} -- Suma = {suma_C}""")



# Paso 3: Manipulación y Análisis de Datos
# Total de ventas por mes: Suma las ventas de los tres productos para cada mes.
# Promedio de ventas por producto: Calcula el promedio de ventas por producto.
# Mes con mayor y menor ventas: Identifica qué mes tuvo el total de ventas más alto y cuál el más bajo usando las funciones np.argmax y np.argmin.
suma_mesT = np.add(ventas_A, ventas_B, ventas_C)#vector del total de ventas por mes
dic_suma_mesT = {str(k): int(i) for k, i in zip(meses, suma_mesT)}
promedio_A = np.average(ventas_A)
promedio_B = np.average(ventas_B)
promedio_C = np.average(ventas_C)
max_ventas_mes = np.argmax(suma_mesT)
min_ventas_mes = np.argmin(suma_mesT)

print(f"""
Total de ventas por mes:
{dic_suma_mesT}

Promedio de ventas por producto: 
Producto A: {promedio_A:.2f}
Producto B: {promedio_B:.2f}
Producto C: {promedio_C:.2f}

Mes con mayor ventas del Año:
{meses[max_ventas_mes]} = {suma_mesT[max_ventas_mes]}
Mes con menor ventas del Año:
{meses[min_ventas_mes]} = {suma_mesT[min_ventas_mes]}""")

# Paso 4: Operaciones Avanzadas con NumPy
# Reshape y Transposición:
# Crea una matriz 2D con las ventas de los tres productos y transforma su forma (reshape) a un array tridimensional con dimensiones (3, 4, 3).
# Transpone la matriz de ventas para que las filas se conviertan en columnas.
# Invertir arrays: Invierte las ventas de cada producto en orden de meses.
# Aplanar la matriz: Convierte la matriz de ventas a un array unidimensional.

matriz_ventas = np.vstack((ventas_A, ventas_B, ventas_C))
#transformamos la matriz en una matriz de 3 dimenciones (3 capas, 4 filas, 3 columnas)
matriz_rashape = matriz_ventas.reshape(3,4,3)
matriz_ventas_Traspuesta = matriz_ventas.T
invertir_A = ventas_A[::-1]
invertir_B = ventas_B[::-1]
invertir_C = ventas_C[::-1]
aplanar_matriz_ventas = matriz_ventas.flatten()

print(f"""
Matriz de Ventas:
{matriz_ventas}
Tranformacion de Matriz en (3 capas, 4 filas, 3 columnas):
{matriz_rashape}
Transpuesta de matriz de ventas:
{matriz_ventas_Traspuesta}
Invertir Ventas por producto:
Producto A = {invertir_A}
Producto B = {invertir_B}
Producto C = {invertir_C}
Aplanamiento de Matriz de Ventas:
{aplanar_matriz_ventas}""")


# Paso 5: Análisis de Elementos Únicos
# Utiliza np.unique para encontrar los elementos únicos en los datos de ventas y cuenta cuántas veces aparece cada uno.
valor_venta_unicos, cantidad_VVU = np.unique(matriz_ventas, return_counts=True)
print(f"""
Valor de ventas Unico: {valor_venta_unicos}
Repeticiones de cada Valor de ventas Unico: 
{cantidad_VVU}""")


# Paso 6: Indexación y Slicing
# Ventas del primer trimestre: Extrae las ventas de los tres primeros meses del año.
# Indexación booleana: Selecciona los meses donde el total de ventas de los tres productos supere los 800.
# Selección avanzada: Usa una lista de índices para seleccionar las ventas de los meses pares (o selecciona los meses a tu elección) y muestra esas ventas en una nueva matriz.
Ventas_primerTrimestre = suma_mesT[:3]
dic_trimestre = {str(k): int(i) for k, i in zip(meses[:3], Ventas_primerTrimestre)}
total_ventas_producto = np.array((sum(ventas_A),sum(ventas_B),sum(ventas_C)))
mayores_ventasProducto = total_ventas_producto[total_ventas_producto > 800]
index_ventas = np.random.randint(1,12,4)
meses_seleccion_ventas = suma_mesT[index_ventas]
meses_seeccion = meses[index_ventas]
dic_meses_seleccion = {str(k): int(i) for k, i in zip(meses_seeccion, meses_seleccion_ventas)}
print(f"""
Primer trimestre de Vestas: {dic_trimestre}
Productos con ventas mayores a 800: {mayores_ventasProducto}
Mostrar meses Aleatorios: {dic_meses_seleccion}""")
