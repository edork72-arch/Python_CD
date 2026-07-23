import numpy as np

#¿Qué hace el broadcasting? Permite operar arrays de distintas dimensiones tratando al más pequeño como si tuviera la forma del más grande, sin copiar datos.

prices = np.array([100,200,300])
discount = np.array([0.9])
discount_precio = prices * discount
print(discount_precio)

prices = np.random.randint(100,500, size=(3,3))
discount = np.array([10,20,30])
discount_precio = prices + discount
print(prices)
print(discount_precio)


# ¿Cuál es la diferencia entre all y any? all exige que todos los elementos cumplan la condición; any solo requiere que uno la cumpla.
array = np.array([1,2,3,4,5])
print(np.all(array > 9))
print (np.any(array > 0))


# ¿Qué hace np.concatenate y cómo se usa?
# La concatenación une dos o más arrays en uno solo a lo largo de un eje:
array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatenar_a = np.concatenate((array_a, array_a))
concatenar_ab = np.concatenate((array_a, array_b))
print(concatenar_a)
print(concatenar_ab)


# ¿Cuándo usar vstack y hstack?
# El stacking apila arrays generando una nueva dimensión [7:20]:
# np.vstack((A, B)) apila los arrays verticalmente, creando una matriz con cada array como fila.
stacked_v = np.vstack((array_a, array_b))
print(stacked_v)
# np.hstack((A, B)) los une horizontalmente, equivalente a la concatenación en una sola fila.
sateced_h = np.hstack((array_a, array_b))
print(sateced_h)


array_c = np.arange(1,10)
#al dividir el array debe ser posible dejar todos los array del mismo tamaño, de no ser asi, saltara un valueError
split_array = np.split(array_c, 3)
print(array_c)
print(split_array)

