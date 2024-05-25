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

# Ejemplo de uso
empleado1 = Empleado(codigo=1, nombre="Juan", apellido="Pérez", ciudad="Buenos Aires", antiguedad=5, horas_trabajadas=160)
sueldo_empleado1 = empleado1.CalcularSueldo()
print(f"El sueldo del empleado {empleado1.nombre} es ${sueldo_empleado1}")
