

# ================== sala.py ==================


class Sala:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la sala
        self.peliculas = []  # Lista de películas que proyecta
        self.personas = []  # Lista de personas en la sala
    
    def agregar_pelicula(self, pelicula):  # Agrega película al catálogo
        self.peliculas.append(pelicula)
    
    def agregar_persona(self, persona):  # Agrega persona a la sala
        self.personas.append(persona)
    
    def contar_personas(self):  # Cantidad de personas en la sala
        return len(self.personas)
    
    def calcular_duracion_total(self):  # Suma duración de todas las películas
        duracion_total = 0
        for pelicula in self.peliculas:
            duracion_total += pelicula.duracion_minutos
        return duracion_total
    
    def proyectar_pelicula(self, pelicula):  # Proyecta y afecta a las personas
        personas_que_quedan = []  # Lista para personas que no se retiran
        for persona in self.personas:
            persona.ver_pelicula(pelicula, self)
            if not persona.debe_retirarse():  # Si no se retira
                personas_que_quedan.append(persona)
        self.personas = personas_que_quedan  # Actualiza lista sin retirados
    
    def obtener_peliculas_ordenadas(self):  # Ordena por duración (mayor a menor)
        peliculas_ordenadas = self.peliculas[:]  # Copia la lista
        # Ordenamiento burbuja (manual)
        for i in range(len(peliculas_ordenadas)):
            for j in range(len(peliculas_ordenadas) - 1 - i):
                if peliculas_ordenadas[j].duracion_minutos < peliculas_ordenadas[j + 1].duracion_minutos:
                    # Intercambia
                    aux = peliculas_ordenadas[j]
                    peliculas_ordenadas[j] = peliculas_ordenadas[j + 1]
                    peliculas_ordenadas[j + 1] = aux
        return peliculas_ordenadas
    
    def es_sangrienta(self):  # Si alguna película produce rechazo >= 50 en todos
        for pelicula in self.peliculas:
            rechazo = pelicula.calcular_rechazo_base(self)
            if rechazo >= 50:
                return True
        return False

