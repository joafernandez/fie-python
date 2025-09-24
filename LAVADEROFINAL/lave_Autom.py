

class Automatico:

    PRECIO_FIJO = 100
    TIEMPO_FIJO = 10

    def calcular_precio(self):
        return Automatico.PRECIO_FIJO * Automatico.TIEMPO_FIJO

    def __str__(self):
        return f"AutoWash (Automático, precio={Automatico.PRECIO_FIJO}, tiempo={Automatico.TIEMPO_FIJO})"
