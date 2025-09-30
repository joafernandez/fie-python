
from sala import Sala
from persona import Persona

class Entrada:
    def __init__(self, persona: Persona, sala: Sala):
        self.persona = persona
        self.sala = sala

    def usar(self):
        #Agrega a la persona a la sala si cumple condiciones (ej: duración < 120, no está apretado)
        if self.conviene():
            self.sala.agregar_persona(self.persona)

    def conviene(self) -> bool:
        # Ejemplo de condiciones (según el enunciado)
        total_duracion = sum(p.mostrar_duracion for p in self.sala.peliculas)
        return total_duracion < 120 and len(self.sala.personas) <= 100
