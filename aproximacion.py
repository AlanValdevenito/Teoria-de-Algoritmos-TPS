import sys, heapq, time
from utils import crear_grafo, parsear_argumentos
from grafo import Grafo

def obtener_aristas(grafo):
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if (w, v) not in aristas: 
                aristas.append((v, w))
    return aristas

def modularizacion(grafo, comunidades):
    Q = 0
    m = len(obtener_aristas(grafo))

    for i in grafo.obtener_vertices():
        for j in grafo.adyacentes(i):
            if comunidades[i] == comunidades[j]:
                peso_ij = grafo.peso_arista(i, j)
                k_i = len(grafo.adyacentes(i))
                k_j = len(grafo.adyacentes(j))
    
                Q += peso_ij - (k_i * k_j) / (2 * m)

    return Q / (2*m)


def mejor_comunidad(grafo, comunidades, nodo):
    original = comunidades[nodo]
    vecinos = grafo.adyacentes(nodo)
    comunidades_vecinas = set(comunidades[v] for v in vecinos)
    mejor_delta = 0
    mejor_com = original

    for c in comunidades_vecinas:
        comunidades[nodo] = c
        nueva_mod = modularizacion(grafo, comunidades)
        comunidades[nodo] = original
        actual_mod = modularizacion(grafo, comunidades)
        delta_Q = nueva_mod - actual_mod

        if delta_Q > mejor_delta:
            mejor_delta = delta_Q
            mejor_com = c

    return mejor_com, mejor_delta

def fase1(grafo, comunidades):
    cambiado = True
    while cambiado:
        cambiado = False
        for nodo in grafo.obtener_vertices():
            mejor, delta = mejor_comunidad(grafo, comunidades, nodo)

            if comunidades[nodo] != mejor and delta > 0:
                comunidades[nodo] = mejor
                cambiado = True

    return comunidades

def fase2(grafo, comunidades):
    nuevo_grafo = Grafo(False)
    clusters = agrupar_por_comunidad(comunidades)

    for c in clusters:
        nuevo_grafo.agregar_vertice(c)

    for v, w in obtener_aristas(grafo):
        c1, c2 = comunidades[v], comunidades[w]
        peso = grafo.peso_arista(v, w)

        if not nuevo_grafo.pertenece_vertice(c1):
            nuevo_grafo.agregar_vertice(c1)
        if not nuevo_grafo.pertenece_vertice(c2):
            nuevo_grafo.agregar_vertice(c2)
        if nuevo_grafo.estan_unidos(c1, c2):
            nuevo_peso = nuevo_grafo.peso_arista(c1, c2) + peso
            nuevo_grafo.agregar_arista(c1, c2, nuevo_peso)
        else:
            nuevo_grafo.agregar_arista(c1, c2, peso)

    return nuevo_grafo

def algoritmo_louvain(grafo, K):
    comunidades = {v: v for v in grafo.obtener_vertices()}
    i = 0
    while True:
        i += 1
        comunidades = fase1(grafo, comunidades)
        nuevo_grafo = fase2(grafo, comunidades)
        if len(nuevo_grafo.obtener_vertices()) == len(grafo.obtener_vertices()) or len(nuevo_grafo.obtener_vertices()) <= K:
            break

        nuevas_comunidades = {}
        for v in grafo.obtener_vertices():
            nuevas_comunidades[v] = comunidades[v]

        grafo = nuevo_grafo
        comunidades = nuevas_comunidades

    return comunidades

def agrupar_por_comunidad(comunidades):
    clusters = {} 
    for v, c in comunidades.items():
        if c not in clusters:
            clusters[c] = []
        clusters[c].append(v)
    return clusters

def calcular_diametros(grafo, comunidades):
    clusters = agrupar_por_comunidad(comunidades)
    diametros = {}

    for comunidad, nodos in clusters.items():
        max_distancia = 0
        for nodo in nodos:
            distancias = dijkstra(grafo, nodo, comunidad, comunidades)
            max_en_este_nodo = max([d for d in distancias.values() if d < float('inf')], default=0)
            max_distancia = max(max_distancia, max_en_este_nodo)
        diametros[comunidad] = max_distancia

    return diametros

def dijkstra(grafo, origen, comunidad, comunidades):
    distancias = {v: float('inf') for v in grafo.obtener_vertices() if comunidades[v] == comunidad}
    distancias[origen] = 0
    heap = [(0, origen)]

    while heap:
        dist, v = heapq.heappop(heap)
        if dist > distancias[v]:
            continue
        for w in grafo.adyacentes(v):
            if comunidades[w] != comunidad:
                continue 
            peso = grafo.peso_arista(v, w)
            if distancias[w] > dist + peso:
                distancias[w] = dist + peso
                heapq.heappush(heap, (distancias[w], w))
    return distancias

def aproximacion(grafo, k):
    asignacion = algoritmo_louvain(grafo, k)
    clusters = agrupar_por_comunidad(asignacion)
    diametros = calcular_diametros(grafo, asignacion)

    return clusters, diametros

def main():
    args = parsear_argumentos()

    grafo = crear_grafo(args.archivo)

    if args.adyacentes:
        print("Adyacentes del grafo:")
        print(f"{grafo}\n")

    if args.temporizador:
        inicio = time.time()

    clusters, diametros = aproximacion(grafo, args.clusters)

    if args.temporizador:
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos\n")
    
    print("Asignación:")
    for idx, (_, nodos) in enumerate(clusters.items()):
        print(f"Cluster {idx} : {nodos}")

    print("\nDiámetros de cada comunidad:")
    for comunidad, diametro in diametros.items():
        print(f"Comunidad {comunidad}: Diámetro máximo {diametro}")

if __name__ == '__main__':
    main()
