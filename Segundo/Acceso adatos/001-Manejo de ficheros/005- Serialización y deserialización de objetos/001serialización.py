variable1 = "de momento añado un texto"
variable2 = "aunque no estará claro si es de la variable1 o la variable2"

archivo = open("archivo.txt",'w')
archivo.write(variable1+variable2)
archivo.close()
