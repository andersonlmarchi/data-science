import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv('files/anotacoes.txt', sep='\t', header=None, names=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'])
print(df)

# a. Medida padrão para decisão de venda
# Aqui, vamos assumir que a melhor medida padrão é a média
media = df.mean()
print(f'Média da circunferência:\n{media}')

# b. Identificar mudanças significativas entre grupos
# Aqui, vamos dividir os dados em dois grupos baseados na média e comparar as médias dos grupos
grupo1 = df[df < media]
grupo2 = df[df >= media]

media_grupo1 = grupo1.mean()
media_grupo2 = grupo2.mean()

print(f'Média do Grupo 1: \n{media_grupo1} \nMédia do Grupo 2: \n{media_grupo2}')

# c. Verificar anotações erradas
# Aqui, vamos considerar anotações erradas como aquelas que são 3 desvios padrão longe da média
desvio_padrao = df.std()
anotacoes_erradas = df[(df < media - 3*desvio_padrao) | (df > media + 3*desvio_padrao)]

print(f'Anotações erradas: \n{anotacoes_erradas}')

# d. Diagrama de dispersão
for column in df.columns:
    plt.scatter(df.index, df[column])

plt.title('Diagrama de Dispersão')
plt.xlabel('Índice')
plt.ylabel('Circunferência')
plt.savefig('images/diagrama_dispersao.png')

# e. Histogramas
df.hist(bins=4)
plt.title('Histograma')
plt.xlabel('Circunferência')
plt.ylabel('Frequência')
plt.savefig('images/histograma.png')