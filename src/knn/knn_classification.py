import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, classification_report

students = pd.read_csv('files/dados_alunos.csv')

print(students.head())

print(students.describe())

print(students.info())

## KNN para classificação
x = students[['hours_studied', 'practice_test']]
y = students['passed_exam']

scaler = MinMaxScaler()
x = scaler.fit_transform(x)

print(x)

knn = KNeighborsClassifier(n_neighbors = 3)

knn.fit(x, y.values.ravel())

y_pred = knn.predict(x)
print(y_pred)

cm = confusion_matrix(y, y_pred)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = ['Aprovado', 'Reprovado'])
disp.plot()
plt.show()
plt.clf()

print(f'Acurácia de: ', accuracy_score(y, y_pred) * 100, '%')

print(classification_report(y, y_pred))

# testando acurácia em relação ao número de vizinhos
neighbors = np.arange(1, len(x))
train_accuracy = np.empty(len(neighbors))

for k in range(1, len(x) - 1):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(x, y.values.ravel())
    train_accuracy[k] = knn.score(x, y)

k = 0
for i in train_accuracy:
    print(f'Número de vizinhos: {k + 1} - Acurácia: {i}')
    k += 1

plt.plot(neighbors, train_accuracy, label = 'Acurácia do conjunto de treino')
plt.legend()
plt.xlabel('Número de vizinhos')
plt.ylabel('Acurácia')
plt.show()
plt.clf()
