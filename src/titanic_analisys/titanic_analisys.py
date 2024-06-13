# Analise o conjunto de dados `titanic`. 
# Estes dados contêm informações sobre os passageiros do Titanic, incluindo o valor que pagaram 
# pela passagem e se sobreviveram ou não (nota: este é um subconjunto dos dados completos disponíveis). 
# Para praticar as habilidades aprendidas nesta aula, vamos investigar se existe uma associação entre a 
# tarifa que um passageiro pagou ( `Fare`) e se ele sobreviveu ou não (`Survived`, que é igual a `0` se 
# o passageiro morreu e `1` se sobreviveu):

# - Calcule a diferença na tarifa **média** paga pelos que sobreviveram e pelos que morreram. Qual grupo pagou uma tarifa média mais alta?
# - Calcule a diferença na tarifa **mediana** entre aqueles que sobreviveram e aqueles que morreram.
# - Crie gráficos boxplot relacionando as variáveis de tarifas e sobrevivência. Agora que você pode ver a distribuição dos dados, as 
#   diferenças médias/medianas parecem relativamente pequenas ou grandes?
# - Crie histogramas sobrepostos de tarifas por sobrevivência. Isso fornece alguma informação adicional?

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

titanic = pd.read_csv('files/titanic.csv')
print(titanic.head())
print(titanic.info())
print(titanic.describe(include = 'all'))

# Separa os grupos em pessoas que morreram e sobreviveram
fare_survived = titanic.Fare[titanic.Survived == 1]
fare_died = titanic.Fare[titanic.Survived == 0]

# Calcula a diferença na tarifa média paga pelos que sobreviveram e pelos que morreram

mean_fare_survived = np.mean(fare_survived)
mean_fare_died = np.mean(fare_died)

print('Média da tarifa paga pelos que sobreviveram:', mean_fare_survived)
print('Média da tarifa paga pelos que morreram:', mean_fare_died)
print('Diferença entre as médias:', mean_fare_survived - mean_fare_died)

# Calcula a diferença na tarifa mediana entre aqueles que sobreviveram e aqueles que morreram
median_fare_survived = np.median(fare_survived)
median_fare_died = np.median(fare_died)

print('Mediana da tarifa paga pelos que sobreviveram:', median_fare_survived)
print('Mediana da tarifa paga pelos que morreram:', median_fare_died)
print('Diferença entre as medianas:', median_fare_survived - median_fare_died)

# Cria gráficos boxplot relacionando as variáveis de tarifas e sobrevivência
sb.boxplot(data = titanic, x = 'Survived', y = 'Fare')
plt.savefig('images/associacao_entre_variaveis_titanic.png')

plt.clf()

# Cria histogramas sobrepostos de tarifas por sobrevivência
plt.hist(fare_died, color='red', alpha = 0.5, density=True, label = 'Morreram')
plt.hist(fare_survived, color='blue', alpha = 0.5, density=True, label = 'Sobreviveram')

plt.legend()
plt.savefig('images/associacao_entre_variaveis_titanic2.png')
