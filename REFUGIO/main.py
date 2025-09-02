from refugio import Refugio
from perro import Perro
from gato import Gato
from ave import Ave
from adoptante_novato import AdoptanteNovato
from adoptante_benefactor import AdoptanteBenefactor
from datetime import date, timedelta


# crear refugio
refugio = Refugio()

# una mascota
perro = Perro(1, "Firulais", date.today() - timedelta(days=40))
refugio.agregar_mascota(perro)

# un adoptante
ana = AdoptanteNovato(100, "Ana")
refugio.registrar_adoptante(ana)

# listar disponibles
print("Disponibles:")
for m in refugio.listar_disponibles():
    print("-", m.apodo)

# saludar
perro.saludar()

# adopción
if ana.puede_adoptar():
    refugio.registrar_adopcion(perro, ana, date.today())

# historial
print("Historial:")
for a in refugio.adopciones:
    print(f"{a['adoptante'].nombre} adoptó a {a['mascota'].apodo}")
