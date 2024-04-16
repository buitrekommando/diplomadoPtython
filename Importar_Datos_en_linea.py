import pandas as pd
import json
import urllib.request
import requests

# URL de un archivo CSV alojado en GitHub
'''
url_csv = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(url_csv)
print('*********************************************************************************')
print('URL de un archivo CSV alojado en GitHub')
print(df.head())
print('*********************************************************************************')


# URL de un archivo JSON alojado en un servidor

url_json = 'https://jsonplaceholder.typicode.com/posts'
response = urllib.request.urlopen(url_json)
data = json.loads(response.read())
df = pd.json_normalize(data)
print('*********************************************************************************')
print('URL de un archivo JSON alojado en un servidor')
print(df.head(10))
print('*********************************************************************************')

'''
url = "https://es.wikipedia.org/wiki/Econom%C3%ADa_de_M%C3%A9xico"
r = requests.get(url)
df = pd.read_html(r.text)
print('*********************************************************************************')
print('Datos de tablas de Wikipedia')
print(df)
print('*********************************************************************************')
