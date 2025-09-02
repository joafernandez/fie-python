from datetime import date, timedelta
from mascota import Mascota

class Perro(Mascota):
    def disponible(self):
        return (not self.adoptada) and (date.today() >= self.fecha_ingreso + timedelta(days=30))

    def saludar(self):
        if self.disponible():
            print("Guau")
            
# el que sabe cuantos perro se puede adopatar es la clase PERRO 
