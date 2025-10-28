# --- main.py ---

from tienda import Tienda
from usuario import Usuario
from producto import Mueble, Bebida

# Crear tienda
tienda = Tienda()

# Crear usuarios
juan = Usuario("Juan", 17, 200, 0, extranjero=False)
celia = Usuario("Celia", 25, 1000, 200, extranjero=True)

# Agregar usuarios a la tienda
tienda.agregar(juan)
tienda.agregar(celia)

# Crear productos
sofa = Mueble("Sofá", 500, 100)
cerveza = Bebida("Cerveza", 100, 10)

# Agregar productos a la tienda
tienda.agregar_producto(sofa)
tienda.agregar_producto(cerveza)

# Usuarios agregan productos a su carrito
juan.agregar_producto(sofa)
juan.agregar_producto(cerveza)   # debería bloquearse por ser menor

celia.agregar_producto(cerveza)  # puede comprar

# Vender productos (control de edad en bebidas)
tienda.vende(juan)
tienda.vende(celia)

# Aplicar descuento si tienen saldo negativo
tienda.descuento(juan)
tienda.descuento(celia)

# Mostrar resultados finales
print("\n📋 Estado final:")
print("Juan - saldo:", juan.saldo, "| puntos:", juan.acumulacion_puntos, "| carrito:", [p.nombre for p in juan.carrito_productos])
print("Celia - saldo:", celia.saldo, "| puntos:", celia.acumulacion_puntos, "| carrito:", [p.nombre for p in celia.carrito_productos])
print("Stock disponible en tienda:", [p.nombre for p in tienda.lista_productos_disponibles])