


# ================== complejo.py ==================


class Complejo:
    def __init__(self):
        self.salas = []  # Lista de salas del complejo
    
    def agregar_sala(self, sala):  # Agrega sala al complejo
        self.salas.append(sala)
    
    def calcular_tolerancia_promedio(self):  # Promedio de tolerancia de todos
        total_tolerancia = 0
        total_personas = 0
        for sala in self.salas:
            for persona in sala.personas:
                total_tolerancia += persona.tolerancia
                total_personas += 1
        
        if total_personas == 0:  # Evita división por cero
            return 0
        return total_tolerancia / total_personas
    
    def obtener_salas_sangrientas(self):  # Salas que tienen película con rechazo >= 50
        salas_sangrientas = []
        for sala in self.salas:
            if sala.es_sangrienta():
                salas_sangrientas.append(sala)
        return salas_sangrientas
