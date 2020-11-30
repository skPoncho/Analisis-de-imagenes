from PIL import Image

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

def Desplazamiento(rutaimagen,desplazamiento):
    imagen = Image.open(rutaimagen)     
    imgResultado = Image.new('RGB', imagen.size)      

    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            r,g,b = imagen.getpixel((i,j))
            R = r + desplazamiento
            G = g + desplazamiento
            B = b + desplazamiento
            if (R > 255):
                R = 255
            if (R < 0):
                R = 0
            if (G > 255):
                G = 255
            if (G < 0):
                G = 0
            if (B > 255):
                B = 255
            if (B < 0):
                B = 0
            pixel = tuple ([R,G,B])
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Desplazamiento.jpg")
    #imgResultado.show()
    #imgResultado.close()
    return imgResultado
    
def Expansion(rutaimagen):    
    #imagen = Grises1(rutaimagen)
    imagen = Image.open(rutaimagen)
    imgResultado = Image.new('RGB',imagen.size)
    
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
            pixel = tuple ([P, P, P])            
            imgResultado.putpixel((i,j),pixel)
    imgResultado.save("Espansion.jpg")
    return imgResultado
        
im3 = Expansion("Frutas.png")
im3.show()
