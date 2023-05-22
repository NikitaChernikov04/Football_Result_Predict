import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# загрузка датасета
data = pd.read_csv('football_scores.csv')
print(data.to_string())
# кодирование категориальных признаков
le = LabelEncoder()
data['Home'] = le.fit_transform(data['Home'])
data['Guest'] = le.fit_transform(data['Guest'])

# разделение датасета на признаки и целевую переменную
X = data[['Home Score', 'Guest Score']]
y = data['Result']

# разделение датасета на обучающую и тестовую выборки
train_size = int(0.7 * len(data))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# создание объекта линейной регрессии
regressor = LinearRegression()

# обучение модели на обучающей выборке
regressor.fit(X_train, y_train)

# оценка точности модели на тестовой выборке
score = regressor.score(X_test, y_test)

# Создание объектов для графика регрессии и точек данных
fig, ax = plt.subplots()
ax.scatter(X_test['Home Score'], y_test, color='black')

# Вычисление предсказанных значений целевой переменной на тестовой выборке
y_pred = regressor.predict(X_test)

# Добавление линии регрессии на график
ax.plot(X_test['Home Score'], y_pred, color='blue', linewidth=3)

# Добавление заголовка и меток осей на график
ax.set_title('Linear Regression')
ax.set_xlabel('Home Score')
ax.set_ylabel('Result')

# Отображение графика на экране
plt.show()

print('Точность модели на тестовой выборке: {:.2f}'.format(score))

# Load the dataset
data = pd.read_csv('football_scores.csv')

# Transform the result of the matches into a continuous scale
data['result'] = data['score'].apply(lambda x: int(x.split(':')[0]) - int(x.split(':')[1]))

# Encode the categorical features
data = pd.get_dummies(data, columns=['Home', 'Guest'])

# Split the dataset into features and target variables
X = data.drop(['score', 'result'], axis=1)
y = data['result']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create an XGBoost regressor object
xgb_reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=3)

# Fit the regressor to the training set
xgb_reg.fit(X_train, y_train)

# Predict the target variable on the testing set
y_pred = xgb_reg.predict(X_test)

# Evaluate the accuracy of the model on the testing set
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print('RMSE:', rmse)

# Compute the predicted values on the testing set
y_pred = xgb_reg.predict(X_test)

# Create objects for regression and data points
reg_line = np.linspace(y_test.min(), y_test.max(), 100)
data_points = plt.scatter(y_test, y_pred)

# Add a regression line
plt.plot(reg_line, reg_line, color='red')

# Set the title and labels of the plot
plt.title('Regression Plot')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')

# Show the plot
plt.show()