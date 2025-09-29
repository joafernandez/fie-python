
from datetime import date
from abc import ABC, abstractmethod

class Lugar(ABC):
    def __init__(self,provincia:str):
        self.provincia = provincia

    @abstractmethod
    def obtener_superficie(self):
        pass    

class Oficina(Lugar):

    SUPERFICIE_FIJA = 120

    def __init__(self, provincia:str):
        super().__init__(provincia)

    def obtener_superficie(self):
        return Oficina.SUPERFICIE_FIJA

class Ciudad(Lugar):
    
    def __init__(self, provincia:str,superficie:float):
        super().__init__(provincia)
        self.superficie = superficie

    def obtener_superficie(self):
        return self.superficie

class ZonaRural(Lugar):

    def __init__(self, provincia,ancho:float,largo:float):
        super().__init__(provincia)
        self.largo = largo
        self.ancho = ancho

        
    def obtener_superficie(self):
        return self.largo*self.ancho 


class Tarea(ABC):
    def __init__(self,nombre:str,fecha_inicio:date,costo:float,lugar:Lugar,dependencias:list['Tarea']=None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio        
        self.costo = costo  
        self.lugar = lugar
        self.dependencias : list[Tarea]
        if dependencias != None:
            self.dependencias  = dependencias 
        else:
            self.dependencias = []


    def margen_anterior(self)->int:
        """
        Saber el margen anterior de una tarea, que es la cantidad de días entre que se hace la
        última de las tareas de las que depende, y el día indicado para esa tarea. Si la tarea no
        depende de ninguna, su margen anterior es 0
        """
        if len(self.dependencias) == 0:
            return 0
        else:
            ultima_fecha = max(tarea.fecha_inicio for tarea in self.dependencias )
            return (self.fecha_inicio - ultima_fecha).days
                
    def se_puede_hacer(self):
        for d in self.dependencias:
            if d.fecha_inicio > self.fecha_inicio:
                return False
        return True    

    def agregar_dependencia(self,tarea:'Tarea'):
        self.dependencias.append(tarea)    

    @abstractmethod
    def impacto_financiero(self):
        pass


class TareaProduccion(Tarea):
    def __init__(self, nombre, fecha_inicio, costo, lugar, dependencias = None):
        super().__init__(nombre, fecha_inicio, costo, lugar, dependencias)        
        self.servicios : list[float] = []

    def agregar_servicio(self,servicio:float):
        self.servicios.append(servicio)

    def impacto_financiero(self):
        return -sum(self.servicios)

class TareaRecaudacion(Tarea):
    def __init__(self, nombre, fecha_inicio, costo, lugar, dependencias = None,ingreso:float=0):
        super().__init__(nombre, fecha_inicio, costo, lugar, dependencias)
        self.ingreso = ingreso

    def impacto_financiero(self):
        return self.ingreso

class TareaReunion(Tarea):
    def __init__(self, nombre, fecha_inicio, costo, lugar, dependencias = None):
        super().__init__(nombre, fecha_inicio, costo, lugar, dependencias)

    def impacto_financiero(self):
        return 0.0


class Proyecto:
    def __init__(self,nombre:str,presupuesto:float):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas:list[Tarea] = []

    

    def agregar_tarea(self,tarea:Tarea):
        self.tareas.append(tarea)

    # "requerimientos"
    def provincias_en_rango(self,desde:date,hasta:date)->list[str]:
        """ 
        1. Saber en qué provincias va a haber actividad de un 
        proyecto para un rango de fechas. De
        cada oficina se sabe la ciudad, de cada ciudad y zona 
        rural se sabe la provincia
        """
        lista = []
        for tarea in self.tareas:
            # if tarea.fecha_inicio >= desde and  tarea.fecha_inicio <= hasta:
            if desde <= tarea.fecha_inicio <= hasta:
                lista.append(tarea.lugar.provincia)
        return lista
    
    def saldo_en_fecha(self,fecha:date):
        """ 
        3. Saber el saldo de un proyecto a una fecha, que debe 
        tener en cuenta todas las tareas hasta
        esa fecha inclusive.
        """
        saldo = self.presupuesto
        for tarea in self.tareas:
            if tarea.fecha_inicio <= fecha:
                saldo += tarea.impacto_financiero()
        return saldo
    
    def superficie_promedio(self)->float:
        """
            2. Saber la superficie promedio en la que se desarrollan 
            las tareas de un proyecto. Para las
            oficinas se establece una superficie, la misma para todas en m2.
            Para  las  ciudades  se  informa  explícitamente  la  superficie  en  m2.
            Las zonas rurales se asumen como rectangulares; se informa ancho y largo.
        """
        cantidad = len(self.tareas)
        suma = 0
        if cantidad > 0:
            for tarea in self.tareas:
                suma += tarea.lugar.obtener_superficie()
            return suma/cantidad                
        else:
            return 0.0                
        
    def es_coherente(self)->bool:
        """ 
        5. Saber si un proyecto es coherente; es coherente si pueden hacerse todas las tareas en la
        fecha indicada.
        """
        for tarea in self.tareas:
            if not tarea.se_puede_hacer():
                return False
        return True    
            

def main():
    oficina = Oficina("Cordoba")
    ciudad = Ciudad("Buenos Aires",1000)
    campo = ZonaRural("Santa Fe",100,100)

    p = Proyecto("Sarasa",1000)

    t1 = TareaRecaudacion("Juntar plata",date(2025,1,10),oficina,None,500)
    t2 = TareaProduccion("Gastar",date(2025,1,12),1000,ciudad,None)
    t2.agregar_servicio(100)
    t2.agregar_servicio(100)
    t2.agregar_servicio(100)
    t3 = TareaReunion("Nos juntamos",date(2025,1,15),1000,campo)

    p.agregar_tarea(t1)
    p.agregar_tarea(t2)
    p.agregar_tarea(t3)

    print("Saldo",p.saldo_en_fecha(date(25,1,12)))    





if __name__ == "__main__":
    main()