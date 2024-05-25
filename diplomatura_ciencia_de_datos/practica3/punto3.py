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

    def __str__(self):
        # Personalizar la representación en cadena
        return f"{self.codigo} - {self.nombre} {self.apellido}"

# Ejemplo de uso
empleado1 = Empleado(codigo=1010, nombre="Mariano", apellido="Ferrero", ciudad="Rafaela", antiguedad=10, horas_trabajadas=90)
print(empleado1)
