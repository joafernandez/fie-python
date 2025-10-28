
# -*- coding: utf-8 -*-
"""
tienda_virtual.py
-----------------
Coordina usuarios y stock. Aplica reglas de negocio que no pertenecen
ni a Producto ni a Usuario (orquestación de casos de uso).
"""

from producto import BebidaAlcoholica

class Tienda:
    def __init__(self):
        self.usuarios = []
        self.stock = []  # productos disponibles

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_a_stock(self, producto):
        self.stock.append(producto)

    def devolver_a_stock(self, producto):
        self.stock.append(producto)

    # --- reglas de orquestación ---

    def _retirar_bebidas_a_menores(self, usuario):
        """Seguridad extra: si el usuario es menor, quitamos las bebidas del carrito y las devolvemos a stock."""
        if usuario.edad >= 18:
            return
        restantes = []
        for p in usuario.carrito:
            if isinstance(p, BebidaAlcoholica):
                self.devolver_a_stock(p)
            else:
                restantes.append(p)
        usuario.carrito = restantes

    def gestionar_venta(self, usuario):
        """
        - Retira bebidas a menores (si las hubiera, defensivo).
        - Ejecuta la compra a través del usuario.
        - Devuelve el total pagado.
        """
        self._retirar_bebidas_a_menores(usuario)
        return usuario.comprar(self)

    def gestionar_morosidad(self):
        """
        - A los usuarios con saldo negativo, restar 100 puntos.
        - Actualizar nivel después de penalizar.
        """
        for u in self.usuarios:
            if u.saldo < 0:
                u.puntos = max(0, u.puntos - 100)
                u.actualizar_nivel()
