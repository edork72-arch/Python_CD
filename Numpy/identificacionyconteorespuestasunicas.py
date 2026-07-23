import numpy as np

# Para empezar, digamos que ya tenemos las respuestas de los clientes en una variable. Lo que queremos es determinar cuáles son las respuestas únicas presentes. Aquí es donde utilizamos numpy.unique.
survey_responses = np.array(
    ["bueno", "excelente", "malo", 
     "bueno", "bueno", "malo", 
     "malo", "bueno", "excelente", 
     "malo"])

print(np.unique(survey_responses))


# ¿Cómo contar la frecuencia de cada elemento?
# Además de identificar los elementos únicos, saber cuántas veces aparecen también es fundamental para un análisis más profundo. Afortunadamente, numpy.unique también puede ayudarnos con esto.
# Contar las frecuencias de los elementos únicos
elementos_unicos, conteos = np.unique(survey_responses, return_counts=True)
print(elementos_unicos)
print(conteos)

# ¿Cómo usar vistas para manipular arrays?
# Veamos cómo una vista afecta tanto a la variable original como a ella misma:
x = np.arange(10)
vista = x[1:3]

print(x)
print(vista)

# Modificar la vista
x[1:3] = [10, 11]
print(x)
print(vista)


# ¿Cómo evitar modificaciones no deseadas usando copias?
# Para situaciones donde solo se requiere acceder a la información sin modificar el array original, crear una copia es la solución.
# Crear una copia de la porción del array
copia = x[1:3].copy()

# Hacer cambios en el array original
x[1:3] = [12, 13]
print(x)
print(copia)

#saber si un array es una copia o no.
# si es una copia devuelve "none", y si es la vista, devuelve el array.
print(copia.base)
print(vista.base)