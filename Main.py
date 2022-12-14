#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()

            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: \n")

            global list_of_numbers
            list_of_numbers = []

            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            for num in re.findall(r'\b[0-9]+\b', data):
                list_of_numbers.append(num)
            for k, i in enumerate(list_of_numbers):
                self.plainTextEdit.insertPlainText("{0:5}".format(i))
                # чтобы текст был в виде таблицы, делаем отступ после
                # 6 элемента
                if ((k + 1) % 5) == 0:
                    self.plainTextEdit.appendPlainText("")

    def process_data(self):
        if validation_of_data():

            max_pos1, max_num1 = find_max1()
            max_pos2, max_num2 = find_max2()
            summa = 0
            for n in list_of_numbers:
                summa += int(n)
            print(summa)

            self.plainTextEdit.appendPlainText("Максимальный элемент первой строки = " + str(max_num1) + '\n')
            self.plainTextEdit.appendPlainText("Максимальный элемент второй строки = " + str(max_num2) + '\n')

            # -*- выполнение задания -*-
            if summa >= 100:
                changing_the_third_line()
                list_of_numbers[max_pos1] , list_of_numbers[max_pos2] = list_of_numbers[max_pos2] , list_of_numbers[max_pos1]

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')

                # выводим список на экран
                for k, i in enumerate(list_of_numbers):
                    self.plainTextEdit.insertPlainText("{0:5}".format(i))
                    # чтобы текст был в виде таблицы, делаем отступ после
                    # 6 элемента
                    if ((k + 1) % 5) == 0:
                        self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Сумма меньше 100 \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл

        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for k, i in enumerate(list_of_numbers):
                file.write(i + " ")
                if ((k + 1) % 5) == 0:
                    file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_max1():
    """
    находим максимальное число в списке
    :return: максимальное число

    """

    max_num1 = 0
    for i, n in enumerate(list_of_numbers):
        if i <= 5:
            if max_num1 < int(n):
                max_num1 = int(n)
                pos1 = int(i)
    return pos1, max_num1


def find_max2():
    """
    находим максимальное число в списке
    :return: максимальное число

    """

    max_num2 = 0
    for i, n in enumerate(list_of_numbers):
        if 5 < int(i) + 1 <= 10:
            if max_num2 < int(n):
                max_num2 = int(n)
                pos2 = int(i)
    return pos2, max_num2


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False
        return True
    else:
        return False


def changing_the_third_line():
    for i, n in enumerate(list_of_numbers):
        if 10 < int(i) + 1 <= 15:
            list_of_numbers[i] = 1

    pass





def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
