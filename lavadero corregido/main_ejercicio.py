"""
Consigna de trabajo:
1) Hacer una bandada de dos gaviotas, una paloma, una cotorra y dos loros barranqueros, en forma de V.
2) Representar a un auto que les guste, que inicialmente esté limpio y ubicarlo en Buenos Aires.
3) Crear a SmallLav, un pequeño lavadero artesanal porteño donde trabajan 3 personas.

4) Crear test de las siguientes situaciones:
a) Que pase una paloma gorda por encima del auto.
b) Que la bandada antes mencionada pase por encima del auto.
c) Que sobre Buenos Aires caiga una lluvia de ceniza volcánica.
d) Llevar el auto a SmallLav, hacerlo lavar y saber cuánto costó.
e) Que la bandada cambie su formación de V a W y vuelva a pasar por el auto
f) Llevar el auto al lavadero más barato de Buenos Aires y hacerlo lavar.
"""

from gaviotas import Gaviota
from palomas import Paloma
from otras_aves import OtrasAves
from vehiculo import Vehiculo
from bandada import Bandada
from lave_Autom import Automatico
from lava_Arte import Artesanal
from ciudad import Ciudad

def main():
    # (1) Bandada en V con especies pedidas
    g1 = Gaviota(20)
    g2 = Gaviota(10)
    p1 = Paloma(300)  # una paloma
    c1 = OtrasAves("Cotorra")  # una cotorra
    l1 = OtrasAves("Loro Barranquero")
    l2 = OtrasAves("Loro Barranquero")

    b1 = Bandada('V')
    for ave in (g1, g2, p1, c1, l1, l2):
        b1.agregar_a_lista_aves(ave)

    print("=== Bandada Inicial ===")
    print(b1)

    # (2) Auto limpio en Buenos Aires
    bsas = Ciudad()
    auto = Vehiculo("Auto", "AAA123", 0)  # limpio
    bsas.agregar_auto(auto)
    print("\n=== Ciudad / Auto ===")
    print(bsas)
    print(auto)

    # (3) SmallLav (artesanal con 3 personas) + uno automático para (f)
    small_lav = Artesanal(3)
    auto_wash = Automatico()
    bsas.agregar_lavadero(small_lav)
    bsas.agregar_lavadero(auto_wash)

    print("\n=== Lavaderos en la ciudad ===")
    for lav in bsas.lista_lavaderos:
        print(str(lav))

    # (4a) Paloma gorda pasa por encima del auto
    print("\n-- (a) Paloma gorda ensucia el auto --")
    paloma_gorda = Paloma(1200)
    paloma_gorda.ensuciar(auto)
    print(auto)

    # (4b) La bandada pasa por encima del auto
    print("\n-- (b) Bandada (V) pasa por el auto --")
    b1.ensuciar(auto)
    print(auto)

    # (4c) Lluvia de ceniza en Buenos Aires
    print("\n-- (c) Lluvia de ceniza (50 mg) --")
    bsas.ensuciar_ceniza(50)
    print(auto)

    # (4d) Llevar el auto a SmallLav y saber cuánto costó (y limpiar)
    print("\n-- (d) Lavado en SmallLav (artesanal) --")
    precio_small = small_lav.calcular_precio(auto)
    auto.limpiar()
    print(f"Precio SmallLav: {precio_small} | {auto}")

    # (4e) Cambiar formación a W y volver a pasar
    print("\n-- (e) Cambiar formación a W y pasar nuevamente --")
    b1.cambiar_formacion('W')
    b1.ensuciar(auto)
    print(auto)

    # (4f) Lavar en el lavadero más barato de la ciudad
    print("\n-- (f) Lavar en el lavadero más barato --")
    elegido, precio = bsas.lavar_en_mas_barato(auto)
    print(f"Elegido: {elegido} | Precio: {precio} | {auto}")

if __name__ == '__main__':
    main()
