# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'healthcare.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 1451, 901))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 253, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setStyleSheet("background-color: rgb(0, 253, 255);")
        self.homepage.setObjectName("homepage")
        self.health_care = QtWidgets.QLabel(self.homepage)
        self.health_care.setGeometry(QtCore.QRect(470, 50, 471, 81))
        self.health_care.setStyleSheet("font: 48pt \"Cochin\";\n"
"color: rgb(148, 23, 81);\n"
"")
        self.health_care.setAlignment(QtCore.Qt.AlignCenter)
        self.health_care.setObjectName("health_care")
        self.name = QtWidgets.QLabel(self.homepage)
        self.name.setGeometry(QtCore.QRect(430, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setStyleSheet("font: 24pt \".AppleSystemUIFont\";\n"
"font: italic 24pt \"Arial\";")
        self.name.setObjectName("name")
        self.name_input = QtWidgets.QLineEdit(self.homepage)
        self.name_input.setGeometry(QtCore.QRect(540, 280, 401, 41))
        self.name_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_input.setObjectName("name_input")
        self.surname = QtWidgets.QLabel(self.homepage)
        self.surname.setGeometry(QtCore.QRect(360, 370, 161, 31))
        self.surname.setStyleSheet("\n"
"font: italic 24pt \"Arial\";")
        self.surname.setObjectName("surname")
        self.surname_input = QtWidgets.QLineEdit(self.homepage)
        self.surname_input.setGeometry(QtCore.QRect(540, 360, 401, 41))
        self.surname_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.surname_input.setObjectName("surname_input")
        self.TC = QtWidgets.QLabel(self.homepage)
        self.TC.setGeometry(QtCore.QRect(470, 450, 61, 31))
        self.TC.setStyleSheet("\n"
"font: italic 24pt \"Arial\";")
        self.TC.setObjectName("TC")
        self.TC_input = QtWidgets.QLineEdit(self.homepage)
        self.TC_input.setGeometry(QtCore.QRect(540, 440, 401, 41))
        self.TC_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TC_input.setObjectName("TC_input")
        self.age = QtWidgets.QLabel(self.homepage)
        self.age.setGeometry(QtCore.QRect(450, 540, 71, 31))
        self.age.setStyleSheet("\n"
"font: italic 24pt \"Arial\";")
        self.age.setObjectName("age")
        self.age_input = QtWidgets.QLineEdit(self.homepage)
        self.age_input.setGeometry(QtCore.QRect(540, 530, 401, 41))
        self.age_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.age_input.setObjectName("age_input")
        self.push_button = QtWidgets.QPushButton(self.homepage)
        self.push_button.setGeometry(QtCore.QRect(810, 630, 131, 31))
        self.push_button.setStyleSheet("background-color: rgb(0, 249, 0);\n"
"font: 57 24pt \"Avenir\";")
        self.push_button.setObjectName("push_button")
        self.stackedWidget.addWidget(self.homepage)
        self.symptoms = QtWidgets.QWidget()
        self.symptoms.setObjectName("symptoms")
        self.stackedWidget.addWidget(self.symptoms)
        self.suggestions = QtWidgets.QWidget()
        self.suggestions.setObjectName("suggestions")
        self.stackedWidget.addWidget(self.suggestions)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.health_care.setText(_translate("MainWindow", "HEALTH CARE"))
        self.name.setText(_translate("MainWindow", "NAME"))
        self.surname.setText(_translate("MainWindow", "SURNAME"))
        self.TC.setText(_translate("MainWindow", "TC"))
        self.age.setText(_translate("MainWindow", "AGE"))
        self.push_button.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
