# Carlos Alfonso Barrón Rivera 2019630166
from PIL import Image

def abrir_imagen(ruta):
    imagen = Image.open(ruta)
    return imagen

def cerrar_imagen(imagen):
    imagen.close()

def crear_imagen(tipo_imagen,tamanio):
    nueva_imagen = Image.new(tipo_imagen, tamanio)
    return nueva_imagen

def guardar_imagen(imagen,datos,nombre_imagen):
    imagen.putdata(datos)
    imagen.save(nombre_imagen)

def escala_de_grises(img_inicial,img_grises):#obtiene una imagen en escala de grises a partir de una imagen RGB

    imagen = abrir_imagen(img_inicial)#se abre la imagen inicial

    datos = imagen.getdata()#se obtienen las matrices de la imagen

    nivel_gris = [(datos[x][0] + datos[x][1] + datos[x][2]) // 3 for x in range(len(datos))]#se hace el promedio de los 3 canales en numero entero

    imagen_gris = crear_imagen('L', imagen.size)#se indica que es una imagen en escala de grises del tamaño de la imagen inicial

    guardar_imagen(imagen_gris,nivel_gris,img_grises)#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_gris)#se cierra la imagen creada
    cerrar_imagen(imagen)#se cierra la imagen


def negativo_RGB(img_inicial,nombre_img_negativo):#obtiene el negativo de de la imagen deseada tipo RGB

    imagen = abrir_imagen(img_inicial)#se abre la imagen inicial
    datos = list(imagen.getdata())#se obtienen las matrices de la imagen

    datos_invertidos = [(255 - datos[x][0], 255 - datos[x][1], 255 - datos[x][2]) for x in range(len(datos))]#se hace la resta de 255 menos el valor de cada pixel para obtener su negativo

    imagen_invertida = crear_imagen('RGB', imagen.size)#se indica que es una imagen en rgb del tamaño de la imagen inicial

    guardar_imagen(imagen_invertida,datos_invertidos,nombre_img_negativo)#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_invertida)#se cierra la imagen creada
    cerrar_imagen(imagen)#se cierra la imagen

def negativo_de_escala_grises(img_inicial,nombre_img_negativo):#obtiene el negativo de de la imagen deseada tipo escala de grises

    imagen = abrir_imagen(img_inicial)#se abre la imagen inicial
    datos = imagen.getdata()

    datos_invertidos = [255 - x for x in datos]

    imagen_invertida = crear_imagen('L', imagen.size)#se indica que es una imagen en rgb del tamaño de la imagen inicial

    guardar_imagen(imagen_invertida,datos_invertidos,nombre_img_negativo)#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_invertida)#se cierra la imagen creada
    cerrar_imagen(imagen)#se cierra la imagen

def negativo_de_binaria(img_inicial,img_negativa_binaria):

    imagen = abrir_imagen(img_inicial)#se abre la imagen inicial
    datos = imagen.getdata()

    datos_invertidos = [1 - x for x in datos]

    imagen_invertida = crear_imagen('1', imagen.size)#se indica que es una imagen en rgb del tamaño de la imagen inicial

    guardar_imagen(imagen_invertida,datos_invertidos,img_negativa_binaria)#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_invertida)#se cierra la imagen creada
    cerrar_imagen(imagen)#se cierra la imagen

escala_de_grises('foto_perfil.jpg','foto_perfil_grises.jpg')
negativo_RGB("foto_perfil.jpg","foto_perfil_negativa.jpg")
negativo_de_escala_grises("foto_perfil_grises.jpg","foto_perfil_grises_negativo.jpg")
negativo_de_binaria("imagen_binaria.jpg","negativa_binaria.jpg")
