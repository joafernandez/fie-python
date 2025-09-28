
from abc import ABC, abstractmethod
from persona import Persona


class Estrategia_Permiso(ABC):
    
    @abstractmethod
    def quien_puede_ver(self,persona:Persona):
        pass
    
    
class Publico(Estrategia_Permiso):
    
    def quien_puede_ver(self,persona:Persona): 
        return "todos" 
    
    
       
class Amigos(Estrategia_Permiso):
    
    def quien_puede_ver(self,persona:Persona):
        return persona.mostrar_lista_amigos
    

class Algunos(Estrategia_Permiso):
    def __init__(self):
        super().__init__()
        self.lista_algunos=[]
        
    def quien_puede_ver(self,persona:Persona):
       return self.lista_algunos
        
 
    
    