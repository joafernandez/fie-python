
from abc import ABC, abstractmethod



class EstrategiaProyectil(ABC):  # SOLO INTERFAZ!
    
    @abstractmethod
    def disparar(self, tanque,otro_tanque):  # le paso las 2 instancias de los tanques
        pass


class ProyectilAP(EstrategiaProyectil):         #-----------------------------------------------------
    def __init__(self, penetracion, dano):
        self.penetracion = penetracion
        self.dano = dano

    def disparar(self, tanque,otro_tanque):
        if self.penetracion >= otro_tanque.blindaje:
            otro_tanque.recibir_dano(self.dano)


class ProyectilHE(EstrategiaProyectil):
    def __init__(self, penetracion, dano):
        self.penetracion = penetracion
        self.dano = dano

    def disparar(self, tanque,otro_tanque):
        if self.penetracion >= otro_tanque.blindaje:
            otro_tanque.recibir_dano(self.dano)


class ProyectilAPDS(EstrategiaProyectil):
    def __init__(self, penetracion, dano):
        self.penetracion = penetracion
        self.dano = dano

    def disparar(self, tanque,otro_tanque):
        if self.penetracion >= otro_tanque.blindaje:
          otro_tanque.recibir_dano(self.dano)
