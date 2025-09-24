class Vehiculo:
    def __init__(self, tipo: str, patente: str, suciedad: int):
        self.__tipo: str = tipo
        self.__patente: str = patente
        self.__suciedad: int = suciedad

    #  Propiedades (acceso controlado a atributos privados) 

    @property
    def patente(self) -> str:
        return self.__patente

    @property
    def suciedad(self) -> int:
        return self.__suciedad

    @property
    def tipo(self) -> str:
        return self.__tipo

    @suciedad.setter
    def suciedad(self, cantidad: int):
        self.__suciedad = cantidad

    def se_ensucia(self, cantidad):  #INCREMENTO SUCIEDAD
        self.__suciedad += cantidad

    def limpiar(self): #LIMPIA TOTAL
        self.__suciedad = 0

    def __str__(self):
        return f"Patente: {self.patente} ({self.tipo}) Mugre: {self.suciedad}"
