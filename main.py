import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

"""
    это короче калькулятор роста вы тут рост будете измерять.
    тут в общем приколы по типу рост и вес вводите и вам 
    выводит ваш рост и вес ихихи.
"""


class HeightWeightCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор роста и веса")

        self.height_label = QLabel("Рост (см):")
        self.height_input = QLineEdit()
        self.weight_label = QLabel("Вес (кг):")
        self.weight_input = QLineEdit()

        self.result_label = QLabel("")

        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        """
        иихихихихихих эта фун кция выводит результаты на экран
        """

    def calculate(self):
        self.result_label.setText(
            f"Ваш рост: {self.height_input.text()}, ваш вес: {self.weight_input.text()}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = HeightWeightCalculator()
    calculator.show()
    sys.exit(app.exec())
