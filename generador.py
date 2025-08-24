import sys
from utils import generar_entrada_aleatoria, parsear_generacion, guardar_archivo

RUTA_ARCHIVO = "tests/gen/gen-"
SEPARADOR = "-"

def main():

    if len(sys.argv) < 3:
        print("Por favor, indique la cantidad de elementos y el rango de valores")
        return
    
    n = int(sys.argv[1])
    rango_min = int(sys.argv[2])
    rango_max = int(sys.argv[3])

    timestamps_aproximados, transacciones = generar_entrada_aleatoria(n, rango_min, rango_max)

    entrada_parseada = parsear_generacion(timestamps_aproximados, transacciones)

    archivo = RUTA_ARCHIVO + str(n) + SEPARADOR + str(rango_min) + SEPARADOR + str(rango_max)
    guardar_archivo(archivo, entrada_parseada)

if __name__ == '__main__':
    main()