
from persona import Persona
from enfermedad import Infecciosa, Autoinmune, InfecciosaAutoinmune


def main():
    # punto 1
    print("____________________________________________________________________________________________")
    lupus=Autoinmune(1000)
    malaria=Infecciosa(40000)
    persona1=Persona(20,5000000) #arranca con 5M de celulas
    print (f"cantidad de celulas de la persona: {persona1.celulas}") 
    
    persona1.vivir_un_dia()
    
    lupus.hacer_efecto(persona1)
    malaria.hacer_efecto(persona1)
    print (f"cantidad de celulas de la persona luego de efecto : {persona1.celulas}") 
    
    #punto 2
    print("____________________________________________________________________________________________")
    malaria.atenuar(5000)
    lupus.atenuar(500)
    persona1.limpiar_curadas()
    print (f"cantidad de celulas de la persona luego atenuar: {persona1.celulas}") 
    if persona1.esta_sana():
        print("la persona esta sana")
    else:
        print ("sigue enferma")
        
     
    #punto 3
    print("____________________________________________________________________________________________")
    persona1.recibir_medicamento(300000)
    print (f"cantidad de celulas de la persona medicada: {persona1.celulas}") 
    if persona1.esta_sana():
        print("la persona esta sana")
    else:
        print ("sigue enferma")
     
    #punto 4
    print("____________________________________________________________________________________________")
    enfermedad_multiple=InfecciosaAutoinmune(200000)
    print ("se enfermo x2") 
    enfermedad_multiple.hacer_efecto(persona1)
    print (f"cantidad de celulas de la persona enferma otra vz ahora es  : {persona1.celulas}") 
    if persona1.esta_sana():
        print("la persona esta sana")
    else:
        print ("sigue enferma")
    
 
 

 
 

if __name__ == "__main__":
    main()




"""


 Clase Enfermedad (abstracta):
   Tiene 3 tipos (Infecciosa, Autoinmune, Mixta). Cada una calcula sus efectos 
   de forma diferente. Sabe atenuarse y sabe si está curada.

 Clase Infecciosa:
   Es una enfermedad que sube la temperatura de la persona. Puede reproducirse 
   (empeorar).

 Clase Autoinmune:
   Es una enfermedad que destruye células de la persona. No se reproduce.

 Clase InfecciosaAutoinmune:
   Es una enfermedad que hace las dos cosas: sube temperatura Y destruye células. 
   Puede reproducirse.

 Clase Persona:
   Es la que contrae enfermedades, vive días (las enfermedades hacen efecto), 
   recibe medicamentos (atenúa sus enfermedades) y puede saber si está sana.


"""