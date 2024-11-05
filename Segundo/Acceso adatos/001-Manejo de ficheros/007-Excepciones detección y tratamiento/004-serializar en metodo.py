import json

class Cliente:
    def __init__(self):
        self.nombre = None
        self.apellidos = None
        self.emails = {"personal":[],"profesional":[]}
    def to_dict(self):
        return {
                "nombre": self.nombre,
                "apellidos": self.apellidos,
                "emails": self.emails
            }

class Producto:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.peso = None
        self.dimensiones = {"x":None,"y":None,"z":None}

clientes = []
clientes.append(Cliente())

clientes[-1].nombre = "Sharon"
clientes[-1].apellidos = "Minguet Chirivella"
clientes[-1].emails['profesional'].append("shertech2@gmail.com")
clientes[-1].emails['profesional'].append("shertechstore@gmail.com")
clientes[-1].emails['personal'].append("minguetchsharon@gmail.com")

print(clientes[-1].emails)

archivo = open("clientes.json",'w')
json.dump(clientes[-1].to_dict() ,archivo,indent=4)
archivo.close()
                             
