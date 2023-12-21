from PyQt5 import QtWidgets, QtCore
import csv


class extended_button_clicked(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)

    def set_main_window(self, main_window):
        self.main_window = main_window
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):

        if hasattr(self, 'main_window'):
            name = self.main_window.name_input.text()
            surname = self.main_window.surname_input.text()
            tc = self.main_window.TC_input.text()
            age = self.main_window.age_input.text()

            with open('records.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, surname, tc, age])

            self.clear_inputs()

        else:
            print("Error")

    def clear_inputs(self):
        self.TC_input.clear()
        self.name_input.clear()
        self.surname_input.clear()
        self.age_input.clear()
