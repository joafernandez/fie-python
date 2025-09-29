from bebida import Agua, Gaseosa, Cortado, GranizadoCafeCremoso
from maquina import MaquinaExpendedora

if __name__ == "__main__":
    # Crear bebidas
    agua = Agua()
    gaseosa = Gaseosa()
    cortado = Cortado()
    granizado = GranizadoCafeCremoso()

    # Crear máquina
    maquina = MaquinaExpendedora()
    maquina.agregar_bebida(agua)
    maquina.agregar_bebida(gaseosa)
    maquina.agregar_bebida(cortado)
    maquina.agregar_bebida(granizado)

    # 1. Preparar gaseosa y granizado
    b = maquina.preparar_bebida("Gaseosa")
    precio = maquina.cobrar(b)
    maquina.registrar_cobro(precio)

    b = maquina.preparar_bebida("Granizado de café cremoso")
    precio = maquina.cobrar(b)
    maquina.registrar_cobro(precio)

    # 2. Recaudación total
    print(f"Recaudación total: ${maquina.recaudacion_total()}")

    # 3. Bebida más cara
    mas_cara = maquina.bebida_mas_cara()
    print(f"La bebida más cara es {mas_cara.nombre} (${mas_cara.calcular_precio()})")
