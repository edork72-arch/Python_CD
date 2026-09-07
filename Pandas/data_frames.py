import pandas as pd
import numpy as np

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
retail_data = pd.read_csv(file_path, encoding='latin1')
print(retail_data.head())


print("-------crear data frames desde un Array(numpy)------------")
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df_from_array = pd.DataFrame(data, columns=['A','B','C'])
print(df_from_array)


print("--------crear data frames desde una lista -----------")
data = [[1,'jhon', 22], [2,'ana', 23]]
df_from_list = pd.DataFrame(data, columns=['ID','NAME','EDAD'])
print(df_from_list)


print("------crear data frames desde una lista que contiene diccionarios-------------")
data = [{'ID': 1, 'NAME': 'Jhon', 'EDAD': 22}]
df_from_dict_list = pd.DataFrame(data)
print(df_from_dict_list)


print("------crear data frames desde un diccionarios que contiene listas-------------")
data = {'ID': [1,2,3], 'NAME': ['Jhon','Ana','Juan'], 'EDAD': [22,24,25]}
df_from_dict = pd.DataFrame(data)
print(df_from_dict)


print("------crear data frames desde undiccionario que tiene series-------------")
data = {'ID': pd.Series([1,2,3]), 'NAME': pd.Series(['Jhon','Ana','Juan']), 'EDAD': pd.Series([22,24,25])}
df_from_series_dict = pd.DataFrame(data)
print(df_from_series_dict)