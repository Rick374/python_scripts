from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score

# Cargar el dataset de cáncer de pecho de Wisconsin
data = load_breast_cancer()
X = data.data
y = data.target

# Separar los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Naive Bayes
algoritmo = GaussianNB()

# Entrenando el modelo
algoritmo.fit(X_train, y_train)

# Realizar una predicción
y_pred = algoritmo.predict(X_test)

# Calcular la precisión del modelo
precision = precision_score(y_test, y_pred)

print("Precisión del modelo: {:.2f}%".format(precision * 100))
