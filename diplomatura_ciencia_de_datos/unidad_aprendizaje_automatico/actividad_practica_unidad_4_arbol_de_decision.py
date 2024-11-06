import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Generamos un dataset aleatorio
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Parámetros para modificar max_depth y analizar el ajuste del modelo
max_depth_values = [2, 3, 4, 5, 6]

# Figura para graficar
plt.figure(figsize=(12, 8))

# Entrenar y graficar el modelo para diferentes valores de max_depth
for i, max_depth in enumerate(max_depth_values):
    regr = DecisionTreeRegressor(max_depth=max_depth)
    regr.fit(X, y)

    # Predicción
    X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
    y_pred = regr.predict(X_test)

    # Gráfico de entradas y salidas
    plt.subplot(3, 2, i + 1)
    plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="datos")
    plt.plot(X_test, y_pred, color="cornflowerblue", label=f"max_depth={max_depth}", linewidth=2)
    plt.xlabel("datos")
    plt.ylabel("objetivo")
    plt.title(f"Regresión con Árbol de Decisión\nmax_depth={max_depth}")
    plt.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
