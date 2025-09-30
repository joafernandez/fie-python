
from sala import Sala
from entrada import Entrada
from persona import Persona
from strategy_persona import Normal, Cinefilo, Fanatico
from peli import Pelicula
from strategy_peli import Z, Terror

def main():
    # Crear sala y película
    sala1 = Sala("Sala A")
    peli1 = Pelicula(18.00, 90)   # 90 min

    # Agregar película a la sala
    sala1.agregar_pelicula(peli1)

    # Crear personas con diferentes estados
    persona1 = Persona(100, Normal())
    persona2 = Persona(100, Cinefilo())
    persona3 = Persona(100, Fanatico())

    # Cada persona compra entrada
    Entrada(persona1, sala1).usar()
    Entrada(persona2, sala1).usar()
    Entrada(persona3, sala1).usar()

    # Proyectar la película de Terror
    sala1.proyectar(peli1, Terror())

    # Mostrar tolerancia final de las personas
    for p in sala1.personas:
        print(f"{p.estrategia.__class__.__name__} → tolerancia: {p.mostrar_nivel_tolerancia}")

if __name__ == "__main__":
    main()
