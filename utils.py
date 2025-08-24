import re

import random
import string
import requests

URL_PALABRAS = "https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/refs/heads/master/0_palabras_todas.txt"

def leer_palabras(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def leer_cadena_desencriptada(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def leer_archivo_esperado(filename, archivo_palabras, archivo_cadena_desencriptada):
    resultado_buscado = (archivo_palabras, archivo_cadena_desencriptada)
    resultado_actual = None

    resultados = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if (resultado_actual == resultado_buscado) and not line:
                break

            if not line:
                continue

            match = re.match(r'Palabras:\s(.+),\sentrada:\s*(.+)', line)

            if match:
                resultado_actual = tuple(m.strip() for m in match.groups())
                continue

            if (resultado_actual == resultado_buscado):
                resultados.append(line)

    return resultados

def generar_entrada_aleatoria(cantidad_palabras, cantidad_palabras_desencriptadas, largo_maximo_palabras, valido):
    palabras = requests.get(URL_PALABRAS).text.splitlines()

    palabras_validas = [p.lower() for p in palabras if p.isalpha() and len(p) >= 3 and len(p) <= largo_maximo_palabras]

    palabras_elegidas = random.sample(palabras_validas, cantidad_palabras)

    if valido:
        palabras_aleatorias = random.choices(palabras_elegidas, k = cantidad_palabras_desencriptadas)
        cadena_desencriptada_elegida = ''.join(palabras_aleatorias)
    
    else:
        palabras_aleatorias = random.choices(palabras_elegidas, k = cantidad_palabras_desencriptadas - 1)
        cadena_desencriptada_elegida_parcial = ''.join(palabras_aleatorias)

        ruido = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 10)))
        indice_ruido = random.randint(0, len(cadena_desencriptada_elegida_parcial))
        
        cadena_desencriptada_elegida = (
            cadena_desencriptada_elegida_parcial[:indice_ruido] +
            ruido +
            cadena_desencriptada_elegida_parcial[indice_ruido:]
        )

    return palabras_elegidas, cadena_desencriptada_elegida

def guardar_entrada_aleatoria(ruta_archivo_palabras, palabras, ruta_archivo_cadena, cadena_desencriptada):

    with open(ruta_archivo_palabras, "w", encoding="utf-8") as archivo_palabras:
        for palabra in palabras:
            archivo_palabras.write(palabra + "\n")

    with open(ruta_archivo_cadena, "w", encoding="utf-8") as archivo_cadena:
        archivo_cadena.write(cadena_desencriptada)

def verificador(palabras, cadena_desencriptada, mensaje):

    # Verificamos que todas las palabras del mensaje se encuentren en el diccionario
    for palabra in mensaje.split():
        if palabra not in palabras:
            return False
        
    # Verificamos que la concatenacion del mensaje sea exactamente igual a la cadena desencriptada
    mensaje_concatenado = "".join(mensaje.split())
    return cadena_desencriptada == mensaje_concatenado