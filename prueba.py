import json
import random

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)
        
lista_peliculas = leer_archivo("peliculasNew.json")



def boca():
    lista_peliculas = leer_archivo("peliculasNew.json")

    while True:
        titu = input("ingrese el titulo: ")
        for x in lista_peliculas:
            if titu in x['titulo']:
                print(x)
                print(f"Titulos encontrados para modificar: {titu['titulo']}")
                False
        break
boca()    