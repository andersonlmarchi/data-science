from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
import pandas as pd

# carregando CANDIDATOS.CSV
dados = pd.read_csv('files/CANDIDATOS.csv')

evidencias_treino, evidencias_teste, hipoteses_treino, hipoteses_teste = train_test_split(dados.iloc[:,0:9],dados['S'],
                                                                                          random_state=0, test_size=0.3)
                                                         
# Aplica o classificador NaiveBayes Categórico
classificador = CategoricalNB()


# Aplica o treinamento
modelo = classificador.fit(evidencias_treino, hipoteses_treino)

# Realizar previsões - inferência preditiva
predicao = classificador.predict(evidencias_teste)

print(evidencias_teste)
print(predicao)

# Mostrar a acurácia ou precisão do aprendizado sobre os novos dados (conjunto de teste)
precisao = accuracy_score(hipoteses_teste, predicao)
print("Precisão = ",round(precisao*100,2)," %")
