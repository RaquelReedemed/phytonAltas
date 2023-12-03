import json
import random

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)
        
lista_peliculas = leer_archivo("peliculasNew.json")


def buscar_pelicula_titulo():
   
    titulo_buscado = input("Ingrese el titulo de la pelicula que desee buscar: ")
    encontrada = False

    for pelicula in lista_peliculas:
        if pelicula["titulo"] == titulo_buscado:
            print(pelicula)
            encontrada = True
            break
    if not encontrada:
      print("Pelicula no existente")   

buscar_pelicula_titulo()


def buscar_titulo_id():

    id_buscado = int(input("Ingrese id:"))

    for pelicula in lista_peliculas:

        if pelicula['id'] == id_buscado:
           print(pelicula)
   
buscar_titulo_id()    

