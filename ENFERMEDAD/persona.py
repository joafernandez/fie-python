
class Persona:  # UNA PERSONA!
    def __init__(self,dias_enfermo:int,temperatura:int,celulas_buenas:int):
        self.__dias_enfermo=dias_enfermo
        self.__lista_enfermedad=[] #ire agregando malaria,lups ...etc
        self.__temperatura=temperatura  #puede cambiar seter
        self.__celulas_buenas=celulas_buenas #puede cambiar sette
    
        
               
    @property
    def mostrar_dias_enfermo(self)->int:
        return self.__dias_enfermo
    
    @property
    def mostrar_temperatura(self)->int:
        return self.__temperatura
     
     # hacer setter temp
    @mostrar_temperatura.setter
    def mostrar_temperatura (self,cantidad:int):
    #controlo q no ingrese cant negativa
        if cantidad<0:
            self.__temperatura=0
        else:            
            self.__temperatura=cantidad
     
     
    @property
    def mostrar_celulas_buenas(self)->int:
        return self.__celulas_buenas
    
    #hacer setter celulas buenas afectadas por las malas
    @mostrar_celulas_buenas.setter
    def mostrar_celulas_buenas(self, cantidad:int):
      #controlo q no ingrese cant negativa
        if cantidad<0:
            self.__celulas_buenas=0
        else:            
            self.__celulas_buenas=cantidad
          
    
    @property
    def mostrar_lista_enfermedad(self):
        return self.__lista_enfermedad
    
    

    def agregar_enfermedad(self,nombre_enfermedad:object):  #agrego de que se va enfermando- O SEA SE ENFERMA!
        return self.__lista_enfermedad.append(nombre_enfermedad)
    
   #BUENO NO ENTENDI AL FINAL ESTO LO PEGO :
    def vivir_un_dia(self):
        self.__dias_enfermo += 1   # suma un día
        for enfermedad in self.__lista_enfermedad:
            
        # pregunto por el nombre de la clase, no con import
            nombre = enfermedad.__class__.__name__

        if nombre == "Infeccion":
            enfermedad.aumentar_temperatura(self)
            enfermedad.infeccion_reproduce()

        elif nombre == "Autoinmune":
            enfermedad.destruir(self)

        elif nombre == "Mixta":
            enfermedad.aumentar_temperatura(self)
            enfermedad.infeccion_reproduce()
            enfermedad.destruir(self)
    

    
    
    
    def __str__(self):
        return f"Persona enferma de :{self.__lista_enfermedad} ,cantidad de dias enfermo:{self.__dias_enfermo}"
        