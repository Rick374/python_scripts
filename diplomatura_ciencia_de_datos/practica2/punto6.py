#Punto 6
def verificar_dias_mes(mes, dias):
    # Diccionario con la cantidad máxima de días por mes
    max_dias_por_mes = {
        1: 31,  # Enero
        2: 28,  # Febrero (considerando años no bisiestos)
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31,  # Octubre
        11: 30,  # Noviembre
        12: 31   # Diciembre
    }

    # Verificar si la cantidad de días es igual, menor o mayor al máximo del mes
    if dias == max_dias_por_mes.get(mes):
        print(f"{dias} es la cantidad máxima de días del mes.")
    elif dias < max_dias_por_mes.get(mes):
        print(f"{dias} NO es la cantidad máxima de días del mes.")
    else:
        print(f"{dias} supera a la cantidad máxima de días del mes.")

# Uso de la función
verificar_dias_mes(1, 31)
verificar_dias_mes(2, 31)
