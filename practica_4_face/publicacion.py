from abc import ABC,abstractmethod
from estrategia_permiso import Estrategia_permiso


class Publicacion(ABC):
    def __init__(self,estrategia_permiso):
        self.estrategia_permiso=estrategia_permiso #___________lo define estrategia
        self.me_gusta=0
        
    
    @abstractmethod
    def calcular_espacio_KB(self): #________IMPLEMENTAN TODAS 
        pass
    
    
    def agregar_mg(self):
        self.me_gusta+=1
        
    def ver_publicacion(self,usuario,influencer_que_publica):
        return self.estrategia_permiso.quien_puede_ver(usuario,influencer_que_publica) #______________ llama a la Estrategia PERMISO
        
        
    
    
class Texto(Publicacion):
    def __init__(self,texto,estrategia_permiso):
        super().__init__(estrategia_permiso)
        self.texto=texto
        
    def calcular_espacio_KB(self):
        return len(self.texto) #tam del texto 
    
    
class Foto(Publicacion):
    FACTOR_COMPRESION=0.7  #puede cambiar
    def __init__(self,alto,ancho,estrategia_permiso):
        super().__init__(estrategia_permiso)
        self.alto=alto
        self.ancho=ancho
      

    def calcular_espacio_KB(self):
        espacio=self.alto*self.ancho*Foto.FACTOR_COMPRESION
        return espacio
            
    
class Video(Publicacion):
    def __init__(self,estrategia_calidad,duracion_seg,estrategia_permiso):
        super().__init__(estrategia_permiso)
        self.calidad=estrategia_calidad #____________________lo define la estrategia
        self.duracion_seg=duracion_seg

    def calcular_espacio_KB(self): # uso una ESTRATEGIA 
        tam= self.calidad.calcular_tam_video()
        
    
#__________________________________ESTRATEGIA DE VIDEO ____________________________________________________

class Estrategia_Calidad(ABC):
    @abstractmethod
    def calcular_tam_video(self,segundos):
        pass
    
class Normal(Estrategia_Calidad):
    def calcular_tam_video(self,segundos):
        return segundos
        
    
class HD (Estrategia_Calidad):
    def calcular_tam_video(self,segundos):
        return segundos*3
    
    