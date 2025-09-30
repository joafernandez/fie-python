
from peli import Pelicula
from persona import Persona
from strategy_peli import EstrategiaPelicula

class Sala:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.peliculas: list[Pelicula] = []
        self.personas: list[Persona] = []

    def agregar_pelicula(self, pelicula: Pelicula):
        self.peliculas.append(pelicula)

    def agregar_persona(self, persona: Persona):
        self.personas.append(persona)

    def proyectar(self, pelicula: Pelicula, estrategia: EstrategiaPelicula):
        #Proyecta una película, calcula rechazo y se lo aplica a cada persona
        puntos = pelicula.rechazo(estrategia, len(self.personas))
        for persona in self.personas:
            persona.aplicar_rechazo(puntos)

    def mostrar_peliculas(self):
        return sorted(self.peliculas, key=lambda p: p.mostrar_duracion, reverse=True)
