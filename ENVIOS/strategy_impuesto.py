
#calcular_impuesto()

from abc import ABC, abstractmethod



class Estrategia_impuesto(ABC):
    def __init__(self):
        pass
    
    @abstractmethod   
    def impuesto(self,envio:"Envio", estrategia_recargo:"Estrategia_recargo"):
        pass
    
    
   # se aplican sobre el pprecio neto =precio base+recargos /hacer este calculo en envio 
class Iva(Estrategia_impuesto): 
  def impuesto(self,envio:"Envio", estrategia_recargo:"Estrategia_recargo"):
      return  envio.precio_neto(estrategia_recargo)*0.2  # O SEA NO TENGO Q CALCULAR YA SE SABE Q SE LE MULTIPLICA AL NETO??
  

  
class Multicategoria(Estrategia_impuesto):
    def impuesto(self,envio:"Envio", estrategia_recargo:"Estrategia_recargo"):
        if len(envio.mostrar_categoria) >3: # contar lista
            return envio.precio_neto(estrategia_recargo)*0.01
        return 0

class Aduanero(Estrategia_impuesto):
    def impuesto(self,envio:"Envio", estrategia_recargo:"Estrategia_recargo"):
        if  envio.mostrar_ubicacion_Origen.mostrar_pais!= envio.mostrar_ubicacion_Destino.mostrar_pais:
          return envio.precio_neto(estrategia_recargo)*0.5
        return 0
   
class Extrano(Estrategia_impuesto):
    def impuesto(self,envio:"Envio", estrategia_recargo:"Estrategia_recargo"):
        if  envio.mostrar_precio_base % 2==0:
            return envio.precio_neto(estrategia_recargo)*0.1
        return 0
    