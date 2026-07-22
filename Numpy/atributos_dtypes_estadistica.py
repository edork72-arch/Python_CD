import numpy as np


# ¿Cómo crear un array y leer sus atributos clave?

# Para crear un array simple usas np.array([[1,2,3],[4,5,6]]). Una vez creado, puedes consultar tres atributos esenciales que te dicen todo lo que necesitas saber sobre su forma [01:13]:

# ndim: número de dimensiones del array. Un truco práctico es contar los corchetes al inicio o al final.
# shape: tamaño en cada dimensión. Para el ejemplo anterior, devuelve (2, 3), es decir, dos vectores de tres elementos cada uno.
# dtype: tipo de dato de los elementos. En este caso, int64.
array = np.array([[1,2,3],[4,5,6]])
print(array.ndim)
print(array.shape)
print(array.dtype)


# Los tres tipos más comunes que aparecen en la clase son:

# uint8: entero sin signo de 8 bits, con valores entre 0 y 255. Perfecto para colores de imagen, donde cada canal va justamente en ese rango.
# float32: número de punto flotante de 32 bits. Útil en cálculos científicos que requieren precisión moderada y ahorro de memoria.
# float64: número de punto flotante de 64 bits. Es el tipo por defecto de NumPy para decimales y ofrece mayor precisión que float32.
z = np.array(3, dtype=np.uint8)
print(z)

# ¿Cómo especifico el dtype al crear un array?
# Lo defines como argumento al construir el array. Por ejemplo, z = np.array(3, dtype=np.uint8) crea un escalar de tipo uint8, mientras que double_array = np.array([1,2,3], dtype=np.float64) convierte enteros a flotantes [04:23]. Notarás que el 1 se imprime como 1., indicando que el cero decimal está implícito.
# ¿Cómo convertir el tipo de dato de un array existente?
# NumPy permite cambiar el dtype sobre la marcha con el método astype. Por ejemplo, si tu variable z está en uint8 y necesitas decimales, puedes hacer z = z.astype(np.float64) y el valor 3 pasará a representarse como 3. con su decimal incluido.
double_array = np.array([1,2,3], dtype='d')
print(double_array)


# ¿Cómo aplicar estadística básica con NumPy?

# Una de las grandes ventajas de NumPy es que la estadística viene incluida. Sobre el array [[1,2,3],[4,5,6]] puedes calcular tres medidas fundamentales con una sola línea cada una [06:11]:

# Suma con np.sum(array): devuelve 21, el total de todos los elementos.
# Media con np.mean(array): devuelve 3.5, el promedio aritmético.
# Desviación estándar con np.std(array): devuelve aproximadamente 1.70, que mide cuánto se dispersan los valores respecto a la media.
add = np.sum(array)
print(add)

mean = np.mean(array)
print(mean)

stp = np.std(array)
print(stp)