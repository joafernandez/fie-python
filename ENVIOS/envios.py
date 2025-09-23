from ubicacion import Ubicacion 
from strategy_recarga import Estrategia_recargo
from strategy_impuesto import Estrategia_impuesto 


class Envio:
    def __init__(self,peso:float,precio_base:float,categoria:list,origen:Ubicacion,destino:Ubicacion):
        self.__peso=peso
        self.__precio_base=precio_base
        self.__categoria=categoria  
        self.__origen=origen # no se GUARDA!!! ES UNA CLASE DECLARADA
        self.__destino=destino
    
    @property
    def mostrar_peso(self)->float:
        return self.__peso

    
    @property
    def mostrar_precio_base(self)->float:
        return self.__precio_base

    
    @property
    def mostrar_categoria(self)->str:
        return self.__categoria
    

    @property
    def mostrar_ubicacion_Origen(self)->object:
        return self.__origen
    
    @property
    def mostrar_ubicacion_Destino(self)->object:
        return self.__destino
    
    
    # el precio neto= precio base +recargos (llamo a estrategia recargo)
    def precio_neto (self,estrategia:Estrategia_recargo):
        return self.__precio_base + estrategia.calcular_recargo(self) #(no estoy segura dle SELF)
    
    
    
    def precio_bruto(self, estrategia_impuesto: Estrategia_impuesto, estrategia_recargo: Estrategia_recargo):
        return self.precio_neto(estrategia_recargo) + estrategia_impuesto.impuesto(self,estrategia_recargo)
    #llamo a precion neto y le sumo impuesto 
        
    
    
    def calcular_recargo(self,estrategia:Estrategia_recargo): # aca llamo a la estrategia q me de el recargo corresp
        return estrategia.calcular_recargo(self) # SI LLEGARA A NECESITAR DATOS DE ESTA CLASE LUEGO AGREGO SELF!!!
  
    def calcular_impuesto(self,estrategia:Estrategia_impuesto): # aca llamo a la estrategia q me de el impuesto corresp
        return estrategia.impuesto(self) # ir a hcer estartegia


    def __str__(self):
         return f"((peso:){self.__peso}(precio_base:){self.__precio_base}(categoria:){self.__categoria}(origen:){self.__origen} (destino:{self.__destino}))"
   
     

      
        
        
    