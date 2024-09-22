
# Primera lista
lista_punto_4 = [5, "mayo", 3.1415926535]

# 4.1
ultimo_valor = lista_punto_4[-1]
print("Último valor:", ultimo_valor)

# 4.2
elementos_inversos = lista_punto_4[::-1]
print("Elementos en orden inverso:", elementos_inversos)

# 4.3
primeros_dos_valores = lista_punto_4[:2]
print("Primeros 2 valores:", primeros_dos_valores)

# 4.4
lista_punto_4.insert(-1, "diplo_datos_ucse")
print("Lista con la palabra agregada:", lista_punto_4)

# 4.5
del lista_punto_4[1]
print("Lista después de eliminar el segundo elemento:", lista_punto_4)

# Punto 5
for elemento in lista_punto_4:
    try:
        print("Mayúsculas:", elemento.upper())
        print("Multiplicado por 2:", elemento * 2)
    except AttributeError:
        print(f"Error: No se puede convertir a mayúsculas - Elemento: {elemento}")
    except TypeError:
        print(f"Error: No se puede multiplicar - Elemento: {elemento}")
