from vehiculo import Vehiculo

class OtrasAves:
    """    Otras aves genéricas con un ensuciamiento de valor fijo.
    Ejemplos: Cotorra, Loro Barranquero, etc.
    """
    VALOR_FIJO = 10  # Atributo de clase

    def __init__(self, nombre: str):
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    def ensuciar(self, vehiculo: Vehiculo):
        """Ensucia el vehículo un valor fijo (10)."""
        vehiculo.se_ensucia(OtrasAves.VALOR_FIJO)

    def __str__(self):
        return f"{self.nombre} "
