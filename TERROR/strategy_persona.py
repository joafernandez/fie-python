

from abc import ABC, abstractmethod

class Estrategia_Persona(ABC):
    
    @abstractmethod
    def decrementar_tolerancia(self, puntos: float) :#cuántos puntos - según persona
        pass




class Normal(Estrategia_Persona):#------------------------------------------------------
    
    def decrementar_tolerancia(self, puntos: float):
        return puntos  


class Cinefilo(Estrategia_Persona):
    
    def decrementar_tolerancia(self, puntos: float):
        return puntos / 2  # siente la mitad


class Fanatico(Estrategia_Persona):
    def decrementar_tolerancia(self, puntos: float):
        return puntos if puntos > 30 else 0  # solo si supera 30
