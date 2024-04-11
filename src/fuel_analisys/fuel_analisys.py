import os
import pandas as pd
# import matplotlib.pyplot as plt

# get file full path
file_path = os.path.join(os.path.dirname(__file__), 'COMBUSTIVEIS.csv')
df = pd.read_csv(file_path)
print(df)

# variancia dos preços por cidade e tipo de combustivel
print("Variância dos preços por cidade e tipo de combustivel")
print(df.groupby(['CIDADE', 'COMBUSTIVEL'])['PRECO'].var())
print("------------------------")

# desvio padrão dos preços por cidade e tipo de combustivel
print("Desvio padrão dos preços por cidade e tipo de combustivel")
print(df.groupby(['CIDADE', 'COMBUSTIVEL'])['PRECO'].std())
print("------------------------")

# desvio padrão dos preços por tipo de combustível
print("Desvio padrão dos preços por tipo de combustível")
print(df.groupby(['COMBUSTIVEL'])['PRECO'].std())
print("------------------------")

# variancia dos preços por tipo de combustível
print("Variância dos preços por tipo de combustível")
print(df.groupby(['COMBUSTIVEL'])['PRECO'].var())
print("------------------------")

# média dos preços por cidade e tipo de combustivel
print("Média dos preços por cidade e tipo de combustivel")
print(df.groupby(['CIDADE', 'COMBUSTIVEL'])['PRECO'].mean())
print("------------------------")

# média dos preços por tipo de combustível
print("Média dos preços por tipo de combustível")
print(df.groupby(['COMBUSTIVEL'])['PRECO'].mean())
print("------------------------")

# mediana dos preços por cidade e tipo de combustivel
print("Mediana dos preços por cidade e tipo de combustivel")
print(df.groupby(['CIDADE', 'COMBUSTIVEL'])['PRECO'].median())
print("------------------------")

# mediana dos preços por tipo de combustível
print("Mediana dos preços por tipo de combustível")
print(df.groupby(['COMBUSTIVEL'])['PRECO'].median())
print("------------------------")

# posto com o combustivel de maior preco por cidade
print("Posto com o combustivel de maior preco por cidade")
print(df.loc[df.groupby(['CIDADE'])['PRECO'].idxmax()])
print("------------------------")

# posto com o combustivel de menor preco por cidade
print("Posto com o combustivel de menor preco por cidade")
print(df.loc[df.groupby(['CIDADE'])['PRECO'].idxmin()])
print("------------------------")
