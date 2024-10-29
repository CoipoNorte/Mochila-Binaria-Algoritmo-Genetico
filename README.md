# Algoritmo Genético - Problema de la Mochila Binaria

Este proyecto utiliza un **Algoritmo Genético** (AG) para resolver el problema de la **mochila binaria**. El objetivo es seleccionar una combinación de objetos, cada uno con un valor y un peso determinado, de manera que el valor total se maximice sin exceder la capacidad de la mochila.

## Descripción del Problema

Dado un conjunto de objetos con valores y pesos, y una capacidad máxima que la mochila puede cargar, el objetivo es determinar qué objetos incluir en la mochila para **maximizar el valor total** sin superar la capacidad permitida. La selección óptima se realiza mediante Algoritmos Genéticos, que son métodos de optimización basados en los principios de la evolución natural. Igual que en un robo no???

## Algoritmo Genético para Resolver el Problema

El Algoritmo Genético sigue estos pasos para encontrar la combinación óptima: ñ.n

### 1. Inicialización de la Población

El AG comienza generando una **población de soluciones aleatorias**, cada una representada como un **cromosoma**. En este problema, un cromosoma es una secuencia binaria (por ejemplo, `[1, 0, 1, 1, 0]`), donde cada posición representa un objeto:
- `1` indica que el objeto está incluido en la mochila.
- `0` indica que el objeto no está incluido.

Cada cromosoma en la población representa una posible solución al problema.

### 2. Evaluación (Función de Fitness)

Cada cromosoma se evalúa para calcular su **fitness**:
- La **función de fitness** calcula el valor total de los objetos seleccionados en el cromosoma.
- Si el peso total de los objetos seleccionados excede la capacidad máxima de la mochila, el fitness se establece en `0`, penalizando así soluciones no válidas.

### 3. Selección de Padres

Para crear la próxima generación de soluciones, el AG selecciona los cromosomas más aptos (aquellos con mayor fitness) de la población actual:
- Los mejores cromosomas se eligen como **padres** para reproducirse y crear nuevos cromosomas.
- Este proceso simula la selección natural, en la que solo las soluciones más viables tienen oportunidad de pasar sus genes a la siguiente generación.

### 4. Cruce (Crossover)

El **cruce** combina pares de padres para generar nuevos cromosomas (hijos):
- Se selecciona un punto de cruce aleatorio en el cromosoma.
- Se combina la primera parte de un padre con la segunda parte del otro para crear un hijo.
- Esto permite que las soluciones evolucionen al explorar nuevas combinaciones de objetos.

### 5. Mutación

Para introducir variabilidad y evitar el estancamiento en soluciones locales, se aplica **mutación** a algunos cromosomas:
- Con una baja probabilidad, se muta una posición del cromosoma, cambiando un `1` a `0` o viceversa.
- La mutación es crucial para explorar configuraciones de objetos que podrían no ser posibles solo con el cruce.

### 6. Evolución a través de Generaciones

El proceso de evaluación, selección, cruce y mutación se repite durante varias generaciones:
- Con cada generación, la población se vuelve más apta y converge hacia soluciones con un mayor valor total, respetando la capacidad de la mochila.

### Resultados

En este ejemplo, después de 200 generaciones, el algoritmo encontró la siguiente mejor solución:

```plaintext
Generación 1, Mejor Valor: 220
Generación 101, Mejor Valor: 249
Generación 200, Mejor Valor: 249

Mejor Solución:
Configuración del Cromosoma: [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 
0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
Objetos seleccionados:
 - Objeto 1: Valor = 10, Peso = 2
 - Objeto 2: Valor = 8, Peso = 1
 - Objeto 4: Valor = 5, Peso = 1
 - Objeto 5: Valor = 12, Peso = 3
 - Objeto 7: Valor = 7, Peso = 1
 - Objeto 12: Valor = 10, Peso = 2
 - Objeto 13: Valor = 8, Peso = 1
 - Objeto 14: Valor = 15, Peso = 4
 - Objeto 15: Valor = 5, Peso = 1
 - Objeto 18: Valor = 7, Peso = 1
 - Objeto 19: Valor = 11, Peso = 3
 - Objeto 23: Valor = 10, Peso = 2
 - Objeto 24: Valor = 8, Peso = 1
 - Objeto 25: Valor = 15, Peso = 4
 - Objeto 26: Valor = 5, Peso = 1
 - Objeto 27: Valor = 12, Peso = 3
 - Objeto 28: Valor = 9, Peso = 2
 - Objeto 29: Valor = 7, Peso = 1
 - Objeto 34: Valor = 10, Peso = 2
 - Objeto 35: Valor = 8, Peso = 1
 - Objeto 37: Valor = 5, Peso = 1
 - Objeto 39: Valor = 9, Peso = 2
 - Objeto 40: Valor = 7, Peso = 1
 - Objeto 44: Valor = 14, Peso = 3
 - Objeto 45: Valor = 10, Peso = 2
 - Objeto 46: Valor = 8, Peso = 1
 - Objeto 48: Valor = 5, Peso = 1
 - Objeto 50: Valor = 9, Peso = 2
Valor Total: 249
Peso Total: 50
Capacidad Máxima de la Mochila: 50
```
En este resultado, el valor total de los objetos seleccionados es 249, utilizando exactamente la capacidad máxima de la mochila (50). Esto muestra la capacidad del Algoritmo Genético para optimizar combinaciones de objetos, maximizando el valor mientras se respeta la restricción de capacidad.