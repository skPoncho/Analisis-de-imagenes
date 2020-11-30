# Carlos Alfonso Barrón Rivera 2019630166
from PIL import Image
import sys

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
    imagen.show()

def ecualizacion(img):#obtiene la ecualizacion en escala de grises
    imagen = abrir_imagen(img)#se abre la imagen inicial
    histogramImagen  = imagen.histogram()
    datos = imagen.getdata()#se obtienen las matrices de la imagen


    n_g = [256]
    pg_g = [256]
    ecualizacion = []
    n_g = imagen.histogram()#SE SACAN

    #for x in range(1,256):
        #contador = 0
        #for y in range(len(datos)):
            #if(datos[y] == x):
                #contador = contador + 1
        #n_g.append(contador)


    cant_datos = len(datos)

    p_g = [(n_g[x-1]/cant_datos) for x in range(1,256)]

    for x in range(len(p_g)):
        if(x==0):
            pg_g[0] = p_g[0]
        else:
            valor = round(pg_g[x-1]+p_g[x],4)
            if(valor > .999 ):
                valor = 1
            pg_g.append(valor)


    ecualizacion = [((6.34133*pg_g[x])**(1/3)) for x in range(len(pg_g))]


    imagen_ecualizacion = crear_imagen('L', imagen.size)

    guardar_imagen(imagen_ecualizacion,ecualizacion,"imagenes/ecualizacion_img.jpg")#se guardan los datos de la imagen nueva

    histogramImagen  = imagen_ecualizacion.histogram()
    for x in range(len(histogramImagen)):
        print("valor en  : "+str(x)+" es : "+str(histogramImagen[x]))

    cerrar_imagen(imagen_ecualizacion)#se cierra la imagen creada
    cerrar_imagen(imagen)
ecualizacion("imagenes/foto_escala_grises.jpg")
