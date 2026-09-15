import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
df = pd.read_csv(file_path, encoding='latin1')

#Contar la cantidad de datos donde se menciona cada pais 
country_count = df['Country'].value_counts()
print(country_count)

#sumamos las cantidades agrupadas por pais 
country_group = df.groupby('Country')['Quantity'].sum()
print(country_group)

#Encontrar la media y la suma de el precio unitario por pais 
country_group_mean = df.groupby('Country')['UnitPrice'].agg(['mean', 'sum'])
print(country_group_mean)

#Agrupar por mas de una columna
country_stock_group = df.groupby(['Country', 'StockCode'])['Quantity'].sum()
print(country_stock_group)

#Usar una funcion para agrupar
def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()

revenue_per_country = df.groupby('Country').apply(total_revenue)
print(revenue_per_country)