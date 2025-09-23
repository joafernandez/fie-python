

from abc import ABC, abstractmethod


class Estrategia_pago(ABC):  # aplique estartegia xq luegoo puedo agregar otros descuentos en el futuro
    
    @abstractmethod
    def descuento(self)->float: 
        pass
    

class Telepeaje(Estrategia_pago):
    
    def descuento(self)->float:
        return 0.5
            
    
class Sube(Estrategia_pago):
    
    def descuento(self)->float:
        return 0.7
          
    
class Efectivo(Estrategia_pago):
    
    def descuento(self)->float:
        return 1.0
    
          