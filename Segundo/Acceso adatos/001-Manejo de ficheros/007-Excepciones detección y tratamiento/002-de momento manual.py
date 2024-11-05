class Cliente:
    def __init__(self):
        self.nombre = None
        self.apellidos = None
        self.emails = {"personal":[],"profesional":[]}

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
clientes[-1].emails['profesional'].append("shertechstore@jgmail.com")
clientes[-1].emails['personal'].append("minguetchsharon@gmail.com")

##puedo especificar el mail que quiero que me saque añadiendo ['profesional o personal']
print(clientes[-1].emails)      
