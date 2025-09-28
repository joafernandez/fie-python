

from persona import Persona

class Enfermedad:###################################################################################################
    def __init__(self, cant_celulas:int):
        self.__cant_celulas=cant_celulas
        
    @property
    def mostrar_cant_celulas(self):
        return self.__cant_celulas
    
    @mostrar_cant_celulas.setter
    def mostrar_cant_celulas(self, cantidad:int):
        if cantidad < 0:
         self.__cant_celulas = 0
        else:
            self.__cant_celulas = cantidad

    

    def se_etenua(self,medicamento:int):# baja la cantidad de celulas
        if medicamento >0:# si la per consume medicament
            self.__cant_celulas-= (medicamento*15)#la celula se resta multiicado 15
        #control que puedo ahcer 
            if self.__cant_celulas<0: #si me quedo negativo
                self.__cant_celulas=0 #lo pongo en cero 
    
    def esta_sana(Self):
        if Self.__cant_celulas==0:
         print("persona sana")
         
         
         
    def __str__(self):
        return f" la cantidad de celulas es la siguiente: {self.mostrar_cant_celulas}"
    
    
    
    
class Infeccion(Enfermedad):######################################################################################
    def __init__(self, cant_celulas,tipo:str):
       super().__init__(cant_celulas)
       self.__tipo=tipo # ejemplo si es la malaria 
         
       
    @property
    def mostrar_tipo_infeccion(self):
        return self.__tipo
           
       
    def aumentar_temperatura(self,persona:Persona):
        if self.mostrar_tipo_infeccion.lower()=="malaria":  #paso a mayusculas para evitar errores
            persona.mostrar_temperatura += (self.__cant_celulas/1000) # usar SETTER
        
    def infeccion_reproduce(self):
       self.__cant_celulas=self.mostrar_cant_celulas * 2
       
       
       
    def __str__(self):
        return f" TIPO DE INFECCION:{self.mostrar_tipo_infeccion} TCELULAS:{self.__cant_celulas}"
        
       
       
class Autoinmune(Enfermedad):####################################################################################
    def __init__(self, cant_celulas,tipo:str):
       super().__init__(cant_celulas)
       self.__tipo=tipo # ejemplo si es lupu
       
    @property
    def mostrar_tipo_autoinmune(self):
        return self.__tipo 
       
   
       
    def destruir(self,persona:Persona):
        if self.mostrar_tipo_autoinmune.lower()== "lupus":
            persona.mostrar_celulas_buenas-= self.mostrar_cant_celulas # USAR EL SETTER PARA ACCEDER
         
        
        
class Mixta(Autoinmune,Infeccion):
     def __init__(self, cant_celulas, tipo:str):
        super().__init__(cant_celulas, tipo)
       
       
       
       
       
       
       
       