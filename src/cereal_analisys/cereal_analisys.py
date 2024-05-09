import pandas as pd

cereals = pd.read_csv('files/cereais.csv', index_col=0)

# visualizando as primeiras linhas
print(cereals.head())
print('-----------------------------------------')

# tipos de dados
print(cereals.dtypes)
print('-----------------------------------------')

# informações
print(cereals.info())
print('-----------------------------------------')

# categorias de shelf
print(cereals['shelf'].unique())
print('-----------------------------------------')

# categorias de type
print(cereals['type'].unique())
print('-----------------------------------------')

# elimina os NaN da coluna shelf
cereals = cereals.dropna(subset=['shelf'])
print('-----------------------------------------')

# imprime as infos
print(cereals.info())
print('-----------------------------------------')

# converte name e mfr para string
cereals['name'] = cereals['name'].astype('string')
cereals['mfr'] = cereals['mfr'].astype('string')

# imprime as infos
print(cereals.info())
print('-----------------------------------------')

# categorizar a coluna shelf
cereals['shelf'] = pd.Categorical(cereals['shelf'], ['bottom', 'middle', 'top'], ordered=True)

# imprime as infos
print(cereals.info())
print('-----------------------------------------')

# criando codificação one hot para a coluna mfr
cereals = pd.get_dummies(cereals, columns=['mfr'])

# imprime o cabeçcalho do dataset
print(cereals.head())
print('-----------------------------------------')
