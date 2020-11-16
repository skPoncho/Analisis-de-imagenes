#Funcion MAX y MIN

from PIL import Image
import sys

def Maximo (rutaimagen1, rutaimagen2):
    imagen1 = Image.open(rutaimagen1)
    imagen2 = Image.open(rutaimagen2)
    
    if (imagen1.size != imagen2.size):
        print ("No es posible calcular el maximo de las dos imagenes porque tienen diferentes tamaños")
        sys.exit()
    
    Resultado = Image.new('RGB', imagen2.size)
    imagenaux1 = Image.new('RGB', imagen1.size)
    imagenaux2 = Image.new('RGB', imagen2.size)
   
    datosImg1 = Image.Image.getdata(imagen1)
    datosImg2 = Image.Image.getdata(imagen2)
    
    imagenaux1.putdata(datosImg1)
    imagenaux2.putdata(datosImg2)
    
    ancho,alto = imagen1.size
    for i in range (ancho):
        for j in range (alto):
            r1,g1,b1 = imagenaux1.getpixel((i,j))
            r2,g2,b2 = imagenaux2.getpixel((i,j))
            rr = max(r1, r2)
            gr = max(g1, g2)
            br = max(b1, b2)
            pixel = tuple ([rr,gr,br])
            Resultado.putpixel((i,j),pixel)
    Resultado.show()
    Resultado.save("maximo.jpg")
    Resultado.close()
    
def Minimo (rutaimagen1, rutaimagen2):
    imagen1 = Image.open(rutaimagen1)
    imagen2 = Image.open(rutaimagen2)
    
    if (imagen1.size != imagen2.size):
        print ("No es posible calcular el minimo de las dos imagenes porque tienen diferentes tamaños")
        sys.exit()
    
    Resultado = Image.new('RGB', imagen2.size)
    imagenaux1 = Image.new('RGB', imagen1.size)
    imagenaux2 = Image.new('RGB', imagen2.size)
   
    datosImg1 = Image.Image.getdata(imagen1)
    datosImg2 = Image.Image.getdata(imagen2)
    
    imagenaux1.putdata(datosImg1)
    imagenaux2.putdata(datosImg2)
    
    ancho,alto = imagen1.size
    for i in range (ancho):
        for j in range (alto):
            r1,g1,b1 = imagenaux1.getpixel((i,j))
            r2,g2,b2 = imagenaux2.getpixel((i,j))
            rr = min(r1, r2)
            gr = min(g1, g2)
            br = min(b1, b2)
            pixel = tuple ([rr,gr,br])
            Resultado.putpixel((i,j),pixel)
    Resultado.show()
    Resultado.save("minimo.jpg")
    Resultado.close()

Maximo ("Amazon.jpg" , "Acuarelas.jpg")
Minimo ("Letras.png" , "Acuarelas.jpg")