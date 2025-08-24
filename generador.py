import argparse

from utils import generar_grafo_lista

def main():
    parser = argparse.ArgumentParser(description="Genera un grafo con forma de lista.")
    parser.add_argument("archivo", type=str, help="Nombre del archivo de salida")
    parser.add_argument("vertices", type=int, help="Cantidad de vértices (mínimo 2)")

    args = parser.parse_args()

    try:
        generar_grafo_lista(args.archivo, args.vertices)
        print(f"Grafo generado correctamente en la ruta '/data/gen/{args.archivo}' con {args.vertices} vértices")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()