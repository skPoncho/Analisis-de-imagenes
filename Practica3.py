from PIL import Image
import sys
import math
from statistics import mode 
import matplotlib.pyplot as plt

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


FiltroMediana("imagenb.jpg")
FiltroModa("imagenb.jpg")
FiltroMax("imagenb.jpg")
FiltroMin("imagenb.jpg")