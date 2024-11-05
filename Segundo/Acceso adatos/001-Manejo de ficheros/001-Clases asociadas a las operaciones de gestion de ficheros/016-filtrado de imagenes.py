import os
import PIL.Image

try:
    imagen = Image.open("20241014.jpg")
    imagen.show()
except:
    print("No ha sido posible cargar la imagen")
