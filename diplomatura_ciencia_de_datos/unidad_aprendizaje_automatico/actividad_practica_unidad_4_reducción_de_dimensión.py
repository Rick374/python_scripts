import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el dataset de dígitos
digits = load_digits()

# Información del dataset
print("Shape of data:", digits.data.shape)
print("Shape of target:", digits.target.shape)

# Dividir datos en entrenamiento y prueba (80/20)
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Definir el clasificador RandomForest
rf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, max_features='log2', random_state=42)

# Entrenar el modelo
rf.fit(X_train, y_train)

# Realizar predicciones
y_pred = rf.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

# Visualización de importancia de características
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Graficar las 10 características más importantes
plt.figure()
plt.title("Importancias de Características")
plt.bar(range(10), importances[indices[:10]], align="center")
plt.xticks(range(10), indices[:10])
plt.xlabel("Índices de Características")
plt.ylabel("Importancia de la Característica")
plt.xlim([-1, 10])
plt.show()
