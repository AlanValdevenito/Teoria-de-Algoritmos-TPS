import argparse

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from tp2 import encontrar_soplon
from utils import generar_entrada_aleatoria

from util import time_algorithm

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

sns.set_theme()

from itertools import product
import random

CANTIDAD_PALABRAS = 1000
LARGO_PALABRAS = 5

def generar_entrada(params):
    cantidad_palabras_desencriptadas, cantidad_palabras = params

    valido = random.choices([True, False], weights=[75, 25])[0]

    palabras, cadena_desencriptada = generar_entrada_aleatoria(cantidad_palabras, cantidad_palabras_desencriptadas, LARGO_PALABRAS, valido)
    return palabras, cadena_desencriptada

def funcion(params, c1, c2):
    params = np.atleast_2d(params)
    n = params[:, 0]
    d = params[:, 1]
    return c1 * n * d + c2

def ajustar_funcion(x, resultados):
    coeficientes, _ = sp.optimize.curve_fit(funcion, x, [resultados[n] for n in x])
    return coeficientes

def graficar_tiempos_ajuste(params, resultados, coeficientes):
    x = [p[0] for p in params]

    tiempos_medidos = [resultados[p] for p in params]
    tiempos_ajustados = [funcion(np.array([p]), coeficientes[0], coeficientes[1]) for p in params]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, tiempos_medidos, '-o', markersize = 5, color = 'b', label = 'Medicion')
    ax.plot(x, tiempos_ajustados, 'r--', label=f"Ajuste ($c_1 = {coeficientes[0]:.2e}$, $c_2 = {coeficientes[1]:.2e}$)")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel('Largo de la cadena desencriptada (n)')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    plt.show()

def calcular_error(x, resultados, coeficientes):
    errors = [np.abs(funcion(np.array([n, CANTIDAD_PALABRAS]), coeficientes[0], coeficientes[1]) - resultados[(n, CANTIDAD_PALABRAS)]) for n in x]
    sse = np.sum(np.power(errors, 2))
    return errors, sse

def graficar_error(x, errors, sse):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, errors, '-o', markersize = 5, color = 'b', label = "Error")
    plt.text(0.05, 0.95, f'SSE = {sse:.10f}', ha='left', va='top', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
    ax.set_title('Error del ajuste')
    ax.set_xlabel('Largo de la cadena desencriptada (n)')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()
    plt.show()

def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Ejecutar mediciones")

    parser.add_argument('--min', type=int, default=100, help='Tamaño mínimo de la cadena desencriptada (por defecto 100)')
    parser.add_argument('--max', type=int, default=1_000, help='Tamaño máximo de la cadena desencriptada (por defecto 1.000)')
    parser.add_argument('--p', type=int, default=20, help='Cantidad de puntos (por defecto 20)')

    args = parser.parse_args()
    return args.min, args.max, args.p

def main():
    # Obtener los argumentos desde la línea de comandos o usar valores por defecto
    valor_minimo, valor_maximo, cantidad_puntos = parsear_argumentos()

    print(f"Valor minimo: {valor_minimo}")
    print(f"Valor maximo: {valor_maximo}")
    print(f"Cantidad de puntos: {cantidad_puntos}\n")

    # Generamos un arreglo con 'cantidad_puntos' valores distribuidos uniformemente entre 'valor_minimo' y 'valor_maximo'
    # Estos puntos x son los valores del eje x de los graficos
    # Representan la cantidad de palabras en la cadena desencriptada (n)
    x = np.linspace(valor_minimo, valor_maximo, cantidad_puntos).astype(int) # Variamos la cantidad de palabras en la cadena desencriptada
    y = [CANTIDAD_PALABRAS] # Fijamos la cantidad de palabras
    print(f"Cantidad de palabras en la cadena desencriptada (cada elemento i es la cantidad de elementos de la invocacion i): {x}\n")

    combinaciones = list(product(x, y))

    print(f"Combinacion de elementos (cada combinacion i es la combinacion de la invocacion i): {combinaciones}\n")

    # Medición de tiempo del algoritmo
    # El algoritmo se ejecuta len(combinaciones) veces con cada valor de combionaciones
    # La funcion 'generar_entrada' recibe un valor n que proviene del arreglo combinaciones y devuelve una entrada aleatoria para la funcion 'encontrar_soplon'
    resultados = time_algorithm(encontrar_soplon, combinaciones, lambda n: generar_entrada(n))

    # Tecnica de cuadrados minimos: Ajusta los parametros c1 y c2 de la funcion cuadratica a los datos de la medicion
    coeficientes = ajustar_funcion(combinaciones, resultados)
    print(f"Coeficientes obtenidos del ajuste cuadratico: c_1 = {coeficientes[0]}, c_2 = {coeficientes[1]}\n")

    # Graficar los resultados y ajuste
    graficar_tiempos_ajuste(combinaciones, resultados, coeficientes)

    # Calcular el error cuadrático
    errors, sse = calcular_error(x, resultados, coeficientes)
    print(f"Error cuadrático total (SSE): {sse:.10f}")

    # Graficar el error cuadrático
    graficar_error(x, errors, sse)

if __name__ == "__main__":
    main()