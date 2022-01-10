import sys

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 360, 350)

        # вызов основной функции
        self.start_calculation()

        # Отображение всех элементов
        self.show()

    # method for widgets
    def start_calculation(self):
        # создание окна вывода
        self.label = QLabel(self)

        #  расположение окна вывода
        self.label.setGeometry(5, 5, 350, 70)


        # Выбор шрифта и его размера
        self.label.setFont(QFont('Arial', 22))

        # Добавление цифр в окно вывода
        push1 = QPushButton("1", self)
        push1.setGeometry(5, 150, 80, 40)

        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)

        push3 = QPushButton("3", self)
        push3.setGeometry(185, 150, 80, 40)

        push4 = QPushButton("4", self)
        push4.setGeometry(5, 200, 80, 40)

        push5 = QPushButton("5", self)
        push5.setGeometry(95, 200, 80, 40)

        push6 = QPushButton("6", self)
        push6.setGeometry(185, 200, 80, 40)

        push7 = QPushButton("7", self)
        push7.setGeometry(5, 250, 80, 40)

        push8 = QPushButton("8", self)
        push8.setGeometry(95, 250, 80, 40)

        push9 = QPushButton("9", self)
        push9.setGeometry(185, 250, 80, 40)

        push0 = QPushButton("0", self)
        push0.setGeometry(5, 300, 80, 40)

        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)

        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 250, 80, 40)

        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)

        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 150, 80, 40)

        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)

        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)

        # очищение вывода
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 200, 40)

        # удаление последнего символа
        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)

        # Добавление евентов
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)

    def action_equal(self):
        # Забирается значение из label
        equation = self.label.text()
        try:
            # матеметическая операция
            ans = eval(equation)

            # вывод ответа
            self.label.setText(str(ans))
        except:
            # если операция не выполнена выведется данные ответ
            self.label.setText("Ошибка")

    def action_plus(self):
        self.label.setText(self.no_duplicate('+'))

    def action_minus(self):
        self.label.setText(self.no_duplicate('-'))

    def action_div(self):
        self.label.setText(self.no_duplicate('/'))

    def action_mul(self):
        self.label.setText(self.no_duplicate('*'))

    def action_point(self):
        self.label.setText(self.no_duplicate('.'))

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        # удаление последнего символа в тексте вывода
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def no_duplicate(self, mark):
        text = self.label.text()
        # Не дает ввести выражение если выражение пустое
        if len(text) == 0:
            return text

        # Проверка на дублирование
        if mark == text[len(text) - 1]:
            result = text
        else:
            result = text + mark

        return self.check_mark(result)

    def check_mark(self, text_result):
        marks = ['+', '-', '/', '*', '.']

        result = text_result
        # Перебор выражений
        for mark in marks:
            # если предыдущее значение в выводе равняется символу, то удаляется последний символ
            if mark == text_result[len(text_result) - 2]:
                result = text_result[:len(text_result) - 1]
                break
            else:
                result = text_result
        return result

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
