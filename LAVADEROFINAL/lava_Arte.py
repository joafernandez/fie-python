class Artesanal:

    COSTO_UNITARIO = 10

    def __init__(self, empleados: int):
        self.empleados = empleados

    def calcular_precio(self, vehiculo):
        tiempo = vehiculo.suciedad / 5
        return self.empleados * tiempo * Artesanal.COSTO_UNITARIO

    def __str__(self):
        return f"SmallLav (Artesanal, empleados={self.empleados}, costo_unit={Artesanal.COSTO_UNITARIO})"
