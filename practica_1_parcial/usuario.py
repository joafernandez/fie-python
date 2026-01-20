from producto import Pesado,Promocion,Taxfree
from producto import Mueble,Bebida
from strategy_nivele import Bronce, Plata, Oro

class Usuario:
    def __init__(self,nombre, edad, saldo,acumulacion_puntos,extranjero=False):
        self.nombre=nombre
        self.edad=edad
        self.saldo=saldo
        self.acumulacion_puntos=acumulacion_puntos
        self.extranjero=extranjero # main=true
        self.nivel= Bronce () #inicialmente arranca con este nivel --->self.nivel  ES UNA ESTRATEGIA
        self.carrito_productos=[] # se agregra/se  recorre!!!
        
                   
        
    def agregar_producto(self,producto:object): # puede ser bebida,indume ,cualqueir cosa
        #niveles
        if isinstance(producto,Bebida):# si el producto es una bebbida
            if not producto.mayor_edad(self):#si llamo a su metodo y no es mayor(o sea=false)
                print("no puede comprar")
                return
        self.carrito_productos.append(producto)#sino agrego
        print("producto agregado a carrito ")      
            
                 
            
        
    def cargar_dinero(self,dinero:float):
       self.saldo+=dinero
        
        
        
    def comprar(self): # el precio de todos! [bebida][ropa][comida][libreria]  
        for aux in self.carrito_productos:
            precio_total= aux.precio_venta()+ aux.costo_envio()
            self.cargar_dinero()
            if self.saldo < precio_total:
                print("no alcanza el dinero")
                return
            self.saldo-=precio_total
            premio= precio_total*0.10
            self.acumulacion_puntos+=premio
    
        self.carrito_productos.clear() # limpiar lista!no 1 producto
            
            
    def actualizar_niveles(self): #LLAMO A LAS ESTARTEGIAS = bronce() =Oro() =Plata()
        if self.acumulacion_puntos>=5000:
            self.nivel= Oro()
       
        elif self.acumulacion_puntos >=1000:
            self.nivel=Plata()
        
        else: 
            self.nivel=Bronce() 
            
       
        
    
     