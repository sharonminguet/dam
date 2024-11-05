import random
import math
import json
# Declaro una clase Npc y le pongo dos sencillas propiedades x e y
class Npc:
    def __init__(self,nuevax,nuevay,nuevoangulo):
        self.x = nuevax
        self.y = nuevay
        self.angulo = nuevoangulo
# Creo una lista de 50 npcs
npcs = [ ]

#Para leer el json
with open('basededatos.json', 'r' ) as archivo:
    datos = json.load(archivo)

#Para convertir una lista de objetos en instancias de Npc
for elemento in datos:
    npcs.append(Npc(elemento['x'],elemento['y'],elemento['angulo']))

#Para comprobar que funciona
for npc in npcs:
    print(npc.x,npc.y,npc.angulo)
