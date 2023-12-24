from PyQt5 import QtWidgets, QtCore, QtGui
import csv


class CombinedButtonClicked(QtWidgets.QPushButton):
    column_names = ['Name','Surname','TC','Age']



    def set_columns(self):
        with open('records.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.column_names)
            writer.writeheader()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(0, 249, 0);\n"
                           "font: 57 24pt \"Avenir\";")
        self.setText("SUBMIT")

    def set_main_window(self, main_window):
        self.main_window = main_window
        self.clicked.connect(self.push_button_clicked)

    def push_button_clicked(self):
        name = self.main_window.name_input.text()
        surname = self.main_window.surname_input.text()
        tc = self.main_window.TC_input.text()
        age = self.main_window.age_input.text()

        with open('records.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            writer.writerow([name, surname, tc, age])

        self.clear_inputs()
        self.set_columns()

        self.main_window.stackedWidget.setCurrentIndex(1)

    def clear_inputs(self):
        self.TC_input.clear()
        self.name_input.clear()
        self.surname_input.clear()
        self.age_input.clear()
