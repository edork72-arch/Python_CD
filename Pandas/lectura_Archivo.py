import pandas as pd 

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
retail_data = pd.read_csv(file_path, encoding='latin1')
print(type(retail_data))
print(retail_data.head())

#Lectura de Excel
#pd.read_excel(path)

#Lectura de JSON
#pd.read_json(path)