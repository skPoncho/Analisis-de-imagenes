import random
from PIL import Image

def ruido(imagen, porcentaje):

    tamaño=imagen.size[0]*imagen.size[1]
    auxiliar=(tamaño*porcentaje)//800

    if imagen.mode=='RGB':
        dato_minimo=(0, 0, 0)
        dato_maximo=(255, 255, 255)

    elif imagen.mode=='L':
        dato_minimo=0
        dato_maximo=255

    #pixeles blancos
    for x in range(auxiliar):

        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)

        imagen.putpixel((coordenada_x, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_maximo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_maximo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_maximo)

    #pixeles negros
    for x in range(auxiliar):

        coordenada_x=random.randrange(2, imagen.width-2)
        coordenada_y=random.randrange(2, imagen.height-2)

        imagen.putpixel((coordenada_x, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y), dato_minimo)
        imagen.putpixel((coordenada_x, coordenada_y+1), dato_minimo)
        imagen.putpixel((coordenada_x+1, coordenada_y+1), dato_minimo)

    return None

foto=Image.open('imagenes/foto_escala_grises.jpg')

#llamado a la funcion pasando como parametro la imagen y el
#porcentaje de ruido deseado
ruido(foto, 2)

foto.save('imagenes/foto_escala_grises_ruido.jpg')
foto.close()
