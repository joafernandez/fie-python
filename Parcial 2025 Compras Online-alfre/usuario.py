
"""
usuario.py
----------
Usuario comprador con:
- saldo, puntos, extranjero
- nivel (Strategy de nivel): Bronce/Plata/Oro
- carrito de productos
Reglas clave: tope de ítems por nivel, margen de giro, puntos=10% del total pagado, actualización de nivel.
"""

from strategy_niveles import Bronce, Plata, Oro
from excepciones import ErrorCarritoLleno, ErrorFondosInsuficientes

class Usuario:
    def __init__(self, nombre, edad, extranjero=False):
        self.nombre = nombre
        self.edad = int(edad)
        self.extranjero = bool(extranjero)

        self.saldo = 0.0
        self.puntos = 0
        # Estrategia de nivel activa (Strategy)
        self.nivel = Bronce()
        # Carrito simple en memoria
        self.carrito = []

    # ---------------- utilidades de nivel ----------------

    def _max_items(self):
        return self.nivel.maximo_producto()

    def _saldo_minimo(self):
        return self.nivel.saldo_minimo()

    def actualizar_nivel(self):
        """
        Política de ascenso/descenso:
        - Oro: puntos >= 15000
        - Plata: 5000 <= puntos < 15000
        - Bronce: puntos < 5000
        Cambiar de nivel = cambiar de ESTRATEGIA (Strategy).
        """
        if self.puntos >= 15000:
            self.nivel = Oro()
        elif self.puntos >= 5000:
            self.nivel = Plata()
        else:
            self.nivel = Bronce()

    # ---------------- API pública ----------------

    def cargar_saldo(self, monto):
        if monto < 0:
            raise ValueError("El monto a cargar debe ser positivo.")
        self.saldo += float(monto)

    def agregar_al_carrito(self, producto):
        # 1) Restricción por nivel (Strategy de nivel)
        limite = self._max_items()
        if limite is not None and len(self.carrito) >= limite:
            raise ErrorCarritoLleno(
                f"Carrito lleno para nivel {self.nivel.nombre()}. Máximo permitido: {limite}.",
                detalle=f"Intentando agregar '{getattr(producto,'nombre','?')}'"
            )
        # 2) Requisitos propios del producto (edad, etc.)
        producto.validar_requisitos(self)
        # 3) Agregar
        self.carrito.append(producto)

    # ---- totales ----

    def total_precios(self):
        total = 0.0
        for p in self.carrito:
            total += p.precio_venta(self)
        return round(total, 2)

    def total_envio(self):
        total = 0.0
        for p in self.carrito:
            total += p.costo_envio()
        return round(total, 2)

    def total_a_pagar(self):
        return self.total_precios() + self.total_envio()

    def comprar(self, tienda):
        """
        Compra TODOS los productos del carrito.
        Pasos:
        - calcular total (precios + envíos)
        - verificar saldo con margen de giro del nivel
        - debitar
        - sumar puntos = 10% del total pagado (int)
        - vaciar carrito
        - actualizar nivel (Strategy de nivel se reemplaza si corresponde)
        Retorna: monto pagado
        """
        total = self.total_a_pagar()

        if self.saldo + (-self._saldo_minimo()) < total and self._saldo_minimo() < 0:
            # Esta forma es menos clara; preferimos comparar directo:
            pass

        # Verificación directa del margen: saldo final no puede ser < saldo_minimo()
        saldo_final = self.saldo - total
        if saldo_final < self._saldo_minimo():
            raise ErrorFondosInsuficientes(
                "Fondos insuficientes para concretar la compra.",
                detalle=f"Total=${total:.2f}, saldo=${self.saldo:.2f}, margen={self._saldo_minimo():.2f}"
            )

        # Debitar
        self.saldo = saldo_final

        # Puntos: 10% del valor pagado
        puntos = int(total * 0.10)
        self.puntos += puntos

        # Vaciar carrito
        self.carrito = []

        # Actualizar nivel
        self.actualizar_nivel()

        return total

    def __str__(self):
        return (f"Usuario({self.nombre}, edad={self.edad}, nivel={self.nivel.nombre()}, "
                f"saldo=${self.saldo:,.2f}, puntos={self.puntos}, extranjero={self.extranjero})")
