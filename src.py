import matplotlib.pyplot as plt
from wordcloud import WordCloud



data = {
    'Python': 20,
    'Data': 15,
    'Machine Learning': 10,
    'Visualization': 8,
    'Code': 6,
    'Algorithm': 5,
    'Programming': 5,
    'Analytics': 4,
    'Big Data': 3,
    'AI': 3,
    'Web Development': 2,
}


# Crear una instancia de WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white')

# Generar la nube de etiquetas
wordcloud.generate_from_frequencies(data)

# Mostrar la nube de etiquetas
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()