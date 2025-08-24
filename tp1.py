import sys

from utils import formatear_resultado, leer_archivo, validar_asignaciones

TIMESTAMP = 0
ERROR = 1

def encontrar_rata(timestamps, transacciones):
    timestamps_ordenados = sorted(timestamps, key=lambda x: x[TIMESTAMP] - x[ERROR])
    asignaciones = []

    for t in transacciones:

        if not timestamps_ordenados:
            break

        ts_index = obtener_timestamp(timestamps_ordenados, t)
        
        if ts_index is None:
            return "No es el sospechoso correcto"
        
        asignaciones.append((t, timestamps_ordenados.pop(ts_index)))
    
    return formatear_resultado(asignaciones)

def obtener_timestamp(timestamps, transaccion):
    min_der = ()

    for i in range(0, len(timestamps)):
        izq = timestamps[i][TIMESTAMP] - timestamps[i][ERROR]
        der = timestamps[i][TIMESTAMP] + timestamps[i][ERROR]

        if not (izq <= transaccion <= der):

            if len(min_der) == 0:
                return None

            break

        if (len(min_der) == 0) or (der < min_der[0]):
            min_der = (der, i)

    return min_der[1]

def main():

    if len(sys.argv) < 2:
        print("Por favor, indique la ruta de un archivo de texto")
        return

    nombre_archivo = sys.argv[1]

    timestamps_aproximados, transacciones = leer_archivo(nombre_archivo)

    resultado = encontrar_rata(timestamps_aproximados, transacciones)

    print(resultado)

    if (resultado == "No es el sospechoso correcto"): return

    if len(sys.argv) > 2 and (sys.argv[2] == '-v'):
        validacion = validar_asignaciones(timestamps_aproximados, transacciones, resultado)
        print(f"\nEl algoritmo encontro una asignacion valida: {validacion[0]}")

        if not validacion[0]:
            print(f"El intervalo asignado mas de 1 vez es: {validacion[1][0]} ± {validacion[1][1]}")

if __name__ == '__main__':
    main()