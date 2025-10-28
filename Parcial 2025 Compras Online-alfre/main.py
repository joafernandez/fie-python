
# -*- coding: utf-8 -*-
"""
main.py
-------
Pequeña demo manual para mostrar el flujo end-to-end.
"""

from tienda_virtual import Tienda
from usuario import Usuario
from producto import Mueble, Indumentaria, BebidaAlcoholica
from strategy import Pesado, Promocion, TaxFree

def main():
    print("=== DEMO E-COMMERCE (Strategy en modificadores y niveles) ===")
    tienda = Tienda()

    # Usuario mayor argentino
    u = Usuario("Ana", edad=25, extranjero=True)
    u.cargar_saldo(100000)
    tienda.registrar_usuario(u)

    # Estrategias (modificadores)
    pesado = Pesado()
    promo30 = Promocion(0.30)
    taxfree = TaxFree()

    # Productos
    mueble = Mueble("Mesa Roble", 60000, [pesado, promo30, taxfree])
    mochila = Indumentaria("Mochila", 5000, [])
    cerveza = BebidaAlcoholica("Cerveza", 1000, [])

    tienda.agregar_a_stock(mueble)
    tienda.agregar_a_stock(mochila)
    tienda.agregar_a_stock(cerveza)

    # Carrito y etiqueta
    u.agregar_al_carrito(mueble)
    print(mueble.etiqueta(u))

    # Intentar venta
    total = tienda.gestionar_venta(u)
    print(f"Total pagado: ${total:,.2f}")
    print(u)

if __name__ == "__main__":
    main()
