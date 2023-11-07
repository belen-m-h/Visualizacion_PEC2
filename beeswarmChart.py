import seaborn as sns
import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza estos con tus propios datos)
import random

data = {
    'Category': ['A'] * 50 + ['B'] * 40 + ['C'] * 30 + ['D'] * 20,
    'Value': [random.gauss(0, 1) for _ in range(140)]
}

# Crear un gráfico de colmena
plt.figure(figsize=(8, 6))
sns.swarmplot(x='Category', y='Value', data=data, palette='Set1')

# Agregar etiquetas y título
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de Colmena')

# Mostrar el gráfico
plt.show()