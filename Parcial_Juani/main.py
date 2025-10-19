from usuario import *
from tienda_virtual import TiendaVirtual
from producto import *
from modificador import *
def main():
    tienda = TiendaVirtual()
    user = Usuario("Juan", 16, 5000, 1, NivelBronce(), True)
    mesa = ProductoMueble("Mesa", 60000)
    factory = FactoryModificador()
    mesa.add_modificador(factory.create_modificador("promocion", 30, mesa))
    mesa.add_modificador(factory.create_modificador("pesado", None, None))
    tax = factory.create_modificador("tax-free", None, mesa)
    mesa.add_modificador(tax)
    print(mesa) # (req 1)
    mesa.remove_modificador(tax)
    print(mesa.get_precio_modificado()) # (60000 + 1000) - 30% + 3000 = 42700 + 3000 = 45700 (req 2)
    mochila = Producto("Mochila", 5000)
    tienda.agregar_producto(mochila)
    user.agregar_al_carrito(mochila, tienda)
    tienda.registrar_usuario(user)
    tienda.gestionar_venta(user)
    print(user.get_saldo()) # 5000 - 5000 = 0
    print(user.get_puntos()) # 1 + 500 = 501 (req 3)
    user.add_puntos(-500)
    user.add_puntos(5000)
    user.actualizar_nivel()
    print(user.nivel.__class__.__name__) # NivelPlata (req 5)
    user.cargar_saldo(-100)
    tienda.gestionar_morosidad()
    print(user.nivel.__class__.__name__) # NivelBronce por morosidad (req 4)
    user.cargar_saldo(5099)
    tienda.agregar_producto(mochila)
    user.agregar_al_carrito(mochila, tienda)
    try:
        tienda.gestionar_venta(user)
    except ValueError as e:
        print(e) # Saldo insuficiente para realizar la compra (req 6)
    user.get_carrito().remove(mochila)
    cerveza = ProductoAlcohol("Cerveza", 200)
    tienda.agregar_producto(cerveza)
    user.agregar_al_carrito(cerveza, tienda)
    try:
        tienda.gestionar_venta(user)
    except ValueError as e:
        print(e) # El usuario no tiene la edad suficiente para comprar alcohol (req 7)
    tax_test = factory.create_modificador("tax-free", None, mochila)
    mochila.add_modificador(tax_test)
    tienda.agregar_producto(mochila)
    user.agregar_al_carrito(mochila, tienda)
    user.cargar_saldo(1)
    tienda.gestionar_venta(user)
    print(user.get_saldo()) # 5000 - (5000 - 21%) = 1050 (req 8)




if __name__ == "__main__":
    main()