import argparse

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from tp1 import encontrar_rata
from utils import generar_entrada_aleatoria, generar_entrada_optima

from util import time_algorithm

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

sns.set_theme()

def generar_entrada(n, valor_minimo, valor_maximo, optimo):
    timestamps_aproximados, transacciones = generar_entrada_aleatoria(n, valor_minimo, valor_maximo) if not optimo else generar_entrada_optima(n, valor_minimo)
    return np.array(timestamps_aproximados), np.array(transacciones)

def f_cuadratica(x, c1, c2):
    return c1 * x**2 + c2

def f_nlogn(x, c1, c2):
    return c1 * x * np.log(x) + c2

def ajustar_logaritmo(x, resultados):
    coeficientes, _ = sp.optimize.curve_fit(f_nlogn, x, [resultados[n] for n in x])
    return coeficientes

def ajustar_funcion_cuadratica(x, resultados):
    coeficientes, _ = sp.optimize.curve_fit(f_cuadratica, x, [resultados[n] for n in x])
    return coeficientes

def graficar_tiempos_ajuste_cuadratico(x, resultados, coeficientes):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, [resultados[n] for n in x], '-o', markersize = 5, color = 'b', label = 'Medicion')
    ax.plot(x, [f_cuadratica(n, coeficientes[0], coeficientes[1]) for n in x], 'r--', label=f"Ajuste cuadrático ($c_1 = {coeficientes[0]:.2e}$, $c_2 = {coeficientes[1]:.2e}$)")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    plt.show()

def graficar_tiempos_ajuste_logaritmico(x, resultados, coeficientes):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, [resultados[n] for n in x], '-o', markersize = 5, color = 'b', label = 'Medición')
    ax.plot(x, [f_nlogn(n, coeficientes[0], coeficientes[1]) for n in x], 'r--', label=f"Ajuste $n \log(n)$ ($c_1 = {coeficientes[0]:.2e}$, $c_2 = {coeficientes[1]:.2e}$)")
    ax.plot(x, [f_cuadratica(n, coeficientes[0], coeficientes[1]) for n in x], 'g--', label="Ajuste $n^2$")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')
    ax.legend()
    plt.show()

def calcular_error_cuadratico(x, resultados, coeficientes):
    errors = [np.abs(f_cuadratica(n, coeficientes[0], coeficientes[1]) - resultados[n]) for n in x]
    sse = np.sum(np.power(errors, 2))
    return errors, sse

def calcular_error_logaritmico(x, resultados, coeficientes):
    errors = [np.abs(f_nlogn(n, coeficientes[0], coeficientes[1]) - resultados[n]) for n in x]
    sse = np.sum(np.power(errors, 2))
    return errors, sse

def graficar_error(x, errors, sse):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x, errors, '-o', markersize = 5, color = 'b', label = "Error")
    plt.text(0.05, 0.95, f'SSE = {sse:.10f}', ha='left', va='top', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
    ax.set_title('Error del ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()
    plt.show()

def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Ejecutar mediciones")
    
    parser.add_argument('--min', type=int, default=100, help='Tamaño mínimo del array (por defecto 100)')
    parser.add_argument('--max', type=int, default=1_000, help='Tamaño máximo del array (por defecto 1.000)')
    parser.add_argument('--p', type=int, default=20, help='Cantidad de puntos (por defecto 20)')
    parser.add_argument('--optimize', type=bool, default=False, help='Modo de generación optima de datos (por defecto false)')

    args = parser.parse_args()
    return args.min, args.max, args.p, args.optimize

def main():
    # Obtener los argumentos desde la línea de comandos o usar valores por defecto
    valor_minimo, valor_maximo, cantidad_puntos, modo = parsear_argumentos()

    print(f"Valor minimo: {valor_minimo}")
    print(f"Valor maximo: {valor_maximo}")
    print(f"Cantidad de puntos: {cantidad_puntos}\n")
    print(f"Ejecutando en modo datos optimos: {modo}")

    # Generamos un arreglo con 'cantidad_puntos' valores distribuidos uniformemente entre 'valor_minimo' y 'valor_maximo'
    # Estos puntos x son los valores del eje x de los graficos
    # Representan la cantidad de elementos (n)
    x = np.linspace(valor_minimo, valor_maximo, cantidad_puntos).astype(int)

    print(f"Cantidad de elementos (cada elemento i es la cantidad de elementos de la invocacion i): {x}\n")

    # Medición de tiempo del algoritmo
    # El algoritmo se ejecuta len(x) veces con cada valor de x
    # La funcion 'generar_entrada' recibe un valor n que proviene del arreglo x y devuelve una entrada aleatoria para la funcion 'encontrar_rata'
    resultados = time_algorithm(encontrar_rata, x, lambda n: generar_entrada(n, valor_minimo, valor_maximo, modo))

    # Tecnica de cuadrados minimos: Ajusta los parametros c1 y c2 de la funcion cuadratica a los datos de la medicion
    coeficientes = ajustar_funcion_cuadratica(x, resultados) if not modo else ajustar_logaritmo(x, resultados)
    print(f"Coeficientes obtenidos del ajuste {'logarítmico' if modo else 'cuadrático'}: c_1 = {coeficientes[0]}, c_2 = {coeficientes[1]}\n")

    # Graficar los resultados y ajuste
    graficar_tiempos_ajuste_cuadratico(x, resultados, coeficientes) if not modo else graficar_tiempos_ajuste_logaritmico(x, resultados, coeficientes)

    # Calcular el error cuadrático
    errors, sse = calcular_error_cuadratico(x, resultados, coeficientes) if not modo else calcular_error_logaritmico(x, resultados, coeficientes)
    print(f"Error logarítmico total (SSE): {sse:.10f}")

    # Graficar el error cuadrático
    graficar_error(x, errors, sse)

if __name__ == "__main__":
    main()
