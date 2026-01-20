

class Plataforma:
    def __init__(self):
        self.usuarios = []  
        self.peliculas = [] 
        self.sem_tematico = None  #todavia no hay recomendacion sem tatematica
    
    def agregar_usuario(self, usuario): 
        self.usuarios.append(usuario)
    
    def agregar_pelicula(self, pelicula):  
        self.peliculas.append(pelicula)
        
        
    # tengo que activar semanas tematicas
    # y sugerir peliculas
    
    def activar_semana_tematica(self, tipo, valor):  #
        self.sem_tematico = {"tipo": tipo, "valor": valor}#diccionario para filtrar tipo: pais, valor:arg
    
    def desactivar_semana_tematica(self):  
        self.sem_tematico = None
    
    
    
    def recomendar_peliculas(self, usuario, cantidad=6):  #hasta 6 peli sugieor
        recomendaciones = [] 
        for aux in self.peliculas: #recorro lista
            if len(recomendaciones) >= cantidad:  # compruebo maximoo de pelis 
                break
            
            if self.sem_tematico is not None: # si hay semana 
                tipo = self.sem_tematico["tipo"] # aca filtro es pais o genero
                valor = self.sem_tematico["valor"] # accion , argtina
                
                if tipo == "genero" and aux.genero != valor:
                    continue
                if tipo == "pais" and aux.pais_origen != valor:
                    continue
            
            recomendaciones.append(aux)
        
        return recomendaciones

#falta preguntar si ya vio? 