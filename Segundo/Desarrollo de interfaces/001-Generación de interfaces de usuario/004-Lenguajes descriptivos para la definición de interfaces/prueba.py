file_path = 'C:/xampp/htdocs/dam/dam/Segundo/Desarrollo de interfaces/001-Generación de interfaces de usuario/004-Lenguajes descriptivos para la definición de interfaces/013-interfaz.xml'

try:
    with open(file_path, 'r') as f:
        print("El archivo se abrió correctamente.")
except FileNotFoundError:
    print("El archivo no se encontró.")
except Exception as e:
    print("Ocurrió un error:", e)
