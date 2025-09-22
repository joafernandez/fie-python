"""Consigna de trabajo:
Se pide realizar la codificación que permita:
1) Hacer una bandada de dos gaviotas, una paloma, una cotorra y dos loros barranqueros, en forma de V.
2) Representar a un auto que les guste, que inicialmente esté limpio y ubicarlo en Buenos Aires.
3) Crear a SmallLav, un pequeño lavadero artesanal porteño donde trabajan 3 personas.
4) Crear test de las siguientes situaciones:
a) Que pase una paloma gorda por encima del auto.
b) Que la bandada antes mencionada pase por encima del auto.
c) Que sobre Buenos Aires caiga una lluvia de ceniza volcánica.
d) Llevar el auto a SmallLav, hacerlo lavar y saber cuánto costó.
e) Que la bandada cambie su formación de V a W y vuelva a pasar por el auto
f) Llevar el auto al lavadero más barato de Buenos Aires y hacerlo lavar."""

from gaviotas import Gaviota
from palomas import Paloma
from otras_aves import OtrasAves
from vehiculo import Vehiculo
from bandada import Bandada
from lave_Autom import Automatico
from lava_Arte import Artesanal
from ciudad import Ciudad

def main():
        g1=Gaviota()
        g2=Gaviota()
        p1=Paloma()
        c1=OtrasAves()
        
        banda1=Bandada("v")
        
        banda1.agregar_a_lista_aves(g1)   # no hice funcion de agregar a la bandada !!!1
        banda1.agregar_a_lista_aves(g2)
        banda1.agregar_a_lista_aves(p1)
        banda1.agregar_a_lista_aves(c1)
        
        buenos_aires=Ciudad()
        auto=Vehiculo("PEUGEOT","X77")
        buenos_aires.agregar_auto(auto)
        
        smallLav=Artesanal(3)
        
        
        
        
        
        
        
        
        
        
        
    
        
        