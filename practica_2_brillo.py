
from PIL import Image
import sys
import math
import matplotlib.pyplot as plt

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
    imagen = abrir_imagen(img).convert("L")
    datos = imagen.getdata()#se obtienen las matrices de la imagen
    gmin = 0
    gmax = 0

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

    ecualizacion = [(f_g[datos[x]]) for x in range(len(datos))]#se cambian los valores

    imagen_ecualizacion = crear_imagen('L', imagen.size)

    guardar_imagen(imagen_ecualizacion,ecualizacion,"imagenes/ecualizacion.jpg")#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_ecualizacion)#se cierra la imagen creada
    cerrar_imagen(imagen)
    Histograma_gris("imagenes/ecualizacion.jpg")


def Contraccion(rutaImagen):
    CMAX = 200
    CMIN = 20
    CFmax = CFmin = 0

    imagenA = Image.open(rutaImagen).convert('L')
    imagenC = Image.new('L',imagenA.size)
    pixelImagenA = imagenA.load()
    histogramImagen  = imagenA.histogram()
    lenHistogramaImagenA = len(histogramImagen)
    ancho, alto = imagenA.size

    for x in range(lenHistogramaImagenA):
        if histogramImagen[x] != 0:
            CFmin = x
            break

    for x in range(lenHistogramaImagenA-1, -1, -1):
        if histogramImagen[x] != 0:
            CFmax = x
            break

    for x in range(ancho):
        for y in range(alto):
            try:
                res1 = float(CMAX -CMIN) / float(CFmax - CFmin)
                res3 = math.ceil(((res1) * (pixelImagenA[x,y] - CFmin)) + CMIN)
                imagenC.putpixel((x,y),int(res3))
            except:
                imagenC.putpixel((x,y),CMIN)

    nombre = "imagenes/imagenContraida.jpg"
    imagenC.save(nombre)
    imagenC.show()
    Histograma_gris("imagenes/imagenContraida.jpg")

def ContraccionColor(rutaImagen,num):
    CMAX = 180
    CMIN = 60
    CFmaxR = CFmaxG = CFmaxB = CFminR = CFminG = CFminB = 0

    imagenA = Image.open(rutaImagen)
    imagenC = Image.new('RGB',imagenA.size)
    pixelImagenA = imagenA.load()
    histogramImagen  = imagenA.histogram()
    histogramaR = histogramImagen[0:256]
    histogramaG = histogramImagen[256:512]
    histogramaB = histogramImagen[512:768]
    lenHistogramaImagenA = len(histogramImagen)

    ancho, alto = imagenA.size
    okR =  okG =  okB = True
    for x in range(0,256):
        if histogramaR[x] != 0 and okR:
            CFminR = x
            okR = False
        if histogramaG[x] != 0 and okG:
            CFminG = x
            okG = False
        if histogramaB[x] != 0 and okB:
            CFminB = x
            okB = False
    okR =  okG =  okB = True
    for x in range(255, -1, -1):
        if histogramaR[x] != 0 and okR:
            CFmaxR = x
            okR = False
        if histogramaG[x] != 0 and okG:
            CFmaxG = x
            okG = False
        if histogramaB[x] != 0 and okB:
            CFmaxB= x
            okB = False

    for x in range(ancho):
        for y in range(alto):
            res1R = float(CMAX -CMIN) / float(CFmaxR - CFminR)
            res1G = float(CMAX -CMIN) / float(CFmaxG - CFminG)
            res1B = float(CMAX -CMIN) / float(CFmaxB - CFminB)
            pixelAux = pixelImagenA[x,y]
            pixelR = pixelAux[0]
            pixelG = pixelAux[1]
            pixelB = pixelAux[2]
            res3R = math.ceil(((res1R) * (pixelR - CFminR)) + CMIN)
            res3G = math.ceil(((res1G) * (pixelG - CFminG)) + CMIN)
            res3B = math.ceil(((res1B) * (pixelB - CFminB)) + CMIN)
            pixel = tuple([int(res3R),int(res3G),int(res3B)])
            imagenC.putpixel((x,y),pixel)



    # histogramImagenC  = imagenC.histogram()
    # histogramaRC = histogramImagenC[0:256]
    # histogramaGC = histogramImagenC[256:512]
    # histogramaBC = histogramImagenC[512:768]
    nombre = "imagenContraidaColor_" + str(num)+  ".jpg"
    imagenC.save(nombre)

def Histograma_gris (rutaimagen):
    imagen = Image.open(rutaimagen)
    x = []
    for i in range (256):
        x.append(i)
    H = imagen.histogram()
    y = H[0:256]
    plt.cla()
    plt.plot(x,y)
    plt.show()
def Grises1 (rutaimagen):
   imagen = Image.open(rutaimagen)
   imagenNegativo = Image.new('RGB', imagen.size)
   datosImg = Image.Image.getdata(imagen)
   imagenNegativo.putdata(datosImg)
   ancho,alto = imagen.size
   for i in range (ancho):
       for j in range (alto):
           r,g,b = imagenNegativo.getpixel((i,j))
           prom = (r + g + b) // 3
           pixel = tuple ([prom,prom,prom])
           imagenNegativo.putpixel((i,j),pixel)
   imagenNegativo.save("foto_grises1.jpg")
   #imagenNegativo.show()
   #imagenNegativo.close()
   return imagenNegativo

def DesplazamientoGris(rutaimagen,desplazamiento):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L', imagen.size)

    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            ng = imagen.getpixel((i,j))
            NG = ng + desplazamiento
            if (NG > 255):
                NG = 255
            if (NG < 0):
                NG = 0
            imgResultado.putpixel((i,j),NG)
    imgResultado.save("imagenes/Desplazamiento.jpg")
    imgResultado.show()
    Histograma_gris("imagenes/Desplazamiento.jpg")
    #imgResultado.close()
    return imgResultado

def ExpansionGris(rutaimagen):
    #imagen = Grises1(rutaimagen)
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)

    MAX = 0
    MIN = 255
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            r = imagen.getpixel((i,j))
            if (r < MIN):
                MIN = r
            if (r > MAX):
                MAX = r

    for i in range (ancho):
        for j in range (alto):
            r = imagen.getpixel((i,j))
            P = round ((r/255)*(MAX-MIN) + MIN)
            imgResultado.putpixel((i,j),P)
    imgResultado.save("imagenes/Expansion.jpg")
    return imgResultado

def Histograma_gris (rutaimagen):
    imagen = Image.open(rutaimagen)
    x = []
    for i in range (256):
        x.append(i)
    H = imagen.histogram()
    y = H[0:256]
    plt.cla()
    plt.plot(x,y)
    plt.show()



#Contraccion("imagenes/img_gris.jpg")#paso 1
#im3 = DesplazamientoGris("imagenes/imagenContraida.jpg",30)#paso 2
#ecualizacion("imagenes/Desplazamiento.jpg")#paso 3
im3 = DesplazamientoGris("imagenes/ecualizacion.jpg",-20)#paso 4
#Histograma_gris("imagenes/imagenContraida_1.jpg")
