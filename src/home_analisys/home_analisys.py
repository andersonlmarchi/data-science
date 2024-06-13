import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

home = pd.read_csv('files/moradias.csv')

print('Dados do cabeçalho')
print(home.head())

print('Informações" do dataframe')
print(home.info())

# Relação de Valor do aluguel pelo tamanho do imóvel
plt.scatter(x = home.size_sqft, y = home.rent)
plt.xlabel('Tamanho (pés quadrados)')
plt.ylabel('Valor Aluguel')

plt.savefig('images/home_analisys_valueXsize.png')

plt.clf()

# Relação de Valor do aluguel pela idade do imóvel
plt.scatter(x = home.building_age_yrs, y = home.rent)
plt.xlabel('Idade (anos)')
plt.ylabel('Valor Aluguel')

plt.savefig('images/home_analisys_valueXage.png')

plt.clf()

# Covariância
home_qtd = home.drop(columns=['neighborhood', 'borough', 'submarket'])
cov_mtx = home_qtd.cov()

# Covariância entre tamanho do imóvel e valor do aluguel
cov_size_rent = cov_mtx.loc['size_sqft', 'rent']
print(f'Covariância entre tamanho do imóvel e valor do aluguel: {cov_size_rent}')

# Covariância entre idade do imóvel e valor do aluguel
cov_age_rent = cov_mtx.loc['building_age_yrs', 'rent']
print(f'Covariância entre idade do imóvel e valor do aluguel: {cov_age_rent}')

# Correlação entre tamanho do imóvel e valor do aluguel
corr_size_rent = stats.pearsonr(home.size_sqft, home.rent)
print(f'Correlação entre tamanho do imóvel e valor do aluguel: {corr_size_rent}')

# Correlação entre idade do imóvel e valor do aluguel
corr_age_rent = stats.pearsonr(home.building_age_yrs, home.rent)
print(f'Correlação entre idade do imóvel e valor do aluguel: {corr_age_rent}')

# Matriz de correlação
corr = home_qtd.corr()
corr.style.background_gradient(cmap='coolwarm').format(precision = 2)

# Salvando a matriz de correlação
corr.to_csv('files/corr.csv')
