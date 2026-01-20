from plataforma import Plataforma
from usuario import Usuario
from pelicula import Pelicula
from caracteristica import Promocional, Exclusiva, Restringida
from suscripcion import PanyAgua, Oro, Diamante


def main():
    plataforma = Plataforma()
    
    
    
    print("_____punto 1___")
    """Verificar que una película exclusiva y promocional de
    $200 con 10 % de descuento tenga el precio final correcto ($216)."""
    
    pelicula1 = Pelicula(" peli de accion ", 120, "accion", "argentina", 18, 200)
    pelicula1.agregar_caracteristica(Exclusiva()) #agrego decorador 
    pelicula1.agregar_caracteristica(Promocional(10)) #otro 
    
    precio_final = pelicula1.calcular_precio_final()
    print(f"precio base: 200")
    print(f"exclusiva + 20%  : {200 * 1.20}")
    print(f"descuento 10% :  {precio_final}")
    print(f"deberia ser 216 : {precio_final == 216}") #deberia darme
    
    
    
    
    
    print("_______-punto 2________")
    #Verificar que un usuario "PanYAgua" pueda reproducir una película gratuita
    
    usuario1 = Usuario("joana", 25, "uruguay",PanyAgua(), 0) #no tiene plata es gratis
    peli_gratis = Pelicula("peli romantica gratis", 90, "romantica", "uruguay", 13, 0)
    
    resultado = usuario1.reproducir_pelicula(peli_gratis)
    print(f"{usuario1.nombre} de pan y agua dberia ver '{peli_gratis.titulo}' gratis: {resultado}")
    
    
    print("_______-punto 3________")
    #3. Verificar que un usuario "PanYAgua" no pueda reproducir contenido pago.
    
    peli_pagada=Pelicula("los 4 fantasticos",40,"accion","argentina",50,150)
    resultado2=usuario1.reproducir_pelicula(peli_pagada)
    print (f"{usuario1.nombre}  de pan y agua NO dberia ver '{peli_pagada.titulo}' : {resultado2}")
    
    
    
    print("_______-punto 4________")
    
    # 4. Verificar que un usuario "Oro" no pueda reproducir contenido exclusivo.
    
    usuario_Oro=Usuario ("romi",25, "francia", Oro(),2000)
    peli_exclusiva= Pelicula("peli exclusiva para ricos",40,"accion","alemania",70,200)
    resultado3= usuario_Oro.reproducir_pelicula(peli_exclusiva)
    print (f"el usuario {usuario_Oro.nombre}  de Oro no puede reproducir:debria ser falso '{peli_exclusiva.titulo}' : {resultado3}")
    
    
    
    
    print("____punto 5_____")
    #Verificar que un usuario "Oro" con saldo $-4900 no pueda reproducir contenido 
    # de $150 al superar el límite permitido para su plan.
    
    usuario_oro_2= Usuario("meli", 28, "chile", Oro(), -4900)
    peli= Pelicula("los 3 chiflados", 45, "comedia", "españa", 12, 150)
    
    print(f"saldo: ${usuario_oro_2.saldo}")
    print(f"el tope de  oro es : {usuario_oro_2.suscripcion.obtener_limite_saldo_negativo()}")
    resultado = usuario_oro_2.reproducir_pelicula(peli)
    print(f"debe ser falso:{resultado}")
    
    
    print("____punto 6_____")
    #6. Verificar que un usuario menor de edad de un país restringido no pueda
    # reproducir contenido que no le corresponde.
    usuario_menor = Usuario("nico", 15, "colombia", Oro(), 5000)
    peli_restringida = Pelicula("la llamada", 105, "terror", "alemania", 18, 200)
    peli_restringida.agregar_caracteristica(Restringida(["venezuela", "colombia"]))
    
    print(f"eddad: {usuario_menor.edad}, minimo: {peli_restringida.edad_minima}")
    print(f"pais: {usuario_menor.pais}, pais restrngido: venezuela, colombia")
    
    resultado = usuario_menor.reproducir_pelicula(peli_restringida)
    print(f"puede reproducir:deberia ser falso: {resultado}")
    
    
    print("____punto 7_____")
    #Verificar que un usuario "Oro" que no puede ver un contenido exclusivo logre 
    # reproducirlo cuando se cambia a "Diamante".
    #me falta metodos
    
    usario_oro_3=Usuario("CATA",33,"boliva",Oro,8000)
    peli_exclusiva=Pelicula("la mascara",40,"comedia","bolivia") 
    
    
    
    
    """
7. Verificar que un usuario "Oro" que no puede ver un contenido exclusivo logre reproducirlo cuando se cambia a "Diamante".
8. Verificar que el método de porcentaje de géneros vistos devuelva correctamente los valores según el historial.
9. Verificar que, al lanzar una semana temática de “Cine Italiano” en los contenidos recomendados, se incluyen películas italianas.
10. Implementar una prueba unitaria del objeto a lección usando al menos un mock."""
    
    
    
  

    
if __name__ == "__main__":
        main()
        
