from bebida import Bebida
from registro import Registro


class Maquina: 
    def __init__(self):
        self.lista_bebidas=[] 
        self.lista_registros_vendidos=[]
        
        
        
    def agregar_bebida(self,bebida):
        self.lista_bebidas.append(bebida)
        
        
    def agregar_registro(self,registro):
        self.lista_registros_vendidos.append(registro)
      
      
# la maq una lista de bebidas: agua, coca, cafe
# producir:
# cual?me dan nombre 
#buscar en la lista? ese nombre
#cuanto esta? pregunto a bebida con su metodo obtener
#cobrar y guardo :
#guardar registrar la venta(bebida, y precio)-->OBJETO REGISTRO
        
    def producir(self,nombre):# hace un cafe
        bebida_que_piden=None # aca guardo la bebida
        for aux in self.lista_bebidas:#recorro
            if aux.nombre==nombre:#si aux la encontro
                bebida_que_piden=aux#la guardo
                break
        precio=bebida_que_piden.obtener_precio()# le pido el PRECIO A LA BEBIDA ENCONTRAD!!!!
        
        registro=Registro(bebida_que_piden) #    creo un OBJETO tipo CLASE REGISTRO 
        
        self.lista_registros_vendidos.append(registro)
            
            
    def calcular_recaudacion_total(self):
        recaudacion=0
        for i in self.lista_registros_vendidos: #la clase registro tiene precio 
            recaudacion+=i.precio
        return recaudacion
        
        


    def obtener_bebida_mas_cara(self): 
        bebida_mas_cara=self.lista_bebidas[0] #por ahora la primera es la mas cara
        #comparo bebidas
        for aux in self.lista_bebidas: #mi lista de bebidas (nomre,ingrediente,estartegiaprecii)
            if aux.obtener_precio()>bebida_mas_cara.obtener_precio(): # si (pido a la bebida el precio ) y comparo con el maximo actual
                bebida_mas_cara=aux # actualizo 
        return bebida_mas_cara
 
 
 
    
# lista_bebidas = [agua(50), gaseosa(150), cortado(250)]
# mas_cara = agua  # Empiezo con agua

# Recorro:
# aux = agua → 50 > 50? NO
# aux = gaseosa → 150 > 50? SÍ → mas_cara = gaseosa
# aux = cortado → 250 > 150? SÍ → mas_cara = cortado
# Resultado: cortado (la más cara)