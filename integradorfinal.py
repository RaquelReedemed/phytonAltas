import json
import random

def ABM_peliculas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        alta()
    elif opcion_submenu == "2":
        print(opcion2_submenu_1)
        modificacion_pelicula_existente()
    elif opcion_submenu == "3":
        print(opcion3_submenu_1)
        baja_pelicula()
    elif opcion_submenu == "4":
        return
    else:
        print("Opción incorrecta, vuelva a ingresar una opción")
        ABM_peliculas()



def calificacion_titulos():
    print(submenu_2)
def reportes_estadisticas():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        print(opcion1_submenu_3)
    elif opcion_submenu == "2":
        print(opcion2_submenu_3)
    elif opcion_submenu == "3":
        print(opcion3_submenu_3)
    elif opcion_submenu == "4":
        return
    else:
        reportes_estadisticas()

#Alta de peliculas

def imprimir_generos(generos_disponibles):
        print("Generos disponibles para la pelicula: ")
        for x in range(0, len(generos_disponibles)):
            print(f"{x + 1} - {generos_disponibles[x]}")

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)


def grabar_archivo(lista_peliculas, nombre_archivo):
        with open(nombre_archivo, "w") as conexion:
            json.dump(lista_peliculas, conexion, indent=4)

def alta():
        lista_peliculas = leer_archivo("peliculasNew.json")
        generos_disponibles = ("Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica")
        clasificacion = ["ATP" , "PG" , "PG-13" , "R", "NC-17"]
        clasificacion_vacio = []

        id_pelicula = random.randint(10000, 99999)
        titulo = input("Ingrese el titulo de la pelicula: ")
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
                if continua == "N":
                    break
                elif continua == "S":
                    continue
        

        duracion = int(input("Ingrese la duracion de la pelicula en minutos: "))
        sinopsis = input("Escriba una sinopsis de la pelicula: ")
        pais_de_origen = input("Ingrese el país de origen de la pelicula: ")
        idioma = input("Ingrese el idioma de la pelicula: ")
        while True:
            clasificacion_ingresada = input("Ingrese una clasificación: ")
            if clasificacion_ingresada in clasificacion:
                clasificacion_vacio.append(clasificacion_ingresada)
            elif clasificacion_ingresada not in clasificacion:
                print("Opción invalida, elija una clasificación valida")
                continue
            break
        calificacion = 0
        disponible = True
                

        peliculas_a_agregar = {
            "id": id_pelicula,
            "titulo": titulo,
            "duracion": duracion,
            "genero": generos,
            "sinopsis": sinopsis,
            "pais_de_origen": pais_de_origen,
            "idioma": idioma,
            "clasificacion": clasificacion_vacio,
            "calificacion": calificacion,
            "disponible": disponible
        }

        lista_peliculas.append(peliculas_a_agregar)
        grabar_archivo(lista_peliculas, "peliculas.json")
        print("Película agregada exitosamente.")         

lista_peliculas = leer_archivo("peliculasNew.json")

def buscar_titulo_id():

    id_buscado = int(input("Ingrese id:"))

    for pelicula in lista_peliculas:
        if pelicula['id'] == id_buscado:
           print(pelicula)
     

def buscar_pelicula_titulo():
   
    titulo_buscado = input("Ingrese el titulo de la pelicula que desee buscar: ")

    for pelicula in lista_peliculas:
        if pelicula["titulo"] == titulo_buscado:
            print(pelicula)
    

def modificacion_pelicula_existente():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        buscar_titulo_id()
    elif opcion_submenu == "2":
        buscar_pelicula_titulo()
    elif opcion_submenu == "3":
        print(submenu_1)
        ABM_peliculas()
    else:
        modificacion_pelicula_existente()
def baja_pelicula():
    opcion_submenu = input("Elija una opción: ")
    if opcion_submenu == "1":
        int(input("Ingrese el id de la pelicula: "))
    elif opcion_submenu == "2":
        buscar_pelicula_titulo()
    elif opcion_submenu == "3":
        print(opcion3_subsubsubmenu_1)
    else:
        baja_pelicula() 
def menu_inicio():
    while True:
        print(menu)
        opcionUsuario = input("ingrese la opcion que desea :")
        if opcionUsuario == "1":
            print(submenu_1)
            ABM_peliculas()
        elif opcionUsuario == "2":
            calificacion_titulos()
        elif opcionUsuario == "3":
            print(submenu_3)
            reportes_estadisticas()
        elif opcionUsuario == "4":
            print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
            break
        else:
            print("opción invalida")
            continue
        

#TODO
menu = "CINEMA+ \n 1. ABM de películas \n 2. Calificación de títulos \n 3. Reportes y estadísticas \n 4. Salir"
submenu_1 = "CINEMA+ \n Alta, Baja y modificación de películas \n 1. Alta de nueva película \n 2. Modificación de película existente \n 3. Baja de película (eliminar) \n 4. Volver"
opcion2_submenu_1 = "CINEMA+ \n Modificar película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion3_submenu_1 = "CINEMA+ \n Eliminar una película existente \n 1. Buscar por id \n 2. Buscar por titulo \n 3. Volver"
opcion4_submenu_1 = "Volver"
opcion3_subsubmenu_1 = "Volver"
opcion3_subsubsubmenu_1 = "Volver"
submenu_2 = "CALIFICACION DE TITULOS"
submenu_3 = "CINEMA+ \n Reportes y estadísticas \n 1. Listado de películas \n 2. Películas de mayor puntaje \n 3. Porcentaje de películas disponibles en la plataforma \n 4. Volver"
opcion1_submenu_3 = "Titulo, Género(s), Calificación ordenado por titulo"
opcion2_submenu_3 = "Listar titulo, género y calificación de las 15 películas de mayor puntaje."
opcion3_submenu_3 = "Imprimir histograma en porcentaje con * de películas disponible contra películas no disponibles."
opcion4_submenu_3 = "Antes de salir, debe preguntarle al usuario si desea finalizar el programa."
submenu_4 = "Saliste del programa. BYE"
#WHILE
while True:
    print(menu)
    opcionUsuario = input("ingrese la opcion que desea :")
    if opcionUsuario == "1":
        print(submenu_1)
        ABM_peliculas()
    elif opcionUsuario == "2":
        calificacion_titulos()
    elif opcionUsuario == "3":
        print(submenu_3)
        reportes_estadisticas()
    elif opcionUsuario == "4":
        print("Saliste del programa, Muchas gracias por utilizar CINEMA+")
        break
    else:
        print("opción invalida")
        continue
