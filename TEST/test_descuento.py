








from clase_descuento import Producto

# descuento funciona bien ?

def test_aplicar_descuento():
    
    p = Producto("Camisa", 100.0) # creo producto con valores
    p.aplicar_descuento(10) #aplico el metodo

    assert p.precio == 90.0 # debería ser 90 




# nombre del producto se guarda bien?

def test_nombre_producto():
    
    p = Producto("Pantalón", 200.0)#  producto con nombre "Pantalón" y precio 200

    assert p.nombre == "Pantalón" # el nombre es pantalon? 
