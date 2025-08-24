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
    plt.xlabel('Valor de k (cantidad de clusters)')
    plt.ylabel('Tiempo promedio (ms)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

def graficar(valores_k, tiempos, archivo):
    plt.figure(figsize=(10, 5))
    plt.plot(valores_k, tiempos, marker='o', linestyle='-', color='blue')
    plt.title(f'Tiempos para archivo {os.path.basename(archivo)}')
    plt.xlabel('Valor de k (cantidad de clusters)')
    plt.ylabel('Tiempo promedio (ms)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def medir_tiempos(algoritmo, grafo, valores_k):
    indices = list(range(len(valores_k)))

    def get_args(idx):
        k = valores_k[idx]
        return grafo, k

    resultados = time_algorithm(algoritmo, indices, get_args)
    return convertir_a_milisegundos(np.array([resultados[i] for i in indices]))

def convertir_a_milisegundos(resultados):
    return resultados * 1000

def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Graficar tiempos de 'Clustering por bajo diametro' variando el valor de k")

    parser.add_argument('--bt', action='store_true', help='Graficar backtracking')
    parser.add_argument('--pl', action='store_true', help='Graficar programacion lineal')
    parser.add_argument('--aprox', action='store_true', help='Graficar aproximacion')
    parser.add_argument('--all', action='store_true', help='Graficar todos los algoritmos en un mismo gráfico')
    parser.add_argument('--archivo', type=str, required=True, help='Ruta al archivo de entrada .txt')
    parser.add_argument('--min', type=int, required=True, help='Valor mínimo de k (clusters)')
    parser.add_argument('--max', type=int, required=True, help='Valor máximo de k (clusters)')
    
    args = parser.parse_args()
    return args, args.archivo, args.min, args.max

def main():
    args, archivo, k_min, k_max = parsear_argumentos()

    grafo = crear_grafo(archivo)
    valores_k = list(range(k_min, k_max + 1))

    if args.all:
        print("Midiendo tiempos para todos los algoritmos...\n")
        tiempos = {}
        
        tiempos[BACKTRACKING] = medir_tiempos(clustering_bajo_diametro, grafo, valores_k)
        tiempos[PROGRAMACION_LINEAL] = medir_tiempos(pl, grafo, valores_k)
        tiempos[APROXIMACION] = medir_tiempos(aproximacion, grafo, valores_k)
        
        graficar_todos(valores_k, tiempos)
        return

    if args.bt:
        print("Midiendo tiempos para algoritmo de Backtracking...")
        tiempos_promedio_ms_bt = medir_tiempos(clustering_bajo_diametro, grafo, valores_k)
        graficar(valores_k, tiempos_promedio_ms_bt, archivo)
        return

    if args.pl:
        print("Midiendo tiempos para algoritmo de Programacion Lineal...")
        tiempos_promedio_ms_pl = medir_tiempos(pl, grafo, valores_k)
        graficar(valores_k, tiempos_promedio_ms_pl, archivo)
        return

    if args.aprox:
        print("Midiendo tiempos para algoritmo de Aproximacion...")
        tiempos_promedio_ms_aproximacion = medir_tiempos(aproximacion, grafo, valores_k)
        graficar(valores_k, tiempos_promedio_ms_aproximacion, archivo)
        return

if __name__ == "__main__":
    main()