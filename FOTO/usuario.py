

from publicacion import Publicacion
from persona import Persona
from strategy_permiso import Estrategia_Permiso

class Usuario(Persona):  # HEREDA DE PERSONA!!!!!
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.lista_publicaciones = []  # publicaciones propias
           

    
    def agregar_publicacion(self,contenido):
        self.lista_publicaciones.append(contenido)
        
    
    def __str__(self):
        return f"publicaciones hechas:{self.lista_pubicaciones}amigos:{[a.nombre for a in self.mostrar_lista_amigos]}"
    
    
    def indicar_me_gusta(self, publicacion: Publicacion):
        cantidad_megusta = publicacion.sumar_me_gusta() # llamo al metodo para sumar me gusta
        return cantidad_megusta
        
    
    def compartir_con(self,estrategia:Estrategia_Permiso): # ACA LLAMO A LA "ESTRATEGIA"  PERMISO Q ME DA LO Q CORRSPPONDE!!! 
       return estrategia.quien_puede_ver(self)  #asi se llamara el metodo
       
        


