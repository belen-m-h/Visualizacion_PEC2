import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Datos de ejemplo (reemplaza estos con tus propios datos)
import random
#
# data = {
#     'Category': ['A'] * 50 + ['B'] * 40 + ['C'] * 30 + ['D'] * 20,
#     'Value': [random.gauss(0, 1) for _ in range(140)]
# }


from pywaffle import Waffle

# Nombre del archivo CSV
csv_file = 'tips.csv'
data = pd.read_csv(csv_file)

print(data)

# Crear un gráfico de colmena
plt.figure(figsize=(8, 6))
sns.swarmplot(data=data, x="day", hue="sex", y="total_bill")

# Agregar etiquetas y título
plt.xlabel('Day')
plt.ylabel('Total bill')
plt.title('Beeswarm Chart')

# Mostrar el gráfico
plt.show()
