


# Base de mascotas
class Mascota:
    def __init__(self, id, apodo, fecha_ingreso):
        self.id = id
        self.apodo = apodo
        self.fecha_ingreso = fecha_ingreso
        self.adoptada = False

    def disponible(self):
        pass  # cada subclase define su regla

    def saludar(self):
        pass  # cada subclase imprime su saludo