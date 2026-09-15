import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
retail_data = pd.read_csv(file_path, encoding='latin1')

# Conocer nombres de columnas
column_name = retail_data.columns
print(column_name)


#Seleccionar una muestra de los datos 
print(retail_data.head(8))


# Numero de filas y numero de columnas 
num_rows, num_columns = retail_data.shape
print('Numero de filas: ', num_rows)
print('Numero de columnas: ', num_columns)



# Uso de describe() para obtener un resumen estadístico.
summary = retail_data.describe()
print("Resumen estadistico\n", summary)



# Cálculo de la media y mediana.
print("------------------------")
mean_value = retail_data['Quantity'].mean()
print("Media de Quantity:", mean_value)

print("------------------------")
median_value = retail_data['Quantity'].median()
print("mediana de Quantity:", median_value)



# Suma y conteo de valores.
print("------------------------")
total_sum = retail_data['Quantity'].sum()
print("Suma de Quantity:", total_sum)

print("------------------------")
count_values = retail_data['Quantity'].count()
print("Conteo de Quantity:", count_values)



# Desviación estándar y varianza.
print("------------------------")
std_dev = retail_data['Quantity'].std()
print("Desviacion estandar de Quantity:", std_dev)

print("------------------------")
variance = retail_data['Quantity'].var()
print("Varianza estandar de Quantity:", variance)



# Mínimo, Máximo y Producto.
print("------------------------")
min_value = retail_data['Quantity'].min()
print("Valor minimo de Quantity:", min_value)

print("------------------------")
max_value = retail_data['Quantity'].max()
print("Valor maximo de Quantity:", max_value)

print("------------------------")
prod_value = retail_data['Quantity'].prod()
print("Producto de Quantity:", prod_value)