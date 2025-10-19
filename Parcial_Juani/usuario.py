class NivelOro:
    saldo_negativo = 20000
    puntos_next = None
    next = None
    prev = None
    def check_carrito(self, carrito):
        return True

class NivelPlata:
    saldo_negativo = 5000
    puntos_next = 20000
    next = NivelOro()
    prev = None
    def check_carrito(self, carrito):
        if len(carrito) > 5:
            return False
        return True
NivelOro.prev = NivelPlata()
class NivelBronce:
    saldo_negativo = 0
    puntos_next = 5000
    next = NivelPlata()
    prev = None
    def check_carrito(self, carrito):
        if len(carrito) > 1:
            return False
        return True
NivelPlata.prev = NivelBronce()
class Usuario:
    def __init__(self, nombre, edad, saldo, puntos, nivel, extranjero):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.puntos = puntos
        self.nivel = nivel
        self.extranjero = extranjero
        self.carrito = []

    def agregar_al_carrito(self, producto, tienda_virtual):
        if self.nivel.check_carrito(self.carrito + [producto]):
            if producto in tienda_virtual.get_productos_disponibles():
                self.carrito.append(producto)
                tienda_virtual.productos_disponibles.remove(producto)
            else:
                raise ValueError("El producto no está disponible en la tienda")
        else:
            raise ValueError("No se puede agregar más productos al carrito con el nivel actual")

    def cargar_saldo(self, monto):
        if monto < 0 and abs(monto) > self.saldo + self.nivel.saldo_negativo:
            raise ValueError("No se puede retirar más dinero del permitido por el nivel")
        self.saldo += monto

    def comprar(self):
        total = sum([p.get_precio() + sum([m.aplicar(self) for m in p.modificadores]) for p in self.carrito])
        if self.saldo - total < -self.nivel.saldo_negativo:
            raise ValueError("Saldo insuficiente para realizar la compra")
        self.saldo -= total
        self.puntos += int(total // 10)
        self.actualizar_nivel()
        self.carrito = []

    def actualizar_nivel(self):
        while self.nivel.next and self.puntos >= self.nivel.puntos_next:
            self.nivel = self.nivel.next
        while self.nivel.prev and self.puntos < self.nivel.prev.puntos_next:
            self.nivel = self.nivel.prev

    def get_carrito(self):
        return self.carrito

    def get_edad(self):
        return self.edad

    def get_saldo(self):
        return self.saldo

    def add_puntos(self, puntos):
        self.puntos += puntos

    def get_puntos(self):
        return self.puntos

    def is_extranjero(self):
        return self.extranjero