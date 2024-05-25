
import cosas

murcielago = cosas.Murcielago("Drácula")
murcielago.volar()  # Imprime "Volando ..."

superheroe = cosas.Superheroe("Clark", "Kent")
print(superheroe.nombre_completo)
print(f"¿Está usando su disfraz? {superheroe.disfraz}")
superheroe.cambiarse()
print(f"¿Está usando su disfraz ahora? {superheroe.disfraz}")
