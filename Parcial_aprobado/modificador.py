class FactoryModificador:
    def create_modificador(self, tipo, desc, producto):
        modificadores = {
            "promocion": ModificadorPromo(desc, producto),
            "pesado": ModificadorPesado(desc, producto),
            "tax-free": ModificadorTaxFree(desc, producto)
        }

        clase_modificador = modificadores.get(tipo)
        if clase_modificador:
            return clase_modificador
        raise ValueError(f"Tipo de modificador '{tipo}' no válido")

class Modificador:
    def __init__(self, descuento, producto):
        self.descuento = descuento # porcentaje, espera un entero
        self.producto = producto

    def __repr__(self):
        return f"Modificador: {self.__class__.__name__}"

class ModificadorPromo(Modificador):
    def aplicar(self, polimorfismo):
        if self.descuento < 0 or self.descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        return -self.producto.get_precio()/100 * self.descuento

class ModificadorPesado(Modificador):
    def aplicar(self, polimorfismo):
            return 3000

class ModificadorTaxFree(Modificador):
    def aplicar(self, usuario):
        if usuario and usuario.is_extranjero():
            return -self.producto.get_precio()*0.21
