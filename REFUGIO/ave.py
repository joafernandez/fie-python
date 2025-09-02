
from mascota import Mascota

class Ave(Mascota):
    def disponible(self):
        return not self.adoptada  # adoptable siempre que no esté adoptada

    def saludar(self):
        if self.disponible():
            print("Pío")

# el que sabe cuantos perro se puede adopatar es la clase AVE 