
from PyQt5 import QtWidgets, QtCore, QtGui
from healthcare import Ui_MainWindow
import csv

from PyQt5.QtCore import pyqtSignal


class CombinedButtonClicked(QtWidgets.QPushButton):
    column_names = ['Name', 'Surname', 'TC', 'Age', 'Symptoms']


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
        symptoms = self.get_selected_symptoms()

        with open('records.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            row = [name, surname, tc, age, symptoms]

            writer.writerow(row)

        self.main_window.stackedWidget.setCurrentIndex(1)
        self.hide()

    def get_selected_symptoms(self):

        checked_boxes = []

        checkboxes = [
            self.main_window.Headache, self.main_window.Stomach_Ache,
            self.main_window.Nausea, self.main_window.Dizziness,
            self.main_window.Joint_Pain, self.main_window.Eye_Redness,
            self.main_window.Burn, self.main_window.Ear_Ache,
            self.main_window.Bruise_on_Body, self.main_window.Cut,
            self.main_window.ToothPain, self.main_window.HairLoss,
            self.main_window.SkinRedness, self.main_window.Breath_Shortness,
            self.main_window.Nose_Flow, self.main_window.Fever,
            self.main_window.Cough, self.main_window.Vomiting,
            self.main_window.Sore_Throat, self.main_window.Insomnia,
            self.main_window.Acne, self.main_window.Nose_Bleed,
            self.main_window.Diarrhea, self.main_window.Costiveness,
            self.main_window.Phlegm,
        ]

        for checkbox in checkboxes:
            if checkbox.isChecked():
                checked_boxes.append(checkbox.objectName())

        print("Checked Boxes:", checked_boxes)

        return checked_boxes
