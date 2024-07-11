import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

houses = pd.read_csv('files/moradias2.csv')

print(houses.head())

print(houses.describe())

print(houses.info())

## KNN para regressão

x = houses[['bedrooms', 'bathrooms', 'size_sqft']]
y = houses['rent']

# Normalizing the dataset
normalizer = MinMaxScaler()
x = normalizer.fit_transform(x)

# Dividing the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

# Training the model with the training set
knn = KNeighborsRegressor(n_neighbors = 50)
knn.fit(x_train, y_train)

# Predicting the rent values
y_pred = knn.predict(x_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared = False)
r2 = r2_score(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print(f'Erro Quadrático Médio (MSE): {mse:.2f}')
print(f'Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f}')
print(f'Coeficiente de Determinação (R²): {r2:.2f}')
print(f'Erro Percentual Absoluto Médio (MAPE): {mape:.2f}%')
