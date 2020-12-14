# Carlos Alfonso Barrón Rivera 2019630166
from PIL import Image
import sys
import math
import matplotlib.pyplot as plt

def ObtenerVecindad8 (i, j, img):
    V = []
    try:
        V.append(img.getpixel((i-1,j-1)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i,j-1)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i+1,j-1)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i-1,j)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i,j)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i+1,j)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i-1,j+1)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i,j+1)))
    except:
        V.append((0, 0, 0))
    try:
        V.append(img.getpixel((i+1,j+1)))
    except:
        V.append((0, 0, 0))
    return V

def FiltroGaussianoG(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            g = V[0] + V[2] + V[6] + V[8] + ((V[1] + V[3] + V[5] + V[7])*2) + V[4]
            g = g // 16
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Gauss.jpg")
    return imgResultado


def FiltroGaussiano_rgb(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    g0 = 0
    g1 = 0
    g2 = 0
    # for x in range (3):
    #     print("hola")
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)

            g0 = (V[0][0] + V[2][0] + V[6][0] + V[8][0] + ((V[1][0] + V[3][0] + V[5][0] + V[7][0])*2) + V[4][0])//16


            g1 = (V[0][1] + V[2][1] + V[6][1] + V[8][1] + ((V[1][1] + V[3][1] + V[5][1] + V[7][1])*2) + V[4][1])//16

            g2 = (V[0][2] + V[2][2] + V[6][2] + V[8][2] + ((V[1][2] + V[3][2] + V[5][2] + V[7][2])*2) + V[4][2])//16
            #print(" R : "+str(g0)+" G : "+str(g1)+" B : "+str(g2))
            pixel = tuple ([g0,g1,g2])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Gauss_rgb.jpg")
    return imgResultado
FiltroGaussiano_rgb("imagenes/montanas.jpg")
