from producto import Mueble, Promocion, Pesado, Taxfree
from usuario import Usuario

class UsuarioMock:
    def algo_prefijado(self): 
        return 1000

def test_1():
    u1 = Usuario("juan", 23, 2000, 0, extranjero=True)
    
    #  decoradores
    p1 = Mueble("sofa", 2000, 400)
    p1 = Promocion(p1, 0.5)   # 50% descuento → 1000
    p1 = Pesado(p1)           # +3000 → 4000
    p1 = Taxfree(p1)          # resta IVA 21% → 3580
    
    valor_real = p1.precio_venta(u1)
    
    # calculo esperado
    precio_venta_correcto = 4000 - (4000 * 0.21)
    
    assert valor_real == precio_venta_correcto
    
    