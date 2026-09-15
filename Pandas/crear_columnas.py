import pandas as pd

file_path = '/mnt/c/Users/edork/python_Workspace/Curso_Python/Python_CD/Online_Retail.csv'
df = pd.read_csv(file_path, encoding='latin1')

#Crear la columna de precio total
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print(df.head())

#Crear columna con dato condicionado 
df['high_value'] = df['TotalPrice'] > 16
print(df['high_value'])


#Ver la informacion de los tipos de datos de las columnas
print(df.info())

#Crear columna sin datos y darle el tipo de dato que deseamos 
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.info())

#Aplicar lambda a una columna
df['DiscountedPrice'] = df['UnitPrice'].apply(lambda x: x * 0.9)
print(df['DiscountedPrice'])

#Transformar datos con datos categoricos
def categorize_price(price):
    if price > 50:
        return 'High'
    elif price > 20:
        return 'Medium'
    else:
        return 'Low'

df['PriceCategory'] = df['TotalPrice'].apply(categorize_price)
print(df['PriceCategory'])