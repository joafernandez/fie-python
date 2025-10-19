from usuario import *
import pytest
class MockProducto:
    def __init__(self, precio):
        self.precio = precio
        self.modificadores = []

    def get_precio(self):
        return self.precio

class MockTiendaVirtual:
    def __init__(self):
        self.productos_disponibles = []

    def get_productos_disponibles(self):
        return self.productos_disponibles
class TestUsuario:
    def test_levelup(self):
        user = Usuario("Ana", 30, 10000, 4900, NivelBronce(), False)
        assert user.nivel.__class__.__name__ == "NivelBronce"
        test = MockProducto(1000)
        tienda = MockTiendaVirtual()
        tienda.productos_disponibles.append(test)
        user.agregar_al_carrito(test, tienda)
        user.comprar()
        assert user.nivel.__class__.__name__ == "NivelPlata"

    def test_too_many_in_cart(self):
        user = Usuario("Ana", 30, 10000, 0, NivelBronce(), False)
        test1 = MockProducto(1000)
        test2 = MockProducto(2000)
        tienda = MockTiendaVirtual()
        tienda.productos_disponibles.extend([test1, test2])
        user.agregar_al_carrito(test1, tienda)
        with pytest.raises(ValueError) as error:
            user.agregar_al_carrito(test2, tienda)
        assert str(error.value) == "No se puede agregar más productos al carrito con el nivel actual"