class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.modificadores = []

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.get_precio()} \n - Modificadores: {self.modificadores}"

    def add_modificador(self, modificador):
        self.modificadores.append(modificador)

    def remove_modificador(self, modificador):
        self.modificadores.remove(modificador)

    def get_precio(self):
        return self.precio
    def get_precio_modificado(self):
        total_modificaciones = sum([m.aplicar(None) for m in self.modificadores])
        return self.get_precio() + total_modificaciones

class ProductoMueble(Producto):
    def get_precio(self):
        return self.precio + 1000

class ProductoAlcohol(Producto):
    pass