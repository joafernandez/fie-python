from maquina import Maquina
from bebida import Bebida, Granizado, Gaseosa ,Agua, Cortado
from registro import Registro






def main():
    
     #creo mi maquina
    maquina1=Maquina()
    
    #creo estrategias
    estrategia_gaseosa=Gaseosa()
    estrategia_garnizado=Granizado()
    estrategia_agua=Agua()
    
       
    #creo las bebidas
    vaso_gaseosa=Bebida("VASO DE GASEOSA",["agua","saborizante","gas"],estrategia_gaseosa)
    granizado_de_cafe_cremoso=Bebida("GRANIZ CAFE CREMOSO",["leche","cafe","azucar","canela"],estrategia_garnizado)
    agua=Bebida("AGUA", ["agua"],estrategia_agua)
    
    
    #agrego las bebidas a la lista de la mquina
    maquina1.agregar_bebida(vaso_gaseosa)
    maquina1.agregar_bebida(granizado_de_cafe_cremoso)
    maquina1.agregar_bebida(agua)
    
    # sirvo produzco
    maquina1.producir("VASO DE GASEOSA")
    maquina1.producir("GRANIZ CAFE CREMOSO")
    maquina1.producir("AGUA")
    
    
    # calculo recaudacion
    print(f"recaudacion total es:$ {maquina1.calcular_recaudacion_total()}")
    
    
    
    #busco la mas cara
    bebida_mas_cara= maquina1.obtener_bebida_mas_cara()
    print(f"la bebida mas cara es:{bebida_mas_cara.nombre} y su precio es:{bebida_mas_cara.obtener_precio()}")          
    
    
if __name__=="__main__":
    main()
    
