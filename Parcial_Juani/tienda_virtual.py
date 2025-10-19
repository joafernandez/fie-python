from producto import *
class TiendaVirtual:
    def __init__(self):
        self.productos_disponibles = []
        self.usuarios = []

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def registrar_usuario(self, usuario):
        if usuario in self.usuarios:
            raise ValueError("El usuario ya existe.")
        self.usuarios.append(usuario)

    def gestionar_venta(self, usuario):
        if usuario not in self.usuarios:
            raise ValueError("Usuario no registrado.")
        for producto in usuario.get_carrito():
            if isinstance(producto, ProductoAlcohol) and usuario.get_edad() < 18:
                usuario.get_carrito().remove(producto)
                self.productos_disponibles.append(producto)
                raise ValueError("El usuario no tiene la edad suficiente para comprar alcohol.")
        usuario.comprar()

    def gestionar_morosidad(self):
        for usuario in self.usuarios:
            if usuario.get_saldo() < 0:
                usuario.add_puntos(-100)
                usuario.actualizar_nivel()

    def get_productos_disponibles(self):
        return self.productos_disponibles