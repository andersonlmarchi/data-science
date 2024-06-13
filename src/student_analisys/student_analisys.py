# Importe as blibliotecas pandas, matplotlib e seaborn
import pandas as pd
import seaborn as sb

# Importe o dataset alunos para um Pandas Dataframe
df = pd.read_csv('files/alunos.csv')

# O dataframe fornecido (`alunos`) inclui as seguintes variáveis/recursos:

# - `address`: localização da residência do aluno ( 'U'para urbano e 'R'para rural)
# - `absences`: o número de vezes que o aluno faltou durante o ano letivo
# - `Mjob`: profissão da mãe do aluno
# - `Fjob`: profissão do pai do aluno
# - `math_grade`: nota final do aluno em matemática, variando de 0 a 20

# Use o método `.head()` pandas para inspecionar as primeiras linhas de dados.
# 1. Use o método `.describe()` para imprimir estatísticas resumidas para todos os cinco recursos do conjunto de dados. Inspecione a saída. Mais estudantes vivem em locais urbanos ou rurais?
print(df.head())
print(df.describe(include = 'all'))

# 2. Vamos começar tentando resumir a coluna `math_grade`. Calcule e imprima a média da `math_grade`.
print('Média das notas de matemática:')
print(df['math_grade'].mean())

# 3. A seguir, calcule e imprima a mediana da variável `math_grade`. Compare esse valor com a média. É menor? maior?
print('Mediana das notas de matemática:')
print(df['math_grade'].median())

# 4. Por fim, calcule e imprima a moda da coluna `math_grade`. Qual é a nota mais comum obtida pelos alunos neste conjunto de dados? Quão diferente é esse número da média e da mediana?
print('Moda das notas de matemática:')
print(df['math_grade'].mode())

# 5. A seguir, vamos resumir a distribuição das notas dos alunos. Calcule e imprima a amplitude da coluna `math_grade`. 
print('Amplitude das notas de matemática:')
print(df['math_grade'].max() - df['math_grade'].min())

# 6.  Calcule e imprima o desvio padrão da coluna `math_grade`. Cerca de dois terços dos valores estão dentro de um desvio padrão da média. O que esse número diz sobre a variação das notas em matemática?
print('Desvio padrão das notas de matemática:')
print(df['math_grade'].std())

### Visualize a distribuição das notas dos alunos
# 7. Agora que resumimos as notas dos alunos usando estatísticas de tendência central e dispersão, vamos visualizar a distribuição usando um histograma. Use a função `histplot()` da biblioteca seaborn para criar um histograma da coluna `math_grade`.
print('Histograma das notas de matemática:')
sb.histplot(df['math_grade'])

# 8. Outra forma de visualizar a distribuição de uma variável quantitativa é por meio de um gráfico box plot. Use a função `boxplot()` para criar um boxplot da coluna `math_grade`.
print('Boxplot das notas de matemática:')
sb.boxplot(x=df['math_grade'])

### Resuma o trabalho das mães
#9. A coluna `Mjob` do conjunto de dados contém informações sobre o que as mães dos alunos fazem como profissão. Resuma a coluna `Mjob` imprimindo o número de alunos que têm mães em cada tipo de trabalho. Qual valor de `Mjob` é mais comum?
print('Resumo do trabalho das mães:')
print(df['Mjob'].value_counts())

# 10. Agora, calcule e imprima a **proporção** de alunos que têm mães em cada tipo de trabalho. Qual a proporção de estudantes que têm mães que trabalham na área da saúde?
print('Proporção do trabalho das mães:')
print(df['Mjob'].value_counts(normalize=True))

### Visualize a distribuição dos empregos das mães
# 11. Agora que usamos estatísticas resumidas para entender as frequências relativas dos empregos de diferentes mães, vamos visualizar as mesmas informações em um gráfico de barras. Use a função `countplot()` da biblioteca seaborn para criar um gráfico de barras da variável `Mjob`.
print('Gráfico de barras do trabalho das mães:')
sb.countplot(x=df['Mjob'])

# 12. Também podemos visualizar as mesmas informações usando um gráfico de pizza. Crie um gráfico de pizza da coluna `Mjob`.
print('Gráfico de pizza do trabalho das mães:')
df['Mjob'].value_counts().plot.pie()
