from abc import ABC, abstractmethod 


#_______________________________________________ESTRATEGIA___________________________________________________________________

class Estrategia(ABC):
    
    @abstractmethod
    def calcular_precio(self): # aca me llama bebida
        pass
    
    
class Agua(Estrategia):
    def calcular_precio(self):
        return 50
    
class Gaseosa(Estrategia):
    def calcular_precio(self):
        return 150
    
class Granizado(Estrategia):
    def calcular_precio(self):
        return 50
    
class Cortado(Estrategia):
    def calcular_precio(self):
        return 250
    

#_____________________________________________________BEBIDA______________________________________________________



from typing import List

class Bebida:
    def __init__(self,nombre,lista_ingredientes:list[str],estrategia_de_precio): #todolo que recibo
        self.nombre=nombre #guardo el nombre
        self.lista_ingredientes=lista_ingredientes # guardo la lista, no pongo [] xq no tengo q crear la recibo d euna
        self.estrategia_precio=estrategia_de_precio # esta es una CLASE STARTEGY QUE ME VA A DAR EL PRECIO 
        

    def mostrar_nombre(self):
        return self.nombre


    def mostrar_ingredientes(self):
        return self.lista_ingredientes
    

    def obtener_precio(self):
        return self.estrategia_precio.calcular_precio() #pregunta a la ESTRATEGIA !!!!!!!

    def preparar_bebida(self):
        texto=" " # inicializo vacio 
        for aux in self.lista_ingredientes: #recorro los ingredientes que tengo
            texto+= aux +" " # voy agregando todos uno al lado de otro
        return texto # devuelvo la bebida con ingredientes
        

    
    
      