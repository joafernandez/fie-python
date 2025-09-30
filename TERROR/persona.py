
        
from strategy_persona import Estrategia_Persona



class Persona:
    def __init__(self, nivel_tolerancia: float, estrategia: Estrategia_Persona):
        self.__nivel_tolerancia = nivel_tolerancia
        self.estrategia = estrategia   # cada persona tiene una estrategia de estado (Normal, Cinefilo, Fanatico)

    @property
    def mostrar_nivel_tolerancia(self):
        return self.__nivel_tolerancia

    def aplicar_rechazo(self, puntos: float):
        self.__nivel_tolerancia -= self.estrategia.decrementar_tolerancia(puntos) # me lo da la estartegia persona 
 
        
        
        

        

     