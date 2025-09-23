
class Ticket:
    def __init__(self,patente:str,valor:float):
        self.__patente=patente
        self.__valor=float(valor) #asi ebvitoo q me manden un int o str
    

    @property
    def datos_patente(self):
        return self.__patente

    
    @property
    def datos_valor(self):
        return self.__valor
