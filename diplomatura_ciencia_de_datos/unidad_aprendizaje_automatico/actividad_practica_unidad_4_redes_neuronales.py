import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Cargar el dataset de dígitos
digits = load_digits()

# Información del dataset
print("Shape of data:", digits.data.shape)
print("Shape of target:", digits.target.shape)

# Dividir datos en entrenamiento y prueba (80/20)
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Definir el clasificador por perceptrón de multi-capa
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, alpha=0.0001, solver='adam', random_state=42)

# Entrenar el modelo
mlp.fit(X_train, y_train)

# Realizar predicciones
y_pred = mlp.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

# Imprimir el reporte de clasificación y matriz de confusión
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))

# Graficar algunas predicciones
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.ravel()):
    ax.imshow(X_test[i].reshape(8, 8), cmap=plt.cm.gray_r)
    ax.set_title(f'Pred: {y_pred[i]} True: {y_test[i]}')
    ax.axis('off')
plt.show()
