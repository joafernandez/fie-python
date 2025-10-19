
# crear :

from tienda_virtual import Tienda  
from usuario import Usuario
from producto import Mueble, Indumentaria, Bebida
from strategy import Pesado, Promocion, Taxfree

def main():
    # Creo la tienda
    tiendita = Tienda()

    # Creo usuarios
    u1 = Usuario("Joana", 34, extrangero=False)  # mayor de edad
    u2 = Usuario("Pedro", 16, extrangero=False)  # menor de edad

    # Les cargo saldo
    u1.ingresar_saldo(20000)
    u2.ingresar_saldo(15000)

    # Creo productos
    m1 = Mueble("Mesa", 6000)
    i1 = Indumentaria("Campera", 5000)
    b1 = Bebida("Vino", 3000, 18)

    # Agrego productos al stock de la tienda
    tiendita.agregar_producto(m1)
    tiendita.agregar_producto(i1)
    tiendita.agregar_producto(b1)

    # Agrego usuarios a la tienda
    tiendita.agregar_usuario(u1)
    tiendita.agregar_usuario(u2)

    # Usuarios agregan productos a su carrito
    u1.agregar_producto(m1)   # yo agrego mesa
    u1.agregar_producto(b1)   # yo agrego vino
    u2.agregar_producto(b1)   # Pedro (menor) intenta agregar Vino
    u2.agregar_producto(i1)   # Pedro agrega Campera

    # Compras
    print(">>> Compra de Joana (mayor)")
    tiendita.comprar(u1)
    print("Saldo:", u1.saldo_inicial)
    print("Puntos:", u1.puntos)
    print("Carrito:", [p.nombre for p in u1.lista_producto])

    print("\n>>> Compra de Pedro (menor)")
    tiendita.comprar(u2)  # la bebida debería volver al stock
    print("Saldo:", u2.saldo_inicial)
    print("Puntos:", u2.puntos)
    print("Carrito:", [p.nombre for p in u2.lista_producto])

    # Mostrar stock de la tienda después de las compras
    print("\nStock de la tienda:")
    print([p.nombre for p in tiendita.lista_producto_tienda])

if __name__ == "__main__":
    main()
