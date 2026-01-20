
from abc import ABC, abstractmethod

"""  def puede_pagar(self, precio):  # le envio precio para ver si le alcanza 
        saldo_despues = self.saldo - precio
        limite = self.suscripcion.obtener_limite_saldo_negativo() # aca llamo al metodo de ESTARTEGIA ________
        return saldo_despues >= limite
        
        
        """


class Suscripcion(ABC):
    
    @abstractmethod
    def puede_ver_contenido_pago(self):  # permite pagar
        pass
    
    @abstractmethod
    def permite_exclusivos(self):  # puede ver contenido exclusivo
        pass
    
    @abstractmethod
    def obtener_limite_saldo_negativo(self):  # limite de slado negativo 
        pass



class PanyAgua(Suscripcion): #todo gratis sincosto
     
    def puede_ver_contenido_pago(self):  
        return False
    
    def permite_exclusivos(self):  
        return False
    
    
    def obtener_limite_saldo_negativo(self):  
        gratis=0
        return gratis
    
    

class Oro(Suscripcion):
    
    def puede_ver_contenido_pago(self):  
        return True #PUEDE
    
    def permite_exclusivos(self):  
        return False#no puede
    
    
    def obtener_limite_saldo_negativo(self):  
        return -5000
    

class Diamante(Suscripcion):
    
    def puede_ver_contenido_pago(self):  
        return True
    
    def permite_exclusivos(self): 
        return True
    
    def obtener_limite_saldo_negativo(self):  
        return -20000
