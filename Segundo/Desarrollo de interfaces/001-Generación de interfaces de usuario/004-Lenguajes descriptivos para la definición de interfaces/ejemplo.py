import xml.etree.ElementTree as ET

# Cargar un archivo XML
tree = ET.parse('013-interfaz.xml')
root = tree.getroot()

# Acceder a elementos
for boton in root.findall('boton'):
    print(boton.text)

# Crear un nuevo elemento y agregarlo
nuevo_boton = ET.Element('boton')
nuevo_boton.text = 'Nuevo Botón'
root.append(nuevo_boton)

# Guardar el nuevo XML
tree.write('013-interfaz.xml')
