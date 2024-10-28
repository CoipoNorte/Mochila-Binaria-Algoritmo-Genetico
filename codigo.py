import pandas as pd
import random
import os
from datetime import datetime

# Variables globales para el algoritmo
capacidad_maxima = 200
tamaño_poblacion = 100
tasa_cruce = 0.8
tasa_mutacion = 0.05
generaciones = 100

# Cargar datos desde CSV
def cargar_datos_csv(ruta_csv):
    datos = pd.read_csv(ruta_csv)
    valores = datos['valor'].tolist()
    pesos = datos['peso'].tolist()
    return valores, pesos

# Ajustar la capacidad máxima global
def actualizar_capacidad(nueva_capacidad):
    global capacidad_maxima
    capacidad_maxima = nueva_capacidad

# Funciones auxiliares del algoritmo
def fitness(cromosoma, valores, pesos):
    peso_total = sum(p * c for p, c in zip(pesos, cromosoma))
    valor_total = sum(v * c for v, c in zip(valores, cromosoma))
    if peso_total > capacidad_maxima:
        return 0  # Asigna un valor de fitness de 0 si el peso excede la capacidad
    return valor_total

def generar_cromosoma_valido(n_items, pesos):
    cromosoma = [0] * n_items
    while True:
        for i in range(n_items):
            cromosoma[i] = random.randint(0, 1)
        peso_total = sum(p * c for p, c in zip(pesos, cromosoma))
        if peso_total <= capacidad_maxima:
            return cromosoma

def seleccion(poblacion, valores, pesos):
    seleccionados = random.choices(poblacion, weights=[fitness(c, valores, pesos) for c in poblacion], k=2)
    return seleccionados

def crossover(parent1, parent2):
    if random.random() < tasa_cruce:
        punto_cruce = random.randint(1, len(parent1) - 1)
        child1 = parent1[:punto_cruce] + parent2[punto_cruce:]
        child2 = parent2[:punto_cruce] + parent1[punto_cruce:]
        return child1, child2
    return parent1, parent2

def mutation(cromosoma):
    for i in range(len(cromosoma)):
        if random.random() < tasa_mutacion:
            cromosoma[i] = 1 - cromosoma[i]
    return cromosoma

# Mostrar detalles de la mejor solución en un formato más ordenado
def mostrar_mejor_solucion(mejor_solucion, valores, pesos):
    solucion_str = []
    solucion_str.append("\nMejor Solución:")
    solucion_str.append(f"Configuración del Cromosoma: {mejor_solucion}")
    solucion_str.append("Objetos seleccionados:")
    total_valor = 0
    total_peso = 0
    for i, selected in enumerate(mejor_solucion):
        if selected == 1:
            solucion_str.append(f" - Objeto {i+1}: Valor = {valores[i]}, Peso = {pesos[i]}")
            total_valor += valores[i]
            total_peso += pesos[i]
    solucion_str.append(f"Valor Total: {total_valor}")
    solucion_str.append(f"Peso Total: {total_peso}")
    solucion_str.append(f"Capacidad Máxima de la Mochila: {capacidad_maxima}")
    return "\n".join(solucion_str)

# Crear archivo de log para cada ejecución
def crear_log(contenido):
    # Crear la carpeta "log" si no existe
    if not os.path.exists("log"):
        os.makedirs("log")
    
    # Crear nombre del archivo con fecha y hora
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_numero = len(os.listdir("log")) + 1
    nombre_archivo = f"log_{log_numero}_{fecha_hora}.txt"
    
    # Guardar el archivo en la carpeta "log"
    ruta_archivo = os.path.join("log", nombre_archivo)
    with open(ruta_archivo, "w") as file:
        file.write(contenido)
    
    print(f"\nRegistro guardado en: {ruta_archivo}")

# Algoritmo Genético Principal
def algoritmo_genetico(ruta_csv):
    valores, pesos = cargar_datos_csv(ruta_csv)
    n_items = len(valores)
    poblacion = [generar_cromosoma_valido(n_items, pesos) for _ in range(tamaño_poblacion)]

    mejor_solucion_global = None
    mejor_valor_global = 0
    log_contenido = []
    top_5_mejores = []

    for generacion in range(generaciones):
        nueva_poblacion = []
        for _ in range(tamaño_poblacion // 2):
            parent1, parent2 = seleccion(poblacion, valores, pesos)
            child1, child2 = crossover(parent1, parent2)
            nueva_poblacion.append(mutation(child1))
            nueva_poblacion.append(mutation(child2))
        poblacion = nueva_poblacion

        # Evaluar las soluciones válidas de esta generación
        soluciones_validas = [c for c in poblacion if sum(p * s for p, s in zip(pesos, c)) <= capacidad_maxima]
        if not soluciones_validas:
            continue
        
        mejor_solucion = max(soluciones_validas, key=lambda c: fitness(c, valores, pesos))
        mejor_valor = fitness(mejor_solucion, valores, pesos)

        # Actualizar la mejor solución global si cumple con la capacidad
        if mejor_valor > mejor_valor_global:
            mejor_valor_global = mejor_valor
            mejor_solucion_global = mejor_solucion

        # Guardar soluciones válidas para el top 5
        top_5_mejores.extend([(c, fitness(c, valores, pesos)) for c in soluciones_validas])
        
        # Mostrar y registrar detalles de la generación actual
        generacion_info = f"\nGeneración {generacion + 1}:\nMejor Valor en esta generación: {mejor_valor}"
        print(generacion_info)
        log_contenido.append(generacion_info)

    # Ordenar y mostrar las 5 mejores soluciones válidas
    top_5_mejores = sorted(top_5_mejores, key=lambda x: x[1], reverse=True)[:5]
    top_5_str = "\nTop 5 Mejores Soluciones:\n"
    for idx, (sol, val) in enumerate(top_5_mejores, 1):
        peso = sum(p * s for p, s in zip(pesos, sol))
        top_5_str += f"{idx}. Valor: {val}, Peso: {peso}, Configuración: {sol}\n"
    print(top_5_str)
    log_contenido.append(top_5_str)

    # Preparar resultados finales para el log
    resultado_final = mostrar_mejor_solucion(mejor_solucion_global, valores, pesos)
    log_contenido.append(resultado_final)
    
    # Crear log de la ejecución
    crear_log("\n".join(log_contenido))

    return mejor_solucion_global, mejor_valor_global, valores, pesos

# Configurar y ejecutar desde la consola
if __name__ == "__main__":
    print("Algoritmo Genético - Problema de la Mochila")
    
    # Configuración automática del CSV
    ruta_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'objetos.csv')
    
    # Solicitar configuración y usar valores globales si la entrada está vacía
    try:
        capacidad_maxima = int(input(f"Capacidad máxima de la mochila (Entero) [{capacidad_maxima}]: ") or capacidad_maxima)
        tamaño_poblacion = int(input(f"Tamaño de la población (Entero entre 1 - 100) [{tamaño_poblacion}]: ") or tamaño_poblacion)
        tasa_cruce = float(input(f"Tasa de cruce (Decimal entre 0.0 - 1.0) [{tasa_cruce}]: ") or tasa_cruce)
        tasa_mutacion = float(input(f"Tasa de mutación (Decimal entre 0.0 - 1.0) [{tasa_mutacion}]: ") or tasa_mutacion)
        generaciones = int(input(f"Número de generaciones (Entero) [{generaciones}]: ") or generaciones)
    except ValueError:
        print("Entrada no válida. Usando valores globales por defecto.")

    # Actualizar la capacidad máxima global
    actualizar_capacidad(capacidad_maxima)
    
    # Ejecutar el algoritmo
    mejor_solucion, valor_maximo, valores, pesos = algoritmo_genetico(ruta_csv)

    # Mostrar resultados finales
    print(mostrar_mejor_solucion(mejor_solucion, valores, pesos))

# CoipoNorte