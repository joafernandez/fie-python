from vehiculo import Vehiculo

class OtrasAves:# ensuciamiento de valor fijo.
   
    VALOR_FIJO = 10  # atributo de clase

    def __init__(self, nombre: str):
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    def ensuciar(self, vehiculo: Vehiculo):
        vehiculo.se_ensucia(OtrasAves.VALOR_FIJO)

    def __str__(self):
        return f"{self.nombre} "
