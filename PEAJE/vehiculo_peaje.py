from abc import ABC, abstractmethod
    

class Vehiculo(ABC):

    def __init__(self,patente): 
        self.__patente = patente
             

    @property # get
    def patente(self)->str:
        return self.__patente    


    def __str__(self):
        return f"patente: {self.patente}"

    @abstractmethod
    def calcular_tarifa(self)->float:
        pass



class Auto(Vehiculo):
    
    TARIFA=100 # atributo de clase ,accedo desde los metodos con self

    def calcular_tarifa(self)->float:
        return self.TARIFA

class Moto(Vehiculo):
    TARIFA=50
    def calcular_tarifa(self)->float:
        return self.TARIFA

class Camion(Vehiculo):
    
    TARIFA = 200
    def __init__(self, patente, cantidad_ejes:int):
        super().__init__(patente)
        self.__cantidad_ejes = cantidad_ejes

    def __str__(self):
        return f"{self.patente} Ejes [{self.cantidad_ejes}]"  # muestro datos

    @property
    def cantidad_ejes(self)->int:
        return self.__cantidad_ejes    

    def calcular_tarifa(self)->float:
        return self.TARIFA * self.cantidad_ejes

