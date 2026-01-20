# ================== pelicula.py ==================
from abc import ABC, abstractmethod


# Clase abstracta base para películas
class Pelicula(ABC):
    def __init__(self, titulo, duracion_minutos):
        self.titulo = titulo  # Nombre de la película
        self.duracion_minutos = duracion_minutos  # Duración en minutos
    
    @abstractmethod
    def calcular_rechazo_base(self, sala):  # Cada tipo calcula diferente
        pass


# Película Clase Z
class ClaseZ(Pelicula):
    def calcular_rechazo_base(self, sala):  # Siempre 2 puntos
        return 2


# Película de Terror
class Terror(Pelicula):
    def calcular_rechazo_base(self, sala):  # 3 puntos cada 5 minutos
        return (self.duracion_minutos // 5) * 3


# Película Bizarra
class Bizarra(Pelicula):
    def calcular_rechazo_base(self, sala):  # Igual a cantidad de personas
        return sala.contar_personas()


# Película Ultraviolenta (punto 6)
class Ultraviolenta(Terror):  # Hereda de Terror porque es similar
    def calcular_rechazo_base(self, sala):  # Duplica el rechazo de terror
        rechazo_terror = super().calcular_rechazo_base(sala)
        return rechazo_terror * 2
