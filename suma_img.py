# Carlos Alfonso Barrón Rivera 2019630166
from PIL import Image

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

resta_imagenes_rgb("imagenes/logo_pregunta.jpg","imagenes/foto_perfil.jpg")
#suma_imagenes_rgb("foto_perfil.jpg","logo_pregunta.jpg")
