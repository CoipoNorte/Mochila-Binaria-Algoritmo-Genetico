from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from codigo import algoritmo_genetico, actualizar_capacidad, capacidad_maxima, tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones

class KnapsackApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Algoritmo Genético - Configuración y Ejecución')
        self.setGeometry(100, 100, 500, 300)

        # Widgets
        self.capacidad_label = QtWidgets.QLabel("Capacidad Máxima de la Mochila:")
        self.capacidad_input = QtWidgets.QSpinBox()
        self.capacidad_input.setRange(1, 1000)
        self.capacidad_input.setValue(capacidad_maxima)

        self.tam_poblacion_label = QtWidgets.QLabel("Tamaño de la Población:")
        self.tam_poblacion_input = QtWidgets.QSpinBox()
        self.tam_poblacion_input.setRange(1, 100)
        self.tam_poblacion_input.setValue(tamaño_poblacion)

        self.tasa_cruce_label = QtWidgets.QLabel("Tasa de Cruce:")
        self.tasa_cruce_input = QtWidgets.QDoubleSpinBox()
        self.tasa_cruce_input.setRange(0.0, 1.0)
        self.tasa_cruce_input.setSingleStep(0.01)
        self.tasa_cruce_input.setValue(tasa_cruce)

        self.tasa_mutacion_label = QtWidgets.QLabel("Tasa de Mutación:")
        self.tasa_mutacion_input = QtWidgets.QDoubleSpinBox()
        self.tasa_mutacion_input.setRange(0.0, 1.0)
        self.tasa_mutacion_input.setSingleStep(0.01)
        self.tasa_mutacion_input.setValue(tasa_mutacion)

        self.generaciones_label = QtWidgets.QLabel("Número de Generaciones:")
        self.generaciones_input = QtWidgets.QSpinBox()
        self.generaciones_input.setRange(1, 1000)
        self.generaciones_input.setValue(generaciones)

        self.ejecutar_button = QtWidgets.QPushButton("Ejecutar Algoritmo")
        self.ejecutar_button.clicked.connect(self.ejecutar_algoritmo)

        self.resultado_output = QtWidgets.QTextEdit()
        self.resultado_output.setReadOnly(True)

        # Layouts
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.capacidad_label)
        layout.addWidget(self.capacidad_input)
        layout.addWidget(self.tam_poblacion_label)
        layout.addWidget(self.tam_poblacion_input)
        layout.addWidget(self.tasa_cruce_label)
        layout.addWidget(self.tasa_cruce_input)
        layout.addWidget(self.tasa_mutacion_label)
        layout.addWidget(self.tasa_mutacion_input)
        layout.addWidget(self.generaciones_label)
        layout.addWidget(self.generaciones_input)
        layout.addWidget(self.ejecutar_button)
        layout.addWidget(self.resultado_output)

        self.setLayout(layout)

    def ejecutar_algoritmo(self):
        # Obtener valores de los inputs y actualizar las variables globales
        actualizar_capacidad(self.capacidad_input.value())
        global tamaño_poblacion, tasa_cruce, tasa_mutacion, generaciones
        tamaño_poblacion = self.tam_poblacion_input.value()
        tasa_cruce = self.tasa_cruce_input.value()
        tasa_mutacion = self.tasa_mutacion_input.value()
        generaciones = self.generaciones_input.value()

        # Ejecutar el algoritmo genético
        mejor_solucion, valor_maximo, valores, pesos = algoritmo_genetico('./objetos.csv')

        # Mostrar el resultado de la mejor solución
        self.resultado_output.setText(self.mostrar_mejor_solucion(mejor_solucion, valores, pesos))

    def mostrar_mejor_solucion(self, mejor_solucion, valores, pesos):
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = KnapsackApp()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
