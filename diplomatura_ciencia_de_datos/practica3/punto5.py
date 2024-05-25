class Animal():
    def __init__(self,nombre):
        self.nombre = nombre

class Murcielago(Animal):
    def volar(self):
        print('Volando ...')

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre_completo = nombre + ' ' + apellido

class Superheroe(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.disfraz = False

    def cambiarse(self):
        self.disfraz = not self.disfraz

class Batman(Superheroe, Murcielago):
    def __init__(self, nombre, apellido):
        # Llamamos al constructor de Superheroe y luego al de Murcielago
        Superheroe.__init__(self, nombre, apellido)
        Murcielago.__init__(self, nombre)

batman = Batman(nombre="Bruce", apellido="Wayne")

print(f"¿Batman tiene su disfraz puesto? {batman.disfraz}")

batman.volar()

batman.cambiarse()

print(f"¿Batman tiene su disfraz puesto ahora? {batman.disfraz}")
