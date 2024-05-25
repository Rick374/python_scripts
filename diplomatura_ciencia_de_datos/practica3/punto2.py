class Empleado:
    def __init__(self, codigo, nombre, apellido, ciudad, antiguedad, horas_trabajadas):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
        self.antiguedad = antiguedad
        self.horas_trabajadas = horas_trabajadas

    def CalcularSueldo(self):
        # Calcular el salario multiplicando por 10000 los años de antigüedad
        salario = self.antiguedad * 10000
        return salario

class EmpleadoPorHora(Empleado):
    def CalcularSueldo(self):
        # Calcular el salario multiplicando las horas trabajadas por 150
        salario = self.horas_trabajadas * 150
        return salario

# Ejemplo de uso
empleado_hora = EmpleadoPorHora(codigo=2, nombre="María", apellido="Gómez", ciudad="Córdoba", antiguedad=3, horas_trabajadas=160)
sueldo_empleado_hora = empleado_hora.CalcularSueldo()
print(f"El sueldo del empleado {empleado_hora.nombre} es ${sueldo_empleado_hora}")
