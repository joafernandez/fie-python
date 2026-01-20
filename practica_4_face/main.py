from usuario import Usuario
from publicacion import Foto, Texto, Video,HD,Normal
from estrategia_permiso import Publico, Algunos,Amigos



def main():
    #usuarios
    U1=Usuario("joana")
    U2=Usuario("romina")
    U3=Usuario("brenda")
    U4=Usuario("franco")
    U_desconocido=Usuario("nn")
    
    #amigos de joana 
    U1.agregar_amigo(U2)
    U1.agregar_amigo(U3)
    U1.agregar_amigo(U4)
    
    #estartegias de permiso
    E1=Publico()
    E2=Algunos()
    E3=Amigos()
       
    
    #publicacion 
    foto1=Foto(100,70,E1)
    foto2=Foto(300,50,E3)
    texto=Texto("HOLA",E3)
    
    
    
    #publicacion de joana
    U1.publicar(foto1)
    U1.publicar(foto2)
    U1.publicar(texto)
    
    print("===========================PUNTO 1=================================================================")
    
    print(f" EL ESPACIO TOTALL ES:{U1.espacio_total_publicacion()}")
    
    print("===========================PUNTO 2================================================================")
    
    lista_mejores_amigos=U1.obtener_mejores_amigos()
    
    print(f"Los mejores amigos de joana son:")
    for amigo in lista_mejores_amigos:
            print(f"  - {amigo.nombre}")
            
            
 # PUNTO 3
print("="*60)
print("PUNTO 3: Amigo más popular")
print("="*60)

# Usar las estrategias ya creadas (Publico, Amigos, Algunos)
foto_romina = Foto(100, 80, Publico())  # ✅ Crear nueva instancia
foto_romina.me_gusta = 50
U2.publicar(foto_romina)

foto_brenda = Foto(150, 100, Publico())
foto_brenda.me_gusta = 100
U3.publicar(foto_brenda)

popular = U1.amigo_popular()
print(f"Amigo más popular: {popular.nombre}")


# PUNTO 4
print("\n" + "="*60)
print("PUNTO 4: Video solo para amigos")
print("="*60)

video_amigos = Video(Normal(), 180, Amigos())  # ✅ Crear instancias nuevas
U1.publicar(video_amigos)

print(f"Video publicado. ¿Romina puede verlo? {video_amigos.ver_publicacion(U2, U1)}")
print(f"¿Desconocido puede verlo? {video_amigos.ver_publicacion(U_desconocido, U1)}")

    
    

if __name__ == "__main__":
    main()
