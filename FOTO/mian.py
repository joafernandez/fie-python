from usuario import Usuario
from publicacion import Foto, Texto, video
from strategy_permiso import Publico, Amigos, Algunos

# Crear usuarios
u1 = Usuario("Joana")
u2 = Usuario("Martín")
u3 = Usuario("Meli")

# Agregar amigos
u1.agregar_amigo(u2)
u1.agregar_amigo(u3)

# Crear publicaciones
foto1 = Foto(100, 200)          # alto=100, ancho=200, factor=0.7 por defecto
texto1 = Texto("Hola, este es mi primer post!")
video1 = video("hd", 120)       # video HD de 120 segundos

# Publicar
u1.agregar_publicacion(foto1)
u1.agregar_publicacion(texto1)
u1.agregar_publicacion(video1)

# Calcular espacio total de publicaciones de u1
espacio_total = sum(p.calcular_espacio() for p in u1.lista_publicaciones)
print("Espacio total usado:", espacio_total, "KB")

# Poner me gusta a una publicación
print("Me gusta foto1:", u2.indicar_me_gusta(foto1))  # Martín da like
print("Me gusta foto1:", u3.indicar_me_gusta(foto1))  # Meli da like

# Ver amigo más popular (el que tiene más me gusta en sus publicaciones)
publicacion_mas_likeada = max(u1.lista_publicaciones, key=lambda p: p.me_gusta)
print("Publicación más popular de Joana tiene:", publicacion_mas_likeada.me_gusta, "me gusta")

# Compartir con estrategias de permiso
print("Permiso Público:", u1.compartir_con(Publico()))
print("Permiso Amigos:", u1.compartir_con(Amigos()))
print("Permiso Algunos:", u1.compartir_con(Algunos()))
