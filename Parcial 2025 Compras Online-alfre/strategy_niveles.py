
# -*- coding: utf-8 -*-
"""
strategy_niveles.py
-------------------
Estrategias de NIVELES de usuario.
¿Por qué Strategy para niveles?
- Cada nivel (Bronce, Plata, Oro) define su propia política de:
  * máximo de productos en carrito,
  * margen de giro (saldo negativo permitido).
- En lugar de preguntar "if nivel == ..." dentro de Usuario, delegamos en
  un objeto estrategia con la MISMA interfaz. Cambiar de nivel = cambiar de estrategia.
"""

class EstrategiaNivel:
    """Interfaz mínima que comparten Bronce/Plata/Oro."""
    def nombre(self):
        return self.__class__.__name__

    def maximo_producto(self):
        """Cantidad máxima de productos en carrito. None = sin límite."""
        return None

    def saldo_minimo(self):
        """Saldo negativo permitido (margen de giro)."""
        return 0


class Bronce(EstrategiaNivel):
    def maximo_producto(self):
        return 1

    def saldo_minimo(self):
        return 0


class Plata(EstrategiaNivel):
    def maximo_producto(self):
        return 5

    def saldo_minimo(self):
        return -5000


class Oro(EstrategiaNivel):
    def maximo_producto(self):
        return None  # sin límite

    def saldo_minimo(self):
        return -20000
