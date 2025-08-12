from gato import Gato 
from perro import Perro
from mascota import Mascota

def main () :
    
    refugio = []
    
    refugio.append(Gato("pepe"))
    refugio.append(Perro("mika"))
    refugio.append(Gato("LEILA"))
    
    print (refugio)
    
    
    for mascota in refugio :  # es una especie de polimorfismo, xq no importa q mascota es
        mascota.saludar()  # sabe saludar 
                   
                   
                   
    mi_perro = Perro("raul")
    tu_gato = Gato("rosi")
    
   
    
    print (mi_perro)
    print(tu_gato)
    
    mi_perro.saludar()
    tu_gato.saludar()
    
     
 if __name__== "__main__" : # es el programa principal q ejecuta las funciones
         
         