# Considere o dataset “pessoas.csv” disponibilizado. Elabore dois diagramas com plotagens
# diferentes para discutir a relação pessoas.peso x pessoas.altura

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('files/pessoas.csv')

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].scatter(df['peso'], df['altura'], color='blue')
ax[0].set_xlabel('Peso')

ax[1].scatter(df['peso'], df['altura'], color='red')
ax[1].set_ylabel('Altura')

plt.savefig('images/people_1.png')

fig, ax = plt.subplots()
ax.scatter(df['peso'], df['altura'], color='green')
ax.set_xlabel('Peso')
ax.set_ylabel('Altura')

plt.savefig('images/people_2.png')

# Repita o gráfico apenas para mulheres.
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].scatter(df[df['sexo'] == 'F']['peso'], df[df['sexo'] == 'F']['altura'], color='blue')
ax[0].set_xlabel('Peso')

ax[1].scatter(df[df['sexo'] == 'F']['peso'], df[df['sexo'] == 'F']['altura'], color='red')
ax[1].set_ylabel('Altura')

plt.savefig('images/people_3.png')

fig, ax = plt.subplots()
ax.scatter(df[df['sexo'] == 'F']['peso'], df[df['sexo'] == 'F']['altura'], color='green')
ax.set_xlabel('Peso')
ax.set_ylabel('Altura')

plt.savefig('images/people_4.png')
