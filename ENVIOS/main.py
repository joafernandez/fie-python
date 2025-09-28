from ubicacion import Ubicacion
from envios import Envio
from strategy_recarga import Categoria, Sobrepeso, Arbitrario
from strategy_impuesto import Iva, Multicategoria, Aduanero, Extrano
from administracion import Administracion

def main():               #MAIN DE PRUEBA/// FUNCIONA:) HACER OTRO !!!!!!!!!
    # Ubicaciones
    origen1 = Ubicacion("Buenos Aires", "Argentina")
    destino1 = Ubicacion("Utrecht", "Paises Bajos")

    origen2 = Ubicacion("Buenos Aires", "Argentina")
    destino2 = Ubicacion("Tucuman", "Argentina")

    # Envíos según la consigna
    envio1 = Envio(5, 1000, ["musica", "arte"], origen1, destino1)
    envio2 = Envio(2, 220, ["musica", "arte", "tecnologia"], origen2, destino2)

    # Estrategias de recargo e impuesto
    recargos = [Categoria(), Sobrepeso(), Arbitrario()]
    impuestos = [Iva(), Multicategoria(), Aduanero(), Extrano()]

    # Administracion
    admin = Administracion()
    admin.agregar_envios_lista(envio1)
    admin.agregar_envios_lista(envio2)

    # Probar precios
    print("=== ENVÍO 1 ===")
    print("Neto:", envio1.precio_neto(Categoria()))  # ejemplo con una estrategia
    print("Bruto:", envio1.precio_bruto(Iva(), Categoria()))

    print("=== ENVÍO 2 ===")
    print("Neto:", envio2.precio_neto(Categoria()))
    print("Bruto:", envio2.precio_bruto(Iva(), Categoria()))

    internacionales = admin.envios_internacionales()
    print("=== ENVÍOS INTERNACIONALES ===")
    for envio in internacionales:
        print(envio)   # esto va a usar __str__ de Envio

if __name__ == "__main__":
    main()