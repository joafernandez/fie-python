from datetime import datetime

# función genérica que retorna la cantidad de meses
# completos entre dos fechas d1 y d2
def mesesEntre(d1, d2):
    completo = -1 if d1.day < d2.day else 0
    return (d1.year - d2.year) * 12 + d1.month - d2.month + completo

class Mascota:
    def __init__(self, numero, nombre, fecha):
        self.numero = numero
        self.nombre = nombre
        self.fecha = fecha
        
    def saludar(self):
        pass
    
    def disponible(self):
        pass
    
class Perro(Mascota):
    def __init__(self, numero, nombre, fecha):
        super().__init__(numero, nombre, fecha)
    
    def saludar(self):
        if self.disponible():
            paint('Guau')
            
    def disponible(self):
        hoy = datetime.now()
        meses = mesesEntre(hoy, self.fecha)
        return meses >= 1

class Gato(Mascota):
    def __init__(self, numero, nombre, fecha):
        super().__init__(numero, nombre, fecha)
    
    def saludar(self):
        if self.disponible():
            print('Miau')
            
    def disponible(self):
        hoy = datetime.now()
        meses = mesesEntre(hoy, self.fecha)
        return meses >= 6
    
class Ave(Mascota):
    def __init__(self, numero, nombre, fecha):
        super().__init__(numero, nombre, fecha)
    
    def saludar(self):
        print('Pio')
            
    def disponible(self):
        return True
    
class Adoptante:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def adoptar(self, mascota):
        pass
    
class Novato(Adoptante):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.adoptado = None
        
    def adoptar(self, mascota):
        puede = self.adoptado is None
        if puede:
            self.adoptado = mascota
        return puede
            
class Benefactor(Adoptante):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.perros = []
        self.gatos = []
        self.aves = []
        
    def adoptar(self, mascota):
        puede = False
        if type(mascota) is Perro:
            if len(perros) < 2:
                self.perros.append(mascota)
                puede = True
        elif type(mascota) is Gato:
            if len(gatos) < 3:
                self.gatos.append(mascota)
                puede = True
        elif type(mascota) is Ave:
            if len(aves) < 5:
                self.aves.append(mascota)
                puede = True
        return puede  
    
class Refugio:
    def __init__(self):
        self.lista_mascotas = []
        self.lista_adoptantes = []
    
    def agregarMascota(self, mascota):
        self.lista_mascotas.append(mascota)
        
    def agregarAdoptante(self, adoptante):
        self.lista_adoptantes.append(adoptante)
        
    def adoptarMascota(self, adoptante, mascota):
        exito = adoptante in self.lista_adoptantes and mascota in self.lista_mascotas and mascota.disponible()
        if exito:		# pregunta si exito es verdadero (True)
            exito = adoptante.adoptar(mascota)
        if exito:
            self.lista_mascotas.remove(mascota)
        return exito
            

refugio = Refugio()
juan = Benefactor('Juan')
ana = Novato('Ana')
refugio.agregarAdoptante(juan)
refugio.agregarAdoptante(ana)

print('Adoptantes: ', refugio.lista_adoptantes)

boby = Perro(1, 'Boby', datetime(2025, 6, 21))
michi = Gato(10, 'Michi', datetime(2025, 7, 18))

refugio.agregarMascota(boby)
refugio.agregarMascota(michi)

print('Mascotas: ', refugio.lista_mascotas)

if refugio.adoptarMascota(ana, michi):
    print(f'{ana.nombre} adoptó a {michi.nombre}')
else:
    print(f'{ana.nombre} no pudo adoptar a {michi.nombre}')

if refugio.adoptarMascota(ana, boby):
    print(f'{ana.nombre} adoptó a {boby.nombre}')

print('Mascotas: ', refugio.lista_mascotas)

if refugio.adoptarMascota(juan, boby):
    print(f'{juan.nombre} adoptó a {boby.nombre}')
else:
    print(f'{juan.nombre} no pudo adoptar a {boby.nombre}')


print('OK')
