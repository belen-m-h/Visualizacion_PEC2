import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd


# Nombre del archivo CSV
csv_file = 'access-to-electricity-vs-gdp-per-capita.csv'
data = pd.read_csv(csv_file)
# Filtra los datos por año
year = 2020
data_2020 = data[data['Year'] == year]
needed_data = data_2020[['Entity', 'Access to electricity (% of population)']]

diccionario_resultante = {}

for index, fila in needed_data.iterrows():
    entity = fila['Entity']
    value = fila['Access to electricity (% of population)']
    diccionario_resultante[entity] = value

data_dict_without_nan = {clave: valor for clave, valor in diccionario_resultante.items() if not pd.isna(valor)}

# Crear una instancia de WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white')

# Generar la nube de etiquetas
wordcloud.generate_from_frequencies(data_dict_without_nan)

# Mostrar la nube de etiquetas
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()