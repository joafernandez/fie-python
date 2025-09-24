from vehiculo import Vehiculo

class Paloma:#ensucir depende de su peso
    def __init__(self, peso: float):
        self.peso: float = peso

    def ensuciar(self, vehiculo: Vehiculo):
        cantidad = self.peso * 0.03
        vehiculo.se_ensucia(cantidad)
        self.peso -= cantidad

    def __str__(self):
        return f"Paloma ==> Peso: {self.peso}"
