class Empleado:
    def __init__(self, codigo, nombre, apellido, ciudad, antiguedad, horas_trabajadas):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
        self.antiguedad = antiguedad
        self.horas_trabajadas = horas_trabajadas

    def CalcularSueldo(self):
        salario = self.antiguedad * 10000
        return salario

class EmpleadoPorHora(Empleado):
    def CalcularSueldo(self):
        salario = self.horas_trabajadas * 150
        return salario

# Crear instancias
empleado1 = Empleado(codigo=1010, nombre="Mariano", apellido="Ferrero", ciudad="Rafaela", antiguedad=10, horas_trabajadas=90)
empleado2 = EmpleadoPorHora(codigo=2020, nombre="Ana", apellido="García", ciudad="Córdoba", antiguedad=5, horas_trabajadas=120)

# Calcular sueldos
sueldo_empleado1 = empleado1.CalcularSueldo()
sueldo_empleado2 = empleado2.CalcularSueldo()

# Imprimir información de las instancias
print(f"Empleado 1: {empleado1} - Sueldo: ${sueldo_empleado1}")
print(f"Empleado 2: {empleado2} - Sueldo: ${sueldo_empleado2}")
