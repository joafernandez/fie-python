

      
class Artesanal:
    def __init__(self,empleado:int): 
        self.empleado=empleado
        self.costoUnitario=10
   
    def calcular_precio( self, Vehiculo):# recibo  vehiculo xq necesito  nivel de suciedad
        tiempo=Vehiculo.nivel_suciedad/5 #no lleva self xq no esta en el objeto guardado se calcula siempre
 
        return  self.empleado*tiempo*self.costoUnitario # el precio es
    
    
    
    

    
    
    