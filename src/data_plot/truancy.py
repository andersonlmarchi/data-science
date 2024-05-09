import pandas as pd
import matplotlib.pyplot as plt

data = {
    'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'registration': [3400, 3800, 3550, 3700, 3780, 3600, 3200, 3340, 3100, 2870, 2200, 1960],
    'truancy': [230, 175, 110, 350, 315, 327, 280, 335, 295, 390, 450, 184]
}

df = pd.DataFrame(data)

# a. Elabore Diagramas de Barras plotando as relações Ano X Matrículas e Ano X Evasão.
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].bar(df['year'], df['registration'], color='blue', label='Matrículas')
ax[0].legend()

ax[1].bar(df['year'], df['truancy'], color='red', label='Evasão')
ax[1].legend()

plt.savefig('images/truancy_1.png')

# b. Considerando o percentual de Evasão Escolar em relação às matriculas em cada ano,
#    faça a plotagem de um gráfico de dispersão e discuta sobre a tendência dos dados.
df['truancy_percent'] = df['truancy'] / df['registration'] * 100

fig, ax = plt.subplots()
ax.scatter(df['year'], df['truancy_percent'], color='green', label='Evasão (%)')
ax.plot(df['year'], df['truancy_percent'], color='green', linestyle='--')
ax.legend()

plt.savefig('images/truancy_2.png')
