class Artesanal:
    """    Lavadero artesanal. El precio depende de la suciedad del vehículo,
    la cantidad de empleados y un costo unitario fijo.
    """

    COSTO_UNITARIO = 10

    def __init__(self, empleados: int):
        """Parámetros: empleados (int) cantidad de personas que trabajan."""
        self.empleados = empleados

    def calcular_precio(self, vehiculo):
        """        Calcula el precio del lavado en función de la suciedad del vehículo.

        Fórmula:
            tiempo = vehiculo.suciedad / 5
            precio = empleados * tiempo * COSTO_UNITARIO
        """
        tiempo = vehiculo.suciedad / 5
        return self.empleados * tiempo * Artesanal.COSTO_UNITARIO

    def __str__(self):
        return f"SmallLav (Artesanal, empleados={self.empleados}, costo_unit={Artesanal.COSTO_UNITARIO})"
