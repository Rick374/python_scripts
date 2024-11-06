import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Cargar dataset de ejemplo
data = load_iris()
X = data.data
y = data.target

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Valores de K y p para experimentar
k_values = [3, 5, 7, 9, 11]
p_values = [1, 2]

# Listas para almacenar precisiones
accuracies = []

# Realizar predicciones
num_predictions = 50
for i in range(num_predictions):
    k = k_values[i // 10]  # Cambiar K cada 10 predicciones
    p = p_values[(i // 10) % 2]  # Cambiar p cada 10 predicciones y alternar entre 1 y 2

    knn = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=p)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Predicción {i + 1}: K={k}, p={p}, Precisión={accuracy:.2f}')

# Graficar las precisiones
plt.plot(range(1, num_predictions + 1), accuracies, marker='o')
plt.xlabel('Número de Predicciones')
plt.ylabel('Precisión')
plt.title('Precisión vs. Número de Predicciones')
plt.grid(True)
plt.show()
