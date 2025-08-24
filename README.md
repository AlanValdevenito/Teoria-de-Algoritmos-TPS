# Trabajo Práctico 3: Comunidades NP-Completas

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de Backtracking para resolver un Problema NP-Completo, así como el análisis de posibles aproximaciones. 

# Ejecucion

### Algoritmo BT

Archivos involucrados: [backtraking.py](backtracking.py)

Para ejecutar el algoritmo, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./backtraking.py <R> <K>
```

donde **R** es la ruta de un archivo txt/csv que representa el grafo y que debe poseer, por ejemplo, el siguiente formato:

```
0,1
0,8
1,4
1,3
1,5
1,6
1,9
2,7
2,3
2,5
3,4
3,6
3,7
3,5
4,9
5,7
5,8
6,7
7,9
8,9
```

y donde **K** es un valor entero que representa la cantidad de clusters.

Tambien es posible ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./backtraking.py <R> <K> -t -a
```

donde el flag **-t** se utiliza para cronometrar el tiempo de ejecucion de nuestro algoritmo y el flag **-a** muestra los adyacentes del grafo elegido.

Para mas informacion sobre los argumentos y flags se puede ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./backtraking.py -h
```

donde el flag **-h** se utiliza para mostrar una ayuda rapida sobre el funcionamiento.

### Algoritmo PL

Archivos involucrados: [programacion_lineal.py](programacion_lineal.py)

Para ejecutar el algoritmo, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./programacion_lineal.py <R> <K>
```

donde **R** es la ruta de un archivo txt/csv que representa el grafo y que debe poseer, por ejemplo, el siguiente formato:

```
0,1
0,8
1,4
1,3
1,5
1,6
1,9
2,7
2,3
2,5
3,4
3,6
3,7
3,5
4,9
5,7
5,8
6,7
7,9
8,9
```

y donde **K** es un valor entero que representa la cantidad de clusters.

Tambien es posible ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./programacion_lineal.py <R> <K> -t -a
```

donde el flag **-t** se utiliza para cronometrar el tiempo de ejecucion de nuestro algoritmo y el flag **-a** muestra los adyacentes del grafo elegido.

Para mas informacion sobre los argumentos y flags se puede ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./programacion_lineal.py -h
```

donde el flag **-h** se utiliza para mostrar una ayuda rapida sobre el funcionamiento.

### Algoritmo Aproximacion

Archivos involucrados: [aproximacion.py](aproximacion.py)

Para ejecutar el algoritmo, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./aproximacion.py <R> <K>
```

donde **R** es la ruta de un archivo txt/csv que representa el grafo y que debe poseer, por ejemplo, el siguiente formato:

```
0,1
0,8
1,4
1,3
1,5
1,6
1,9
2,7
2,3
2,5
3,4
3,6
3,7
3,5
4,9
5,7
5,8
6,7
7,9
8,9
```

y donde **K** es un valor entero que representa la cantidad de clusters.

Tambien es posible ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./aproximacion.py <R> <K> -t -a
```

donde el flag **-t** se utiliza para cronometrar el tiempo de ejecucion de nuestro algoritmo y el flag **-a** muestra los adyacentes del grafo elegido.

Para mas informacion sobre los argumentos y flags se puede ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./aproximacion.py -h
```

donde el flag **-h** se utiliza para mostrar una ayuda rapida sobre el funcionamiento.

# Licencia

Este repositorio se encuentra bajo la Licencia MIT.
