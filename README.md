# Trabajo Práctico 2: Que parezca programación dinámica

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de Programación Dinámica.

# Ejecucion

### Algoritmo PD

Archivos involucrados: [tp2.py](tp2.py)

Para ejecutar el algoritmo, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./tp2.py R1 < R2
```

donde **R1** es la ruta de un archivo txt que debe poseer, por ejemplo, el siguiente formato:

```
argentina
hola
como
eso
es
zanahoria
andar
plancha
compra
reptiles
consistencia
semana
votar
as
reto
```

y donde **R2** es la ruta de un archivo txt con las posibles cadenas que podrian ser mensajes a detectar (una por linea) que debe poseer, por ejemplo, el siguiente formato:

```
esandarholaargentinacompraandarplanchaplanchareptileses
argentinaesholaandarconsistenciwreptilescompraesoretozanahoria
ascomosemanasemanaconsistenciaandarzwnahoriaandarandarplancha
argentinaretocompraplanchaconsistenciaasretoargentinavotarcompra
argentinaargentinaconsistenciazanahoriaargentinaescompraholaconsistenciaargentina
esoesoholaandarandarreptilesasplanchaplanchaandar
comprasemanaescomwconsistenciaesconsistenciaretovotawsemana
argentinaandaresholaasesvotarplanchacompracompra
planchacomocomoconsistenciaesvotarzanahoriavotarandarreto
votarargentinaargentinaandarvotarvotarcomozanahoriaholaeso
holacomoandarretovotarcomprazanahoriasemanavotarargentina
comosemanaesozanahoriaconsistenciasemanaconsistenciaesoconsistenciavotar
retozanahoriasemanaasawvotarasretoargentinareto
andaresesoandarcompraasconsistenciaconsistenciaandarvotar
holaandarconsistenciaandaresoreptilesandarzanahoriaesoreptiles
retosemanaretosemanavotarcomoandarvotarholareptiles
compraandarconsistenciaargentinaesoreptilesretoplanchaasreto
consistenciaretoretoasconsistenciasemanaesosemanaholaeso
esholaholareptilesplanchaconsistenciaholaplanchavotarcomo
comprazanahoriaesozanahoriaconsistenciareptilesvotarcompraholahola
```

El resultado se mostrara por consola con, por ejemplo, el siguiente formato:

```
es andar hola argentina compra andar plancha plancha reptiles es
No es un mensaje
No es un mensaje
argentina reto compra plancha consistencia as reto argentina votar compra
argentina argentina consistencia zanahoria argentina es compra hola consistencia argentina
eso eso hola andar andar reptiles as plancha plancha andar
No es un mensaje
argentina andar es hola as es votar plancha compra compra
plancha como como consistencia es votar zanahoria votar andar reto
votar argentina argentina andar votar votar como zanahoria hola eso
hola como andar reto votar compra zanahoria semana votar argentina
como semana eso zanahoria consistencia semana consistencia eso consistencia votar
No es un mensaje
andar es eso andar compra as consistencia consistencia andar votar
hola andar consistencia andar eso reptiles andar zanahoria eso reptiles
reto semana reto semana votar como andar votar hola reptiles
compra andar consistencia argentina eso reptiles reto plancha as reto
consistencia reto reto as consistencia semana eso semana hola eso
es hola hola reptiles plancha consistencia hola plancha votar como
compra zanahoria eso zanahoria consistencia reptiles votar compra hola hola
```


Tambièn es posible ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./tp2.py R1 -v < R2
```

donde **R1** y **R2** son rutas de un archivo txt con el formato mencionado anteriormente y el flag **-v** se utiliza para validar 
que el mensaje sea correcto.

Un mensaje es correcto si
1. Todas las palabras que conforman el mensaje se encuentran en el diccionario de palabras
2. La concatenacion del mensaje es exactamente igual a la cadena desencriptada

### Pruebas

Archivos involucrados: [tests.py](tests/tests.py)

Para ejecutar los tests, se debe ejecutar el siguiente comando por consola sobre el directorio `tests`:

```echo
python3 ./tests.py
```

Se ejecutaran los casos de prueba que se encuentran en [resources](tests/resources) y se compararan los resultados con los esperados que se encuentran en [expected](tests/expected).

### Generador

Archivos involucrados: [generador.py](generador.py)

Para ejecutar el generador, se debe ejecutar el siguiente comando por consola sobre la ruta raiz del repositorio:

```echo
python3 ./generador.py <cantidad de palabras> <cantidad de palabras de la cadena desencriptada> <largo maximo de palabras> <cadena desencriptada valida>
```

donde **cadena desencriptada valida** debe ser un booleano (true/false) para indicar si se desea generar una entrada que es un mensaje o no.

El generador guardara el resultado en dos archivos distintos en la ruta **tests/gen** con, por ejemplo, el siguiente formato:

```
barboteareis
apezuñase
inspiraron
conspiras
desemballestéis
robotizare
enserenábamos
higienizas
acaserases
suri
metatizas
bipolarizabais
cuina
peptídico
porfiareis
odié
bozaleo
descentralizan
soportes
apuntilláramos
acurrucasteis
cachureen
propagáramos
esprintad
ínvido
computarizar
avoraces
desbaratásemos
entierro
escoria
prontuariasen
encompadrasteis
menguada
apreciaríais
empobrezcamos
robases
refaccionáis
desplantaba
abejeó
ahorraras
```

```
soportesacaserasesencompadrasteisahorrarasmenguadaacurrucasteisbarboteareisbozaleohigienizasahorrarasapuntilláramosrobotizareempobrezcamosdescentralizancomputarizarínvidobipolarizabaisrobasesbozaleoahorrarascuinaporfiareisbarboteareissoportesempobrezcamosdesplantabaentierroporfiareisesprintadesprintad
```

y el siguiente nombre: **gen-cadena/palabras-cantidad-largo-true/false** dependiendo del archivo generado.

# Licencia

Este repositorio se encuentra bajo la Licencia MIT.