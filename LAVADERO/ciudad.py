from vehiculo import Vehiculo
from lava_Arte import Artesanal
from lave_Autom import Automatico



# en la CIUDAD hay lavaderos y autos, y voy agregando a la lista 



class Ciudad: # puede ser:  bsas=Ciudad() , cordoba=Ciudad()   
    def __init__(self): 
        self.lista_autos=[]#agrego autis
        self.lista_lavaderos=[] #agregos lavad
        
        
    def agregar_auto(self,Vehiculo:Vehiculo):
        self.lista_autos.append(Vehiculo)
    
    def agregar_lava_Artesanal(self,Artesanal:Artesanal):
        self.lista_lavaderos.append(Artesanal)  
    
    def agregar_lava_Automatico(self,Automatico:Automatico):
        self.lista_lavaderos.append(Automatico)    
  
  
  # OJOOOOO!!!!  vamos a ensuciar "todos" los vehiculos
  # tenemos que recorrer todo los vehiculos y ensuciar con la ceniza
  # o sea el vehiculo tiene su propio metodo "se_ensucia()"
  # pero la lluvia le da la CANTIDAD 
    
    def ensuciar_ceniza(self,miligramos:int): 
        for a in self.lista_autos:
            a.se_ensucia(miligramos)
    
    
    
    