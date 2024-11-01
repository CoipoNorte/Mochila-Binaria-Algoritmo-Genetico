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
            peso, valor = map(int, fila)  # Nota: Se asume el formato Peso, Valor
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
    return valor_total if peso_total <= capacidad_maxima else 0

# Crear una solución inicial aleatoria
def crear_solucion_aleatoria(num_objetos):
    return [random.randint(0, 1) for _ in range(num_objetos)]

# Crear una solución inicial casi vacía
def crear_solucion_casi_vacia(num_objetos, porcentaje_inicial=0.1):
    solucion = [0] * num_objetos
    num_seleccionados = int(num_objetos * porcentaje_inicial)
    indices = random.sample(range(num_objetos), num_seleccionados)
    for idx in indices:
        solucion[idx] = 1
    return solucion

# Crear una solución inicial con solo 1 objeto seleccionado
def crear_solucion_un_objeto(num_objetos):
    solucion = [0] * num_objetos
    idx = random.randint(0, num_objetos - 1)
    solucion[idx] = 1
    return solucion

# Crear una solución inicial vacía
def crear_solucion_vacia(num_objetos):
    return [0] * num_objetos

# Crear una población inicial según la elección del usuario
def crear_poblacion(num_objetos, tamaño_poblacion, inicializacion):
    if inicializacion == "aleatoria":
        return [crear_solucion_aleatoria(num_objetos) for _ in range(tamaño_poblacion)]
    elif inicializacion == "casi_vacia":
        return [crear_solucion_casi_vacia(num_objetos) for _ in range(tamaño_poblacion)]
    elif inicializacion == "un_objeto":
        return [crear_solucion_un_objeto(num_objetos) for _ in range(tamaño_poblacion)]
    elif inicializacion == "vacia":
        return [crear_solucion_vacia(num_objetos) for _ in range(tamaño_poblacion)]

# Selección de padres mejorada usando torneo
def seleccion(poblacion, valores, pesos, capacidad_maxima, k=3):
    padres = []
    for _ in range(len(poblacion) // 2):
        torneo = random.sample(poblacion, k)
        torneo.sort(key=lambda ind: calcular_fitness(ind, valores, pesos, capacidad_maxima), reverse=True)
        padres.append(torneo[0])
    return padres

# Cruce entre dos soluciones mejorado con cruce uniforme
def crossover(parent1, parent2):
    hijo = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            hijo.append(parent1[i])
        else:
            hijo.append(parent2[i])
    return hijo

# Mutación mejorada
def mutacion(solucion, tasa_mutacion):
    return [1 - bit if random.random() < tasa_mutacion else bit for bit in solucion]

# Algoritmo Genético para resolver el problema de la mochila
def algoritmo_genetico(valores, pesos, capacidad_maxima, tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones, inicializacion):
    num_objetos = len(valores)
    poblacion = crear_poblacion(num_objetos, tamaño_poblacion, inicializacion)
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

        # Mostrar progreso cada 50 generaciones
        if gen % 50 == 0 or gen == generaciones - 1:
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
    
    print("\nOpciones de inicialización:")
    print("1. Aleatoria")
    print("2. Casi Vacía")
    print("3. Solo 1 Objeto")
    print("4. Vacía")
    opcion = input("Selecciona el tipo de inicialización (1-4): ").strip()
    
    if opcion == '1':
        inicializacion = "aleatoria"
    elif opcion == '2':
        inicializacion = "casi_vacia"
    elif opcion == '3':
        inicializacion = "un_objeto"
    elif opcion == '4':
        inicializacion = "vacia"
    else:
        print("Opción inválida. Usando inicialización aleatoria por defecto.")
        inicializacion = "aleatoria"

    # Ejecutar el algoritmo genético
    mejor_solucion, mejor_valor = algoritmo_genetico(valores, pesos, capacidad_maxima, tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones, inicializacion)

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
