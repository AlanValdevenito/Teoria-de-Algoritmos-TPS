# Trabajo Práctico 1: La mafia de los algortimos greedy

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. 

# Ejecucion

### Algoritmo Greedy

Archivos involucrados: [tp1.py](tp1.py)

Para ejecutar el algoritmo, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./tp1.py <R>
```

donde **R** es la ruta de un archivo txt que debe poseer, por ejemplo, el siguiente formato:

```
5
599,12
727,49
892,82
856,70
229,45
213
607
711
806
816
```

El resultado se mostrara por consola con, por ejemplo, el siguiente formato:

```
213 --> 229 ± 45
607 --> 599 ± 12
711 --> 727 ± 49
806 --> 856 ± 70
816 --> 892 ± 82
```

**Adicional:** Cualquier linea que arraque con un '#' sera considerado un comentario y no se tendra en cuenta.

Tambièn es posible ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./tp1.py <R> -v
```

donde **R** es la ruta de un archivo txt con el formato mencionado anteriormente y el flag **-v** se utiliza para validar 
que la asignacion sea correcta.

Una asignacion es correcta si
1. La transacción está dentro del intervalo asignado.
2. Hay una relacion 1 a 1 entre las transacciones y los intervalos. Es decir, no puede haber un mismo intervalo asignado a 2 o mas transacciones.

### Pruebas

Archivos involucrados: [tests.py](tests/tests.py)

Para ejecutar los tests, se debe ejecutar el siguiente comando por consola sobre el directorio `tests`:

```echo
python3 ./tests.py
```

Se ejecutaran los casos de prueba que se encuentran en [resources](tests/resources) y se compararan los resultados con los esperados que se encuentran en [expected](tests/expected).

Adicional: Cualquier linea que arraque con un '#' sera considerado un comentario y no se tendra en cuenta.

### Generador

Archivos involucrados: [generador.py](generador.py)

Para ejecutar el generador, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./generador.py <n> <rango minimo> <rango maximo>
```

donde **n** es la cantidad de elementos, **rango minimo** es el valor minimo y **rango maximo** es el valor maximo que podran tomar los timestamps.

El generador guardara el resultado en la ruta **tests/gen** con, por ejemplo, el siguiente formato:

```
10
408,804
281,260
370,384
196,115
310,905
679,827
794,672
132,502
826,52
510,90
162
166
322
433
531
548
572
623
674
815
```

y el siguiente nombre: **gen-n-rango_minimo-rango_maximo**.

### Mediciones

Archivos involucrados: [mediciones.py](mediciones/mediciones.py)

Para ejecutar el codigo relacionado a las mediciones, se debe ejecutar el siguiente comando por consola sobre el directorio `mediciones`:

```echo
python3 ./mediciones.py --min <valor> --max <valor> --p <valor>
```

donde el flag **--p** indica la cantidad de elementos, el flag **--min** indica el valor minimo y el flag **--max** indica el valor maximo que pueden tomar los timestamps/errores.

Se mostraran dos ventanas, la primera con un grafico del ajuste cuadratico y la segunda con un grafico del error.

Para el grafico del error, se utiliza el error cuadratico total (SSE) el cual se calcula como

$SSE = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

donde $y_i$ es el valor real, $\hat{y}_i$ es el valor predicho y $n$ la cantidad de puntos.

# Dependencias

### Mediciones

```echo
sudo apt update
sudo apt install python3-pip
```

```echo
pip install matplotlib
```

```echo
pip install seaborn
```

```echo
pip install spicy
```

# Licencia

Este repositorio se encuentra bajo la Licencia MIT.