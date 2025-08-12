from mascota import Mascota

class Gato:(Mascota)
    def __init__(self, nombre ) :  
        super().__init__(nombre) #super llama metodo de clase padre mascota
        
      
        
    def saludar (self) : 
        super ().saludar () # cuando uso super agrego lo que ya tiene y agrego lo mio  y si no uso? solo seria mi mteodo
        print ( "miau")
        
        