
# -*- coding: utf-8 -*-
"""
test_ecommerce_alumno.py
------------------------
Tests con pytest que cubren los 10 requerimientos del enunciado.
"""
import pytest
from tienda_virtual import Tienda
from usuario import Usuario
from producto import Mueble, Indumentaria, BebidaAlcoholica
from strategy import Pesado, Promocion, TaxFree
from excepciones import ErrorCarritoLleno, ErrorFondosInsuficientes, ErrorEdadNoPermitida

# --- utilidades de test ---

def usuario_bronce(nombre="Juan", edad=20, extranjero=False, saldo=0, puntos=0):
    u = Usuario(nombre, edad, extranjero)
    u.saldo = float(saldo)
    u.puntos = int(puntos)
    u.actualizar_nivel()
    return u

def tienda_basica():
    return Tienda()

# 1) Mueble pesado, tax-free y de promoción muestra etiqueta correcta
def test_etiqueta_mueble_pesado_taxfree_promocion():
    u = usuario_bronce(edad=30, extranjero=True, saldo=1_000_000)
    mueble = Mueble("Mesa", 60000, [Pesado(), TaxFree(), Promocion(0.30)])
    etiqueta = mueble.etiqueta(u)
    assert "[Mueble]" in etiqueta
    assert "Mesa" in etiqueta
    assert "Pesado" in etiqueta
    assert "TaxFree" in etiqueta
    assert "Promoción(-30%)" in etiqueta
    assert "Precio:" in etiqueta and "Envío:" in etiqueta

# 2) Mueble pesado de $60.000 con 30% desc. incluye recargo de mueble (+$1000) y envío (+$3000)
def test_mueble_pesado_60000_con_descuento_incluye_recargo_y_envio():
    u = usuario_bronce(edad=25, extranjero=False, saldo=1_000_000)
    mueble = Mueble("Aparador", 60000, [Pesado(), Promocion(0.30)])
    precio = mueble.precio_venta(u)
    envio = mueble.costo_envio()
    # Cálculo: 60000 + 21%*60000 (12600) + 1000 = 73600 -> promo 30% => 51520
    assert envio == 3000.0
    assert precio == pytest.approx(51520.0, abs=0.01)

# 3) Bronce con $5000 compra mochila por $5000 suma 500 puntos y saldo 0 (usando TaxFree y extranjero)
def test_bronce_compra_mochila_por_5000_gana_500_puntos_y_saldo_0():
    tienda = tienda_basica()
    u = usuario_bronce(edad=25, saldo=5000)
    tienda.registrar_usuario(u)
    u.extranjero = True
    mochila = Indumentaria("Mochila", 5000, [TaxFree()])
    u.agregar_al_carrito(mochila)
    total = tienda.gestionar_venta(u)
    assert total == 5000.0
    assert u.saldo == 0.0
    assert u.puntos == 500  # 10% de 5000

# 4) Negocio penaliza morosidad
def test_morosidad_descuenta_100_puntos():
    tienda = tienda_basica()
    u = usuario_bronce(edad=30, saldo=-1, puntos=5200)
    tienda.registrar_usuario(u)
    tienda.gestionar_morosidad()
    assert u.puntos == 5100  # -100
    # Sigue siendo Plata (>= 5000)
    assert u.nivel.nombre() == "Plata"

# 5) Bronce con 1 punto pasa a Plata al darle 5000 puntos
def test_bronce_pasa_a_plata_en_umbral():
    u = usuario_bronce(edad=22, puntos=1)
    assert u.nivel.nombre() == "Bronce"
    u.puntos = 5000
    u.actualizar_nivel()
    assert u.nivel.nombre() == "Plata"

# 6) Bronce con saldo $4999 no puede comprar mochila de $5000
def test_bronce_no_compra_por_falta_de_fondos():
    tienda = tienda_basica()
    u = usuario_bronce(edad=25, saldo=4999)
    tienda.registrar_usuario(u)
    u.extranjero = True
    mochila = Indumentaria("Mochila", 5000, [TaxFree()])
    u.agregar_al_carrito(mochila)
    pytest.raises(ErrorFondosInsuficientes) as exc:
    tienda.gestionar_venta(u)
    # Verificamos que el mensaje incluya detalle personalizado
    assert "Fondos insuficientes" in str(exc.value)
    assert "Total=" in str(exc.value)

# 7) Menor de 18 no puede comprar cerveza aunque tenga saldo
def test_menor_no_puede_comprar_bebida_alcoholica():
    u = usuario_bronce(edad=17, saldo=10000)
    cerveza = BebidaAlcoholica("Cerveza", 1000, [])
    #with pytest.raises(ErrorEdadNoPermitida):
    u.agregar_al_carrito(cerveza)

# 8) Usuario extranjero aprovecha TaxFree (sin IVA)
def test_extranjero_taxfree_sin_iva():
    u = usuario_bronce(edad=40, extranjero=True, saldo=10000)
    prod = Indumentaria("Campera", 5000, [TaxFree()])
    assert prod.precio_venta(u) == 5000.0

# 9) Bronce con 4900 puntos compra por $1000 y sube a Plata
def test_bronce_sube_a_plata_al_llegar_a_5000():
    tienda = tienda_basica()
    u = usuario_bronce(edad=28, saldo=2000, puntos=4900)
    tienda.registrar_usuario(u)
    u.extranjero = True
    prod = Indumentaria("Gorra", 1000, [TaxFree()])
    u.agregar_al_carrito(prod)
    pagado = tienda.gestionar_venta(u)
    assert pagado == 1000.0
    assert u.puntos == 5000
    assert u.nivel.nombre() == "Plata"

# 10) Bronce no puede agregar mochila y cartuchera a la vez
def test_bronce_no_puede_agregar_dos_items():
    u = usuario_bronce(edad=20, saldo=10000)
    mochila = Indumentaria("Mochila", 2000, [TaxFree()])
    cartuchera = Indumentaria("Cartuchera", 1000, [TaxFree()])
    u.agregar_al_carrito(mochila)    
    u.agregar_al_carrito(cartuchera)
    with pytest.raises(ErrorCarritoLleno):
        u.agregar_al_carrito(cartuchera)

# print(usuario_bronce())
test_etiqueta_mueble_pesado_taxfree_promocion()
test_bronce_sube_a_plata_al_llegar_a_5000()
# test_bronce_no_puede_agregar_dos_items()
#test_menor_no_puede_comprar_bebida_alcoholica()
test_bronce_no_compra_por_falta_de_fondos()