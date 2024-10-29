import csv
import random
import numpy as np

# Función para leer datos desde el CSV
def leer_datos_csv(nombre_archivo):
    valores = []
    pesos = []
    with open(nombre_archivo, newline='') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            valor, peso = map(int, fila)
            valores.append(valor)
            pesos.append(peso)
    return valores, pesos

# Función para mostrar los datos de los objetos en consola
def mostrar_datos(valores, pesos):
    print("Objetos en la mochila:")
    print("Índice | Valor | Peso")
    for i, (valor, peso) in enumerate(zip(valores, pesos)):
        print(f"{i+1:6} | {valor:5} | {peso:4}")

# Calcular el puntaje total (fitness) de una solución
def calcular_fitness(solucion, valores, pesos, capacidad_maxima):
    peso_total = sum(peso * seleccion for peso, seleccion in zip(pesos, solucion))
    valor_total = sum(valor * seleccion for valor, seleccion in zip(valores, solucion))
    return valor_total if peso_total <= capacidad_maxima else 0  # Puntaje 0 si excede la capacidad

# Crear una solución inicial casi vacía
def crear_solucion_casi_vacia(num_objetos, porcentaje_inicial=0.1):
    solucion = [0] * num_objetos
    num_seleccionados = int(num_objetos * porcentaje_inicial)
    indices = random.sample(range(num_objetos), num_seleccionados)
    for idx in indices:
        solucion[idx] = 1
    return solucion

# Crear una población inicial con mochilas casi vacías
def crear_poblacion(num_objetos, tamaño_poblacion, porcentaje_inicial=0.1):
    return [crear_solucion_casi_vacia(num_objetos, porcentaje_inicial) for _ in range(tamaño_poblacion)]

# Selección de padres basada en el fitness
def seleccion(poblacion, valores, pesos, capacidad_maxima):
    puntuaciones = [(solucion, calcular_fitness(solucion, valores, pesos, capacidad_maxima)) for solucion in poblacion]
    puntuaciones.sort(key=lambda x: x[1], reverse=True)
    return [solucion for solucion, puntaje in puntuaciones[:len(puntuaciones) // 2]]

# Cruce entre dos soluciones
def crossover(parent1, parent2):
    punto_cruce = random.randint(1, len(parent1) - 1)
    hijo = parent1[:punto_cruce] + parent2[punto_cruce:]
    return hijo

# Mutación de una solución
def mutacion(solucion, tasa_mutacion):
    for i in range(len(solucion)):
        if random.random() < tasa_mutacion:
            solucion[i] = 1 - solucion[i]  # Cambia de 1 a 0 o de 0 a 1
    return solucion

# Algoritmo Genético para resolver el problema de la mochila
def algoritmo_genetico(valores, pesos, capacidad_maxima, tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones):
    num_objetos = len(valores)
    poblacion = crear_poblacion(num_objetos, tamaño_poblacion, porcentaje_inicial=0.1)  # Inicia con mochilas casi vacías
    mejor_solucion = None
    mejor_valor = 0

    for gen in range(generaciones):
        # Selección de padres
        padres = seleccion(poblacion, valores, pesos, capacidad_maxima)
        nueva_poblacion = []

        # Crear nueva población mediante cruce y mutación
        while len(nueva_poblacion) < tamaño_poblacion:
            parent1, parent2 = random.sample(padres, 2)
            if random.random() < tasa_cruce:
                hijo = crossover(parent1, parent2)
                hijo = mutacion(hijo, tasa_mutacion)
                nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        # Evaluar la mejor solución de la generación
        for solucion in poblacion:
            valor_total = calcular_fitness(solucion, valores, pesos, capacidad_maxima)
            if valor_total > mejor_valor:
                mejor_valor = valor_total
                mejor_solucion = solucion

        # Mostrar progreso cada 100 generaciones
        if gen % 100 == 0 or gen == generaciones - 1:
            print(f"Generación {gen+1}, Mejor Valor: {mejor_valor}")

    return mejor_solucion, mejor_valor

# Función principal para ejecutar el programa
def main():
    # Leer datos desde el CSV
    nombre_archivo = "mochila50.csv"
    pesos, valores = leer_datos_csv(nombre_archivo)

    # Mostrar los datos de los objetos
    mostrar_datos(valores, pesos)

    # Pedir configuración al usuario
    capacidad_maxima = int(input("\nCapacidad máxima de la mochila: "))
    tamaño_poblacion = int(input("Tamaño de la población (ej. 100): "))
    tasa_cruce = float(input("Tasa de cruce (0.0 - 1.0, ej. 0.8): "))
    tasa_mutacion = float(input("Tasa de mutación (0.0 - 1.0, ej. 0.05): "))
    generaciones = int(input("Número de generaciones: "))

    # Ejecutar el algoritmo genético
    mejor_solucion, mejor_valor = algoritmo_genetico(valores, pesos, capacidad_maxima, tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones)

    # Verificar si se encontró una solución válida
    if mejor_solucion is None or mejor_valor == 0:
        print("\nNo se encontró ninguna solución válida que respete el límite de peso de la mochila.")
    else:
        # Mostrar la mejor solución
        peso_total = sum(peso * seleccion for peso, seleccion in zip(pesos, mejor_solucion))
        print("\nMejor Solución:")
        print("Configuración del Cromosoma:", mejor_solucion)
        print("Objetos seleccionados:")
        for i, seleccionado in enumerate(mejor_solucion):
            if seleccionado == 1:
                print(f" - Objeto {i+1}: Valor = {valores[i]}, Peso = {pesos[i]}")
        print(f"Valor Total: {mejor_valor}")
        print(f"Peso Total: {peso_total}")
        print(f"Capacidad Máxima de la Mochila: {capacidad_maxima}")

if __name__ == "__main__":
    main()
