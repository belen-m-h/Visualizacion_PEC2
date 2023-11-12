import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Nombre del archivo CSV
csv_file = 'per-capita-electricity-fossil-nuclear-renewables.csv'
data = pd.read_csv(csv_file)
# Filtra los datos por año
year = 2020
entity= 'Spain'
data_2020 = data[data['Year'] == year]
data_2020_spain = data_2020[data_2020['Entity'] == entity]
needed_data = data_2020_spain[['Fossil fuel electricity per capita (kWh) (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)',
       'Nuclear electricity per capita (kWh) (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)',
       'Renewable electricity per capita (kWh) (adapted for visualization of chart per-capita-electricity-fossil-nuclear-renewables)']]
diccionario_resultante = needed_data.to_dict(orient='index')



data = pd.DataFrame(
    {
        'labels': diccionario_resultante[4980].keys(),
        'values': diccionario_resultante[4980].values(),
    },
).set_index('labels')
iconos_por_categoria = ['fire', 'atom', 'leaf']

fig = plt.figure(
    FigureClass=Waffle,

    values= data['values'] / 100,  # Convert actual number to a reasonable block number
    legend= {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 8},
    title= {'label': 'Fossil, Nuclear, Renewables', 'loc': 'left', 'fontsize': 12},
    icons=iconos_por_categoria,
    rows=5,  # Outside parameter applied to all subplots, same as below
    font_size=24,
    colors=["#FF5733", "#3366FF", "#33FF65"],
    figsize=(6, 5)
)

fig.suptitle('Per capita electricity type', fontsize=14, fontweight='bold')
fig.supxlabel('1 block = 1000 vehicles', fontsize=8, x=0.14)
fig.set_facecolor('#EEEDE7')

plt.show()