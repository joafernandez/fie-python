  
"""
1. Cobrar a un auto con “SUBE”, una moto en efectivo y un camión de 3 ejes con “Pass”. 

2. Calcular el valor de recaudación total de los peajes. 
3. Encontrar la patente del mejor cliente, sería aquel que más gastó en los peajes. 
4. Agregar tarifa especial para autos eléctricos (20% de un auto  común), 
y otra de $0 para cualquier tipo de vehículo gubernamental."""





from vehiculo_peaje import Auto, Camion, Moto
from cabina import Cabina
from strategy_pago import Sube, Telepeaje, Efectivo
from un_ticket import Ticket

    
def main():
    
    auto1=Auto("lwd")
    moto1=Moto("lwg")
    camion1=Camion("lfg",3)
    
    cabina = Cabina()
   
    valorauto=cabina.cobrar(auto1,Sube())
    valormoto=cabina.cobrar(moto1,Telepeaje())
    valorcamion=cabina.cobrar(camion1,Efectivo())


    ticket1=Ticket(auto1.patente,valorauto)
    ticket2=Ticket(moto1.patente,valormoto)
    ticket3=Ticket(camion1.patente,valorcamion)


    cabina.agregar_ticket(ticket1)
    cabina.agregar_ticket(ticket2)
    cabina.agregar_ticket(ticket3)
    
 
    print(cabina)

if __name__ == "__main__":
    main()
    
    
 






