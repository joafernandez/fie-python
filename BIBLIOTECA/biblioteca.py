from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = set()
        self.socios = set()
        def total_existencias(self):
        return len(self.libros)

    def agregar_libro(self, libro: Libro):
        self.libros.add(libro)

    def eliminar_libro(self, libro: Libro):
        self.libros.remove(libro)

    def prestar_libro(self, socio: Socio,libro:libro):
        if libro not in self.librosDispnibles:
            print ("la biblio no tiene ejemplar")
            return
        if socio not in self.socios:
            print ("el socio no esta asociado")
            return
        prestamo= prestamo(socio, libro)
        self.prestamos.append(prestamo)
        socio.retirar (prestamo)
        self.librosDisponibles.remove(libro)
        
        
    def recibirLibro (self, libro:Libro)
    
        
        
    def total_prestamos(self):
        pass

    def agregar_socio(self, socio):
        self.socios.add(socio)

    def eliminar_socio(self, socio):
        self.socios.remove(socio)

    def total_socios(self):
        return len(self.socios)