from PIL import Image
import sys
import math
from statistics import mode
import matplotlib.pyplot as plt

#Entradas: coordenadas del pixel (i, j) y la imagen
#Salida: Un arreglo con los valores de la vecindad del pixel
def ObtenerVecindad8(i, j, img):
    V = []
    for x in range (i-1, i+2):
        for y in range (j-1, j+2):
            try:
                V.append(img.getpixel((x,y)))
            except:
                if (img.mode != 'L'):
                    V.append((0,0,0))
                else:
                    V.append(0)
    return V

def ObtenerVecindad58(i, j, img): #Vecindad 5x5
    V = []
    for x in range (i-2, i+3):
        for y in range (j-2, j+3):
            try:
                V.append(img.getpixel((x,y)))
            except:
                if (img.mode != 'L'):
                    V.append((0,0,0))
                else:
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
            Li = ObtenerVecindad8(i, j, imagen)
            for z in range (len(Li)):
                r = r + Li[z][0]
                g = g + Li[z][1]
                b = b + Li[z][2]
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

def FiltroGaussianoC3(rutaimagen):
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
def FiltroGaussianoC3(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    g0 = 0
    g1 = 0
    g2 = 0

    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            g0 = (V[0][0] + V[2][0] + V[6][0] + V[8][0] + ((V[1][0] + V[3][0] + V[5][0] + V[7][0])*2) + V[4][0])//16
            g1 = (V[0][1] + V[2][1] + V[6][1] + V[8][1] + ((V[1][1] + V[3][1] + V[5][1] + V[7][1])*2) + V[4][1])//16
            g2 = (V[0][2] + V[2][2] + V[6][2] + V[8][2] + ((V[1][2] + V[3][2] + V[5][2] + V[7][2])*2) + V[4][2])//16

            pixel = tuple ([g0,g1,g2])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Gauss_rgb.jpg")
    return imgResultado
def FiltroGaussianoG5(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad58(i, j, imagen)
            g = V[0] + V[4] + V[20] + V[24] + ((V[1] + V[5] + V[3] + V[9] + V[15] + V[21] + V[19] + V[23])*4) + ((V[2] + V[14] + V[22] + V[10])*6) + ((V[6] + V[16] + V[18] + V[8])*16) + ((V[7] + V[11] + V[17] + V[13])*24) + (V[12]*36)
            g = g // 246
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Gauss5.jpg")
    return imgResultado

def FiltroGaussianoC5(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad58(i, j, imagen)
            r = V[0][0] + V[4][0] + V[20][0] + V[24][0] + ((V[1][0] + V[5][0] + V[3][0] + V[9][0] + V[15][0] + V[21][0] + V[19][0] + V[23][0])*4) + ((V[2][0] + V[14][0] + V[22][0] + V[10][0])*6) + ((V[6][0] + V[16][0] + V[18][0] + V[8][0])*16) + ((V[7][0] + V[11][0] + V[17][0] + V[13][0])*24) + (V[12][0]*36)
            g = V[0][1] + V[4][1] + V[20][1] + V[24][1] + ((V[1][1] + V[5][1] + V[3][1] + V[9][1] + V[15][1] + V[21][1] + V[19][1] + V[23][1])*4) + ((V[2][1] + V[14][1] + V[22][1] + V[10][1])*6) + ((V[6][1] + V[16][1] + V[18][1] + V[8][1])*16) + ((V[7][1] + V[11][1] + V[17][1] + V[13][1])*24) + (V[12][1]*36)
            b = V[0][2] + V[4][2] + V[20][2] + V[24][2] + ((V[1][2] + V[5][2] + V[3][2] + V[9][2] + V[15][2] + V[21][2] + V[19][2] + V[23][2])*4) + ((V[2][2] + V[14][2] + V[22][2] + V[10][2])*6) + ((V[6][2] + V[16][2] + V[18][2] + V[8][2])*16) + ((V[7][2] + V[11][2] + V[17][2] + V[13][2])*24) + (V[12][2]*36)
            r = r // 246
            g = g // 246
            b = b // 246
            pixel = tuple ([r, g, b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Gauss5.jpg")
    return imgResultado

def FiltroMaxG(rutaimagen):
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
    imgResultado.save("Max2.jpg")
    return imgResultado

def FiltroMaxC(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            r = max(V)
            g = max(V)
            b = max(V)
            pixel = tuple([r,g,b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Max2.jpg")
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
    imgResultado.save("Min2.jpg")
    return imgResultado

def FiltroMinC(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            r = min(V)
            g = min(V)
            b = min(V)
            pixel = tuple([r,g,b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Min2.jpg")
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
    imgResultado.save("Mediana2.jpg")
    return imgResultado

def FiltroMedianaC(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            Vo = sorted(V)
            r = Vo[4]
            g = Vo[4]
            b = Vo[4]
            pixeñ = tuple([r,g,b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Mediana2.jpg")
    return imgResultado

def FiltroModa(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            try:
                g = mode(V)
            except:
                g = V[4]
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Moda2.jpg")
    return imgResultado

def FiltroModa(rutaimagen):
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    ancho,alto = imagen.size
    r = 0
    g = 0
    b = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            try:
                r = mode(V)
            except:
                r = V[4]
            try:
                g = mode(V)
            except:
                g = V[4]
            try:
                b = mode(V)
            except:
                b = V[4]
            pixel = tuple([r,g,b])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Moda2.jpg")
    return imgResultado
FiltroMediana("imagenes/foto_escala_grises.jpg")    
#imagen = Image.open("Gris.jpg")
#Aux = ObtenerVecindad58(0,0, imagen)
#print (Aux)
#print (imagen.dtype())
