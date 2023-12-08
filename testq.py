import json

def leer_archivo(nombre_archivo):
        with open(nombre_archivo, 'r') as conexion:
            return json.load(conexion)
        
lista_peliculas = leer_archivo("peliculasNew.json")

titu = input("ingrese el titulo: ")

for x in lista_peliculas:
   if titu in x['titulo']:
    print(f"titulos: {x['titulo']}")
   else:
       print("no encontrada") 
       break
       

# print(f"Titulos encontrados para modificar: {x['titulo']}")