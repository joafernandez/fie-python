"""
Usuarios


+realizan las compras()


-dinero en su cuenta 
compras() ++ puntos lealtad
se conoce:
-edad
-su saldo disponible, 
-sus puntos acumulados,
-su nivel actual, // ACA FALTO ESTRATEGIA!!!1 NIVEL PREGUNTAR???
-si es extranjero o nacional,
- su carrito de productos.
 
El sistema de niveles funciona de la siguiente manera "SEGUN" los "puntos" acumulados:

● Bronce: es el nivel inicial de todo usuario nuevo. Solo permite tener un producto en el carrito
a la vez y no puede tener saldo negativo.
● Plata: Se alcanza al acumular 5.000 puntos. Permite tener hasta 5 productos en el carrito y un
saldo negativo de $5000.
● Oro: Se alcanza con 15.000 puntos. No tiene restricciones en la cantidad de productos en el
carrito y un saldo negativo de $20000
1

El nivel se actualiza automáticamente cuando el usuario alcanza los puntos necesarios, pero también
puede descender si pierde puntos por penalizaciones.


Se pide que los usuarios puedan:
1) Agregar un producto a su carrito, respetando las restricciones de su nivel actual y
verificando que cumple con los requisitos del producto (por ejemplo, la edad para bebidas
alcohólicas).
2) Cargar saldo en su cuenta para poder realizar compras.
3) Realizar la compra de todos los productos de su carrito, lo cual implica:
○ calcular el precio total de los productos (aplicando tax-free si corresponde) más el
costo de envío; 

FALTAAAAAAAA!!!!!!!!!!!!!!

○ verificar que tiene saldo suficiente;
○ debitar el monto de su saldo;
○ acreditar puntos equivalentes al 10% del valor pagado; //no habia hecho
○ vaciar el carrito.//no habia hecho
● Actualizar nivel: Luego de cada compra se actualiza el nivel del usuario """


from producto import Producto
from strategy_niveles import Bronce, Oro, Plata  #(maximo_producto() y saldo_minimo())

class Usuario:
    def __init__(self,nombre:str,edad:int,extrangero=False): 
        self.nombre=nombre
        self.edad=edad
        self.extrangero=extrangero #si no paso nada es falso nacional
        self.saldo_inicial=0 #se sabe q va cambiando
        self.lista_producto=[]
        self.puntos=0# cada vz q compra incrementa
        self.estrategia=Bronce() #nivel actual que comienza con bronce la primera vz
        
        
    def ingresar_saldo(self,monto):
        self.saldo_inicial+=monto
        
        
        
    def agregar_producto(self,producto:Producto): #calculo antes el max_prodcuto llamo a la estartegia
        if len(self.lista_producto)>= self.estrategia.maximo_producto():
             raise ValueError ("no se puede comprar ")
        self.lista_producto.append(producto)
            
            
    def comprar(self,producto:Producto): 
        total=0
        for aux in self.lista_producto:
            total+= aux.precio_venta(self) 
        #cuando compro me tiene q quedar un saldo_minimo(), segun estrategia niveles    
        if self.saldo_inicial - total < self.estrategia.saldo_minimo():
            raise ValueError ("se pasa el saldo minimo")
        self.saldo_inicial-=total
        acreditar_puntos= int (total*0.1) #es el 10% de la compra, y convierto en int
        self.puntos+=acreditar_puntos 
        self.actualizar() # ya no es bronce()
        
        
        
    def actualizar(self): #los puntos cambian significa q pasan a otro nivel
        if self.puntos >=15000:
            self.estrategia= Oro()
        elif self.puntos >=5000:
            self.estrategia = Plata()
        else:
            self.estrategia = Bronce()
        
        
#pase como parametro la estrategia y para eso lo llamo directo
#producto lo llame con self y era parametrooooooooo
#precio_venta( aca le paso usuario como es la misma clase=self)
# en actualizar() puse mal los <=
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
        
    