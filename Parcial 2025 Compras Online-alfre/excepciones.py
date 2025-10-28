
# -*- coding: utf-8 -*-
"""
excepciones.py
--------------
Excepciones de dominio para el e-commerce.
Se diseñan con soporte para mensajes claros y un mecanismo simple para
"componer" detalles adicionales cuando se requiera.
"""

class ErrorECommerce(Exception):
    """
    Excepción base del dominio.
    - mensaje_base: texto principal explicando el problema.
    - detalle: texto opcional para concatenar contexto adicional.
    """
    def __init__(self, mensaje_base, detalle=None):
        mensaje = str(mensaje_base)
        if detalle:
            # Si el llamador aporta un detalle, lo concatenamos de forma segura.
            mensaje = f"{mensaje_base} | Detalle: {detalle}"
        super().__init__(mensaje)


class ErrorEdadNoPermitida(ErrorECommerce):
    """Se lanza si el usuario no cumple con la edad mínima requerida para un producto."""
    pass


class ErrorCarritoLleno(ErrorECommerce):
    """Se lanza cuando el usuario intenta superar el máximo de productos permitido por su nivel."""
    pass


class ErrorFondosInsuficientes(ErrorECommerce):
    """Se lanza cuando el saldo (considerando el margen negativo del nivel) no alcanza para comprar."""
    pass
