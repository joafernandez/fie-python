
class Ubicacion:
    def __init__(self,pais:str,ciudad:str):
        self.__pais=pais
        self.__ciudad=ciudad
        
        
    @property
    def mostrar_pais (self):
        return self.__pais
        
        
    @property
    def mostrar_ciudad (self):
        return self.__ciudad
    
    
    def __str__(self):
        return f" (PAIS: {self.__pais}, CIUDAAD: {self.__ciudad})"
    
    
    
    