import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

students = pd.read_csv('files/alunos2.csv')
print(students.head())

print(students.info())

print(students.describe(include = 'all'))

## Associação entre variáveis
### Entre variável quantitativa e categórica
# 1. Pontuação de cada endereço (urbano ou rural) em duas listas separadas
score_urban = students.G3[students.address == 'U']
score_rural = students.G3[students.address == 'R']

media_urban = np.mean(score_urban)
media_rural = np.mean(score_rural)

print('Média das notas de alunos urbanos:', media_urban)
print('Média das notas de alunos rurais:', media_rural)

# Bloxplot comparando as notas dos alunos urbanos e rurais
#sb.boxplot(data= students, x = students.address, y = students.G3)

# Histogramas sobrepostos
plt.hist(score_rural, color='red', alpha = 0.5, density=True, label = 'Rural')
plt.hist(score_urban, color='blue', alpha = 0.5, density=True, label = 'Urbano')

plt.legend()

plt.xlabel('Pontuação')
plt.savefig('images/associacao_entre_variaveis.png')

plt.clf()

# Gera a figura com 1 linha e 2 colunas
fig, asx = plt.subplots(1, 2, figsize = (10, 5))

# Plota o boxplot no primeiro subplot
sb.boxplot(data = students, x = 'address', y = 'G3', ax=asx[0])
asx[0].set_title('Boxplot')

# Plota os histogramas sobrepostos no segundo subplot
asx[1].hist(score_rural, color='red', alpha = 0.5, density=True, label = 'Rural')
asx[1].hist(score_urban, color='blue', alpha = 0.5, density=True, label = 'Urbano')
asx[1].set_title('Histogramas sobrepostos')
asx[1].set_xlabel('Pontuação')
asx[1].set_ylabel('Densidade')
asx[1].legend()

# Ajusta o espaçamento entre os subplots
plt.tight_layout()
plt.savefig('images/associacao_entre_variaveis2.png')

plt.clf()

# Cria uma figura com 1 linha e 2 colunas
fig, asx = plt.subplots(1, 2, figsize = (10, 5))

sb.boxplot(data = students, x = 'Mjob', y = 'G3', ax=asx[0])
asx[0].set_title('Boxplot da Profissão da Mãe')
sb.boxplot(data = students, x = 'Fjob', y = 'G3', ax=asx[1])
asx[1].set_title('Boxplot da Profissão do Pai')

plt.tight_layout()
plt.savefig('images/associacao_entre_variaveis3.png')
