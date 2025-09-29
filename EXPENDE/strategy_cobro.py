from abc import ABC, abstractmethod

class EstrategiaPrecio(ABC):
    @abstractmethod
    def calcular_precio(self, bebida):
        pass


class PrecioAgua(EstrategiaPrecio):
    def calcular_precio(self, bebida):
        return 50


class PrecioGaseosa(EstrategiaPrecio):
    def calcular_precio(self, bebida):
        return 50 * 3  # triple que el agua


class PrecioCortado(EstrategiaPrecio):
    def calcular_precio(self, bebida):
        return 250


class PrecioGranizado(EstrategiaPrecio):
    def calcular_precio(self, bebida):
        return 50 * len(bebida.ingredientes)
