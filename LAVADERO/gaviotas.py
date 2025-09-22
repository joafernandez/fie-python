from vehiculo import Vehiculo


class Gaviota:
    def __init__(self,cantidad_pescado:int):
        self.cantidad_pescado:int = cantidad_pescado

        
    def ensuciar(self,vehiculo:Vehiculo):
        cantidad = self.cantidad_pescado*3
        vehiculo.ensuciar(cantidad)

  