import matplotlib.pyplot as plt

# Datos de ejemplo: Cantidad de elementos por categoría
categorias = ['A', 'B', 'C', 'D']
cantidad_elementos = [15, 30, 45, 20]

# Crear una figura
fig, ax = plt.subplots()

# Configurar la ubicación de los iconos
x = [1, 2, 3, 4]  # Posiciones en el eje x
y = [1] * len(categorias)  # Posición en el eje y (en este caso, todos en la misma línea)

# Dibujar iconos para cada categoría
for i in range(len(categorias)):
    ax.text(x[i], y[i], categorias[i], fontsize=25, ha='center', va='center', color='blue')
    ax.text(x[i], y[i], f'({cantidad_elementos[i]})', fontsize=10, ha='center', va='bottom', color='black')

# Configurar límites del gráfico
ax.set_xlim(0, 5)
ax.set_ylim(0, 3)

# Configurar etiquetas y título
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Icon Chart')

# Mostrar el gráfico
plt.show()