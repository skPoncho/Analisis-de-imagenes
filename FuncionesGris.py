from PIL import Image
import matplotlib.pyplot as plt

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
    imgResultado.save("Desplazamiento.jpg")
    #imgResultado.show()
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
    imgResultado.save("Expansion.jpg")
    return imgResultado