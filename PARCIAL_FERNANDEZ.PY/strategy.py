
""" los productos pueden tener modificadores que afectan 

-precio venta 
-costo de envío:  // es un atributo tb ojo


1)  Promoción: reduce el "precio venta" del producto en un porcentaje determinado.


2)  Pesado:  agrega a su "precio venta" un extra por envío en $3000.


# NECSITO USUARIO
3)  Tax-Free: disponible solo para "usuarios extranjeros", elimina el agregado de IVA al "precio de
venta" del producto. 

Todos los productos que no tengan este modificador se agregara el IVA
del 21% sobre el precio base.

"""

#le tengo q pasar monto a sumar al producto con un metodo ->sumar_modificador()



from abc import ABC,abstractmethod
class Estrategia_Modificador(ABC):#--------------------------------------------------------------------

    @abstractmethod
    def sumar_modificador(self,precio:int,usuario):
        pass
    
    
    
    
    
    
    
class Promocion(Estrategia_Modificador):#-------------------------------------------------------------
    def __init__(self,porcentaje:float):
        super().__init__()
        self.porcentaje=porcentaje  
        
        
    # reduce el "precio de venta" porcentaje determinado. 
    def sumar_modificador(self,precio:int,usuario): #aca el usuario no usa 
        precio -= (precio*self.porcentaje)
        return precio
                
    

    
class Pesado(Estrategia_Modificador):#---------------------------------------------------------------
    def sumar_modificador(self,precio:int,usuario):#aca el usuario no usa 
        return precio + 3000 # extra por envío 
        
        
        
        
class Taxfree(Estrategia_Modificador):#---------------------------------------------------------------
    def sumar_modificador(self,precio:int,usuario): #solo aca sire usuario:ES EXTRANGERO ?  IVA
        return precio 
        

        
# otra vez me confundi la variable precio con self.precio  :(
#falta IVA en taxfree