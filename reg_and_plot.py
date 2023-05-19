import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Leggi i dati dal file CSV
data = pd.read_csv('C:\\Users\\masto\\OneDrive\\Desktop\\frizer.csv')

# Estrai le colonne di pressione e temperatura
X = data.iloc[:, 1].values.reshape(-1, 1)
y = data.iloc[:, 0].values.reshape(-1, 1)

# Crea un'istanza di LinearRegression e addestra il modello sui dati
model = LinearRegression()
model.fit(X, y)

# Stampa i parametri del modello
print("Coefficiente angolare: ", model.coef_[0][0])
print("Intercetta: ", model.intercept_[0])
print("R^2 score: ", model.score(X, y))
print("MSE: ", np.mean((model.predict(X) - y) ** 2))


# Genera il grafico della pressione in funzione della temperatura e la retta di regressione lineare
#plt.scatter(X, y, color='blue')
#plt.plot(X, model.predict(X), color='red')
#plt.xlabel('Temperatura')
#plt.ylabel('Pressione')
#plt.title('Regressione lineare della pressione in funzione della temperatura')
#plt.show()
# Calcola il punto di intersezione con l'asse delle temperature
intercept_temp = -model.intercept_[0] / model.coef_[0][0]

# Crea un array di temperature per il grafico della retta di regressione
temp_range = np.linspace(X.min(), intercept_temp).reshape(-1, 1)

# Prevedi i valori di pressione corrispondenti alle temperature
y_pred = model.predict(temp_range)

# Crea un'istanza di LinearRegression e addestra il modello sui dati di temperatura e zero pressione
X2 = X.copy()
y2 = np.zeros_like(y)
model2 = LinearRegression()
model2.fit(X2, y2)

# Crea un grafico a dispersione dei dati e della retta di regressione
plt.scatter(X, y, color='b')
plt.plot(temp_range, y_pred, color='r')

# Aggiungi le etichette degli assi
plt.xlabel('Temperatura')
plt.ylabel('Pressione')

# Aggiungi una linea orizzontale a zero pressione
plt.axhline(0, color='black', lw=0.5)

# Mostra il punto di intersezione con l'asse delle temperature
plt.axvline(intercept_temp, color='black', linestyle='--')
plt.annotate(f'Temperatura di intersezione: {intercept_temp:.2f}', xy=(intercept_temp, 0),
             xytext=(intercept_temp, 2), ha='center', va='bottom',
             arrowprops=dict(arrowstyle='->', color='black'))

# Mostra il grafico
plt.show()