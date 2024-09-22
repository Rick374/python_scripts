
def leer(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        # Leer cada línea y mostrarla
        for linea in archivo:
            print(linea.strip())  # Elimina los saltos de línea al final
    print(f"Contenido del archivo '{nombre_archivo}':")

# Ejemplo de uso
nombre_archivo = "archivo_punto7.txt"  # Cambia el nombre del archivo según necesites
leer(nombre_archivo)
