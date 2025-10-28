
# -*- coding: utf-8 -*-
"""
producto.py
-----------
Modelo de productos. Implementa el "esqueleto" de cálculo de precio y envío, y
permite componer modificadores (estrategias) para cambiar el comportamiento
sin ensuciar la clase con condicionales.
"""

from strategy import Estrategia_Modificador, Pesado, Promocion, TaxFree

class Producto:
    """
    Clase base de productos.
    Reglas:
    - IVA: 21% del precio_base, salvo que el producto tenga el modificador TaxFree
      y el usuario sea extranjero.
    - Recargo por tipo: las subclases pueden sumar un importe fijo al precio de venta
      (p.ej. Mueble: +$1000).
    - Modificadores (Strategy): se aplican EN CADENA sobre el precio de venta ya armado.
    - Envío: es la suma de 'costo_envio_extra()' de cada modificador.
    """
    def __init__(self, nombre, precio_base, modificadores=None):
        self.nombre = nombre
        self.precio_base = float(precio_base)
        self.modificadores = list(modificadores) if modificadores else []

    # ---------- hooks de subclases ----------

    def recargo_por_tipo(self):
        """Recargo fijo propio del tipo (por defecto, 0)."""
        return 0.0

    def validar_requisitos(self, usuario):
        """
        Cada tipo de producto puede imponer requisitos al usuario (p.ej., edad).
        Por defecto, no hay requisitos.
        """
        return

    # ---------- utilidades internas ----------

    def _tiene_taxfree(self):
        return any(isinstance(m, TaxFree) for m in self.modificadores)

    def _iva_aplicable(self, usuario):
        """
        IVA = 21% del PRECIO BASE, salvo que:
        - el producto tenga TaxFree Y
        - el usuario sea extranjero
        """
        if self._tiene_taxfree() and getattr(usuario, "extranjero", False):
            return 0.0
        return self.precio_base * 0.21

    # ---------- API de precio/envío/etiqueta ----------

    def costo_envio(self):
        """Suma de costos de envío que aportan los modificadores (Strategy)."""
        total = 0.0
        for mod in self.modificadores:
            total += mod.costo_envio_extra()
        return total

    def precio_venta(self, usuario):
        """
        Precio de venta final (SIN envío):
        1) precio_base
        2) + IVA (si corresponde)
        3) + recargo por tipo (ej. Mueble)
        4) aplicar modificadores (Promoción, etc) sobre el resultado
        """
        precio = self.precio_base
        precio += self._iva_aplicable(usuario)
        precio += self.recargo_por_tipo()
        # Aplicamos todas las estrategias de precio
        for mod in self.modificadores:
            precio = mod.aplicar_precio(precio, self, usuario)
        # Redondeamos a 2 decimales por presentación
        return round(precio, 2)

    def etiqueta(self, usuario):
        """
        Etiqueta legible para mostrar en pantalla o imprimir tickets.
        Explicita el uso de Strategy listando los modificadores.
        """
        tipo = self.__class__.__name__
        mods = ", ".join(m.descripcion() for m in self.modificadores) if self.modificadores else "Sin modificadores"
        return (f"[{tipo}] {self.nombre} | {mods} | "
                f"Precio: ${self.precio_venta(usuario):,.2f} | "
                f"Envío: ${self.costo_envio():,.2f}")


class Mueble(Producto):
    """Mueble: recargo fijo de $1000 en el precio de venta por logística."""
    def recargo_por_tipo(self):
        return 1000.0


class Indumentaria(Producto):
    """Indumentaria: sin recargo extra propio."""
    pass


class BebidaAlcoholica(Producto):
    """Bebida alcohólica: valida edad >= 18 al agregarse al carrito."""
    def validar_requisitos(self, usuario):
        # La validación de edad se hace aquí (regla del producto),
        # además la Tienda hace una verificación defensiva al vender.
        if getattr(usuario, "edad", 0) < 18:
            from excepciones import ErrorEdadNoPermitida
            raise ErrorEdadNoPermitida(
                "El usuario es menor de 18 años: no puede comprar bebidas alcohólicas.",
                detalle=f"Usuario '{getattr(usuario, 'nombre', '?')}', edad={getattr(usuario,'edad','?')}"
            )
