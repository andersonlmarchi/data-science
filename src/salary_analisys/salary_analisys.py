import pandas as pd

c1 = {
    'nome': ['João', 'Pedro', 'Maria', 'Ana', 'Snadra'],
    'idade': [40, 35, 53, 17, 28],
    'salario': [1500, 3500, 2600, 3500, 5000],
}

df1 = pd.DataFrame(c1)

# somatoria dos salarios
print("Somatória dos salários")
print(df1['salario'].sum())
print("------------------------")

# media dos salarios
print("Média dos salários")
print(df1['salario'].mean())
print("------------------------")

# menor idade
print("Menor idade")
print(df1['idade'].min())
print("------------------------")

# media de idades
print("Média de idades")
print(df1['idade'].mean())
print("------------------------")

# imprimir idades
print("Idades")
print(df1['idade'])
print("------------------------")

# mediana das idades
print("Mediana das idades")
print(df1['idade'].median())
print("------------------------")

# moda dos salários
print("Moda dos salários")
print(df1['salario'].mode())
print("------------------------")

# desvio padrão das idades
print("Desvio padrão das idades")
print(df1['idade'].std())
print("------------------------")


c2 = {
    'nome': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z'],
    'idade': [32, 19, 25, 48, 65, 53, 41, 26, 43, 28, 70, 37, 33, 28, 40, 17, 21, 25, 27, 51, 18, 62, 35, 29, 19, 38],
    'sexo': ['F', 'F', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F'],
    'escolaridade': ['SUPERIOR', 'MÉDIO', 'MÉDIO', 'FUNDAMENTAL', 'MÉDIO', 'MÉDIO', 'FUNDAMENTAL', 'FUNDAMENTAL', 'SUPERIOR', 'FUNDAMENTAL', 'MÉDIO', 'FUNDAMENTAL', 'SUPERIOR', 'SUPERIOR', 'FUNDAMENTAL', 'FUNDAMENTAL', 'MÉDIO', 'MÉDIO', 'FUNDAMENTAL', 'SUPERIOR', 'MÉDIO', 'FUNDAMENTAL', 'FUNDAMENTAL', 'SUPERIOR', 'SUPERIOR', 'MÉDIO'],
    'salario': [7400, 1800, 2050, 1300, 1900, 1750, 1500, 1450, 5200, 1650, 3400, 1450, 3850, 4100, 1380, 1400, 9100, 1600, 1500, 3500, 2300, 1350, 1600, 6700, 3900, 2500]
}

df2 = pd.DataFrame(c2)
print("Dataframe 2")
print(df2)

# média salarial por sexo
print("Média salarial por sexo")
print(df2.groupby('sexo')['salario'].mean())
print("------------------------")

# media salarial por escolaridade
print("Média salarial por escolaridade")
print(df2.groupby('escolaridade')['salario'].mean())
print("------------------------")

# desvio padrão dos salários de escolaridade MÉDIO
print("Desvio padrão dos salários de escolaridade MÉDIO")
print(df2[df2['escolaridade'] == 'MÉDIO']['salario'].std())
print("------------------------")

# escolaridade mais frequente e quantas vezes essa moda aparece no conjunto
print('Escolaridade mais frequente do conjunto é ', df2['escolaridade'].mode().max(), ' com ', df2['escolaridade'].value_counts().max(), ' ocorrências.')
print("------------------------")

# 3 maiores salários
print("3 maiores salários")
print(df2.nlargest(3, 'salario'))
print("------------------------")

# 3 menores salários
print("3 menores salários")
print(df2.nsmallest(3, 'salario'))
print("------------------------")

# separar salários por escolaridade e obter os quantis (25%)
print("Separar salários por escolaridade e obter os quantis (25%)")
print("0º quantil")
print(df2.groupby('escolaridade')['salario'].quantile(0))
print("------------------------")
print("1º quantil")
print(df2.groupby('escolaridade')['salario'].quantile(0.25))
print("------------------------")
print("2º quantil")
print(df2.groupby('escolaridade')['salario'].quantile(0.50))
print("------------------------")
print("3º quantil")
print(df2.groupby('escolaridade')['salario'].quantile(0.75))
print("------------------------")
print("4º quantil")
print(df2.groupby('escolaridade')['salario'].quantile(1))
print("------------------------")

# discrepância de salários por escolaridade
print("Discrepância de salários por escolaridade")
print(df2.groupby('escolaridade')['salario'].max() - df2.groupby('escolaridade')['salario'].min())
print("------------------------")

# discrepância por descio padrão de salários por escolaridade
print("Discrepância por descio padrão de salários por escolaridade")
print(df2.groupby('escolaridade')['salario'].std())
print("------------------------")