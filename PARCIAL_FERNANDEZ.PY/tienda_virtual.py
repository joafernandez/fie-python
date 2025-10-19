

""" Tienda Virtual
 conoce :
- todos los usuarios 
- todos los productos

tienda debe poder:

1) Gestionar venta: dado un usuario con productos en su carrito, permite la compra().
Si el usuario es menor y lleva bebidas alcohólicas se las retira del carrito y las pone() nuevamente en
los productos disponibles.

2) Gestionar la morosidad: aplica descuento() de 100 puntos a los usuarios con saldo negativo."""


from usuario import Usuario

class Tienda:
    def __init__(self):
        self.lista_usuario=[]#agregar // para ver EDAD 
        self.lista_producto_tienda=[] # de la tienda
        
        
    def agregar_usuario(self,usuario):
        self.lista_usuario.append(usuario)
        
    
    def agregar_producto(self,producto): # le pase usuario antes mal
        self.lista_producto_tienda.append(producto)
        
        
        
    def comprar(self,usuario):
        lista_productos_autorizados=[] #aca voy a guardar lo q si puede comprar
        
        for aux in usuario.lista_producto: # recorro lista de productos DEL UUSUARIO!!!
            #instance: este producto es de tipo bebida?
            if isinstance(aux,Bebida) and usuario.edad <18:
                self.lista_producto_tienda.append(aux)#devolver a la tienda 
            else:
                lista_productos_autorizados.append(aux)
                
        usuario.lista_producto=lista_productos_autorizados #ahora si se puede llevar
        usuario.comprar()
       
       
    
    def morosidad(self,usuario):
        for aux in self.lista_usuario:
            if aux.saldo_inicial <0:
                aux.puntos-=100
            
            
    #metodos mal comprar()  y morosidad()
    
        
    
    
    
    