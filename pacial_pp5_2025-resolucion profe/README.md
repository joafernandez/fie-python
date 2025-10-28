# E-Commerce (Modelo OO en Python)

Este módulo modela un e-commerce con Productos (y subtipos), Usuarios y una Tienda Virtual.

## Estructura
- `ecommerce/products.py`: `Producto`, `Mueble`, `Indumentaria`, `BebidaAlcoholica` y helper `crear_mueble_vidrio_fuera_de_temporada`.
- `ecommerce/users.py`: `Usuario`, Niveles (`Bronce`, `Plata`, `Oro`) y lógica de compra.
- `ecommerce/store.py`: `TiendaVirtual` con utilidades de administración.
- `main.py`: ejemplos y verificaciones de los escenarios solicitados.

## Reglas destacadas
- IVA 21% sobre el precio base.
- `Mueble` suma $1000 al precio final.
- `Pesado` suma $1000 al envío y `Frágil` $500 al envío.
- `Ganga` fuerza precio final 0 (independiente del precio base o recargos por tipo), pero el envío se cobra según corresponda.
- Bebidas alcohólicas solo pueden agregarse al carrito de usuarios mayores de 18.
- Compra:
  - descuenta dinero; suma puntos = 10% del valor pagado; vacía carrito; actualiza nivel.
- Niveles por puntos: `Bronce` (1 ítem), `Plata` (5.000 pts, hasta 5 ítems), `Oro` (15.000 pts, sin límite).

## Ejecutar ejemplos
```
python3 main.py
```
