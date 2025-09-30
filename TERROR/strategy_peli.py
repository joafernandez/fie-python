

from abc import ABC, abstractmethod


class EstrategiaPelicula(ABC):
    @abstractmethod
    def rechazar(self, pelicula, cantidad_personas: int = 0):
        pass


class Z(EstrategiaPelicula):
    def rechazar(self, pelicula, cantidad_personas: int = 0):
        return 2


class Terror(EstrategiaPelicula):
    def rechazar(self, pelicula, cantidad_personas: int = 0):
        return (3 * pelicula.mostrar_duracion) / 5


class Bizarra(EstrategiaPelicula):
    def rechazar(self, pelicula, cantidad_personas: int = 0):
        return cantidad_personas