# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar el dataset digits
digits = load_digits()

# Crear un DataFrame de pandas con los datos y las etiquetas
df = pd.DataFrame(data=digits.data, columns=[f'pixel_{i}' for i in range(digits.data.shape[1])])
df['target'] = digits.target

# Exportar el DataFrame a un archivo CSV
df.to_csv('digits_dataset.csv', index=False)

print("Datos exportados a digits_dataset.csv")

# Mostrar información del dataset
print("Shape of the dataset:", digits.data.shape)
print("Number of classes:", len(digits.target_names))

# Separar el dataset en conjuntos de entrenamiento (80%) y test (20%)
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Crear el clasificador de red neuronal por perceptrón de múltiples capas
mlp = MLPClassifier(hidden_layer_sizes=(13, 13, 13), max_iter=500)

# Entrenar el modelo
mlp.fit(X_train, y_train)

# Realizar predicciones
predictions = mlp.predict(X_test)

# Evaluar la precisión del modelo
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Mostrar algunas imágenes de prueba y sus predicciones
fig, axes = plt.subplots(2, 4, figsize=(8, 4))
for ax, image, prediction, label in zip(axes.ravel(), X_test, predictions, y_test):
    ax.imshow(image.reshape(8, 8), cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'P: {prediction}, T: {label}')
    ax.axis('off')

plt.show()
