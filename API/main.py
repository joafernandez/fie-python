from abc import ABC , abstractmethod
            
class Tarjeta_debito: #-----------------------------------------------------------------------------------------
    def __init__(self,codigo:int,saldo:float):  #cuenta codigo :12344444   
        self.codigo=codigo
        self.saldo=saldo

    def descontar(self,importe): 
        if self.saldo<importe: #si el saldo es menor al importe
            raise ValueError ("no alcanza el saldo") 
    
        if importe>3000: # y si es mayor a 3mil
             iva=importe*0.21
             importe-=iva
             
        self.saldo-=importe
    
    

class Tarjeta_credito (ABC): #-------------------------------------------------------------------------------------
    def __init__(self,deuda:int):
        self.deuda=deuda
     
    @abstractmethod 
    def gastar(self,importe):
       pass
    
   
   

class Blanca(Tarjeta_credito):
    def __init__(self, deuda):
        super().__init__(deuda)
        
    LIMITE=10000 #para gastos 
    
    def gastar(self, importe):  
        if self.deuda + importe  > self.LIMITE :#si la deuda q tengo mas lo q vppy a gastar supera el limite
            raise ValueError ("supero los limites de la tarejta de credito blanca")
        self.deuda+=importe
        
        
        
class Dorada(Tarjeta_credito):
    def __init__(self, deuda):
        super().__init__(deuda)
    
    
    
    def gastar(self,importe):
        self.deuda+=importe
     
           
        
        
class Cuenta:#-------------------------------------------------------------------------------------------------
    def __init__(self,dni:int,tipo_moneda:str,tarjeta:object):
        self.__tipo_moneda=tipo_moneda
        self.__dni=dni
        self.__tarjeta_debito=tarjeta #mostar
        self.__lista_tarjetas_credito=[]#agregar DIFICIL
        

      
    @property
    def mostrar_dni(self):
        return self.__dni
        
    @property
    def mostrar_tarjeta_debito_asociada(self):
        return self.__tarjeta_debito
    
    def agregar_tarjeta_credito(self,tajeta:object):
        self.__lista_tarjetas_credito.append(tajeta)
        
    
    @property
    def mostrar_lista_tarjetas_credito(self):
        for aux in self.__lista_tarjetas_credito:
            print(aux.deuda)
            
        

    def comprobar_moneda(self):
        if self.__tipo_moneda.lower()!="pesos":
            raise ValueError ("solo se permite pagar con pesos")
        
    
    def calcular_deuda_total(self):
        deuda_total = 0  # arranco en 0, voy a acumular la deuda
        for aux in self._Cuenta__lista_tarjetas_credito:  # recorro todas las tarjetas de crédito
            deuda_total += aux.deuda  # sumo la deuda de cada tarjeta a la acumulada
        return deuda_total  # devuelvo la suma total de deudas de esta cuenta
        



class Banco:
    def __init__(self):
            self.tabla_cuenta={}  #creo un DICCIONARIO {cuanta y dni}
            
            
            
            """    DNI        CUENTA
                 38123456    Cuenta Joana
                 40222333    Cuenta Pedro    """
            
            
            
    def agregar_cuenta(self, cuenta):  # agrego a la tabla
        self.tabla_cuenta[cuenta.mostrar_dni]=cuenta #la clave es el dni

        
    def consultar_saldo(self,dni:int):  #busco en la tabla
        for aux in self.tabla_cuenta:#recorro los dni (es la clave de busqueda)
            if aux==dni: #si el aux encuentra el dni 
                   la_cuenta= self.tabla_cuenta[aux]# paso a la 2da columna y guardo la cuenta
                   #ahora consulto a esa cuenta la tarjeta con el saldo
                   return la_cuenta.mostrar_tarjeta_debito_asociada.saldo
        raise ValueError ("No existe cuenta para ese DNI")
    
    
    
            
    def consultar_deuda(self,dni:int):  #busco en la tabla
        for aux in self.tabla_cuenta:#recorro los dni (es la clave de busqueda)
            if aux==dni: #si el aux encuentra el dni 
                   cuenta_correcta= self.tabla_cuenta[aux]# paso a la 2da columna y guardo la cuenta
                   #ahora consulto a esa cuenta la LISTA DE TARJETAS
                   total_deuda=0
                   for aux2 in cuenta_correcta._Cuenta__lista_tarjetas_credito: #uso la lista de esta cuenta
                       total_deuda+=aux2.deuda
                   return total_deuda
    
        raise ValueError("No existe cuenta para ese DNI")
                
          
       
    def consumir_debito(self,tarjeta:Tarjeta_debito,importe:int):
        tarjeta.descontar(importe)
            
            
    def consumir_credito(self,tarjeta:Tarjeta_credito,importe:int):
        tarjeta.gastar(importe)
                
                

    def mejor_cliente(self):
        mejor_dni = None   # todavía no hay ( None = vacío)
        mayor_deuda = -1   # arranco con -1 para que cualquier deuda real sea mayor

        
        for aux in self.tabla_cuenta:# Recorro todas las claves(DNI)
            cuenta_correcta = self.tabla_cuenta[aux]  # saco la cuenta asociada a ese DNI
            deuda_total = cuenta_correcta.calcular_deuda_total()  # llamo al metodo deuda total()

            # comparo si esta cuenta debe más que la mayor encontrada hasta ahora
            if deuda_total > mayor_deuda:
                mayor_deuda = deuda_total  # actualizo la mayor deuda
                mejor_dni = aux  # guardo el DNI de este cliente HASTA AHORA
                

        return mejor_dni  # devuelvo el DNI del cliente con mayor deuda


if __name__ == "__main__":
    # Débito
    debito1 = Tarjeta_debito(1234, 10000)
    debito2 = Tarjeta_debito(5678, 5000)

    # Cuentas
    cuenta1 = Cuenta(dni=38123456, tipo_moneda="pesos", tarjeta=debito1)
    cuenta2 = Cuenta(dni=40222333, tipo_moneda="pesos", tarjeta=debito2)

    # Crédito
    t1_blanca = Blanca(deuda=2000)
    t1_dorada = Dorada(deuda=3000)
    cuenta1.agregar_tarjeta_credito(t1_blanca)
    cuenta1.agregar_tarjeta_credito(t1_dorada)

    t2_blanca = Blanca(deuda=1000)
    cuenta2.agregar_tarjeta_credito(t2_blanca)

    # Banco
    banco = Banco()
    banco.agregar_cuenta(cuenta1)
    banco.agregar_cuenta(cuenta2)

    # Pruebas
    print("Saldo 38123456:", banco.consultar_saldo(38123456))
    print("Deuda 38123456:", banco.consultar_deuda(38123456))
    print("Saldo 40222333:", banco.consultar_saldo(40222333))
    print("Deuda 40222333:", banco.consultar_deuda(40222333))
    print("Mejor cliente:", banco.mejor_cliente())

    # Consumos
    banco.consumir_debito(debito1, 5000)
    banco.consumir_credito(t1_blanca, 1500)
    print("Saldo 38123456 post débito:", banco.consultar_saldo(38123456))
    print("Deuda Blanca de 38123456:", t1_blanca.deuda)
