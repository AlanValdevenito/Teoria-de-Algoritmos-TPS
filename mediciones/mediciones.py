import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from utils import crear_grafo
from backtracking import clustering_bajo_diametro 
from aproximacion import aproximacion
from programacion_lineal import pl
from util import time_algorithm

sns.set_theme()

BACKTRACKING = 'backtracking'
APROXIMACION = 'aproximacion'
PROGRAMACION_LINEAL = 'programacion lineal'

def graficar_todos(x, tiempos_dict):
    plt.figure(figsize=(12, 6))
    for nombre_algoritmo, tiempos in tiempos_dict.items():
        plt.plot(x, tiempos, marker='o', linestyle='-', label=nombre_algoritmo)
    plt.title('Tiempos promedio por algoritmo')
    plt.xlabel('Archivo y cantidad de clusters')
    plt.ylabel('Tiempo promedio (ms)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

def graficar(x, y, algoritmo):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title(f'Tiempo promedio de {algoritmo}')
    plt.xlabel('Archivo y cantidad de clusters')
    plt.ylabel('Tiempo promedio (ms)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def medir_tiempos(algoritmo, casos):
    indices = list(range(len(casos)))

    def get_args(idx):
        return casos[idx]

    resultados = time_algorithm(algoritmo, indices, get_args)

    return convertir_a_milisegundos(np.array([resultados[i] for i in indices]))

def convertir_a_milisegundos(resultados):
    return resultados * 1000

def crear_casos():
    nombres = ['10_3.txt 2', 
               '10_3.txt 5', 
               '22_3.txt 3', 
               '22_3.txt 4', 
               # '22_3.txt 10', 
               '22_5.txt 2', 
               # '22_5.txt 7', 
               '30_3.txt 2', 
               # '30_3.txt 6', 
               '30_5.txt 5', 
               '40_5.txt 3',
               # '45_3.txt 7',
               '50_3.txt 3']
    
    casos = [
        (crear_grafo('../data/resources/10_3.txt'), 2),
        (crear_grafo('../data/resources/10_3.txt'), 5),
        (crear_grafo('../data/resources/22_3.txt'), 3),
        (crear_grafo('../data/resources/22_3.txt'), 4),
        # (crear_grafo('../data/resources/22_3.txt'), 10),
        (crear_grafo('../data/resources/22_5.txt'), 2),
        # (crear_grafo('../data/resources/22_5.txt'), 7),
        (crear_grafo('../data/resources/30_3.txt'), 2),
        # (crear_grafo('../data/resources/30_3.txt'), 6),
        (crear_grafo('../data/resources/30_5.txt'), 5),
        (crear_grafo('../data/resources/40_5.txt'), 3),
        # (crear_grafo('../data/resources/45_3.txt'), 7),
        (crear_grafo('../data/resources/50_3.txt'), 3),
    ]

    return casos, nombres

def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Graficar tiempos de 'Clustering por bajo diametro' por algoritmo")

    parser.add_argument('--bt', action='store_true', help='Graficar backtracking')
    parser.add_argument('--pl', action='store_true', help='Graficar programacion lineal')
    parser.add_argument('--aprox', action='store_true', help='Graficar aproximacion')
    parser.add_argument('--all', action='store_true', help='Graficar todos los algoritmos en un mismo gráfico')
    
    return parser.parse_args()

def main():
    args = parsear_argumentos()
    casos, nombres = crear_casos()

    if args.all:
        print("Midiendo tiempos para todos los algoritmos...\n")
        tiempos = {}
        
        tiempos[BACKTRACKING] = medir_tiempos(clustering_bajo_diametro, casos)
        tiempos[PROGRAMACION_LINEAL] = medir_tiempos(pl, casos)
        tiempos[APROXIMACION] = medir_tiempos(aproximacion, casos)
        
        graficar_todos(nombres, tiempos)
        return

    if args.bt:
        print("Midiendo tiempos para algoritmo de Backtracking...")
        tiempos_promedio_ms_bt = medir_tiempos(clustering_bajo_diametro, casos)
        graficar(nombres, tiempos_promedio_ms_bt, BACKTRACKING)
        return

    if args.pl:
        print("Midiendo tiempos para algoritmo de Programacion Lineal...")
        tiempos_promedio_ms_pl = medir_tiempos(pl, casos)
        graficar(nombres, tiempos_promedio_ms_pl, PROGRAMACION_LINEAL)
        return

    if args.aprox:
        print("Midiendo tiempos para algoritmo de Aproximacion...")
        tiempos_promedio_ms_aproximacion = medir_tiempos(aproximacion, casos)
        graficar(nombres, tiempos_promedio_ms_aproximacion, APROXIMACION)
        return

if __name__ == "__main__":
    main()