

# MODELO de REGISTRO  ( cafe, $50)


class Registro:
    def __init__(self,bebida):
       self.bebida=bebida
       self.precio=bebida.obtener_precio()
       
       
    def mostrar_registro(self):
        return f"bebida:{self.bebida.nombre} precio:{self.precio}"


