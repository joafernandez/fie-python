
# -*- coding: utf-8 -*-
"""
strategy.py
-----------
Estrategias de "modificadores" de productos.
¿Por qué Strategy acá?
- Cada modificador (Promoción, Pesado, TaxFree) es una POLÍTICA independiente que puede cambiar
  y combinarse. En lugar de escribir muchos if/elif dentro de Producto, desacoplamos cada regla
  en un objeto con la misma interfaz. Así:
    * Respetamos Open/Closed (agregar nuevos modificadores sin tocar Producto).
    * Probamos cada política en aislamiento (tests más simples).
    * Componemos dinámicamente varias políticas (p.ej. Pesado + Promoción + TaxFree).
"""

class Estrategia_Modificador:
    """
    Interfaz mínima:
    - aplicar_precio(precio_actual, producto, usuario) -> float: altera el precio de venta.
    - costo_envio_extra() -> float: suma al costo de envío.
    - descripcion() -> str: nombre "humano" para construir etiquetas.
    """
    def aplicar_precio(self, precio_actual, producto, usuario):
        # Por defecto no cambia el precio
        return precio_actual

    def costo_envio_extra(self):
        # Por defecto no agrega costo de envío
        return 0.0

    def descripcion(self):
        return self.__class__.__name__


class Pesado(Estrategia_Modificador):
    """
    Producto difícil de manipular.
    Regla: suma ARS 3000 al costo de envío.
    """
    def costo_envio_extra(self):
        return 3000.0

    def descripcion(self):
        return "Pesado(+envío $3000)"


class Promocion(Estrategia_Modificador):
    """
    Descuento porcentual sobre el PRECIO DE VENTA ya compuesto (base + IVA + recargos por tipo).
    'porcentaje' va de 0.0 a 1.0 (ej: 0.30 = 30%).
    """
    def __init__(self, porcentaje):
        if porcentaje < 0 or porcentaje > 1:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 1.")
        self.porcentaje = porcentaje

    def aplicar_precio(self, precio_actual, producto, usuario):
        descuento = precio_actual * self.porcentaje
        return precio_actual - descuento

    def descripcion(self):
        return f"Promoción(-{int(self.porcentaje*100)}%)"


class TaxFree(Estrategia_Modificador):
    """
    No altera el precio por sí sola, pero su mera presencia habilita
    la eliminación del IVA si y solo si el USUARIO es EXTRANJERO.
    La lógica de IVA vive en Producto (un único lugar), esta estrategia
    solo sirve como "bandera" y para documentación en la etiqueta.
    """
    def descripcion(self):
        return "TaxFree(solo extranjero)"
