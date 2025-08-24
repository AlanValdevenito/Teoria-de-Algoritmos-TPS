import unittest

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from utils import *
from tp2 import encontrar_soplon

class TestsMafiaDinamica(unittest.TestCase):

    def test01_encontrar_soplon_lorem_ipsum(self):
        palabras = leer_palabras('./resources/lorem_ipsum_words.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/lorem_ipsum_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'lorem_ipsum_words.txt', 'lorem_ipsum_in.txt')

        self.assertEqual(resultado, resultado_esperado)

    def test02_encontrar_soplon_corto_10_in(self):
        palabras = leer_palabras('./resources/corto.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/10_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'corto.txt', '10_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test03_encontrar_soplon_corto_50_in(self):
        palabras = leer_palabras('./resources/corto.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/50_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'corto.txt', '50_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test04_encontrar_soplon_mediano_70_in(self):
        palabras = leer_palabras('./resources/mediano.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/70_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'mediano.txt', '70_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test05_encontrar_soplon_mediano_100_in(self):
        palabras = leer_palabras('./resources/mediano.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/100_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'mediano.txt', '100_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test06_encontrar_soplon_corto_120_in(self):
        palabras = leer_palabras('./resources/corto.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/120_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'corto.txt', '120_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test07_encontrar_soplon_mediano_15_in(self):
        palabras = leer_palabras('./resources/mediano.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/15_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'mediano.txt', '15_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test08_encontrar_soplon_grande_80_in(self):
        palabras = leer_palabras('./resources/grande.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/80_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'grande.txt', '80_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)
    
    def test09_encontrar_soplon_grande_60_in(self):
        palabras = leer_palabras('./resources/grande.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/60_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'grande.txt', '60_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test10_encontrar_soplon_grande_150_in(self):
        palabras = leer_palabras('./resources/grande.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/150_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'grande.txt', '150_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def test11_encontrar_soplon_gigante_200_in(self):
        palabras = leer_palabras('./resources/gigante.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/200_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'gigante.txt', '200_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)
    
    def test12_encontrar_soplon_gigante_500_in(self):
        palabras = leer_palabras('./resources/gigante.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/500_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'gigante.txt', '500_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)
    
    def test13_encontrar_soplon_supergigante_2000_in(self):
        palabras = leer_palabras('./resources/supergigante.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/2000_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'supergigante.txt', '2000_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)
    
    def test14_encontrar_soplon_supergigante_5000_in(self):
        palabras = leer_palabras('./resources/supergigante.txt')
        cadenas_desencriptadas = leer_cadena_desencriptada('./resources/5000_in.txt')

        resultado = []

        for cadena_desencriptada in cadenas_desencriptadas:
            mensaje = encontrar_soplon(palabras, cadena_desencriptada)
            resultado.append(mensaje)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', 'supergigante.txt', '5000_in.txt')
        
        self.assertEqual(resultado, resultado_esperado)

if __name__ == '__main__':
    unittest.main()