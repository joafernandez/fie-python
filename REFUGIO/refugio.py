# Coordinador del sistema (usa listas y append)
class Refugio:
    def __init__(self):
        self.mascotas = []     # todas las mascotas
        self.adoptantes = []   # todos los adoptantes
        self.adopciones = []   # historial: dicts simples

    # 1) listar mascotas disponibles
    def listar_disponibles(self):
        return [m for m in self.mascotas if m.disponible()]

    # 2) agregar mascota
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    # 3) registrar adoptante
    def registrar_adoptante(self, adoptante):
        self.adoptantes.append(adoptante)

    # 4) registrar adopción
    def registrar_adopcion(self, mascota, adoptante, fecha):
        if not mascota.disponible():
            raise ValueError("La mascota no está disponible.")
        if not adoptante.puede_adoptar(mascota):
            raise ValueError("El adoptante no puede adoptar esta mascota.")

        mascota.adoptada = True
        adoptante.registrar_adopcion(mascota)
        self.adopciones.append({
            "mascota": mascota,
            "adoptante": adoptante,
            "fecha": fecha
        })
