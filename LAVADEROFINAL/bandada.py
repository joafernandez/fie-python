from vehiculo import Vehiculo
from strategy_formacion import estrategia_formacion

class Bandada:
    def __init__(self, formacion: estrategia_formacion):
        self.lista_aves=[]  #  loros,gabiotas....
        self.formacion=formacion # v, x ,w...

    def cambiar_formacion(self,nueva_formacion:estrategia_formacion):
        self.formacion = nueva_formacion
    
    def agregar_a_lista_aves(self,objetoAve): # agregar las aves 
            self.lista_aves.append(objetoAve)
    
    def ensuciar(self,vehiculo:Vehiculo): # le pasa el vehiculo a la estrategia para  q ensucie
        self.formacion.ensuciar(self.lista_aves,vehiculo)  # implementar estrategia ---->
    
    def __str__(self):
        cadena = f"Bandada En {self.formacion}\n"
        for ave in self.lista_aves:
            cadena += str(ave) + "\n"
        return cadena
            
            
        
       
                    
     