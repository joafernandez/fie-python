



class Vehiculo:
    def __init__(self, tipo:str, patente:str,suciedad:int):
        self.__tipo:str=tipo
        self.__patente:str=patente
        self.__suciedad:int=suciedad
        
        
    #PERMITIR ACCESOS A DATOS PRIVADOS !
    
    @property # patente
    def patente(self)->str: # devuelve -> cadena 
        return self.__patente
    
    @property # suciedad 
    def suciedad (self)-> int:
        return self.__suciedad
    
    @property # tipo
    def tipo (self)-> str:
        return self.__tipo
    
           
    @suciedad.setter # suciedad siempre se esta modificando
    def suciedad(self,cantidad:int):  # la cantidad es lo q ensucian las aves 
        self.__suciedad = cantidad   
        
    
    
        
#  la  SUCIEDAD  se (+) (=0)
    

    def se_ensucia(self,cantidad): # si se ensucia la cantidad d mugre incrementa
         self.__suciedad+=cantidad # la idea es modif no necsito devolver
        
        

    def limpiar(self):# si se lava ,ahora la cantidad de mugre queda en cero
        self.__suciedad=0
    
    