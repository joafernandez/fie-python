"""Productos

 -nombre 
 - precio base. 

- precio de venta()= precio base + montos  modificadores -> llamar strategy para ver cual 


3 tipos (en un futuro se agreguen)

1) Muebles:  recargo $1000 en su precio de venta()

2)Indumentaria: no recargos 

3) Bebidas Alcohólicas: solo compradas por usuarios mayores de 18 años



Un producto puede tener múltiples modificadores simultáneamente."lista de MODIFICADOR[]"

mueble pesado en promoción del 30% que un usuario extranjero compra tax-free: sería un mueble
(con su recargo de $1000), pesado (sumando $3000 al envío), en promoción (reduciendo el precio un
30%) y sin IVA."""
        

from abc import ABC,abstractmethod

from strategy import Pesado, Promocion, Taxfree


class Producto(ABC):
    def __init__(self,nombre:str,precio_base:int):
        self.nombre=nombre
        self.precio_base=precio_base
        self.lista_modicadores=[] #tengo q agregar ,ya es la estrategia 
  
    def agregar_modficador(self,modificador):
        self.lista_modicadores.append(modificador)
        
    
    @abstractmethod
    def precio_venta(self,usuario): # usuario es para el iva y saber si extrangero
        pass
    


class Mueble(Producto):#--------------------------------------------------------------------------------
    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)
      
        
   # RECARGO=1000 
    
    def precio_venta(self,usuario):
        precio=self.precio_base+1000
        for aux in self.lista_modicadores: #recorro lista
            precio=aux.sumar_modificador(precio,usuario) #llamo a laestartegia 
        return self.precio
        
        
    
class Indumentaria(Producto):#---------------------------------------------------------
    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)
      
        
             
    def precio_venta(self,usuario): 
        precio=self.precio_base #no tengorecargo 
        for aux in self.lista_modicadores: #recorro lista
            precio=aux.sumar_modificador(precio,usuario) #llamo a laestartegia 
        return self.precio
        
        
class Bebida (Producto):# solo pueden ser compradas por usuarios mayores de 18 años
    def __init__(self, nombre, precio_base,edad:int):
        super().__init__(nombre, precio_base)
              
        
  
    def precio_venta(self,usuario):
        if self.edad >18:
        
            for aux in self.lista_modicadores: #recorro lista
                precio=aux.sumar_modificador(precio,usuario) #llamo a laestartegia 
                return self.precio



"""me confundi:
precio con precio_base :(


"""
