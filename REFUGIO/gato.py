from datetime import date, timedelta
from mascota import Mascota

class Gato(Mascota):
    def disponible(self):
        return (not self.adoptada) and (date.today() >= self.fecha_ingreso + timedelta(days=180))

    def saludar(self):
        if self.disponible():
            print("Miau")

# el que sabe cuantos perro se puede adopatar es la clase GATO  (uso polimorfismo)
