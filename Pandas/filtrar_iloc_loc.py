from logging.config import valid_ident

import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
retail_data = pd.read_csv(file_path, encoding='latin1')

# En ambos casos la notación es la misma: primero indicas filas y después columnas, separadas por una coma dentro de los corchetes.
# ¿Qué es iloc en Pandas? Es un selector que extrae filas y columnas usando su posición numérica dentro del data frame, empezando desde cero.
# ¿Qué es loc en Pandas? Es un selector que accede a los datos usando el nombre de la etiqueta de la fila o columna, no su posición.


#uso de iloc
#obtener el primer dato
first_date = retail_data.iloc[0]
print(first_date)

#seleccionar filas y columnas que se desean 
#pedire las primeras 8 filas y las 2 primeras columnas.
value_retail = retail_data.iloc[:8, :2]
print(value_retail)
#pido las primeras dos columnas y todas las filas
value_retail = retail_data.iloc[: , :2] 
print(value_retail)
#pido todas las columnas y las 8 primeras filas
value_retail = retail_data.iloc[:8]
print(value_retail)



#uso de loc
# en loc es lo mismo solo que usamos los nombres de las filas o las columnas
# pedire la 1,2 y 5 fila y las columnas Quantity y UnitPrice
# con la lista decidimos que datos especificos que remos ver en filas o columnas.
value_retail = retail_data.loc[[1,2,5], ['Quantity','UnitPrice']]
print(value_retail)
# pedire las primeras 5 filas y las columnas desde Quantity a UnitPrice
value_retail = retail_data.loc[:5, 'Quantity':'UnitPrice']
print(value_retail)