
from abc import ABC, abstractmethod


class Enfermedad(ABC):#___________________________________________________________________________________________
    def __init__(self, celulas_amenazadas):
        self.celulas_amenazadas = celulas_amenazadas  # cantidad de celulas que afecta
    
    @abstractmethod
    def hacer_efecto(self, persona):  # POLIMORFISMO!
        pass
    
    def atenuar(self, cantidad):  # baja las celulas que amenza
        self.celulas_amenazadas -= cantidad
        if self.celulas_amenazadas < 0:  # compruebo q no sea negatv
            self.celulas_amenazadas = 0 #lo dejo en cero 
    
    def esta_curada(self):  # defino una persona curada 
        return self.celulas_amenazadas == 0

#_______________________________________________________________HERENCIAS______________________________________________
class Infecciosa(Enfermedad):
    
    def hacer_efecto(self, persona): # sube temperatura: milesima parte de celula amenazadas 
        aumento_temperatura = self.celulas_amenazadas / 1000
        persona.temperatura += aumento_temperatura
    
    def reproducirse(self):  # duplica
        self.celulas_amenazadas = self.celulas_amenazadas * 2






class Autoinmune(Enfermedad):
    def hacer_efecto(self, persona): # destruye,resta celulas de la persona
        persona.celulas -= self.celulas_amenazadas 





class InfecciosaAutoinmune(Enfermedad):
    # Hace AMBOS efectos
    # efecto infeccioso: sube temperatura
    # efecto autoinmune: destruye celulas
      
      
    def hacer_efecto(self, persona):
        aumento_temperatura = self.celulas_amenazadas / 1000
        persona.temperatura += aumento_temperatura
        persona.celulas -= self.celulas_amenazadas
    
    
    
    def reproducirse(self):  # puede reproducirse como infecciosa
        self.celulas_amenazadas = self.celulas_amenazadas * 2
