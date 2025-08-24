import re
import random

def leer_archivo(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip() and not line.startswith("#")]

    n = int(lines[0])

    timestamps_aproximados = []

    for i in range(1, n + 1):
        t, e = map(int, lines[i].split(','))
        timestamps_aproximados.append((t,e))

    transacciones = [int(lines[i]) for i in range(n + 1, 2 * n + 1)]

    return timestamps_aproximados, transacciones

def leer_archivo_esperado(filename, archivo_buscado):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip() and not line.startswith("#")]

    archivo_actual = None
    resultados = []

    for line in lines:
        line = line.strip()

        if line.endswith(".txt"):
            archivo_actual = line
            continue

        if archivo_actual == archivo_buscado:
            if "No es el sospechoso correcto" in line:
                return "No es el sospechoso correcto"

            izquierda, derecha = line.split(" --> ")
            transaccion = int(izquierda)
            timestamp, error = map(int, derecha.replace("±", "").split())
            resultados.append(f"{transaccion} --> {timestamp} ± {error}")

    return "\n".join(resultados) if resultados else "Archivo no encontrado"

def formatear_resultado(resultado):
    resultado = "\n".join(f"{transaccion} --> {timestamp} ± {error}" for transaccion, (timestamp, error) in resultado)
    return resultado

def parsear_asignaciones(asignaciones):
    transacciones = []
    ts_aproximados = []

    for linea in asignaciones.strip().split("\n"):
        match = re.match(r"(\d+)\s-->\s(\d+)\s±\s(\d+)", linea)
        if match:
            transaccion = int(match.group(1))
            ts = int(match.group(2))
            error = int(match.group(3))

            transacciones.append(transaccion)
            ts_aproximados.append((ts, error))

    return transacciones, ts_aproximados

def validar_asignaciones(timestamps, transacciones, resultado):
    transacciones_resultado, timestamps_resultado = parsear_asignaciones(resultado) # Cada transaccion i se corresponde con el intervalo i
    
    contador = {t: timestamps.count(t) for t in timestamps}

    for i, transaccion in enumerate(transacciones_resultado):

        ts, error = timestamps_resultado[i]
        izq, der = ts - error, ts + error

        # La transacción no está dentro del intervalo
        if not (izq <= transaccion <= der):
            return [False]

        # El intervalo ya fue usado por otra transaccion
        # Esto no puede suceder ya que debe haber una transaccion por cada intervalo (a menos que el intervalo este repetido)
        if contador[timestamps_resultado[i]] <= 0:
            return [False, timestamps_resultado[i]]
        
        contador[timestamps_resultado[i]] -= 1

    return [True]

def guardar_archivo(nombre_archivo, generacion_parseada):

    with open(nombre_archivo, 'w') as file:
        file.write(generacion_parseada)

def parsear_generacion(timestamps_aproximados, transacciones):
    n = len(transacciones)
    resultado = []

    resultado.append(str(n))

    for timestamp, error in timestamps_aproximados:
        resultado.append(f"{timestamp},{error}")

    for transaccion in transacciones:
        resultado.append(str(transaccion))

    return "\n".join(resultado)

def generar_timestamps_aleatorios(n, ts_min, ts_max):
    timestamps = [random.randint(ts_min, ts_max) for _  in range(n)]
    return timestamps

def generar_errores_por_timestamp_aleatorios(timestamps):
    errores = [random.randint(0, ts) for ts in timestamps]
    return errores

def generar_transacciones_ordenadas_aleatorias(n, ts_min, ts_max):
    transacciones = [random.randint(ts_min, ts_max) for _  in range(n)]
    transacciones.sort()
    return transacciones

def generar_entrada_aleatoria(n, rango_min = 0, rango_max = 1000):
    timestamps = generar_timestamps_aleatorios(n, rango_min, rango_max)
    errores = generar_errores_por_timestamp_aleatorios(timestamps)
    timestamps_aproximados = list(zip(timestamps, errores))

    transacciones = generar_transacciones_ordenadas_aleatorias(n, rango_min, rango_max)

    return timestamps_aproximados, transacciones

def generar_timestamps_optimos(n, salto):
    return [i for i in range(salto, (n+1)*salto, salto)]

def generar_errores_por_timestamp_optimos(timestamps, salto):
    return [salto//2 for i in range(len(timestamps))]

def generar_entrada_optima(n, salto):
    timestamps = generar_timestamps_optimos(n, salto)
    errores = generar_errores_por_timestamp_optimos(timestamps, salto)
    timestamps_aproximados = list(zip(timestamps, errores))

    transacciones = timestamps[:]

    return timestamps_aproximados, transacciones
