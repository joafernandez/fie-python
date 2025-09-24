from vehiculo import Vehiculo

class Gaviota:  # gaviota que ensucia según la cantidad de pescado
  
    def __init__(self, cantidad_pescado: int):
        if not isinstance(cantidad_pescado,int) or cantidad_pescado < 0 :
            raise ValueError("la cantidad de pescado debe ser un entero > a cero.")  #ayudacht PRACTICAR!
        self.cantidad_pescado: int = cantidad_pescado

    def ensuciar(self, vehiculo: Vehiculo): #nsucia 3 * cantidad_pescado
       
        cantidad = self.cantidad_pescado * 3
        vehiculo.se_ensucia(cantidad)

    def __str__(self):
        return f"gaviota ==> Cantidad de pescado {self.cantidad_pescado}"
