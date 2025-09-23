class Automatico:
    """    Lavadero automático con precio fijo por un tiempo fijo.
    No depende del nivel de suciedad (diseño del alumno).
    """

    PRECIO_FIJO = 100
    TIEMPO_FIJO = 10

    def calcular_precio(self):
        """Retorna el precio fijo multiplicado por el tiempo fijo."""
        return Automatico.PRECIO_FIJO * Automatico.TIEMPO_FIJO

    def __str__(self):
        return f"AutoWash (Automático, precio={Automatico.PRECIO_FIJO}, tiempo={Automatico.TIEMPO_FIJO})"
