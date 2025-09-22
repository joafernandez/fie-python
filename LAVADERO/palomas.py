
from vehiculo import Vehiculo


class Paloma:
    def __init__(self,peso:float):
        self.peso:float = peso

    def ensuciar(self,vehiculo:Vehiculo):
        cantidad = self.peso*.03
        vehiculo.ensuciar(cantidad)
        self.peso -= cantidad
   