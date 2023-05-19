import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Leggi i dati dal file CSV
data = pd.read_csv('C:\\Users\\masto\\OneDrive\\Desktop\\nome_file.csv')

# Estrai le colonne di pressione e temperatura
X = data.iloc[:, 1].values.reshape(-1, 1)
y = data.iloc[:, 0].values.reshape(-1, 1)

# Crea un'istanza di LinearRegression e addestra il modello sui dati
model = LinearRegression()
model.fit(X, y)

# Calcola l'errore sull'intercetta della retta di regressione
n = len(X)
mean_x = np.mean(X)
var_x = np.var(X, ddof=1)
MSE = np.mean((model.predict(X) - y) ** 2)
errore_intercetta = np.sqrt(MSE * ((1 / n) + (mean_x ** 2 / ((n - 1) * var_x))))

# Calcola l'errore sulla stima del valore di intersezione della retta di regressione
errore_pressione = 1 # Pascal
errore_temperatura = 0.1 # gradi Celsius
m = model.coef_[0][0]
errore_intersezione = np.sqrt((errore_pressione / m)**2 + ((errore_temperatura / m) * mean_x)**2 + errore_intercetta**2)

# Stampa i parametri del modello e l'errore sulla stima dell'intercetta
print("Coefficiente angolare: ", model.coef_[0][0])
print("Intercetta: ", model.intercept_[0])
print("R^2 score: ", model.score(X, y))
print("MSE: ", MSE)
print("Errore sull'intercetta: ", errore_intercetta)
print("Errore sulla stima del valore di intersezione: ", errore_intersezione)
