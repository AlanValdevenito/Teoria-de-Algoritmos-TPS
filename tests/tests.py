import unittest

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from utils import *
from tp1 import encontrar_rata

class TestsMafiaGreedy(unittest.TestCase):

    def tests_encontrar_rata_5_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/5-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '5-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_5_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/5-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '5-no-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_10_es_bis(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/10-es-bis.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '10-es-bis.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_10_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/10-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '10-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_10_no_es_bis(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/10-no-es-bis.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_10_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/10-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_50_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/50-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '50-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_50_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/50-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_100_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/100-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '100-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_100_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/100-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_500_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/500-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '500-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_500_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/500-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_1000(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/1000-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '1000-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_1000_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/1000-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")

    def tests_encontrar_rata_5000_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/5000-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)

        resultado_esperado = leer_archivo_esperado('./expected/esperados.txt', '5000-es.txt')
        
        self.assertEqual(resultado, resultado_esperado)

    def tests_encontrar_rata_5000_no_es(self):
        timestamps_aproximados, timestamps = leer_archivo('./resources/5000-no-es.txt')
        resultado = encontrar_rata(timestamps_aproximados, timestamps)
        
        self.assertEqual(resultado, "No es el sospechoso correcto")
        
if __name__ == '__main__':
    unittest.main()