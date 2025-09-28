from abc import ABC,abstractmethod

class Persona(ABC):
    def __init__(self,dni:str,nombre:str):
        self.__dni:str = dni
        self.__nombre:str = nombre

    @property
    def dni(self)->str:
        return self.__dni

    @property
    def nombre(self)->str:
        return self.__nombre

class Agente(Persona):
    def __init__(self, dni:str, nombre:str,comision:float=0):
        super().__init__(dni, nombre)
        self.__comision:float=comision

   
    def calcular_comision(self,operacion:'Operacion')->float:
        return operacion.calcular_comision()
        
        
        

class Cliente(Persona):
    def __init__(self, dni:str, nombre:str):
        super().__init__(dni, nombre)

class Operacion(ABC):

    def __init__(self,inmueble:'Inmueble',cliente:Cliente,agente:Agente):
        self.__inmueble:Inmueble = inmueble
        self.__cliente:Cliente = cliente
        self.__agente:Agente = agente

    @property
    def inmueble(self)->'Inmueble':
        return self.__inmueble
    @property
    def cliente(self)->'Cliente':
        return self.__cliente
    @property
    def agente(self)->'Agente':
        return self.__agente

    @abstractmethod
    def calcular_comision(self)->float:
        pass    

class Venta(Operacion):
    def __init__(self, inmueble:'Inmueble', cliente:Cliente, agente:Agente,por_comision:float):
        super().__init__(inmueble, cliente, agente)
        self.__por_comision:float= por_comision    

    @property
    def por_comision(self)->float:
        return self.__por_comision
    

    def calcular_comision(self)->float:
        return self.por_comision*self.inmueble.obtener_valor()



class Alquiler(Operacion):
    def __init__(self, inmueble:'Inmueble', cliente:Cliente, agente:Agente,cantidad_meses:int):
        super().__init__(inmueble, cliente, agente)
        self.__cantidad_meses:int=cantidad_meses

    @property
    def cantidad_meses(self)->int:
        return self.__cantidad_meses

    def calcular_comision(self)->float:
        return self.cantidad_meses/5000*self.inmueble.obtener_valor()



class Inmueble(ABC):
    def __init__(self,direccion:str,superficie:float,cantidad_ambientes:int):
        self.__direccion:str=direccion
        self.__superficie:float=superficie
        self.__cantidad_ambientes:int=cantidad_ambientes

    @property
    def direccion(self)->str:
        return self.__direccion

    @property
    def superficie(self)->float:
        return self.__superficie

    @property
    def cantidad_ambientes(self)->int:
        return self.__cantidad_ambientes
    
    @abstractmethod
    def obtener_valor(self)->float:
        pass    

class PH(Inmueble):
        
    VALOR_MINIMO = float(50000)
    VALOR_METRO_CUADRADO = float(4000)

    def __init__(self, direccion, superficie, cantidad_ambientes):
        super().__init__(direccion, superficie, cantidad_ambientes)
    
    def obtener_valor(self)->float:
       importe = self.superficie*PH.VALOR_METRO_CUADRADO
       if importe < PH.VALOR_MINIMO:
           return PH.VALOR_MINIMO
       return importe    

class Departamento(Inmueble):

    VALOR_AMBIENTE = float(35000)
    
    def __init__(self, direccion, superficie, cantidad_ambientes):
        super().__init__(direccion, superficie, cantidad_ambientes)

    def obtener_valor(self)->float:
        return self.cantidad_ambientes*Departamento.VALOR_AMBIENTE

class Casa(Inmueble):
    
    def __init__(self, direccion, superficie, cantidad_ambientes,valor:float):
        super().__init__(direccion, superficie, cantidad_ambientes)
        self.__valor:float = valor

    @property
    def valor(self)->float:
        return self.__valor

    def obtener_valor(self)->float:
        return self.valor


class Inmobiliaria:

    def __init__(self,nombre:str):
        self.__nombre:str=nombre
        self.__lista_agentes:list[Agente] = []
        self.__lista_clientes:list[Cliente] = []
        self.__lista_inmuebles:list[Inmueble] = []

    def agregar_agente(self,agente:Agente)->None:
        if not isinstance(agente,Agente):
            raise ValueError("SOLO SE PUEDEN AGREGAR AGENTES A LA LISTA DE AGENTES")
        self.__lista_agentes.append(agente)

    def agregar_cliente(self,cliente:Cliente)->None:
        if not isinstance(cliente,Cliente):
            raise ValueError("SOLO SE PUEDEN AGREGAR CLIENTES A LA LISTA DE CLIENTES")
        self.__lista_clientes.append(cliente)

    def agregar_inmuebles(self,inmueble:Inmueble)->None:
        if not isinstance(inmueble,Inmueble):
            raise ValueError("SOLO SE PUEDEN AGREGAR INMUEBLES A LA LISTA DE INMUEBLES")
        self.__lista_inmuebles.append(inmueble)


    def hacer_una_venta()->None:
        pass

    def hacer_un_alquiler()->None:
        pass


def main():
    ag1 = Agente("33125125","Raul Suarez")
    
    ca1 = Casa("Salta 123",400,4,125400)
    cl1 = Cliente("41741741","Rosa Ana Esposito")
    v1 = Venta(ca1,cl1,ag1,1.5)
    print(f"calcular comision de la venta: {v1.calcular_comision()}")
    print(f"calcular comision del agente: {ag1.calcular_comision(v1)}")
          

if __name__ == "__main__":    
    main()
