
from abc import ABC , abstractmethod 
from vehiculo import Vehiculo


class estrategia_formacion(ABC):   # ACORDARME que bandada me paso el vehiculo p esuciar!!!!
    
    # BUENO ACA TENGO Q PASARLE:
    # la lista de aves  q componen esa formacion
    # y el auto para ensuciar
    
    @abstractmethod
    def ensuciar (self,lista_aves:list, vehiculo:Vehiculo):
        pass
    
    
    #acordarme que es una lista de objetos ensuciando: 
    
class formacion_l(estrategia_formacion):# ensucia la pri y ult, NO tengo q recorrer neceistoo el tam 
    def ensuciar (self,lista_aves:list, vehiculo:Vehiculo):
        if len(list_aves)>=2: # si el tam es al menos 2 
                lista_aves[0].ensuciar(Vehiculo)
                lista_aves[-1].ensuciar(Vehiculo) 
                
class formacion_v(estrategia_formacion): # todas ensucian
    def ensuciar (self,lista_aves:list, vehiculo:Vehiculo):
        for aux in lista_aves: #con un aux recorro cada ave para q ensucie
            aux.ensuciar(Vehiculo)
                
class formacion_w(estrategia_formacion): # todas ensucian 2 veces
    def ensuciar (self,lista_aves:list, vehiculo:Vehiculo):         
        for aux in lista_aves: 
            aux.ensuciar(Vehiculo)
            aux.ensuciar(Vehiculo)
                     