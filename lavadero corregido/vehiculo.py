class Vehiculo:
    def __init__(self, tipo: str, patente: str, suciedad: int):
        # Atributos privados tal como el diseño del alumno
        self.__tipo: str = tipo
        self.__patente: str = patente
        self.__suciedad: int = suciedad

    # === Propiedades (acceso controlado a atributos privados) ===

    @property
    def patente(self) -> str:
        """Devuelve la patente (str)."""
        return self.__patente

    @property
    def suciedad(self) -> int:
        """Devuelve el nivel de suciedad acumulada (int)."""
        return self.__suciedad

    @property
    def tipo(self) -> str:
        """Devuelve el tipo de vehículo (str), por ejemplo 'Auto' o 'Camion'."""
        return self.__tipo

    @suciedad.setter
    def suciedad(self, cantidad: int):
        """Actualiza el nivel de suciedad (int)."""
        self.__suciedad = cantidad

    def se_ensucia(self, cantidad):
        """        Incrementa la suciedad del vehículo.

        Parámetros:
            cantidad (int|float): cantidad a sumar al nivel de suciedad.
        """
        self.__suciedad += cantidad

    def limpiar(self):
        """Deja la suciedad del vehículo en 0 (limpio)."""
        self.__suciedad = 0

    def __str__(self):
        return f"Patente: {self.patente} ({self.tipo}) Mugre: {self.suciedad}"
