from PIL import Image
import sys
import math
import matplotlib.pyplot as plt

#Entradas: coordenadas del pixel (i, j) y la imagen
#Salida: Un arreglo con los valores de la vecindad del pixel
def ObtenerVecindad8 (i, j, img):
    V = []
    try:
        V.append(img.getpixel((i-1,j-1)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i,j-1)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i+1,j-1)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i-1,j)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i,j)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i+1,j)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i-1,j+1)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i,j+1)))
    except:
        V.append(0)
    try:
        V.append(img.getpixel((i+1,j+1)))
    except:
        V.append(0)
    return V

def FiltropromG(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            for z in range (8):
                g = g + V[z]
            g = g // 9
            imgResultado.putpixel((i,j),g)
    imgResultado.save("FPG.jpg")
    return imgResultado

def FiltropromC(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            for z in range (len(V)):
                r = r + V[z][0]
                g = g + V[z][1]
                b = b + V[z][2]
            r = r // 9
            g = g // 9
            b = b // 9
            pixel = tuple([r,g,b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("FPC.jpg")
    return imgResultado

def FiltropromestandarpesadoG(rutaimagen, N):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            for z in range (8):
                g = g + V[z]
            g = (V[4]* N-1) + g
            g = g // (N + 8)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("FPEPG.jpg")
    return imgResultado

def FiltropromestandarpesadoC(rutaimagen, N):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            for z in range (8):
                r = r + V[z][0]
                g = g + V[z][1]
                b = b + V[z][2]
            r = (V[4][0]* N-1) + r
            g = (V[4][1]* N-1) + g
            b = (V[4][2]* N-1) + g
            r = r // (N + 8)
            g = g // (N + 8)
            b = b // (N + 8)
            pixel = tuple ([r, g, b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("FPEPC.jpg")
    return imgResultado


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

def FiltroMax(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            g = max(V)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Max.jpg")
    return imgResultado

def FiltroMin(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            g = min(V)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Min.jpg")
    return imgResultado

def FiltroMediana(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            Vo = sorted(V)
            g = Vo[4]
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Mediana.jpg")
    return imgResultado

#imagen = Image.open("Acuarelas.jpg")
#Aux = ObtenerVecindad8(60, 50, imagen)
#print (Aux[0][2] + 5)
