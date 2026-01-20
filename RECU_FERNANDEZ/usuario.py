

from pelicula import Pelicula
from suscripcion import Suscripcion

class Usuario:
    def __init__(self, nombre, edad, pais, suscripcion, saldo):#ENVIO ESTRATEGIA
        self.nombre = nombre 
        self.edad = edad  
        self.pais = pais  
        self.suscripcion = suscripcion  # con estartegia elijo ________________________
        self.saldo = saldo 
        self.historial = []  #agregar, para saber q vio
    
    def cambiar_suscripcion(self, nueva):  
        self.suscripcion = nueva
    
    def puede_pagar(self, precio):  # le envio precio para ver si le alcanza 
        saldo_despues = self.saldo - precio
        limite = self.suscripcion.obtener_limite_saldo_negativo() # METOD EST __________________
        return saldo_despues >= limite
    
    
    
    def reproducir_pelicula(self, pelicula):  
        if not pelicula.es_accesible_para(self): # llamo al metood pelicual
            return False 
        
        precio = pelicula.calcular_precio_final() 
        if precio == 0:  # si es gratis
            self.historial.append(pelicula) #agrego a las peli del usuario 
            return True #reproduce
        else:  # si tiene q pagar 
            if not self.suscripcion.puede_ver_contenido_pago(): # METOD EST__________________________su plan no permite esta peli?
                return False #pla no permite pagar
            
            if not self.puede_pagar(precio): #tiene saldo?
                return False #saldo insuficiente
            self.saldo -= precio #sino le resto palta
            self.historial.append(pelicula) #y agrego
            return True #reproduce y paga
        
        
    
    def calcular_porcentajes_generos(self):   # !!!NO ANDA
       print("no me salio retorna un numero")
       return 10
    
    def ha_visto(self, pelicula):  # vio la peli?? 
        return pelicula in self.historial
