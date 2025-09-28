

from abc import ABC, abstractmethod

class Publicacion(ABC):#-------------------------------------------------------------------------------
    def __init__(self):
        self.me_gusta=0
        
    def sumar_me_gusta(self):
        self.me_gusta += 1
        return self.me_gusta
    
    @abstractmethod
    def calcular_espacio(self):
        pass


class Foto(Publicacion):#-----------------------------------------------------------
    def __init__(self,alto:int,ancho:int,factor_compresion:float=0.7):
        super().__init__()
        self.alto=alto
        self.ancho=ancho
        self.factor_compresion=factor_compresion
      
        
    def calcular_espacio(self):
        espacio=(self.alto*self.ancho)*self.factor_compresion 
        return espacio 
            

class Texto (Publicacion):#--------------------------------------------------------
    def __init__(self,texto_publicado:str):
        super().__init__()
        self.texto_publicado=texto_publicado
 

    def calcular_espacio(self):
        espacio= len(self.texto_publicado)
        return espacio 
            

class video (Publicacion):#---------------------------------------------------------
    def __init__(self,calidad:str,duracion:int):
        super().__init__()
        self.calidad=calidad
        self.duracion=duracion
        
    
    def calcular_espacio(self):
        if self.calidad.lower()=="normal":
            espacio=self.duracion
        elif  self.calidad.lower()=="hd":
            espacio=self.duracion*3
        return espacio 
            