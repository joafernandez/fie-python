from strategy_proyectil import EstrategiaProyectil
import random

class Tanque:
    def __init__(self, nombre, blindaje, vida):  # creo instancias de los tanques M4, PVSD
        self.nombre = nombre
        self.blindaje = blindaje
        self.vida = vida # daño 
        self.lista_proyectiles = []  #dice que lleva cualquier cantidad de proyectiles
                                     #LISTA DE INSTANCIAS DE ESTRATEGIAS

    def agregar_proyectil(self, proyectil:EstrategiaProyectil):
        self.lista_proyectiles.append(proyectil)


# un tanque  DISPARA


    def disparar(self, otro_tanque:object):      
        estrategia_elegida= random.choice(self.lista_proyectiles) # elegir un proyectil al AZAR
        estrategia_elegida.disparar(self, otro_tanque) # llamo a ESTRATEGIAA  y disparo
        
        
        #la estartegia se supone q hace el daño en los atributos de cada tanque  luego?
        
        
 
# un tanque  RECIBE DAÑO       

    def recibir_dano(self, cantidad_de_daño): 
        self.vida -= cantidad_de_daño
        
        if self.vida < 0: # si me paso restauro pa q no quede negativo 
            self.vida = 0