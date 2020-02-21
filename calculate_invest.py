print('¿Cuánto dinero planea invertir?')
dinero = input('Ingrese el monto: ')

print('¿Cuánto es la tasa de interés anual?')
tasa = input('Ingrese la tasa (Ej 1% = 0.01): ')

print('¿Cuántos años planea dejar el dinero invertido?')
años = input('Ingrese el número de años: ')

monto = float(dinero) * float(((1+tasa)*años))

print ('El dinero que usted tendrá al cabo de {años} años es: {monto}')