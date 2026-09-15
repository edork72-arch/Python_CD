import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
df = pd.read_csv(file_path, encoding='latin1')

pivot_t = pd.pivot_table(df, values= 'Quantity', index= 'Country', columns='StockCode', aggfunc='sum')
print(pivot_t)

#apilar y desapilar tablas 
df_new = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': [1,2,3],
    'C': [4,5,6]
})

#Apilar datos
df_stack = df_new.stack()
print(df_stack)

#Desapilar
df_unstacked = df_stack.unstack()
print(df_unstacked)