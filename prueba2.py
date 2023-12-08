import json
import random

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)
def grabar_archivo(lista_peliculas, nombre_archivo):
        with open(nombre_archivo, "w") as conexion:
            json.dump(lista_peliculas, conexion, indent=4)
def imprimir_generos(generos_disponibles):
        print("Generos disponibles para la pelicula: ")
        for x in range(0, len(generos_disponibles)):
            print(f"{x + 1} - {generos_disponibles[x]}")    

lista_peliculas = leer_archivo("peliculasNew.json")

# Busca pelicula por titulo (Y las modifica)
def buscar_pelicula_titulo(lista_peliculas):
   
    lista_peliculas = leer_archivo("peliculasNew.json")

       
    while True:
      
        titulo_seleccionado = input("Ingrese el titulo que desea modificar: ")
  
        for x in lista_peliculas:
            if titulo_seleccionado in x['titulo']:
             print(f"titulos: {x['titulo']}")
             

        for pelicula in lista_peliculas:
            # QUE EL USUSARIO ELIJA UNA PELICULA
             if titulo_seleccionado == pelicula['titulo']:
                print(pelicula)
                posicion = lista_peliculas.index(pelicula)
                print(posicion)
                desea = input("Que desea modificar?: ")
                if desea == "titulo":
                    new_titulo = input("Ingrese el nuevo titulo: ")
                    lista_peliculas[posicion]["titulo"] = new_titulo
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "duracion":
                    new_duracion = int(input("Ingrese la nueva duracion: "))
                    lista_peliculas[posicion]["duracion"] = new_duracion #INDEX 
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "genero":
                    generos_disponibles = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica"]
                    generos = []
                    imprimir_generos(generos_disponibles)   
                    while True:
                        rta_genero = input("Ingrese un genero para la pelicula: ")
                        if rta_genero in generos_disponibles:
                            generos.append(rta_genero)
                        else:
                            print("Ingrese un genero valido...")
                            imprimir_generos(generos_disponibles)
                            continue
                        continua = input("Desea agregar otro genero?: (S/N)")
                        if continua == "N":
                            break
                        elif continua == "S":
                            continue
                        else:
                            print("Opcion incorrecta")
                            continua = input("Desea agregar otro genero?: (S/N)")
                            if continua == "S":
                                continue
                            elif continua == "N":
                                break
                            else:
                                print("Opcion incorrecta")
                                continue        
                    lista_peliculas[posicion]["genero"] = generos
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")

                elif desea == "sinopsis":
                    new_sinopsis = input("Ingrese la nueva sinopsis: ")
                    lista_peliculas[posicion]["sinopsis"] = new_sinopsis
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "pais de origen":
                    new_pais = input("Ingrewse el nuevo país de origen: ")
                    lista_peliculas[posicion]["pais_de_origen"] = new_pais
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "idioma":
                    new_idioma = input("Ingrese el nuevo idioma: ")
                    lista_peliculas[posicion]["idioma"] = new_idioma
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "clasificacion":
                    new_clasificacion = input("Ingrese la nueva clasificacion: ")
                    lista_peliculas[posicion]["clasificacion"] = new_clasificacion
                    print(pelicula)
                    grabar_archivo(lista_peliculas, "peliculasNew.json")
                    break
                elif desea == "calificacion":
                    print("hacer")
                elif desea == "disponible":
                    while True:
                        new_disponible = input("Está disponible la pelicula? S/N: ")
                        if new_disponible == "S":
                            lista_peliculas[posicion]["disponible"] = True
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        elif new_disponible == "N":
                            lista_peliculas[posicion]["disponible"] = False
                            print(pelicula)
                            grabar_archivo(lista_peliculas, "peliculasNew.json")
                            break
                        else:
                            print("La opción ingresada es incorrecta")
                break          
        else:
                print("no funciona")


                
def boca():
    lista_peliculas = leer_archivo("peliculasNew.json")

    while True:
        titu = input("ingrese el titulo: ")
        for x in lista_peliculas:
            if titu in x['titulo']:
                print(f"Titulos encontrados para modificar: {x['titulo']}")
                False
        break


buscar_pelicula_titulo(lista_peliculas)