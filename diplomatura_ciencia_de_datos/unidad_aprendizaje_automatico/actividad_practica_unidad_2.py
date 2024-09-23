# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# Cargar el dataset de diabetes
diabetes = datasets.load_diabetes()

# Imprimir el dataset para visualizarlo
print(diabetes, "\n")

# Utilizar la función keys para entender la disposición de los datos
print("Información del dataset")
print(diabetes.keys(), "\n")

# Utilizar la función DESCR para un conocimiento más profundo de los datos
print(diabetes.DESCR, "\n")

# Diccionario para mapear índices a nombres de variables
variables = {
    0: "edad",
    1: "sexo",
    2: "indice de masa corporal",
    3: "presion sanguinea promedio",
    4: "colesterol total",
    5: "LDL",
    6: "HDL",
    7: "colesterol total / HDL",
    8: "LTG (trigliceridos)",
    9: "azucar en sangre (glucosa)"
}

# Función para seleccionar la variable independiente por índice
def seleccionar_variable(indice_variable):
    if indice_variable in variables:
        return diabetes.data[:, np.newaxis, indice_variable], variables[indice_variable]
    else:
        raise ValueError("Índice de variable no válido")

# Seleccionar la variable independiente (por ejemplo, el índice de masa corporal)
indice_variable = 0  # Cambia este valor para seleccionar otra variable
diabetes_X, nombre_variable = seleccionar_variable(indice_variable)

# Variable dependiente
diabetes_y = diabetes.target

# Graficar los puntos de la característica seleccionada
plt.scatter(diabetes_X, diabetes_y)
plt.xlabel(nombre_variable.capitalize())
plt.ylabel('Progresión de la Diabetes')
plt.show()

# Seleccionar el modelo, entrenarlo y hacer una predicción
model = linear_model.LinearRegression()
model.fit(diabetes_X, diabetes_y)

# Hacer una predicción
diabetes_y_pred = model.predict(diabetes_X)

# Graficar la línea de regresión
plt.scatter(diabetes_X, diabetes_y)
plt.plot(diabetes_X, diabetes_y_pred, color='red')
plt.xlabel(nombre_variable.capitalize())
plt.ylabel('Progresión de la Diabetes')
plt.show()

# Imprimir los coeficientes
print('Coeficiente: \n', model.coef_, "\n")
print('Intercepción: \n', model.intercept_, "\n")
