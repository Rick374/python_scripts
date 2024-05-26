# Trabajo Final Unidad Python Diplomatura Ciencia de Datos
import pandas as pd

class Jugador:
    codigo_actual = 1  # Variable estática para asignar códigos únicos

    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo = grupo
        self.codigo = Jugador.codigo_actual
        Jugador.codigo_actual += 1  # Incrementa el código para el próximo jugador

class Partido:
    def __init__(self, codigo_jugador1, codigo_jugador2, grupo, resultados_sets):
        self.codigo_jugador1 = codigo_jugador1
        self.codigo_jugador2 = codigo_jugador2
        self.grupo = grupo
        self.resultados_sets = resultados_sets

    def convertir_formato_a_lista(self, cadena_formato):
        # Dividir la cadena en sets utilizando el punto y coma como separador
        sets_str = cadena_formato.split(";")

        # Procesar cada set para obtener las puntuaciones individuales
        lista_tuplas = []
        for set_str in sets_str:
            puntuaciones = set_str.split("-")
            puntuaciones = [s.replace('(', '').replace(')', '') for s in puntuaciones]
            if len(puntuaciones) == 2:
                set_tupla = (int(puntuaciones[0]), int(puntuaciones[1]))
                lista_tuplas.append(set_tupla)

        return lista_tuplas

    def determinar_ganador(self):
        # Convertir el formato de resultados_sets a una lista de tuplas
        lista_tuplas = self.convertir_formato_a_lista(self.resultados_sets)

        # Calcular la cantidad de sets ganados por cada jugador
        sets_jugador1 = sum(1 for set_jugador1, set_jugador2 in lista_tuplas if set_jugador1 > set_jugador2)
        sets_jugador2 = sum(1 for set_jugador1, set_jugador2 in lista_tuplas if set_jugador2 > set_jugador1)

        if sets_jugador1 > sets_jugador2:
            return self.codigo_jugador1
        elif sets_jugador2 > sets_jugador1:
            return self.codigo_jugador2

class Torneo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []  # Lista de jugadores
        self.partidos = []   # Lista de partidos jugados

    def armar_grupos(self, path_archivo_jugadores, jugadores_grupo):
        try:
            df_jugadores = pd.read_csv(path_archivo_jugadores, header=None, names=["nombre"])
            df_jugadores.sort_values(by="nombre", inplace=True)

            # Crear instancias de Jugador y asignarles códigos
            self.jugadores = [Jugador(nombre, chr(65 + i // jugadores_grupo)) for i, nombre in enumerate(df_jugadores["nombre"])]

            total_jugadores = len(df_jugadores)
            if total_jugadores % jugadores_grupo != 0:
                return f"No es posible conformar grupos de {jugadores_grupo} jugadores con {total_jugadores} disponibles."

            grupos = [self.jugadores[i:i + jugadores_grupo] for i in range(0, total_jugadores, jugadores_grupo)]

            mensaje_grupos = ""
            for i, grupo in enumerate(grupos, start=1):
                mensaje_grupos += f"Grupo {chr(64 + i)}:\n"
                for jugador in grupo:
                    mensaje_grupos += f"  {jugador.nombre} (Código: {jugador.codigo})\n"

            return mensaje_grupos

        except FileNotFoundError:
            return "No se encontró el archivo de jugadores."

    def obtener_codigo_jugador(self, nombre_jugador):
        for jugador in self.jugadores:
            if jugador.nombre.replace(" ", "") == nombre_jugador:
                return jugador.codigo
        return None  # Si no se encuentra el jugador, devuelve None

    def obtener_nombre_jugador(self, codigo_jugador):
        for jugador in self.jugadores:
            if jugador.codigo == codigo_jugador:
                return jugador.nombre
        return None  # Si no se encuentra el jugador, devuelve None

    def leer_partidos_grupos(self, path_archivo_partidos_grupos):
        try:
            df_partidos = pd.read_csv(path_archivo_partidos_grupos, header=None, names=["jugador1", "jugador2", "grupo", "resultados_sets"])

            # Armar los partidos en base a lo leido en el archivo, además actualizar la lista de jugadores con los grupos definitivos
            for _, row in df_partidos.iterrows():
                jugador1_codigo = self.obtener_codigo_jugador(row["jugador1"])
                jugador2_codigo = self.obtener_codigo_jugador(row["jugador2"])
                self.partidos.append(Partido(jugador1_codigo, jugador2_codigo, row["grupo"], row["resultados_sets"]))

                for jugador in self.jugadores:
                    if jugador.codigo == jugador1_codigo:
                        jugador.grupo = row["grupo"]
                    elif jugador.codigo == jugador2_codigo:
                        jugador.grupo = row["grupo"]

        except FileNotFoundError:
            print("No se encontró el archivo de partidos.")

    def obtener_posiciones(self):
        # Inicializar un diccionario para almacenar los puntos por grupo
        puntos_por_grupo = {}

        # Contar los puntos de cada jugador en los partidos
        for partido in self.partidos:
            ganador = partido.determinar_ganador()
            if ganador:
                grupo = partido.grupo
                if grupo not in puntos_por_grupo:
                    puntos_por_grupo[grupo] = {}
                puntos_por_grupo[grupo][ganador] = puntos_por_grupo[grupo].get(ganador, 0) + 2

        # Determinar los ganadores de cada grupo
        ganadores_por_grupo = {}
        for grupo, puntos in puntos_por_grupo.items():
            max_puntos = max(puntos.values())
            ganadores_grupo = [jugador for jugador, puntos in puntos.items() if puntos == max_puntos]
            ganadores_por_grupo[grupo] = ganadores_grupo

        return ganadores_por_grupo

if __name__ == "__main__":
    torneo = Torneo("Torneo de Tenis")
    grupos = torneo.armar_grupos("jugadores.txt", jugadores_grupo=4)
    print("Grupos armados en base a los jugadores inscriptos : \n")
    print(grupos)
    torneo.leer_partidos_grupos("partidos.txt")
    ganadores_por_grupo = torneo.obtener_posiciones()
    print("\nLos ganadores de cada grupo en base al archivo de resultados proporcionado son: \n")
    for grupo in ganadores_por_grupo:
        if len(ganadores_por_grupo[grupo]) == 1:
            print(f"Ganador Grupo {grupo} : {torneo.obtener_nombre_jugador(ganadores_por_grupo[grupo][0])}.")
        else:
            print(f"Ganadores Grupo {grupo} : {torneo.obtener_nombre_jugador(ganadores_por_grupo[grupo][0])}, {torneo.obtener_nombre_jugador(ganadores_por_grupo[grupo][1])}")
