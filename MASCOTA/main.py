from MASCOTA.gato import Gato 
from MASCOTA.perro import Perro
from MASCOTA.mascota import Mascota

def main () :
    
    refugio = []
    
    refugio.append(Gato("pepe"))
    refugio.append(Perro("mika"))
    refugio.append(Gato("LEILA"))
    
    print (refugio)
    
    
    for mascota in refugio :  # es una especie de polimorfismo, xq no importa q mascota es
        mascota.saludar()  # sabe saludar 
                   
                   
                   
    mi_perro = Perro("KKKaul")
    tu_gato = Gato("rHHHosi")
    
   
    
    print (mi_perro)
    print(tu_gato)
    
    mi_perro.saludar()
    tu_gato.saludar()
    
     
 if __name__== "__main__" : # es el programa principal q ejecuta las funciones
         
         