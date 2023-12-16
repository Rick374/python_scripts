class Inversion:
    """Una clase que representa una inversión.

    Attributes:
        principal: La cantidad de dinero invertida inicialmente.
        tasa: La tasa de interés anual.
        tiempo: El número de años de la inversión.
        capitalizacion: El número de veces por año que se capitalizan los intereses.
    """

    def __init__(self, principal, tasa, tiempo, capitalizacion=1):
        """Inicializa una nueva inversión.

        Args:
            principal: La cantidad de dinero invertida inicialmente.
            tasa: La tasa de interés anual.
            tiempo: El número de años de la inversión.
            capitalizacion: El número de veces por año que se capitalizan los intereses.
        """

        self.principal = principal
        self.tasa = tasa
        self.tiempo = tiempo
        self.capitalizacion = capitalizacion

    def calc_tasa_interes_por_periodo(self):
        """Calcula la tasa de interés por periodo seleccionado.

        Returns:
            La tasa de interés por período.
        """

        # Calcula la tasa de interés por período.
        tasa_por_periodo = self.tasa / 100 / self.capitalizacion

        return tasa_por_periodo

    def interes_compuesto(self):
        """Calcula el interés compuesto de la inversión.

        Returns:
            La cantidad de dinero ganada en intereses.
        """

        # Calcula la tasa de interés por período.
        tasa_por_periodo = self.calc_tasa_interes_por_periodo()

        # Calcula el número de períodos.
        num_periodos = self.tiempo * self.capitalizacion

        # Calcula la cantidad de dinero ganada en intereses.
        interes = self.principal * ((1 + tasa_por_periodo) ** num_periodos - 1)

        # Devuelve la cantidad de dinero ganada en intereses.
        return interes

    def valor_final(self):
        """Calcula el valor final de la inversión.

        Returns:
            El valor final de la inversión, incluyendo el principal y los intereses.
        """

        # Calcula el interés compuesto.
        interes = self.interes_compuesto()

        # Calcula el valor final de la inversión.
        valor_final = self.principal + interes

        # Devuelve el valor final de la inversión.
        return valor_final


# Ejemplo de uso.
inversion_inicial = 273111
tasa_interes_porcentaje_diario_mensual_anual = 8.04
tiempo_de_inversion_diario_mensual_anual = 1
periodos_de_capitalizacion_por_dia_mes_año = 1

inversion = Inversion(inversion_inicial, tasa_interes_porcentaje_diario_mensual_anual, tiempo_de_inversion_diario_mensual_anual, periodos_de_capitalizacion_por_dia_mes_año)

tasa_por_periodo = inversion.calc_tasa_interes_por_periodo()
interes = inversion.interes_compuesto()
valor_final = inversion.valor_final()

print("Inversion inicial: {} ".format(inversion_inicial))
print("La tasa interés por periodo es: {} %".format(tasa_por_periodo*100))
print("El interés compuesto es:", interes)
print("El valor final de la inversión es:", valor_final)
