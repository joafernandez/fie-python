from abc import ABC,abstractmethod


class Estrategia_recargo(ABC):
    
    @abstractmethod
    def calcular_recargo(self):
        pass
    


class Categoria(Estrategia_recargo):
 
    def calcular_recargo(self,envio:"Envio"):
        recargo=0
        if "tecnologia" in envio.mostrar_categoria: #busco en lalista de categoria 
            recargo= envio.mostrar_precio_base*0.1
        return recargo
        
        
        
        
class Sobrepeso(Estrategia_recargo):
    
    PESO_DETERMINADO = 1
       
  
    def calcular_recargo(self,envio:"Envio"):
        recargo=0
        if envio.mostrar_peso > self.PESO_DETERMINADO: 
            recargo=80  
        return recargo
    
class Arbitrario(Estrategia_recargo):
    
    def calcular_recargo(self,envio:"Envio"):   #puse comillas xq habia un bucle de llamados , no se como solucioanr sino
        recargo=50
        return recargo

  
       
                
    
    
        