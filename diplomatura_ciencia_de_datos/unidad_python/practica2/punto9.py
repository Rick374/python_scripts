#Punto 9
def escribir(nombre_archivo, lista_elementos):
    with open(nombre_archivo, "w") as archivo:
        # Escribir cada elemento de la lista en una línea separada
        for elemento in lista_elementos:
            archivo.write(str(elemento) + "\n")
    print(f"Los elementos se han guardado en el archivo '{nombre_archivo}'.")

def leer(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        # Leer cada línea y mostrarla
        for linea in archivo:
            print(linea.strip())  # Elimina los saltos de línea al final
    print(f"Contenido del archivo '{nombre_archivo}':")

lista_punto9 = ['Argentina', 46044703, 'Buenos Aires', 2780400, 'peso']
nombre_archivo = "Argentina.txt"
escribir(nombre_archivo, lista_punto9)
leer(nombre_archivo)
