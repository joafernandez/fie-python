"""Main auxiliar: recorre objetos y muestra su comportamiento básico.
No reemplaza los tests automáticos, pero sirve para una demo rápida en clase.
"""
from vehiculo import Vehiculo
from palomas import Paloma
from gaviotas import Gaviota
from otras_aves import OtrasAves
from bandada import Bandada
from ciudad import Ciudad
from lava_Arte import Artesanal
from lave_Autom import Automatico

def main():
    print("=== PRUEBA RÁPIDA DE OBJETOS ===")
    auto = Vehiculo("Auto", "PRB001", 0)
    p = Paloma(100.0)
    g = Gaviota(5)
    l = OtrasAves("Loro Barranquero")

    print(auto)
    p.ensuciar(auto)
    g.ensuciar(auto)
    l.ensuciar(auto)
    print("Luego de aves sueltas:", auto)

    b = Bandada('V')
    b.agregar_a_lista_aves(p)
    b.agregar_a_lista_aves(g)
    b.agregar_a_lista_aves(l)
    b.ensuciar(auto)
    print("Bandada en V ensucia:", auto)

    b.cambiar_formacion('W')
    b.ensuciar(auto)
    print("Bandada en W ensucia nuevamente (doble):", auto)

    c = Ciudad()
    c.agregar_auto(auto)
    c.ensuciar_ceniza(25)
    print("Lluvia de ceniza (25):", auto)

    artis = Artesanal(2)
    auto_wash = Automatico()
    print("Precio artesanal:", artis.calcular_precio(auto))
    print("Precio automático:", auto_wash.calcular_precio())

    elegido, precio = c.lavar_en_mas_barato(auto)
    print("Lavadero elegido (más barato):", elegido, "| Precio:", precio)
    print("Estado final del auto:", auto)

if __name__ == '__main__':
    main()
