import sys

from utils import leer_palabras, verificador

INDEX_BOOL = 0
INDEX_PALABRA = 1

def encontrar_soplon_solucion(mem, n):

    if not mem[n][INDEX_BOOL]:
        return "No es un mensaje"

    solucion = []

    while n > 0:

        if mem[n][INDEX_PALABRA]:
            solucion.append(mem[n][INDEX_PALABRA])
            n -= len(mem[n][INDEX_PALABRA])

        else:
            return "No es un mensaje"

    solucion.reverse()
    return " ".join(solucion)

def encontrar_soplon_dinamico(palabras, cadena_desencriptada, n):
    mem = [(False, "")] * (n + 1)
    mem[0] = (True, "")

    for i in range(1, n + 1):
        for p in palabras:
            j = len(p)

            if (cadena_desencriptada[i - j:i] == p) and mem[i - j][INDEX_BOOL]:
                mem[i] = (True, p)
                break

    return mem

def encontrar_soplon(palabras, cadena_desencriptada):
    n = len(cadena_desencriptada)
    mem = encontrar_soplon_dinamico(palabras, cadena_desencriptada, n)
    solucion = encontrar_soplon_solucion(mem, n)
    return solucion    

def main():

    if len(sys.argv) < 2:
        raise ValueError("Por favor, indique la ruta de un archivo de texto")

    archivo_palabras = sys.argv[1]

    palabras = leer_palabras(archivo_palabras)

    for cadena_desencriptada in sys.stdin:
        cadena_desencriptada = cadena_desencriptada.rstrip()

        if cadena_desencriptada:
            resultado = encontrar_soplon(palabras, cadena_desencriptada)
            print(resultado)

            if (resultado != 'No es un mensaje') and len(sys.argv) > 2 and (sys.argv[2] == '-v'):
                valido = verificador(palabras, cadena_desencriptada, resultado)
                print(f"El mensaje es valido: {valido}")

if __name__ == '__main__':
    main()