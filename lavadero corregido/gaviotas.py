from vehiculo import Vehiculo

class Gaviota:
    """Representa una gaviota que ensucia según la cantidad de pescado ingerido."""
    def __init__(self, cantidad_pescado: int):
        self.cantidad_pescado: int = cantidad_pescado

    def ensuciar(self, vehiculo: Vehiculo):
        """Ensucia 3 * cantidad_pescado."""
        cantidad = self.cantidad_pescado * 3
        vehiculo.se_ensucia(cantidad)

    def __str__(self):
        return f"Gaviota ==> Cantidad de pescado {self.cantidad_pescado}"
