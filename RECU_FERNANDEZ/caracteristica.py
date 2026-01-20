# la clase pelicula me llama para agregar caracteristicas adicionales


from abc import ABC, abstractmethod


#DECORADOR

class Caracteristica(ABC):
    # el  precio se modifca
    # y hay dif accesos
   
    @abstractmethod
    def modificar_precio(self, precio_base):  #le mando precio base para q haga desuento o aumente
        pass
    
    @abstractmethod
    def es_accesible_para(self, usuario, pelicula):  # cada caract verifica su restriccion
        pass


#solo aplica descueto,lo recibo
class Promocional(Caracteristica):#________________________________________________________________________________
    def __init__(self, descuento):
        self.descuento = descuento  
    
    def modificar_precio(self, precio_base):  
        descuento = precio_base * (self.descuento / 100) # ver lugeo          <------- otra vz
        return precio_base - descuento #me da el precio final 
    
    def es_accesible_para(self, usuario, pelicula):  # el usuario  y qu epeli
        return True # siempre accedo


# solo para DIAMANTE y aumenta 20%
class Exclusiva(Caracteristica):
    def modificar_precio(self, precio_base): 
        return precio_base * 1.20  # o 0.20 ?? ver calculo otra v                            z<------
    
    def es_accesible_para(self, usuario, pelicula):  # solo Diamante
        return usuario.suscripcion.permite_exclusivos()


# solo en paiesse 
class Restringida(Caracteristica):
    def __init__(self, paises_restringidos):
        self.paises_restringidos = paises_restringidos  #  que paises no pueden ver 
    
    def modificar_precio(self, precio_base_normal): 
        return precio_base_normal #xq no dice nada precio es igual
    
    def es_accesible_para(self, usuario, pelicula):  # puede acceder si es el pais
        return usuario.pais not in self.paises_restringidos #si el usuario no esta en la lista de paieses restringidos