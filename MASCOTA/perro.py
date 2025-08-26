from MASCOTA.mascota import Mascota

class Perro:(Mascota)
    def __init__(self, nombre ) :  
        super().__init__(nombre) #super llama metodo de clase padre mascota
        
      
        
    def saludar (self) :  
        print ( f"{self.nombre} dice guau")
        
        