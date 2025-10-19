 
""" niveles  "SEGUN" los "puntos" acumulados:

● Bronce: es el nivel inicial de todo usuario nuevo. 
1 producto en carrito
no saldo negativo.


● Plata:  5.000 puntos.
 5 productos en el carrito 
 saldo negativo de $5000.


● Oro: Se alcanza con 15.000 puntos.
No tiene restricciones  productos /// nose 
saldo negativo de $20000


-  El nivel se actualiza  cuando el usuario alcanza los puntos necesarios //sumar

-  puede descender si pierde puntos por penalizaciones. // m falta"""

from abc import ABC, abstractmethod

class Estrategia_Nivel(ABC):
    
    @abstractmethod
    def maximo_producto(self):
        pass
    
    @abstractmethod
    def saldo_minimo(self):
        pass
    
    
class Bronce (Estrategia_Nivel):#es el nivel inicial de todo usuario nuevo. Solo permite tener un producto en el carrito
                                 #a la vez y no puede tener saldo negativo.
    
    def maximo_producto(self):#uno oslo
        return 1
        
   
    def saldo_minimo(self): #saldo inicial
        return 0
    
    
    
class Plata (Estrategia_Nivel):#Se alcanza al acumular 5.000 puntos. Permite tener hasta 5 productos en el carrito y un
                                #saldo negativo de $5000.
    
    def maximo_producto(self):
        return 5
   
    def saldo_minimo(self): #inicia con menso 5mil en adelante
        return -5000
     
    
class Oro (Estrategia_Nivel): #Se alcanza con 15.000 puntos. No tiene restricciones en la cantidad de productos en el
                              #carrito y un saldo negativo de $20000

    
    def maximo_producto(self):
        return float("inf")   # sin límite
   
    def saldo_minimo(self):
        return -20000
    
    
    
# oro tenia q retornar un valor sin limite