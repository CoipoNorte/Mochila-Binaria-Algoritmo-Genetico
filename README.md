# Algoritmo Genético - Problema de la Mochila Binaria

## Descripción

Este proyecto implementa un **algoritmo genético** para resolver el problema de la mochila binaria. El objetivo es maximizar el valor total de los objetos seleccionados dentro de una mochila, sin exceder una capacidad máxima de peso. Los **algoritmos genéticos** son técnicas de optimización basadas en el principio de la selección natural y son particularmente efectivos para resolver problemas complejos donde no existe una solución directa.

## ¿Qué es un Algoritmo Genético?

Un **algoritmo genético (AG)** es un método inspirado en la evolución natural. Funciona mediante la generación y evolución de una población de posibles soluciones a un problema, seleccionando y combinando las mejores soluciones para crear nuevas generaciones. Los pasos principales en un algoritmo genético son:

1. **Inicialización**: Se crea una población inicial de posibles soluciones (cromosomas).
2. **Evaluación (Fitness)**: Se calcula el "fitness" de cada cromosoma, que indica qué tan buena es esa solución.
3. **Selección**: Se eligen los cromosomas más fuertes (con mejor fitness) para crear la próxima generación.
4. **Cruce (Crossover)**: Se combinan pares de cromosomas seleccionados para crear nuevos cromosomas (hijos).
5. **Mutación**: Se realizan pequeñas modificaciones aleatorias en los cromosomas para mantener la diversidad genética.
6. **Repetición**: Se repiten los pasos 2-5 hasta que se alcance el número de generaciones deseado.

## Estructura del Proyecto

- **`codigo.py`**: Script principal que ejecuta el algoritmo genético. Configura los parámetros, maneja la lógica del algoritmo y muestra los resultados finales.
- **`objetos.csv`**: Archivo CSV con la lista de objetos. Cada fila representa un objeto con dos columnas: `valor` y `peso`.
- **`log/`**: Carpeta donde se guardan los archivos de registro (`log`) de cada ejecución del algoritmo. Cada archivo incluye detalles sobre las soluciones encontradas.

## Ejecución del Proyecto

### 1. Preparar el Archivo de Objetos

Asegúrate de tener un archivo llamado `objetos.csv` en el mismo directorio que `main.py`, con el siguiente formato:

```csv
valor,peso
60,10
100,20
120,30
...
```

### 2. Ejecutar el Script

Abre la consola y ejecuta el siguiente comando:

```bash
py codigo.py
```

### 3. Configurar los Parámetros

Al iniciar el script, se te pedirá que ingreses varios parámetros. Puedes presionar "Enter" para usar los valores predeterminados o ingresar tus propios valores:

- **Capacidad máxima de la mochila (Entero)**: Capacidad máxima de peso que puede llevar la mochila.
- **Tamaño de la población (Entero entre 1 - 100)**: Número de soluciones (cromosomas) en cada generación.
- **Tasa de cruce (Decimal entre 0.0 - 1.0)**: Probabilidad de que se realice el cruce entre dos cromosomas.
- **Tasa de mutación (Decimal entre 0.0 - 1.0)**: Probabilidad de que ocurra una mutación en los cromosomas.
- **Número de generaciones (Entero)**: Número de veces que el algoritmo evolucionará la población.

### 4. Resultados

El script mostrará el progreso de las generaciones y, al final, presentará:

- **La mejor solución encontrada**: Incluyendo los objetos seleccionados, su valor total y peso total.
- **Un Top 5 de las mejores soluciones válidas**: Mostrando las configuraciones, valores y pesos.

Además, se generará un archivo de registro en la carpeta `log/`, con todos los detalles de la ejecución para futuras referencias.

## Ejemplo de Salida

```plaintext
Algoritmo Genético - Problema de la Mochila
Capacidad máxima de la mochila (Entero) [100]: 
Tamaño de la población (Entero entre 1 - 100) [100]: 50
Tasa de cruce (Decimal entre 0.0 - 1.0) [0.8]: 
Tasa de mutación (Decimal entre 0.0 - 1.0) [0.05]: 
Número de generaciones (Entero) [100]: 50

Generación 1:
Mejor Valor en esta generación: 750

...

Mejor Solución:
Configuración del Cromosoma: [1, 0, 1, ...]
Objetos seleccionados:
 - Objeto 1: Valor = 60, Peso = 10
 - Objeto 3: Valor = 120, Peso = 30
Valor Total: 180
Peso Total: 40
Capacidad Máxima de la Mochila: 100

Top 5 Mejores Soluciones:
1. Valor: 180, Peso: 40, Configuración: [1, 0, 1, ...]
2. Valor: 175, Peso: 39, Configuración: [1, 0, 1, ...]
3. ...
```

## Principales Parámetros del Algoritmo

1. **Capacidad máxima**: Define el límite de peso que puede llevar la mochila. Las soluciones que exceden este límite no son válidas.
2. **Tamaño de la población**: Controla cuántos posibles cromosomas se consideran en cada generación. Un tamaño mayor puede dar mejores resultados, pero aumentará el tiempo de cálculo.
3. **Tasa de cruce**: Define qué tan frecuentemente se mezclan dos cromosomas para crear nuevos. Una tasa de cruce más alta aumenta la exploración de nuevas soluciones.
4. **Tasa de mutación**: Introduce variaciones aleatorias en los cromosomas para mantener la diversidad genética. Evita que el algoritmo se estanque en una solución local.

## Archivos de Log

Cada ejecución del algoritmo genera un archivo de log en la carpeta `log/` con un nombre en el formato `log_numero_fecha_hora.txt`. Estos archivos contienen:

- Parámetros de configuración usados.
- Progreso de cada generación.
- Resultados finales, incluida la mejor solución y el top 5 de mejores soluciones válidas.

## **Notas para Presentación en Clase:**
- **Cromosomas y genes**: Los cromosomas representan soluciones, y los genes (bits) indican la inclusión o exclusión de un objeto.
- **La selección natural**: El proceso de selección ayuda a mejorar las soluciones a través de generaciones.

## Ejemplo de Valores

- Capacidad máxima de la mochila (Entero): **200**
- Tamaño de la población (Entero entre 1 - 100): **100**
- Tasa de cruce (Decimal entre 0.0 - 1.0): **0.8**
- Tasa de mutación (Decimal entre 0.0 - 1.0): **0.05**
- Número de generaciones (Entero): **100**