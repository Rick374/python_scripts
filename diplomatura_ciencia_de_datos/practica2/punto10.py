#Punto 10
def fibonacci(n):
    # Inicializar los primeros dos valores de la secuencia
    a, b = 0, 1

    # Imprimir los primeros n valores de Fibonacci
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b

# Ejemplo de uso: Imprimir los primeros 10 valores de Fibonacci
n = 10
fibonacci(n)
