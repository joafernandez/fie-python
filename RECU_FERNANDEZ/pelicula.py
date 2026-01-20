
from caracteristica import Caracteristica


class Pelicula:
    def __init__(self, titulo, duracion_minutos, genero, pais_origen, edad_minima, precio_base):
        self.titulo = titulo  
        self.duracion_minutos = duracion_minutos  
        self.genero = genero  
        self.pais_origen = pais_origen 
        self.edad_minima = edad_minima  
        self.precio_base = precio_base  
        self.caracteristicas = []  # aca voy a llamar a los DECORADORES____________________________!
        
    
    def agregar_caracteristica(self, caracteristica):  # voy agergar los DECORADORES_________ 
        self.caracteristicas.append(caracteristica)
    
    def calcular_precio_final(self):  # aplico todas las caract
        precio = self.precio_base
        for aux in self.caracteristicas:
            precio = aux.modificar_precio(precio)
        return precio
    
    def es_accesible_para(self, usuario):  # verifico llamo  CARACTRISTICA
        if usuario.edad < self.edad_minima: #edad
            return False
        for aux in self.caracteristicas: # carct (exclusividad, pais restring)
            if not aux.es_accesible_para(usuario, self):
                return False
        return True
    
    def es_gratuita(self):  # es gratis???
        return self.calcular_precio_final() == 0 #DEVUELVE TRUE SI el costo es cero