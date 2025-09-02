# Base de adoptantes


class Adoptante:
    def __init__(self, nombre, estrategia ):
    
        self.mascota= []
        self.nombre=nombre
        self.estrategia=estrategia

    def regadoptar(self, mascota):
        self.estrategia.puede_Adopatr(self, mascota):
            self.mascota.append(mascota)
    else:
        

    def puede_adoptar(self, mascota):
        return True  # sin límites aquí (los ponen las subclases)
