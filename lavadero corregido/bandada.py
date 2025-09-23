from vehiculo import Vehiculo
from gaviotas import Gaviota
from palomas import Paloma
from otras_aves import OtrasAves

class Bandada:
    """Modela una bandada con formación y lista de aves."""
    FORMACIONES_POSIBLES = ('W', 'V', 'I')

    def __init__(self, formacion: str):
        """Valida la formación inicial (W, V o I)."""
        formacion = formacion.upper()
        if formacion not in Bandada.FORMACIONES_POSIBLES:
            raise ValueError(f"ERROR ==> {formacion} Las formaciones solo pueden ser: {Bandada.FORMACIONES_POSIBLES}")
        self.__formacion: str = formacion
        self.__lista_aves = []

    def agregar_a_lista_aves(self, ave):
        """Agrega un ave a la bandada (no se valida el tipo para respetar el diseño)."""
        self.__lista_aves.append(ave)

    def cambiar_formacion(self, nueva: str):
        """Cambia la formación de la bandada si es válida (W, V o I)."""
        nueva = nueva.upper()
        if nueva not in Bandada.FORMACIONES_POSIBLES:
            raise ValueError(f"Formación inválida: {nueva}")
        self.__formacion = nueva

    def ensuciar(self, Vehiculo: Vehiculo):
        """        Hace pasar la bandada sobre el vehículo y lo ensucia según la formación:

        - V: cada ave ensucia una vez.
        - W: cada ave ensucia dos veces.
        - L: (caso escrito por el alumno; se mantiene aunque no esté en FORMACIONES_POSIBLES)
        """
        if self.__formacion == "V":
            for aux in self.__lista_aves:
                aux.ensuciar(Vehiculo)
        elif self.__formacion == "W":
            for aux in self.__lista_aves:
                aux.ensuciar(Vehiculo)
                aux.ensuciar(Vehiculo)
        elif self.__formacion == "L":  # Se respeta tal cual aparece en el código del alumno
            if len(self.__list_aves) >= 2:  # typo original (se deja como está)
                self.__lista_aves[0].ensuciar(Vehiculo)
                self.__lista_aves[-1].ensuciar(Vehiculo)

    def __str__(self):
        cadena = f"Bandada En {self.__formacion}\n"
        for ave in self.__lista_aves:
            cadena += str(ave) + "\n"
        return cadena
