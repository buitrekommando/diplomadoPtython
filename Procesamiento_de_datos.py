import pandas as pd
import json
import urllib.request

# ************************************************************************
# URL de un archivo JSON alojado en un servidor
# ************************************************************************
url_json = 'https://jsonplaceholder.typicode.com/posts'
response = urllib.request.urlopen(url_json)
data = json.loads(response.read())
df = pd.json_normalize(data)
print(df.head())

# ************************************************************************
# Filtrar datos
# ************************************************************************

# 1. Filtrado por columna igual a un valor específico
# Filtrar por valores en la columna 'userId' igual a 5
filtered_df = df[df['userId'] == 5]
print(filtered_df)

# Filtrado por múltiples condiciones
# Filtrar por valores en la columna 'userId' mayores que 9 y en la columna 'id' menores que 96
filtered_df = df[(df['userId'] > 9) & (df['id'] < 96)]
print(filtered_df)

# Filtrado por valores que pertenecen a una lista
# Crear una lista de valores a filtrar
values_to_filter = [2, 4]
# Filtrar por valores en la columna 'userId' que estén en la lista values_to_filter
filtered_list_df = df[df['userId'].isin(values_to_filter)]
print(filtered_list_df)

# Filtrado basado en una función personalizada
# Definir una función para filtrar valores
def custom_filter(row):
    return row['userId'] % 2 == 0  # Filtrar valores pares en la columna 'userId'

# Aplicar la función de filtro al DataFrame
filtered_custom_df = df[df.apply(custom_filter, axis=1)]
print(filtered_custom_df)

# ************************************************************************
# Usando GroupBy para agrupar datos
# ************************************************************************

#1. Agrupamiento simple por una columna (userId) y contando los elementos de cada grupo
grouped_df = df.groupby('userId').count()
print('Agrupando y contando userId: ')
print(grouped_df)

grouped_df = df.groupby('userId')
print(grouped_df['id'].describe())

# Agrupamiento con múltiples columnas y cálculo de múltiples estadísticas
# Agrupar por la columna 'userId' y calcular la suma y el promedio de los id
grouped_df = df.groupby(['userId']).agg({'id': ['sum', 'mean', 'max','min']})
print(grouped_df)

# Agrupamiento con función de agregación personalizada
# Definir una función de agregación personalizada
def custom_agg_func(arr):
    return arr.max() - arr.min()  # Calcular la diferencia entre el máximo y mínimo

# Aplicar la función de agregación personalizada al agrupar por la columna 'Grupo'
custom_agg_df = df.groupby('userId').agg({'id': custom_agg_func})
print(custom_agg_df)

# ************************************************************************
# Ordenamiento de Datos
# ************************************************************************

# 1. Ordenamiento por una columna de forma ascendente
# Ordenar el DataFrame por la columna 'userId' de forma ascendente
sorted_df = df.sort_values(by='userId')
print(sorted_df)

# 2. Ordenamiento por una columna de forma descendente
# Ordenar el DataFrame por la columna 'userId' de forma descendente
sorted_df = df.sort_values(by='userId', ascending=False)
print(sorted_df)

# 3. Ordenamiento por múltiples columnas
# Ordenar el DataFrame por las columnas 'userId' de forma ascendente y 'id' de forma descendente
sorted_df = df.sort_values(by=['userId', 'id'], ascending=[True, False])
print(sorted_df)

# ************************************************************************
# Busqueda por patrones de texto
# ************************************************************************

# Buscar todas las filas donde el valor en la columna 'title' empiece con 's'
filtered_df = df[df['title'].str.startswith('s')]
print(filtered_df)
# Buscar todas las filas donde el valor en la columna 'title' contenga la letra 'v'
filtered_df = df[df['title'].str.contains('v')]
print(filtered_df)
# Buscar todas las filas donde el valor en la columna 'title' contenga la cadena "volup"
filtered_df = df[df['title'].str.contains("volup")]
print(filtered_df)

# Búsqueda utilizando una función personalizada
# Crear una función de búsqueda personalizada
def custom_search(row):
    return row['userId'] > 5 and row['id'] < 70  # Buscar filas que cumplan esta condición

# Aplicar la función de búsqueda al DataFrame
filtered_custom_df = df[df.apply(custom_search, axis=1)]
print(filtered_custom_df)
