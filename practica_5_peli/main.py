

# ================== main.py ==================
from complejo import Complejo
from sala import Sala
from pelicula import ClaseZ, Terror, Bizarra, Ultraviolenta
from persona import Persona
from tipo_espectador import EspectadorNormal, EspectadorCinefilo, EspectadorFanatico


def main():
    # Crear complejo
    complejo = Complejo()
    
    # Crear salas
    sala1 = Sala("Sala 1")
    sala2 = Sala("Sala 2")
    complejo.agregar_sala(sala1)
    complejo.agregar_sala(sala2)
    
    # Crear películas
    pelicula_z = ClaseZ("Zombies del Espacio", duracion_minutos=30)
    pelicula_terror = Terror("La Casa Maldita", duracion_minutos=60)
    pelicula_bizarra = Bizarra("El Hombre Lagartija", duracion_minutos=45)
    pelicula_ultraviolenta = Ultraviolenta("Masacre en el Bosque", duracion_minutos=50)
    
    # Agregar películas a salas
    sala1.agregar_pelicula(pelicula_z)
    sala1.agregar_pelicula(pelicula_terror)
    
    sala2.agregar_pelicula(pelicula_bizarra)
    sala2.agregar_pelicula(pelicula_ultraviolenta)
    
    # Crear personas
    juan = Persona("Juan", tolerancia=100)
    maria = Persona("Maria", tolerancia=80)
    pedro = Persona("Pedro", tolerancia=150)
    laura = Persona("Laura", tolerancia=50)
    
    
    # ==================== PUNTO 1 ====================
    print("="*60)
    print("PUNTO 1: Verificar si le conviene comprar entrada")
    print("="*60)
    
    conviene_juan = juan.le_conviene_sala(sala1)
    print(f"¿A {juan.nombre} le conviene comprar entrada para {sala1.nombre}? {conviene_juan}")
    print(f"  Duración total: {sala1.calcular_duracion_total()} minutos")
    print(f"  Personas en sala: {sala1.contar_personas()}")
    
    
    # ==================== PUNTO 2 ====================
    print("\n" + "="*60)
    print("PUNTO 2: Comprar entrada")
    print("="*60)
    
    juan.comprar_entrada(sala1)
    maria.comprar_entrada(sala1)
    pedro.comprar_entrada(sala1)
    laura.comprar_entrada(sala2)
    
    print(f"Personas en {sala1.nombre}: {sala1.contar_personas()}")
    print("  Espectadores:")
    for persona in sala1.personas:
        print(f"    - {persona.nombre} (tolerancia: {persona.tolerancia})")
    
    
    # ==================== PUNTO 3 ====================
    print("\n" + "="*60)
    print("PUNTO 3: Proyectar película")
    print("="*60)
    
    print(f"\nProyectando '{pelicula_terror.titulo}' en {sala1.nombre}")
    print("Antes de proyectar:")
    for persona in sala1.personas:
        print(f"  {persona.nombre}: tolerancia = {persona.tolerancia}")
    
    sala1.proyectar_pelicula(pelicula_terror)
    
    print("\nDespués de proyectar:")
    for persona in sala1.personas:
        print(f"  {persona.nombre}: tolerancia = {persona.tolerancia}")
    print(f"Personas que quedaron: {sala1.contar_personas()}")
    
    
    # ==================== PUNTO 4 ====================
    print("\n" + "="*60)
    print("PUNTO 4: Convertir espectador en cinéfilo")
    print("="*60)
    
    if len(sala1.personas) > 0:
        persona_convertir = sala1.personas[0]
        print(f"Convirtiendo a {persona_convertir.nombre} en cinéfilo")
        persona_convertir.cambiar_tipo_espectador(EspectadorCinefilo())
        print(f"  Tipo anterior: Normal")
        print(f"  Tipo actual: Cinéfilo (sentirá mitad del rechazo)")
    
    
    # ==================== PUNTO 5 ====================
    print("\n" + "="*60)
    print("PUNTO 5: Consultas")
    print("="*60)
    
    # 5a. Películas ordenadas por duración
    print(f"\n5a. Películas de {sala1.nombre} (mayor a menor duración):")
    peliculas_ordenadas = sala1.obtener_peliculas_ordenadas()
    for pelicula in peliculas_ordenadas:
        print(f"  - {pelicula.titulo}: {pelicula.duracion_minutos} minutos")
    
    # 5b. Tolerancia promedio del complejo
    tolerancia_promedio = complejo.calcular_tolerancia_promedio()
    print(f"\n5b. Tolerancia promedio del complejo: {tolerancia_promedio:.2f} puntos")
    
    # 5c. Salas sangrientas
    print(f"\n5c. Salas sangrientas:")
    salas_sangrientas = complejo.obtener_salas_sangrientas()
    for sala in salas_sangrientas:
        print(f"  - {sala.nombre}")
    
    
    # ==================== PUNTO 6 ====================
    print("\n" + "="*60)
    print("PUNTO 6: Película ultraviolenta")
    print("="*60)
    
    # Crear sala nueva con personas para probar
    sala3 = Sala("Sala 3")
    complejo.agregar_sala(sala3)
    
    pelicula_ultra = Ultraviolenta("Gore Extremo", duracion_minutos=40)
    sala3.agregar_pelicula(pelicula_ultra)
    
    # Agregar personas nuevas
    carlos = Persona("Carlos", tolerancia=200)
    ana = Persona("Ana", tolerancia=180)
    sala3.agregar_persona(carlos)
    sala3.agregar_persona(ana)
    
    print(f"Película ultraviolenta: {pelicula_ultra.titulo}")
    print(f"  Duración: {pelicula_ultra.duracion_minutos} minutos")
    
    rechazo_ultra = pelicula_ultra.calcular_rechazo_base(sala3)
    rechazo_terror_normal = Terror("Terror normal", 40).calcular_rechazo_base(sala3)
    
    print(f"  Rechazo terror normal (40 min): {rechazo_terror_normal} puntos")
    print(f"  Rechazo ultraviolenta: {rechazo_ultra} puntos (doble)")
    
    print(f"\nProyectando película ultraviolenta:")
    print("Antes:")
    for persona in sala3.personas:
        print(f"  {persona.nombre}: tolerancia = {persona.tolerancia}")
    
    sala3.proyectar_pelicula(pelicula_ultra)
    
    print("\nDespués:")
    for persona in sala3.personas:
        print(f"  {persona.nombre}: tolerancia = {persona.tolerancia}")


if __name__ == "__main__":
    main()


"""
===============================================================================
📚 EXPLICACIÓN POR CLASE
===============================================================================

📌 Clase Pelicula (abstracta):
   Tiene 4 tipos (ClaseZ, Terror, Bizarra, Ultraviolenta). Cada una calcula 
   su rechazo base de forma diferente. Conoce su título y duración.

📌 Clase ClaseZ:
   Es una película que produce rechazo fijo de 2 puntos.

📌 Clase Terror:
   Es una película que produce 3 puntos de rechazo cada 5 minutos de duración.

📌 Clase Bizarra:
   Es una película que produce rechazo igual a la cantidad de personas en la sala.

📌 Clase Ultraviolenta:
   Es una película que hereda de Terror pero duplica el rechazo (tira chorros 
   de sangre cada 15 minutos).

📌 Clase TipoEspectador (abstracta - STRATEGY):
   Tiene 3 tipos (Normal, Cinéfilo, Fanático). Cada uno modifica el rechazo 
   de forma diferente según cómo lo sienten.

📌 Clase EspectadorNormal:
   Estrategia que siente el rechazo completo sin modificar.

📌 Clase EspectadorCinefilo:
   Estrategia que siente la mitad del rechazo.

📌 Clase EspectadorFanatico:
   Estrategia que solo siente rechazo si la película produce más de 30 puntos.

📌 Clase Persona:
   Es el espectador. Tiene nombre, tolerancia y un tipo de espectador (estrategia). 
   Puede verificar si le conviene una sala, comprar entrada, ver películas 
   (disminuye tolerancia) y saber si debe retirarse.

📌 Clase Sala:
   Tiene películas y personas. Puede proyectar películas (afecta tolerancia de 
   personas y retira a los que llegan a cero), calcular duración total, ordenar 
   películas por duración y saber si es sangrienta.

📌 Clase Complejo:
   Tiene varias salas. Puede calcular tolerancia promedio de todas las personas 
   y devolver las salas sangrientas.


===============================================================================
🎨 PATRONES Y DISEÑO APLICADOS
===============================================================================

✅ HERENCIA:
   ClaseZ, Terror, Bizarra y Ultraviolenta heredan de Pelicula porque calculan 
   rechazo diferente. EspectadorNormal, Cinéfilo y Fanático heredan de 
   TipoEspectador porque modifican rechazo diferente. Ultraviolenta hereda de 
   Terror porque es un tipo especial de terror.

✅ COMPOSICIÓN:
   Persona TIENE un TipoEspectador (estrategia que puede cambiar). Sala TIENE 
   películas y personas (listas). Complejo TIENE salas (lista). Son relaciones 
   "tener", no "ser".

✅ STRATEGY:
   Se usa para TipoEspectador (Normal/Cinéfilo/Fanático modifican rechazo 
   diferente). Persona puede cambiar su estrategia en cualquier momento sin 
   cambiar de clase. Evita IFs preguntando "qué tipo de espectador sos".

❌ DECORATOR:
   No se usó en este ejercicio (no había extras opcionales para agregar).

===============================================================================
"""
