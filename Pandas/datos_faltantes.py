import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
retail_data = pd.read_csv(file_path, encoding='latin1')


#identificar los datos faltantes
missing_data = retail_data.isna()
#me imprime falso si el dato exite 
print(missing_data.head())
#sumar los datos faltantes 
missing_data_count = missing_data.sum()
print(missing_data_count)



#eliminar filas con datos faltantes 
no_missing_rows = retail_data.dropna()
print('Datos sin filas con valores faltantes:\n', no_missing_rows)

#eliminar columnas con datos faltantes 
no_missing_column   = retail_data.dropna(axis=1)
print('Datos sin columnas con valores faltantes:\n', no_missing_column)



#rellenar datos vacios 
retail_data_fillef_zeros = retail_data.fillna(0)
retail_data_fillef_zeros_count = retail_data_fillef_zeros.isna().sum()
print(retail_data_fillef_zeros_count)

#rellenar los datos vacios con la media de la columna 
mean_unit_price = retail_data['UnitPrice'].mean()
retail_data_fillef_mean = retail_data['UnitPrice'].fillna(mean_unit_price)
print(retail_data_fillef_mean)