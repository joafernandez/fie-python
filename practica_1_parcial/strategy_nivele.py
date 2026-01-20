

from abc import ABC, abstractmethod

class Estrategia_Nivel(ABC):
    
    @abstractmethod
    def maximo_producto(self):
        pass
        
    @abstractmethod
    def saldo_minimo(self):
        pass
    
    
class Bronce (Estrategia_Nivel):# Solo permite tener un producto en el carrito
                                 #a la vez y no puede tener saldo negativo.
    
    def maximo_producto(self):#uno oslo
        return 1
        
   
    def saldo_minimo(self): #saldo inicial
        return 0
 
    
    
    
class Plata (Estrategia_Nivel):#Permite tener hasta 5 productos en el carrito y un
                                #saldo negativo de $5000.
    
    def maximo_producto(self):
        return 5       
    
   
    def saldo_minimo(self): #inicia con menso 5mil en adelante
     return -5000
     
    
class Oro (Estrategia_Nivel): # No tiene restricciones en la cantidad de productos en el
                              #carrito y un saldo negativo de $20000

    
    def maximo_producto(self):
        return float("inf")
    
    def saldo_minimo(self):
            return -20000
      
    



