import argparse
import os

from grafo import Grafo

ES_DIRIGIDO = False

def crear_grafo(ruta_grafo):
    grafo = Grafo(es_dirigido = ES_DIRIGIDO)

    with open(ruta_grafo) as f:
        for linea in f:
            linea = linea.strip()

            if not linea or linea.startswith('#'): continue

            u, v = map(int, linea.split(','))
            
            if not grafo.pertenece_vertice(u):
                grafo.agregar_vertice(u)
            
            if not grafo.pertenece_vertice(v):
                grafo.agregar_vertice(v)
            
            grafo.agregar_arista(u, v)

    return grafo

def generar_grafo_lista(nombre_archivo, cantidad_vertices):
    if cantidad_vertices < 2:
        raise ValueError("Debe haber al menos 2 vértices para formar una lista")
    
    carpeta_destino = os.path.join(".", "data", "gen")
    os.makedirs(carpeta_destino, exist_ok=True)

    ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

    with open(ruta_completa, "w") as archivo:
        for i in range(cantidad_vertices - 1):
            archivo.write(f"{i},{i+1}\n")

def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Clustering de un grafo con bajo diámetro")
    parser.add_argument("archivo", help="Ruta al archivo que contiene el grafo")
    parser.add_argument("clusters", type=int, help="Número de clusters a generar")
    parser.add_argument("-t", "--temporizador", action="store_true", help="Mostrar tiempo de ejecución")
    parser.add_argument("-a", "--adyacentes", action="store_true", help="Mostrar adyacentes del grafo")
    return parser.parse_args()