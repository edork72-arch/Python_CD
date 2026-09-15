import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
df = pd.read_csv(file_path, encoding='latin1')

#Convertir la columna 'InvoiceDate' a tipo datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Eliminar filas con valores faltantes en las columnas criticas 
df.dropna(subset=['CustomerID','InvoiceDate'], inplace=True)

#Crear una nueva columna 'TotalPrice'
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


#filtrar ventas en el UK
uk_sales = df[df['Country'] == 'United Kingdom']
print(uk_sales)

#filtrar por el valor mayor o menor 
high_quantity_sales = df[df['Quantity'] > 100]
print(high_quantity_sales)

#Realizar mas de una filtracion en una linea de codigo
uk_high_quantity_sales = df[(df['Country'] == 'United Kingdom') & (df['Quantity'] > 300)]
print(uk_high_quantity_sales)

#Filtracion por tiempo
sales_2011 = df[df['InvoiceDate'].dt.year == 2011]
print(sales_2011)

#Filtracion por año y mes 
sales_2010_mes = df[(df['InvoiceDate'].dt.year == 2010) & (df['InvoiceDate'].dt.month == 12)]
print(sales_2010_mes['InvoiceDate'])