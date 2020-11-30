from PIL import Image
import sys
import math
import matplotlib.pyplot as plt

def Contraccion(rutaImagen,num):
    CMAX = 180
    CMIN = 60
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
    nombre = "imagenContraida_" + str(num)+  ".png"
    imagenC.save(nombre)

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
    nombre = "imagenContraidaColor_" + str(num)+  ".png"
    imagenC.save(nombre)

#Contraccion("imagenA.png")
#Contraccion("imagenAC.png",1)
ContraccionColor("imagenAC.png",1)