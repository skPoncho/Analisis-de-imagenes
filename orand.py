#OR and AND de imageA - imagenB

from PIL import Image
import sys

def ImagenNivelGrisOR(rutaImagenA,rutaImagenB):
    Ma = 255
    Mi = 0
    M = 0
    m = 255
    imagenA = Image.open(rutaImagenA).convert('L')
    imagenB = Image.open(rutaImagenB).convert('L')

    anchom,alto = imagenA.size

    imagenT = Image.new('L',imagenA.size)
    imagenC = Image.new('L',imagenA.size)

    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            imagenT.putpixel((x,y),pixelAR | pixelBR)
    
    pixelImagenT = imagenT.load()
    for x in range(anchom):
        for y in range(alto):
            aux = pixelImagenT[x,y]
            if aux > M:
                M = aux
    
    for x in range(anchom):
        for y in range(alto):
            aux = pixelImagenT[x,y]
            if aux < m:
                m = aux
    
    for x in range(anchom):
        for y in range(alto):
            aux = (((pixelImagenT[x,y] - m) / (M - m)) * (Ma - Mi))
            imagenC.putpixel((x,y),aux)

    imagenC.show()
    imagenC.save("ImagenC_BN_OR.png")            
    
def ImagenNivelGrisAND(rutaImagenA,rutaImagenB):
    imagenA = Image.open(rutaImagenA).convert('L')
    imagenB = Image.open(rutaImagenB).convert('L')

    anchom,alto = imagenA.size

    imagenC = Image.new('L',imagenA.size)

    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            imagenC.putpixel((x,y),pixelAR & pixelBR)
    
    imagenC.show()
    imagenC.save("ImagenC_BN_AND.png")

def ImagenColorOR(rutaImagenA,rutaImagenB):
    Ma = 255
    Mi = 0
    MR = 0
    MG = 0
    MB = 0
    mR = 255
    mG = 255
    mB = 255
    imagenA = Image.open(rutaImagenA)
    imagenB = Image.open(rutaImagenB)

    anchom,alto = imagenA.size

    imagenT = Image.new('RGB',imagenA.size)
    imagenC = Image.new('RGB',imagenA.size)

    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            pixelAR0 = pixelAR[0]
            pixelAR1 = pixelAR[1]
            pixelAR2 = pixelAR[2]
            pixelBR0 = pixelBR[0]
            pixelBR1 = pixelBR[1]
            pixelBR2 = pixelBR[2]
            p0 = pixelAR0 | pixelBR0
            p1 = pixelAR1 | pixelBR1
            p2 = pixelAR2 | pixelAR2
            pixel = tuple([p0,p1,p2])
            imagenT.putpixel((x,y),pixel)

    pixelImagenT = imagenT.load()
    for x in range(anchom):
        for y in range(alto):
            aux = pixelImagenT[x,y]
            r = aux[0]
            g = aux[1]
            b = aux[2]
            if r > MR : MR = r
            if g > MG : MG = g
            if b > MB : MB = b
    
    for x in range(anchom):
        for y in range(alto):
            aux = pixelImagenT[x,y]
            r = aux[0]
            g = aux[1]
            b = aux[2]
            if r < mR : mR = r
            if g < mG : mG = g
            if b < mB : mB = b
    
    for x in range(anchom):
        for y in range(alto):
            pixelT = pixelImagenT[x,y]
            p0 = pixelT[0]
            p1 = pixelT[1]
            p2 = pixelT[2]
            auxR = (((p0 - mR) / (MR - mR)) * (Ma - Mi))
            auxG = (((p1 - mG) / (MG - mG)) * (Ma - Mi))
            auxB = (((p2 - mB) / (MB - mB)) * (Ma - Mi))
            aux = tuple([auxR,auxG,auxB])
            imagenC.putpixel((x,y),aux)
    
    imagenC.show()
    imagenC.save("ImagenC_C_OR.png")  

def ImagenColorAND(rutaImagenA,rutaImagenB):
    imagenA = Image.open(rutaImagenA)
    imagenB = Image.open(rutaImagenB)

    anchom,alto = imagenA.size

    imagenC = Image.new('RGB',imagenA.size)

    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            pixelAR0 = pixelAR[0]
            pixelAR1 = pixelAR[1]
            pixelAR2 = pixelAR[2]
            pixelBR0 = pixelBR[0]
            pixelBR1 = pixelBR[1]
            pixelBR2 = pixelBR[2]
            p0 = pixelAR0 & pixelBR0
            p1 = pixelAR1 & pixelBR1
            p2 = pixelAR2 & pixelAR2
            pixel = tuple([p0,p1,p2])
            imagenC.putpixel((x,y),pixel)
    
    imagenC.show()
    imagenC.save("ImagenC_BN_AND.png")

def ImagenBinariaOR(rutaImagenA,rutaImagenB):
    imagenA = Image.open(rutaImagenA).convert('1')
    imagenB = Image.open(rutaImagenB).convert('1')
    anchom,alto = imagenA.size
    imagenC = Image.new('1',imagenA.size)
    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            imagenC.putpixel((x,y),pixelAR | pixelBR)
    
    imagenC.show()
    imagenC.save("ImagenC_B_OR.png")  
    
def ImagenBinariaAND(rutaImagenA,rutaImagenB):
    imagenA = Image.open(rutaImagenA).convert('1')
    imagenB = Image.open(rutaImagenB).convert('1')
    anchom,alto = imagenA.size
    imagenC = Image.new('1',imagenA.size)
    pixelImagenA = imagenA.load()
    pixelImagenB = imagenB.load()

    for x in range(anchom):
        for y in range(alto):
            pixelAR = pixelImagenA[x,y]
            pixelBR = pixelImagenB[x,y]
            imagenC.putpixel((x,y),pixelAR & pixelBR)
    
    imagenC.show()
    imagenC.save("ImagenC_B_AND.png")  
#ImagenNivelGrisOR("imagenABN.png","imagenBBN.png")
#ImagenNivelGrisAND("imagenABN.png","imagenBBN.png")
#ImagenColorOR("imagenAC.png","imagenBC.png")
#ImagenColorAND("imagenAC.png","imagenBC.png")
ImagenBinariaOR("imagenAC.png","imagenBC.png")
ImagenBinariaAND("imagenAC.png","imagenBC.png")
