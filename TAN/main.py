from tanque import Tanque
from strategy_proyectil import ProyectilAP, ProyectilHE, ProyectilAPDS


if __name__ == "__main__":


    m4 = Tanque("M4 Sherman", blindaje=51, vida=400)
    m4.agregar_proyectil(ProyectilAP(92, 110))
    m4.agregar_proyectil(ProyectilHE(38, 250))

    panther = Tanque("PzV Panther", blindaje=85, vida=500)
    panther.agregar_proyectil(ProyectilAP(135, 175))
    panther.agregar_proyectil(ProyectilHE(53, 350))

    tiger = Tanque("PzVI Tiger", blindaje=100, vida=1100)
    tiger.agregar_proyectil(ProyectilAPDS(200, 400))


    print("\n--- COMBATE ---")
    m4.disparar(panther)
    panther.disparar(m4)
    tiger.disparar(m4)

    print("\n--- Estado final ---")
    print(m4.nombre, "vida:", m4.vida)
    print(panther.nombre, "vida:", panther.vida)
    print(tiger.nombre, "vida:", tiger.vida)
