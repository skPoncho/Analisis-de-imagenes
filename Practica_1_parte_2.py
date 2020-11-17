# Carlos Alfonso Barrón Rivera 2019630166
from PIL import Image
import sys

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

def binarizar_imagen(img_inicial,umbral,img_binaria):

    foto = abrir_imagen(img_inicial)#se abre la imagen inicial

    if foto.mode != 'L':
        foto=foto.convert('L')
    datos=foto.getdata()
    datos_binarios=[]

    for x in datos:
        if x<umbral:
            datos_binarios.append(0)
            continue
        #si es mayor o igual a umbral se agrega 1 en ves de 0
        #podria hacerse con 255 en ves de 1
        datos_binarios.append(1)

    #en caso de utilizar 255 como valor superior el metodo new
    #llevaria 'L' en ves de '1' en el primer argumento
    #nueva_imagen = Image.new('1', foto.size)
    nueva_imagen = crear_imagen('1', foto.size)
    guardar_imagen(img_binaria,datos_binarios,img_binaria)
    #nueva_imagen.putdata(datos_binarios)
    #nueva_imagen.save(img_binaria)
    cerrar_imagen(nueva_imagen)
    #nueva_imagen.close()
    foto.close()

def suma_imagenes_grises(img_1,img_2):#obtiene la suma de dos imagenes en escala de grises
    imagen = abrir_imagen(img_1)#se abre la imagen inicial
    datos = imagen.getdata()#se obtienen las matrices de la imagen
    imagen2 = abrir_imagen(img_2)

    datos2 = imagen2.getdata()
    resultante = []
    resultante = [((datos[x] + datos2[x]) // 2) for x in range(len(datos))]

    imagen_suma = crear_imagen('L', imagen.size)

    guardar_imagen(imagen_suma,resultante,"imagenes/imagen_suma_grises.jpg")#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_suma)#se cierra la imagen creada
    cerrar_imagen(imagen)
    cerrar_imagen(imagen2)

def suma_imagenes_rgb(img_1,img_2):#obtiene una imagen en escala de grises a partir de una imagen RGB
    imagen = abrir_imagen(img_1)#se abre la imagen inicial
    datos = imagen.getdata()#se obtienen las matrices de la imagen
    imagen2 = abrir_imagen(img_2)#se abre la imagen inicial
    datos2 = imagen2.getdata()#se obtienen las matrices de la imagen

    resultante = [((datos[x][0] + datos2[x][0] ) // 2,(datos[x][1] + datos2[x][1] ) // 2,(datos[x][2] + datos2[x][2] ) // 2) for x in range(len(datos))]

    imagen_suma = crear_imagen('RGB', imagen.size)#se indica que es una imagen en escala de grises del tamaño de la imagen inicial

    guardar_imagen(imagen_suma,resultante,"imagenes/imagen_suma_rgb.jpg")#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_suma)#se cierra la imagen creada
    cerrar_imagen(imagen)
    cerrar_imagen(imagen2)

def resta_imagenes_grises(img_1,img_2):#obtiene la resta de dos imagenes en escala de grises
        imagen = abrir_imagen(img_1)#se abre la imagen inicial
        datos = imagen.getdata()#se obtienen las matrices de la imagen
        imagen2 = abrir_imagen(img_2)
        datos2 = imagen2.getdata()
        MatrizT = [(datos[x] - datos2[x]) for x in range(len(datos))]
        minimo = min(MatrizT)
        maximo = max(MatrizT)
        resultante = [(round(((MatrizT[x] - minimo)/(maximo-minimo))*255,0)) for x in range(len(MatrizT))]

        imagen_resta = crear_imagen('L', imagen.size)#se indica que es una imagen en escala de grises del tamaño de la imagen inicial

        guardar_imagen(imagen_resta,resultante,"imagen_resta_grises.jpg")#se guardan los datos de la imagen nueva

        cerrar_imagen(imagen_resta)#se cierra la imagen creada
        cerrar_imagen(imagen)
        cerrar_imagen(imagen2)

def resta_imagenes_rgb(img_1,img_2):#obtiene la resta de dos imagenes en escala de grises
        imagen = abrir_imagen(img_1)#se abre la imagen inicial
        datos = imagen.getdata()#se obtienen las matrices de la imagen
        imagen2 = abrir_imagen(img_2)
        datos2 = imagen2.getdata()

        MatrizT_R = [((datos[x][0] - datos2[x][0])) for x in range(len(datos))]#primero se obtiene la matriz T
        minimo_R = min(MatrizT_R)
        dif_R = max(MatrizT_R) - min(MatrizT_R)
        MatrizT_G = [((datos[x][1] - datos2[x][1])) for x in range(len(datos))]#primero se obtiene la matriz T
        minimo_G = min(MatrizT_G)
        dif_G = max(MatrizT_G) - min(MatrizT_G)
        MatrizT_B = [((datos[x][2] - datos2[x][2])) for x in range(len(datos))]#primero se obtiene la matriz T
        minimo_B = min(MatrizT_B)
        dif_B = max(MatrizT_B) - min(MatrizT_B)

        resultante = [(int(((MatrizT_R[x] - minimo_R)/(dif_R))*255),int(((MatrizT_G[x] - minimo_G)/(dif_G))*255),int(((MatrizT_B[x] - minimo_B)/(dif_B))*255)) for x in range(len(MatrizT_R))]

        imagen_resta_rgb = crear_imagen('RGB', imagen.size)#se indica que es una imagen en escala de grises del tamaño de la imagen inicial

        guardar_imagen(imagen_resta_rgb,resultante,"imagen_resta_rgb.jpg")#se guardan los datos de la imagen nueva

        cerrar_imagen(imagen_resta_rgb)#se cierra la imagen creada
        cerrar_imagen(imagen)
        cerrar_imagen(imagen2)

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

binarizar_imagen("imagenes/logo_pregunta.jpg",65,"imagenes/img_binaria.jpg")
resta_imagenes_rgb("imagenes/logo_pregunta.jpg","imagenes/foto_perfil.jpg")
suma_imagenes_rgb("foto_perfil.jpg","logo_pregunta.jpg")
suma_imagenes_grises("imagenes/logo_pregunta.jpg","imagenes/foto_perfil.jpg")
resta_imagenes_grises("imagenes/logo_pregunta.jpg","imagenes/foto_perfil.jpg")

#ImagenNivelGrisOR("imagenABN.png","imagenBBN.png")
#ImagenNivelGrisAND("imagenABN.png","imagenBBN.png")
#ImagenColorOR("imagenAC.png","imagenBC.png")
#ImagenColorAND("imagenAC.png","imagenBC.png")
ImagenBinariaOR("imagenAC.png","imagenBC.png")
ImagenBinariaAND("imagenAC.png","imagenBC.png")
Maximo ("Amazon.jpg" , "Acuarelas.jpg")
Minimo ("Letras.png" , "Acuarelas.jpg")
