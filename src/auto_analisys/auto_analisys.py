# Import pandas
import pandas as pd

# Importe o dataset autos para um Pandas Dataframe
auto = pd.read_csv('files/autos.csv', index_col=0)

#1 Retorne as primeiras 10 linhas do dataframe.
print(auto.head(10))
print('-----------------------------------------')

#2 Retorne os tipos de dados do dataframe com o comando .dtypes
print(auto.dtypes)
print('-----------------------------------------')

#3 Altere a price categoria de int para float com o método .astype() e verifique novamente os tipos de dados com .dtypes.
auto['price'] = auto['price'].astype('float')
print(auto.dtypes)
print('-----------------------------------------')

#4 Converta a variável engine_size para o tipo de dados category com uma ordem de [‘small’, ‘medium’, ‘large’] e verifique a ordem com o método .unique().
auto['engine_size'] = pd.Categorical(auto['engine_size'], ['small', 'medium', 'large'])
print(auto['engine_size'].unique())
print('-----------------------------------------')

#5 Cria uma codificação One_Hot para a variável body-style. Em seguida, verifique o dataframe com .head()
auto = pd.get_dummies(auto, columns=['body-style'])
print(auto.head())
print('-----------------------------------------')

#6 Crie uma nova variável chamada engine_codes que contém os códigos numéricos associados a cada categoria na variável engine_size com o comando .cat.code. Verifique os novos valores com o método .head().
auto['engine_codes'] = auto['engine_size'].cat.codes
print(auto['engine_codes'].unique())
print(auto.head(30))
print('-----------------------------------------')
