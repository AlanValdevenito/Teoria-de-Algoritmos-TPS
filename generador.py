import sys
from utils import generar_entrada_aleatoria, guardar_entrada_aleatoria

RUTA_ARCHIVO_PALABRAS = "tests/gen/gen-palabras-"
RUTA_ARCHIVO_CADENA = "tests/gen/gen-cadena-"
SEPARADOR = "-"

TRUE = "true"

def main():

    if len(sys.argv) < 3:
        print("Por favor, indique la cantidad de elementos y el rango de valores")
        return
    
    cantidad_palabras = int(sys.argv[1])
    cantidad_palabras_desencriptadas = int(sys.argv[2])
    largo_maximo_palabras = int(sys.argv[3])
    valido = (sys.argv[4].lower() == TRUE)

    palabras, cadena_desencriptada = generar_entrada_aleatoria(cantidad_palabras, cantidad_palabras_desencriptadas, largo_maximo_palabras, valido)

    ruta_archivo_palabras = RUTA_ARCHIVO_PALABRAS + str(cantidad_palabras) + SEPARADOR + str(largo_maximo_palabras) + SEPARADOR + str(sys.argv[4].lower())
    ruta_archivo_cadena = RUTA_ARCHIVO_CADENA + str(cantidad_palabras_desencriptadas) + SEPARADOR + str(largo_maximo_palabras) + SEPARADOR + str(sys.argv[4].lower())
    guardar_entrada_aleatoria(ruta_archivo_palabras, palabras, ruta_archivo_cadena, cadena_desencriptada)

if __name__ == '__main__':
    main()