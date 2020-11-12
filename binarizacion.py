from PIL import Image

foto=Image.open('montanas.jpg')

#si la imagen no es a escala de grises se hace la conversion

if foto.mode != 'L':
    foto=foto.convert('L')

#el umbral esta forzosamente comprendido entre 1 y 254 para las
#imagenes de 8 bits a escala de grises
umbral=75

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
nueva_imagen=Image.new('1', foto.size)
nueva_imagen.putdata(datos_binarios)
nueva_imagen.save('montanas_binaria.jpg')

nueva_imagen.close()
foto.close()
