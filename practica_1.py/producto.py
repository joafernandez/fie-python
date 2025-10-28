
class Producto: # no es ABC xq las hijas no deben(si o si) implementar un metodo igual
    def __init__(self,nombre,precio_base,costo_envio):
        self.nombre=nombre
        self.precio_base=precio_base
        self.costo_envio=costo_envio
        
        
    def precio_venta(self): # el decordor usa este metodo para definir precio total
        return self.precio_base

    def precio_envio(self): # el decordaor usa este metodo para definir costo total 
        return self.costo_envio 
    
    
    
class Mueble(Producto):
    def __init__(self, nombre, precio_base, costo_envio):
        super().__init__(nombre, precio_base, costo_envio)
        
    def recargo_precio_venta(self): 
        return super().precio_venta()+1000 #llamo al metdo de la clase padre(no poli)
    
  

class Bebida(Producto):
    def __init__(self, nombre, precio_base, costo_envio):
        super().__init__(nombre, precio_base, costo_envio)
         
         
    def mayor_edad(self,usuario:object): #llama a una clase objeto usuario para saber mayoria de edad 
        if usuario.edad >=18:
            return True #puede comprar 

        else:
            print("no puede comprar")
            return False  
            





 # DECORADOR: puede tener varios modificadores simultaneamente       
        
  
class Decorador_de_producto(Producto): #hereda el comportamiento de un Producto
    def __init__(self, producto:object): # recibe un producto ya creado para modificar su precio
        self.producto=producto
        
    def precio_venta(self): #polimorfismo del metodo de  Producto
        return self.producto.precio_venta()  #llama al metodo de producto que esta envolviendo
    # se redefine en las subclases


    
class Promocion(Decorador_de_producto):
    def __init__(self, producto,descuento):
        super().__init__(producto)
        self.descuento=descuento
    
    def precio_venta(self): 
        precio_venta_final=self.producto.precio_venta()
        precio_venta_final*=(1-self.descuento) # 1-0,30=0,70 
        return  precio_venta_final
        
    

class Pesado(Decorador_de_producto):
    def __init__(self, producto):
        super().__init__(producto)
        
   
    def precio_venta(self): 
        precio_venta_final=self.producto.precio_venta()
        precio_venta_final+=3000 #calcula y guarda
        return  precio_venta_final
    

class Taxfree(Decorador_de_producto):
    def __init__(self, producto):
        super().__init__(producto)
    
    
    def precio_venta(self,usuario:object): #reibe datos del usuario extranjero o no 
        iva= self.producto.precio_venta() *0.21
        precio_venta_final=self.producto.precio_venta()
        
        if usuario.extranjero: #si este(self) usuarios es extrannjero...
             precio_venta_final-=iva 
        else:
            precio_venta_final+=iva
            
        return precio_venta_final
            
          
        