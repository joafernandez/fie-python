


from strategy_peli import EstrategiaPelicula #LA que me da el emtodo rechazar()
from abc import ABC, abstractmethod

class Pelicula(ABC):
    def __init__(self,horario:float,duracion:float):
        super().__init__()
        self.__horario=horario
        self.__duracion=duracion
        
    @property
    def mostrar_horario(self):
        return self.__horario
    
    @property
    def mostrar_duracion(self):
        return self.__duracion
        
    def __str__(self):
        return f" horario:{self.__horario}, duracion:{self.__duracion}"
    
    
    def rechazo(self,estrategia:EstrategiaPelicula, cantidad_personas: int = 0): #tiene q venir de la ESTRATEGIA
        return estrategia.rechazar(self, cantidad_personas) #este es un metodo que devuelve puntos 
        
    # a la persona le produuce un rechazo y me devuelve puntos
        
            
    
    

    