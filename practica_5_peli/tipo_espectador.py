

# ================== tipo_espectador.py ==================
from abc import ABC, abstractmethod


# Estrategia para calcular rechazo según tipo de espectador
class TipoEspectador(ABC):
    @abstractmethod
    def calcular_rechazo(self, rechazo_base):  # Cada tipo modifica diferente
        pass


# Espectador Normal
class EspectadorNormal(TipoEspectador):
    def calcular_rechazo(self, rechazo_base):  # Rechazo sin modificar
        return rechazo_base


# Espectador Cinéfilo
class EspectadorCinefilo(TipoEspectador):
    def calcular_rechazo(self, rechazo_base):  # Siente la mitad
        return rechazo_base / 2


# Espectador Fanático
class EspectadorFanatico(TipoEspectador):
    def calcular_rechazo(self, rechazo_base):  # Solo si supera 30
        if rechazo_base > 30:
            return rechazo_base
        else:
            return 0
