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
