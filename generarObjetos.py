import pandas as pd
import random
import os

# Generar datos aleatorios para el archivo CSV
data = {
    'valor': [random.randint(50, 200) for _ in range(50)],
    'peso': [random.randint(5, 30) for _ in range(50)]
}

df = pd.DataFrame(data)

# Obtener la ruta del directorio actual
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Guardar el archivo en el directorio actual
df.to_csv(os.path.join(ruta_actual, 'objetos.csv'), index=False)
