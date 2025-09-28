

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__lista_amigos = []   # lista privada
        
    @property
    def mostrar_lista_amigos(self):
        return self.__lista_amigos
    
    def agregar_amigo(self,nombre):
        self.__lista_amigos.append(nombre)
        
        
        
        
        
        
        
    