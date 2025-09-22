"""
Contexto: 
Se sabe que en una autopista se cobra peaje a los vehículos que la usan. 
Los autos y camiones tienen diferentes formas de calcular la tarifa: para 
el auto es un valor único ($100) mientras que en los camiones $200 por 
cada eje, las motos pagan la mitad del valor del auto. Y además hay 
diferentes formas de pago: con telepeaje “Pass”, con la tarjeta Sube y en 
efectivo (50%, 70%, %100 del valor estándar respectivamente).  
Se tienen que registrar los cobros de peaje con el valor cobrado y la 
patente del vehículo.  
Realizar código para: 
1. Cobrar a un auto con “SUBE”, una moto en efectivo y un camión de 
3 ejes con “Pass”. 
2. Calcular el valor de recaudación total de los peajes. 
3. Encontrar la patente del mejor cliente, sería aquel que más gastó en 
los peajes. 
4. Agregar tarifa especial para autos eléctricos (20% de un auto 
común), y otra de $0 para cualquier tipo de vehículo 
gubernamental.
"""

from abc import ABC,abstractmethod

class Tarifario:
    TARIFA_AUTO = float(100)
    TARIFA_MOTO = TARIFA_AUTO / 2
    TARIFA_EJE  = float(200)
    TARIFA_OFICIAL  = float(0)
    TARIFA_ELECTRICA  = TARIFA_AUTO * .2


class MetodoPago(ABC):
    @abstractmethod
    def factor_cobro()->float:
        pass    

class PagoPass(MetodoPago):
    def factor_cobro()->float:
        return 0.5

class PagoTarjeta(MetodoPago):
    def factor_cobro()->float:
        return 0.7

class PagoEfectivo(MetodoPago):
    def factor_cobro()->float:
        return 1.0
    

class Cobro:
    def __init__(self,patente:str,monto:float):
        self.__patente = patente
        self.__monto = monto
        

    @property
    def patente(self)->str:
        return self.__patente    

    @property
    def descripcion(self)->str:
        return self.__descripcion

    @property
    def monto(self)->float:
        return self.__monto

    def __str__(self):
        return f"Patente {self.patente} ${self.monto:10.2f}"
    
    
    
    
    

class Vehiculo(ABC):

    def __init__(self,patente:str,es_gubernamental:bool = False): # Constructor
        self.__patente = patente
        self.__es_gubernamental = es_gubernamental

    @property # get
    def patente(self)->str:
        return self.__patente    

    @property
    def es_gubernamental(self)->bool: # get
        return self.__es_gubernamental
    


    def __str__(self):
        return f"{self.patente} Oficial: ({self.es_gubernamental}) Tarifa: $ {self.calcular_tarifa()} "

    @abstractmethod
    def calcular_tarifa(self)->float:
        pass





class Auto(Vehiculo):
    def __init__(self, patente, es_gubernamental = False):
        super().__init__(patente, es_gubernamental)


    def calcular_tarifa(self)->float:
        return Tarifario.TARIFA_AUTO

class Moto(Vehiculo):
    def __init__(self, patente, es_gubernamental = False):
        super().__init__(patente, es_gubernamental)

    def calcular_tarifa(self)->float:
        return Tarifario.TARIFA_MOTO

class Camion(Vehiculo):
    def __init__(self, patente, cantidad_ejes:int,es_gubernamental = False):
        super().__init__(patente, es_gubernamental)
        self.__cantidad_ejes = cantidad_ejes

    def __str__(self):
        return f"{self.patente} Oficial: ({self.es_gubernamental}) Ejes [{self.cantidad_ejes}]"

    @property
    def cantidad_ejes(self)->int:
        return self.__cantidad_ejes    

    def calcular_tarifa(self)->float:
        return Tarifario.TARIFA_EJE * self.cantidad_ejes


class CabinaPeaje():

    def __init__(self):
        self.__lista_cobros:list[Cobro] = []


    def cobra(self,vehiculo:Vehiculo,metodo_pago:MetodoPago) -> Cobro:
        importe = vehiculo.calcular_tarifa() * metodo_pago.factor_cobro()
        cobro = Cobro(vehiculo.patente,importe)
        self.__lista_cobros.append(cobro)

        return cobro
                      
    def __str__(self):
        cadena = "Listado de Cobros de la Cabina\n"

        for cob in self.__lista_cobros:
            cadena += f"{cob}\n"

    
def main():
    
    v = Auto("abc111")
    print(v)
    vg = Auto("aaa666",True)
    print(vg)

    c = Camion("yyy111",6)
    print(c)

    cab = CabinaPeaje()

    cab.cobra(v,PagoEfectivo())
    cab.cobra(vg,PagoEfectivo())
    cab.cobra(v,PagoTarjeta())
    cab.cobra(c,PagoEfectivo())


    print(cab)
main()




