from abc import ABC,abstractmethod


class Estrategia_permiso(ABC):
    @abstractmethod
    
    def quien_puede_ver(self,usuario,publicador):
        pass
    
class Publico(Estrategia_permiso):
    def quien_puede_ver(self,usuario,publicador):
        return True
        
    
    
class Amigos(Estrategia_permiso):
    def quien_puede_ver(self,usuario,publicador):
        return publicador.es_amigo(usuario)

    
class Algunos(Estrategia_permiso): # tiene que ser una lista especifica
    def __init__(self):
        self.usuarios_permitidos = []  
    
    def agregar_usuario_permitido(self, usuario):  
        self.usuarios_permitidos.append(usuario)
    
    def quien_puede_ver(self, usuario, publicador):  # solo si esta en la lista
        return usuario in self.usuarios_permitidos 
    
    
    