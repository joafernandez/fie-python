
from enfermedad import Enfermedad


class Persona:
    def __init__(self, temperatura, celulas):
        self.temperatura = temperatura  # temperatura 
        self.celulas = celulas  # cantidad celulas sanas
        self.enfermedades = []  # lista de enfermedades/objetos que puede tener /agregar/eliminar
    
    def contraer_enfermedad(self, enfermedad):  # agregar enfermedad
        self.enfermedades.append(enfermedad)
    
    
    # voy a recorrer todas las enfermedades y hacer efecto en cada una 
    def vivir_un_dia(self): 
        for aux_enfermedad in self.enfermedades:
            aux_enfermedad.hacer_efecto(self)  # llamo al metodo de la enf <---------------------------
    
    
    def recibir_medicamento(self, dosis_ml):  # recibo la dosis y atenua
        cantidad_atenuar = dosis_ml * 15  #esto es lo q atenua a acda una
        for enfermedad in self.enfermedades: #miro la lista una por una
            enfermedad.atenuar(cantidad_atenuar) #llamo al metodo
        
        # elimino enfermedades cuaradas
        self.enfermedades = [aux for aux in self.enfermedades if not aux.esta_curada()]
        # lista de enfermedad= es igual a toda enfermedad que no este curada 
    


    def esta_sana(self):  # la persona esta sana?????
        return len(self.enfermedades) == 0 # cuento la lista de enfermedades el tam
    
    def curar_hasta_sanar(self, dosis_ml):  # recibe medicamento hasta estar sana
        while not self.esta_sana(): #mientras sana no llegue a cero 
            self.recibir_medicamento(dosis_ml)

    def limpiar_curadas(self):
        self.enfermedades = [e for e in self.enfermedades if not e.esta_curada()]