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

def ecualizacion(img):#obtiene la ecualizacion en escala de grises
    imagen = Image.open(img).convert("L")
    histogramImagen  = imagen.histogram()
    datos = imagen.getdata()#se obtienen las matrices de la imagen
    gmin = 0
    gmax = 0
    print("histograma imagen original ")
    print(histogramImagen)

    pg_g = [0]
    ecualizacion = []
    f_g = []
    n_g = imagen.histogram()#SE SACAN los valores de gris

    cant_datos = len(datos)
    p_g = [(n_g[x-1]/cant_datos) for x in range(1,257)]#se saca la probabilidad

    for x in range(len(p_g)):#probabilidad acumulada
        if(x==0):
            pg_g[0] = p_g[0]
        else:
            valor = round(pg_g[x-1]+p_g[x],4)
            if(valor > .999 ):
                valor = 1
            pg_g.append(valor)

    for x in range(len(n_g)):#se busca gmin
        if(n_g[x] != 0):
            gmin = x
            break
    for x in range(255,-1,-1):#se busca gmax
        if(n_g[x] != 0):
            gmax = x
            break
    resta_cubos = (gmax**(1/3))-(gmin**(1/3))

    for x in range(0,256):
        valor = (resta_cubos * pg_g[x]+(gmin**(1/3)))**3
        f_g.append(valor)

    ecualizacion = [(f_g[datos[x]]) for x in range(len(datos))]

    imagen_ecualizacion = Image.new('L', imagen.size)
    #imagen_ecualizacion = crear_imagen('L', imagen.size)

    #guardar_imagen(imagen_ecualizacion,ecualizacion,"imagenes/ecualizacion_img.jpg")#se guardan los datos de la imagen nueva
    imagen_ecualizacion.putdata(ecualizacion)
    imagen_ecualizacion.save("imagenes/ecualizacion_img.jpg")
    imagen_ecualizacion.show()

    histogramImagen  = imagen_ecualizacion.histogram()
    print("histograma imagen procesada ")
    print(histogramImagen)

    cerrar_imagen(imagen_ecualizacion)#se cierra la imagen creada
    cerrar_imagen(imagen)
ecualizacion("imagenes/prueba.jpg")
