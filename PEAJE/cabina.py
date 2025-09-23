
from strategy_pago import Estrategia_pago
from vehiculo_peaje import Vehiculo
from un_ticket import Ticket


class Cabina():
    def __init__(self):
        self.lista_ticket=[] #lista que tiene ticket, [valor,patente]  
                             # es un atributo se accede con self 
        
    
    def agregar_ticket(self,ticket:Ticket):
        self.lista_ticket.append(ticket)
        
 


    def cobrar(self,vehiculo:Vehiculo,estrategia:Estrategia_pago ): # necesito la tarifa * Y LLAMO A LA ESTRATEGIA!!!!!
        return vehiculo.calcular_tarifa()*estrategia.descuento()
    
    def total_Recaudado(self)->float: #no le paso lista xq esta adentro de la clase
        contador=0.0
        for aux in self.lista_ticket:  # aux es un ticket
            contador+= aux.datos_valor
        return contador
            
    def patente_ganador(self)->float:
        # la idea es recorrer la lista
        #tomar un tiket y ponerlo en la tabla
        #cada vz q pongo en la tabla a su vez me fijo si ya existe la patente y le sumo el valor
        #si no existe tengo q decir el valor inicial es cero sumale esto.
        
        tabla={} #creo una tabla
        for aux in self.lista_ticket:#cada vz que recorro 
           tabla[aux.datos_patente]=tabla.get(aux.datos_patente,0.0)+ aux.datos_valor #leo patente sumo e inserto
           
        if not tabla:  #si la tabla esta vacia 
            return None
           
        ganador = max(tabla,key=tabla.get) #uso la funcion max
        return ganador
     
     
     
    def __str__(self):
        return f" (total recaudado:{self.total_Recaudado()})(patente ganador:{self.patente_ganador()})"
    
    