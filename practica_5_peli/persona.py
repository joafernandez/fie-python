
# ================== persona.py ==================
from tipo_espectador import EspectadorNormal


class Persona:
    def __init__(self, nombre, tolerancia):
        self.nombre = nombre  # Nombre de la persona
        self.tolerancia = tolerancia  # Nivel de tolerancia en puntos
        self.tipo_espectador = EspectadorNormal()  # Por defecto es normal
        self.sala_actual = None  # En qué sala está
    
    def cambiar_tipo_espectador(self, nuevo_tipo):  # Cambia su tipo
        self.tipo_espectador = nuevo_tipo
    
    def le_conviene_sala(self, sala):  # Verifica si le conviene comprar
        duracion_total = sala.calcular_duracion_total()
        esta_apretado = sala.contar_personas() > 100
        return duracion_total < 120 and not esta_apretado
    
    def comprar_entrada(self, sala):  # Compra si le conviene
        if self.le_conviene_sala(sala):
            sala.agregar_persona(self)
            self.sala_actual = sala
    
    def ver_pelicula(self, pelicula, sala):  # Disminuye tolerancia
        rechazo_base = pelicula.calcular_rechazo_base(sala)
        rechazo_sentido = self.tipo_espectador.calcular_rechazo(rechazo_base)
        self.tolerancia -= rechazo_sentido
    
    def debe_retirarse(self):  # Si tolerancia llegó a cero o menos
        return self.tolerancia <= 0
