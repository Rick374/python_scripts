#Punto 7
def escribir(nombre_archivo, lista_elementos):
    with open(nombre_archivo, "w") as archivo:
        # Escribir cada elemento de la lista en una línea separada
        for elemento in lista_elementos:
            archivo.write(str(elemento) + "\n")
    print(f"Los elementos se han guardado en el archivo '{nombre_archivo}'.")

# Ejemplo de uso
mi_lista = ["Hola", "mundo", 123, "Python", 3.14]
nombre_archivo = "archivo_punto7.txt"
escribir(nombre_archivo, mi_lista)
