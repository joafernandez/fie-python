class Mascota:
    def __init__(self, nombre):  
        self.nombre = Mascota._validar_nombre(nombre)
        
    def saludar(self):
       print (f"{self, name} dice: ",end= "") # polimorfismo para las clases 
        
     @staticmethod
     def _validar_noombre(nombre) :
        if not insistance (nombre, str) :
            raise TypeError("deb ser cadena")
        if not nombre : 
            raise ValueError ("no puede ser vacio")
        return nombre # el dato esta ok, retorno
    
    def saludar (self) :  
        print ( f"{self.nombre} dice guau")
        
        