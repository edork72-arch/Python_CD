import pandas as pd

#Crear dataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1,2,3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value1': [4,5,6]
})


#realisar merge
ineer_merged = pd.merge(df1, df2, on='key', how='inner')
print(ineer_merged)

outer_merged = pd.merge(df1, df2, on='key', how='outer')
print(outer_merged)

left_merged = pd.merge(df1, df2, on='key', how='left')
print(left_merged)

right_merged = pd.merge(df1, df2, on='key', how='right')
print(right_merged)

#Crear dataFrame
df3 = pd.DataFrame({
    'A': ['A0','A1','A2'],
    'B': ['B0','B1','B2']
})

df4 = pd.DataFrame({
    'A': ['A3','A4','A5'],
    'B': ['B3','B4','B5']
})

#Concatenar
vertical_concat = pd.concat([df3,df4])
print(vertical_concat)

horizontal_concat = pd.concat([df3,df4], axis=1)
print(vertical_concat)


# Crear DataFrames de ejemplo con índices
df5 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df6 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])

joined = df5.join(df6, how='inner')
print(joined)