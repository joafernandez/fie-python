from abc import ABC
from strategy_cobro import PrecioAgua, PrecioGaseosa, PrecioCortado, PrecioGranizado

class Bebida(ABC):
    def __init__(self, nombre, estrategia_precio):
        self.nombre = nombre
        self.ingredientes = []
        self.estrategia_precio = estrategia_precio

    def calcular_precio(self):
        return self.estrategia_precio.calcular_precio(self)


class Agua(Bebida):
    def __init__(self):
        super().__init__("Agua", PrecioAgua())
        self.ingredientes = ["agua"]


class Gaseosa(Bebida):
    def __init__(self):
        super().__init__("Gaseosa", PrecioGaseosa())
        self.ingredientes = ["agua", "saborizante", "gas"]


class Cortado(Bebida):
    def __init__(self):
        super().__init__("Cortado", PrecioCortado())
        self.ingredientes = ["café", "leche"]


class GranizadoCafeCremoso(Bebida):
    def __init__(self):
        super().__init__("Granizado de café cremoso", PrecioGranizado())
        self.ingredientes = ["leche", "café", "azúcar morena", "canela"]
