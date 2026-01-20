from abc import ABC, abstractmethod


    #publicar texto,foto,video
    # ver publicacion
    #indicar me gusta
    #pone permisos en la publi 
    #calcular espaciototal de publicaciones
    #mejores amigo(los q pueden ver)
    #buscar un amigo y contar el que mas mg tiene
class Usuario:   
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_amigos=[]
        self.lista_publicaciones=[]
        
        
    def agregar_amigo(self, usuario):  
        self.lista_amigos.append(usuario)
    
    def es_amigo(self, usuario):  
        return usuario in self.lista_amigos
    
    def publicar(self, publicacion):  # agrega
        self.lista_publicaciones.append(publicacion)
    
        
    def espacio_total_publicacion(self):
        total=0
        for aux in self.lista_publicaciones: #recorro mis publi
            total+= aux.calcular_espacio_KB() # a cada una le calculo el espacio total
        return total
                   
                   
    def contar_mg_total(self,usuario):
        cantidad=0
        for aux in usuario.lista_publicaciones:
            cantidad+= aux.me_gusta
        return cantidad
        
                               
        
    def amigo_popular(self):# el que mas me gusta tiene
        amigo=self.lista_amigos[0] #al primero de la lista   // actualizar
        maximo_mg=self.contar_mg_total(amigo) #le cuento los mg  // actualizar
        for aux in self.lista_amigos:
            nuevo_max=self.contar_mg_total(aux)
            if nuevo_max > maximo_mg:
                    amigo=aux #actualizo
                    maximo_mg=nuevo_max#actualizo
        return amigo  
        
        
    def obtener_mejores_amigos(self): 
        mejores_amigos = [] #creo una lisrta
        for amigo in self.lista_amigos:
            puede_ver_todas = True  # supongo q ve mis publi
            for publicacion in self.lista_publicaciones:
                if not publicacion.ver_publicacion(amigo, self):  # si no puede ver una
                    puede_ver_todas = False #cambio
                    break
            if puede_ver_todas:  # si puede ver todas, es mejor amigo
                mejores_amigos.append(amigo)
        return mejores_amigos
        
        
   
        
        
        
    
    
  
    

    