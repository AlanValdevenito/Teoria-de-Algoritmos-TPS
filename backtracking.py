import math, time
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

def es_valido_extender(cluster, v, distancias_globales, mejor_resultado, distancia_actual_cluster, aristas_usadas):
    nueva_distancia = distancia_actual_cluster
    nuevas_aristas = []

    for w in cluster:
        a1 = (v, w)
        a2 = (w, v)

        if a1 in aristas_usadas or a2 in aristas_usadas:
            continue

        d = distancias_globales[v].get(w, math.inf)
        nueva_distancia = max(nueva_distancia, d)

        if nueva_distancia >= mejor_resultado:
            return False, distancia_actual_cluster, []

        nuevas_aristas.append(a1)
        nuevas_aristas.append(a2)

    return True, nueva_distancia, nuevas_aristas

def backtracking(grafo, vertices, k, clusters, indice, mejor_resultado, mejor_asignacion,
        distancias_globales, clusters_usados, distancias_cluster, aristas_usadas):

    clusters_vacios = k - clusters_usados
    if len(vertices) - indice < clusters_vacios:
        return mejor_resultado, mejor_asignacion

    if indice == len(vertices):
        peor_cluster = max(distancias_cluster[:clusters_usados])
        if peor_cluster < mejor_resultado:
            return peor_cluster, [list(cluster) for cluster in clusters[:clusters_usados]]
        return mejor_resultado, mejor_asignacion

    actual = vertices[indice]

    for i in range(clusters_usados + 1):
        if i >= k:
            continue
        if len(clusters[i]) == 0 and i != clusters_usados:
            continue

        valido, nueva_distancia, nuevas_aristas = es_valido_extender(
            clusters[i], actual, distancias_globales, mejor_resultado,
            distancias_cluster[i], aristas_usadas
        )
        if not valido:
            continue

        clusters[i].append(actual)
        vieja_distancia = distancias_cluster[i]
        distancias_cluster[i] = nueva_distancia
        for arista in nuevas_aristas:
            aristas_usadas.add(arista)

        nuevo_clusters_usados = clusters_usados
        if i == clusters_usados:
            nuevo_clusters_usados += 1

        if max(distancias_cluster[:clusters_usados + 1]) >= mejor_resultado:
            clusters[i].pop()
            distancias_cluster[i] = vieja_distancia
            for arista in nuevas_aristas:
                aristas_usadas.remove(arista)
            continue

        mejor_resultado, mejor_asignacion = backtracking(
            grafo, vertices, k, clusters, indice + 1,
            mejor_resultado, mejor_asignacion,
            distancias_globales, nuevo_clusters_usados, distancias_cluster, aristas_usadas
        )

        clusters[i].pop()
        distancias_cluster[i] = vieja_distancia
        for arista in nuevas_aristas:
            aristas_usadas.remove(arista)

    return mejor_resultado, mejor_asignacion

def clustering_bajo_diametro(grafo, k):

    vertices = grafo.obtener_vertices()
    vertices.sort(key=lambda v: len(grafo.adyacentes(v)), reverse=True)

    clusters = [[] for _ in range(k)]
    distancias_globales = {}
    for v in vertices:
        distancias_globales[v] = bfs_distancias(grafo, v)

    distancias_cluster = [0 for _ in range(k)]

    mejor_diametro, mejor_asignacion = backtracking(
        grafo, vertices, k, clusters, 0, math.inf, None,
        distancias_globales, 0, distancias_cluster, set()
    )

    return mejor_asignacion, mejor_diametro   

def main():
    args = parsear_argumentos()

    grafo = crear_grafo(args.archivo)

    if args.adyacentes:
        print("Adyacentes del grafo:")
        print(f"{grafo}\n")

    if args.temporizador:
        inicio = time.time()

    asignacion_clusters, distancia_maxima = clustering_bajo_diametro(grafo, args.clusters)

    if args.temporizador:
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos\n")

    print("Asignación:")
    for i, cluster in enumerate(asignacion_clusters):
        print(f"Cluster {i} : {cluster}")
    
    print(f"\nMáxima distancia dentro del cluster: {distancia_maxima}")

if __name__ == '__main__':
    main()
