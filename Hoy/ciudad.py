from vehiculo import Vehiculo
from lava_Arte import Artesanal
from lave_Autom import Automatico


class Ciudad:#Representa una ciudad que administra vehículos y lavaderos

    def __init__(self):
        self.lista_autos = []
        self.lista_lavaderos = []

    def agregar_auto(self, vehiculo: Vehiculo):
        self.lista_autos.append(vehiculo)

    def agregar_lavadero(self, lavadero):
        self.lista_lavaderos.append(lavadero)

    def ensuciar_ceniza(self, miligramos: int): #ensucia con ceniza
        for a in self.lista_autos:
            a.se_ensucia(miligramos)

    #  corregidp
    def precio_lavado(self, lavadero, vehiculo: Vehiculo): # devuelve el precio del lavado según el tipo de lavadero
        try:
            return lavadero.calcular_precio(vehiculo)  # Artesanal
        except TypeError:
            return lavadero.calcular_precio()         # Automático



   #ayuda CORREGIDO
    def lavar_en_mas_barato(self, vehiculo: Vehiculo):
        if not self.lista_lavaderos:
            raise RuntimeError("No hay lavaderos cargados en la ciudad.")

        elegido = self.lista_lavaderos[0]# Inicializamos con el primer lavadero como candidato
        precio_minimo = self.precio_lavado(elegido, vehiculo)

        for lavadero in self.lista_lavaderos: # Recorremos el resto comparando precios
            precio_actual = self.precio_lavado(lavadero, vehiculo)
            if precio_actual < precio_minimo:
                elegido = lavadero
                precio_minimo = precio_actual

        vehiculo.limpiar()
        return elegido, precio_minimo

    def __str__(self):
        return (f"Ciudad con {len(self.lista_autos)} vehículo(s) y "
                f"{len(self.lista_lavaderos)} lavadero(s)")
