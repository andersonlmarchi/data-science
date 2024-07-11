from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Carregamento a partir do Dataset em \\anaconda3\pkgs\scikit-learn-0.24.2-py39hf11a4ad_1\Lib\site-packages\sklearn\datasets\data
dados = load_breast_cancer()

#Lista da Variável de Classificação - Hipóteses Diagnósticas (Saída)
nome_classes_hipoteses = dados['target_names']

#Lista da Classificação binária das entradas do DataSet: 0 - Maligno, 1 - Benigno
dados_hipoteses = dados['target']

#Lista dos atributos - são as evidências apresentadas ao classificador bayesiano
nome_evidencias = dados['feature_names']
dados_evidencias = dados['data']

# Visualização das listas
print("Nome das classes de saída: H1 = ",nome_classes_hipoteses[0]," e H2 = ",nome_classes_hipoteses[1])
print("Registro 1 do Dataset = ", dados_hipoteses[0])
print("Nomes dos atributos: evidências da Rede:")
c=1
for k in nome_evidencias:
    print(c,".",k)
    c+=1
print("Valores das evidências do 1o. registro do DataSet = ",dados_evidencias[0])

# Contagem de casos do jeito bruto
cont0=0
cont1=0
for k in dados_hipoteses:
    if(k==0):
        cont0+=1
    else:
        cont1+=1
print("Casos Malignos = ",cont0)
print("Casos Benignos = ",cont1)

# Divisão dos conjuntos de Treinamento e de Teste
evidencias_treino, evidencias_teste, hipoteses_treino, hipoteses_teste = train_test_split(dados_evidencias,dados_hipoteses,
                                                          test_size=0.3)

# Aplica o classificador NaiveBayes Gaussiano
classificador = GaussianNB()

# Aplica o treinamento
modelo = classificador.fit(evidencias_treino, hipoteses_treino)

# Realizar previsões - inferência preditiva
predicao = classificador.predict(evidencias_teste)
print(predicao)

# Mostrar a acurácia ou precisão do aprendizado sobre os novos dados (conjunto de teste)
precisao = accuracy_score(hipoteses_teste, predicao)
print("Precisão = ",round(precisao*100,2)," %")

# predição de um novo caso 1
novas_evidencias = [21.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471,0.2419, 0.7871, 1.095, 0.9053, 8.589, 153.4,
                    0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019, 0.1622, 0.6656,
                    0.7119, 0.2654, 0.4601, 0.1189]
diagnostico=classificador.predict([novas_evidencias])
print(diagnostico)

# predição de um novo caso 2
novas_evidencias =[13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,
                   0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259]
diagnostico=classificador.predict([novas_evidencias])
print(diagnostico)