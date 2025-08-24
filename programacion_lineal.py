import sys

import math, sys, time
import pulp
from collections import deque
from utils import crear_grafo, parsear_argumentos

def bfs_distancias(grafo, origen):
    distancias = {origen: 0}
    visitados = set([origen])
    cola = deque([origen])

    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                distancias[w] = distancias[v] + 1
                cola.append(w)
    return distancias

def programacion_lineal(grafo, vertices, k, clusters, distancias_globales):
    n = len(vertices)
    k = min(k, n)

    # Creo el problema y agrego las variables
    problema = pulp.LpProblem("Clustering_Bajo_Diametro", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("x", [(v, c) for v in vertices for c in range(k)], cat="Binary")
    y = pulp.LpVariable.dicts("y", [c for c in range(k)], cat="Binary")
    D = pulp.LpVariable("D", lowBound=0, cat="Integer")

    problema += D

    # Agrego las restricciones
    for v in vertices:
        problema += pulp.lpSum(x[v, c] for c in range(k)) == 1, f"asignacion_{v}"

    for c in range(k):
        for v in vertices:
            problema += x[v, c] <= y[c]

    problema += pulp.lpSum(y[c] for c in range(k)) <= k, "limite_clusters"

    for u in vertices:
        for v in vertices:
            if u < v:
                d_uv = distancias_globales[u].get(v, math.inf)
                if math.isfinite(d_uv):
                    for c in range(k):
                        problema += d_uv * (x[u, c] + x[v, c] - 1) <= D, f"diametro_{u}_{v}_{c}"

    # Resuelvo el problema y reconstruyo la solucion
    status = problema.solve()

    for v in vertices:
        for c in range(k):
            if pulp.value(x[v, c]) > 0.5:
                clusters[c].append(v)
                break

    return int(pulp.value(D)), clusters
    
def clustering_bajo_diametro(grafo, k):
    
    vertices = grafo.obtener_vertices()
    vertices.sort(key=lambda v: len(grafo.adyacentes(v)), reverse=True)

    clusters = [[] for _ in range(k)]
    distancias_globales = {}
    for v in vertices:
        distancias_globales[v] = bfs_distancias(grafo, v)

    return grafo, vertices, k, clusters, distancias_globales

def clustering_bajo_diametro_pl(grafo, vertices, k, clusters, distancias_globales):
    mejor_diametro, mejor_asignacion = programacion_lineal(grafo, vertices[:], k, clusters[:], distancias_globales)

    return mejor_asignacion, mejor_diametro

def pl(grafo, k):
    grafo, vertices, k, clusters, distancias_globales = clustering_bajo_diametro(grafo, k)
    asignacion_clusters, distancia_maxima = clustering_bajo_diametro_pl(grafo, vertices, k, clusters, distancias_globales)
    return asignacion_clusters, distancia_maxima

def main():
    args = parsear_argumentos()

    grafo = crear_grafo(args.archivo)

    if args.temporizador:
        inicio = time.time()

    asignacion_clusters, distancia_maxima = pl(grafo, args.clusters)

    if args.adyacentes:
        print("Adyacentes del grafo:")
        print(f"{grafo}\n")

    if args.temporizador:
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos\n")

    print("Asignación:\n")
    for i, cluster in enumerate(asignacion_clusters):
        print(f"Cluster {i} : {cluster}")
    
    print(f"Máxima distancia dentro del cluster: {distancia_maxima}")

if __name__ == '__main__':
    main()
