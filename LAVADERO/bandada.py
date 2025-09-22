from vehiculo import Vehiculo
from gaviotas import Gaviota
from palomas import Paloma
from otras_aves import OtrasAves




class Bandada:
    def __init__(self,formacion:str):
        self.lista_aves=[]  # agregar 
        self.formacion:str=formacion
    
        def agregar_a_lista_aves(self,objetoAve): # falta!!!!!
            self.lista_aves.append(objetoAve)
        


    # acordarme q UNA ave ensucia asi : ensuciar(vehiculo)
    #ahora son MUCHAS, entones recorro la lista de aves y ensucio
    
   
    
    def ensuciar(self,Vehiculo:Vehiculo,formacion:str):
        
        if formacion=="v": # todas ensucian
            for aux in self.lista_aves: #con un aux recorro cada ave
                aux.ensuciar(Vehiculo)
                
                
        elif formacion=="w":# ensucian 2 veces
            for aux in self.lista_aves: 
                aux.ensuciar(Vehiculo)
                aux.ensuciar(Vehiculo)
                     
                     
        elif formacion=="l": #ensucia la pri y ult,no tengo q recorrer neceistoo el tam 
            if len(self.list_aves)>=2: # si el tam es al menos 2 
                self.lista_aves[0].ensuciar(Vehiculo)
                self.lista_aves[-1].ensuciar(Vehiculo) 
                
                
            
            
        
       
                    
     