from usuario import Usuario
from producto import Mueble, Bebida

class Tienda:
    def __init__(self):
        self.lista_usuarios=[]#agregar   juan, celia, mica
        self.lista_productos_disponibles=[]#agergar  remera, azucar , sofa, cerveza
        
        
    def agregar(self,usuario:object):
        self.lista_usuarios.append(usuario)
        
        
    def agregar_producto(self,producto:object):
        self.lista_productos_disponibles.append(producto)
        
       #juan 
       # 17 años
       # 200 pesos 
       #carrito:[sofa][azucar][remera][cerveza]
               
    def vende (self,usuario):
        for aux in usuario.carrito_productos[:]: #recorro  carrito
            if isinstance(aux,Bebida) and usuario.edad <18: #y es menor
                print("NO PUEDE COMPRAR")
                usuario.carrito_productos.remove(aux) #lo quito del carrito
                self.lista_productos_disponibles.append(aux)
                
    def descuento (self,usuario):
        for aux in self.lista_usuarios: #recorro lista de usuarios registrados
            if usuario.saldo <0: #si tiene saldo negativo
                usuario.acumulacion_puntos-=1000 #le resto mil puntos
                
            
        
    
    

                
            
        
    