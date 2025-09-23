from vehiculo import Vehiculo

class Paloma:
    """Representa una paloma cuyo ensuciamiento depende de su peso."""
    def __init__(self, peso: float):
        self.peso: float = peso

    def ensuciar(self, vehiculo: Vehiculo):
        """        Ensucia el vehículo con el 3% del peso actual de la paloma
        y reduce el peso de la paloma en esa misma cantidad.
        """
        cantidad = self.peso * 0.03
        vehiculo.se_ensucia(cantidad)
        self.peso -= cantidad

    def __str__(self):
        return f"Paloma ==> Peso: {self.peso}"
