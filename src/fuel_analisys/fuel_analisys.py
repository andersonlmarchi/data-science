# Importar as bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Carregar o arquivo CSV
df = pd.read_csv('files/COMBUSTIVEIS.csv')

# Visualizar os primeiros registros do dataframe
print(df.head())

# Calcular estatísticas descritivas para cada cidade e tipo de combustível
statistics = df.groupby(['CIDADE', 'COMBUSTIVEL']).agg(
    media_preco=('PRECO', 'mean'),
    mediana_preco=('PRECO', 'median'),
    desvio_padrao=('PRECO', 'std'),
    variancia=('PRECO', 'var')
).reset_index()

print(statistics)

# Configurar o estilo do seaborn
sns.set_theme(style="whitegrid")

# Criar visualizações para cada tipo de combustível comparando entre as cidades
def plot_fuel_prices_by_fuel(df):
    unique_fuels = df['COMBUSTIVEL'].unique()
    fig_paths = []
    
    for fuel in unique_fuels:
        fuel_data = df[df['COMBUSTIVEL'] == fuel]
        plt.figure(figsize=(12, 6))
        palettes = sns.color_palette("husl", len(df['CIDADE'].unique()))
        sns.boxplot(x='CIDADE', y='PRECO', hue='CIDADE', data=fuel_data, palette=palettes, legend=False)
        plt.title(f'Preços do {fuel.capitalize()} nas Cidades')
        plt.xlabel('Cidade')
        plt.ylabel('Preço (R$)')
        
        # Definir a escala do eixo y a cada 20 centavos, específico para cada combustível
        min_price = fuel_data['PRECO'].min()
        max_price = fuel_data['PRECO'].max()
        plt.yticks([round(x, 2) for x in np.arange(min_price, max_price + 0.2, 0.2)])
        
        # Salvar a figura
        fig_path = f'images/precos_{fuel.lower()}_cidades.png'
        plt.savefig(fig_path)
        plt.close()
        fig_paths.append(fig_path)
    
    return fig_paths

# Plotar e salvar as visualizações
fig_paths = plot_fuel_prices_by_fuel(df)
for path in fig_paths:
    print(f'Figura salva em: {path}')
