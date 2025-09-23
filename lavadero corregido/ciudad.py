from vehiculo import Vehiculo
from lava_Arte import Artesanal
from lave_Autom import Automatico


class Ciudad:
    """Representa una ciudad que administra vehículos y lavaderos."""

    def __init__(self):
        """Inicializa colecciones vacías de vehículos y lavaderos."""
        self.lista_autos = []
        self.lista_lavaderos = []

    def agregar_auto(self, vehiculo: Vehiculo):
        """Agrega un vehículo a la ciudad."""
        self.lista_autos.append(vehiculo)

    def agregar_lavadero(self, lavadero):
        """Agrega un lavadero (Artesanal o Automático) a la ciudad."""
        self.lista_lavaderos.append(lavadero)

    def ensuciar_ceniza(self, miligramos: int):
        """        Ensucia todos los vehículos de la ciudad por efecto de ceniza volcánica.

        Parámetros:
            miligramos (int): cantidad de suciedad a agregar por vehículo.
        """
        for a in self.lista_autos:
            a.se_ensucia(miligramos)

    # === Helpers para (f) ===
    def precio_lavado(self, lavadero, vehiculo: Vehiculo):
        """        Devuelve el precio del lavado según el tipo de lavadero.
        Soporta:
            - Artesanal.calcular_precio(vehiculo)
            - Automatico.calcular_precio()
        """
        try:
            return lavadero.calcular_precio(vehiculo)  # Artesanal
        except TypeError:
            return lavadero.calcular_precio()         # Automático

    def lavar_en_mas_barato(self, vehiculo: Vehiculo):
        """
        Selecciona el lavadero más barato para el vehículo, limpia el vehículo
        y retorna (lavadero_elegido, precio).
        """
        if not self.lista_lavaderos:
            raise RuntimeError("No hay lavaderos cargados en la ciudad.")

        # Inicializamos con el primer lavadero como candidato
        elegido = self.lista_lavaderos[0]
        precio_minimo = self.precio_lavado(elegido, vehiculo)

        # Recorremos el resto comparando precios
        for lavadero in self.lista_lavaderos:
            precio_actual = self.precio_lavado(lavadero, vehiculo)
            if precio_actual < precio_minimo:
                elegido = lavadero
                precio_minimo = precio_actual

        vehiculo.limpiar()
        return elegido, precio_minimo

    def __str__(self):
        return (f"Ciudad con {len(self.lista_autos)} vehículo(s) y "
                f"{len(self.lista_lavaderos)} lavadero(s)")
