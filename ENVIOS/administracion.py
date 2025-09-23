from envios import Envio



class Administracion:
    def __init__(self):
        self.lista_envios=[]
        
        
    """ self.__peso=peso
        self.__precio_base
        self.__categoria 
        self.__origen
        self.__destino=                     """
         
    
    
    def agregar_envios_lista(self,envio:Envio):
        self.lista_envios.append(envio)
        
     
    def __str__(self):
        return f"{self.lista_envios}"
    
        
    def envios_internacionales(self):   ## REPASAAAAAAAAAAAAAAAAAAAAAR!!!!!!!!!!!!
        lista_internacional = []
        for envio in self.lista_envios:   # recorro todos los envios que fui guardando
            if envio.mostrar_ubicacion_Origen.mostrar_pais != envio.mostrar_ubicacion_Destino.mostrar_pais:
                lista_internacional.append(envio)
        return lista_internacional
    
    

    
    def __str__(self):
        return f"{self.envios_internacionales}"
    
   
    
    