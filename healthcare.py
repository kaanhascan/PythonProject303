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
        MainWindow.resize(1514, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, -90, 1541, 1290))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 150, 255);")
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
        self.name.setGeometry(QtCore.QRect(440, 290, 101, 31))
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
        self.surname.setGeometry(QtCore.QRect(370, 370, 161, 31))
        self.surname.setStyleSheet("\n"
"font: italic 24pt \"Arial\";")
        self.surname.setObjectName("surname")
        self.surname_input = QtWidgets.QLineEdit(self.homepage)
        self.surname_input.setGeometry(QtCore.QRect(540, 360, 401, 41))
        self.surname_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.surname_input.setObjectName("surname_input")
        self.TC = QtWidgets.QLabel(self.homepage)
        self.TC.setGeometry(QtCore.QRect(480, 450, 61, 31))
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

        from common_utils import CombinedButtonClicked

        combined_button_clicked = CombinedButtonClicked(self.centralwidget)
        combined_button_clicked.setGeometry(QtCore.QRect(810, 630, 131, 31))
        combined_button_clicked.set_main_window(self)
        self.push_button.clicked.connect(combined_button_clicked.push_button_clicked)

        self.stackedWidget.addWidget(self.homepage)
        self.symptoms = QtWidgets.QWidget()
        self.symptoms.setObjectName("symptoms")

        self.Headache = QtWidgets.QCheckBox(self.symptoms)
        self.Headache.setGeometry(QtCore.QRect(30, 70, 181, 31))
        self.Headache.setStyleSheet("font: 24pt \"Avenir\";\n"
"background-color: rgb(235, 235, 235);")
        self.Headache.setObjectName("Headache")

        self.Stomach_Ache = QtWidgets.QCheckBox(self.symptoms)
        self.Stomach_Ache.setGeometry(QtCore.QRect(230, 70, 251, 31))
        self.Stomach_Ache.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Stomach_Ache.setObjectName("Stomach_Ache")

        self.Nausea = QtWidgets.QCheckBox(self.symptoms)
        self.Nausea.setGeometry(QtCore.QRect(490, 70, 151, 31))
        self.Nausea.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Nausea.setObjectName("Nausea")

        self.Dizziness = QtWidgets.QCheckBox(self.symptoms)
        self.Dizziness.setGeometry(QtCore.QRect(650, 70, 181, 31))
        self.Dizziness.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Dizziness.setObjectName("Dizziness")

        self.Joint_Pain = QtWidgets.QCheckBox(self.symptoms)
        self.Joint_Pain.setGeometry(QtCore.QRect(840, 70, 191, 31))
        self.Joint_Pain.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Joint_Pain.setObjectName("Joint_Pain")

        self.Eye_Redness = QtWidgets.QCheckBox(self.symptoms)
        self.Eye_Redness.setGeometry(QtCore.QRect(1040, 70, 221, 31))
        self.Eye_Redness.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Eye_Redness.setObjectName("Eye_Redness")

        self.Burn = QtWidgets.QCheckBox(self.symptoms)
        self.Burn.setGeometry(QtCore.QRect(1270, 70, 101, 31))
        self.Burn.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Burn.setObjectName("Burn")

        self.Ear_Ache = QtWidgets.QCheckBox(self.symptoms)
        self.Ear_Ache.setGeometry(QtCore.QRect(1380, 70, 151, 31))
        self.Ear_Ache.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Ear_Ache.setObjectName("Ear_Ache")

        self.Bruise_on_Body = QtWidgets.QCheckBox(self.symptoms)
        self.Bruise_on_Body.setGeometry(QtCore.QRect(30, 230, 351, 30))
        self.Bruise_on_Body.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Bruise_on_Body.setObjectName("Bruise_on_Body")

        self.Cut = QtWidgets.QCheckBox(self.symptoms)
        self.Cut.setGeometry(QtCore.QRect(390, 230, 81, 31))
        self.Cut.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Cut.setObjectName("Cut")

        self.ToothPain = QtWidgets.QCheckBox(self.symptoms)
        self.ToothPain.setGeometry(QtCore.QRect(480, 230, 211, 30))
        self.ToothPain.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.ToothPain.setObjectName("ToothPain")

        self.HairLoss = QtWidgets.QCheckBox(self.symptoms)
        self.HairLoss.setGeometry(QtCore.QRect(700, 230, 181, 30))
        self.HairLoss.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.HairLoss.setObjectName("HairLoss")

        self.SkinRedness = QtWidgets.QCheckBox(self.symptoms)
        self.SkinRedness.setGeometry(QtCore.QRect(900, 230, 241, 30))
        self.SkinRedness.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.SkinRedness.setObjectName("SkinRedness")

        self.Breath_Shortness = QtWidgets.QCheckBox(self.symptoms)
        self.Breath_Shortness.setGeometry(QtCore.QRect(1160, 230, 371, 30))
        self.Breath_Shortness.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Breath_Shortness.setObjectName("Breath_Shortness")

        self.Nose_Flow = QtWidgets.QCheckBox(self.symptoms)
        self.Nose_Flow.setGeometry(QtCore.QRect(30, 380, 201, 30))
        self.Nose_Flow.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Nose_Flow.setObjectName("Nose_Flow")

        self.Fever = QtWidgets.QCheckBox(self.symptoms)
        self.Fever.setGeometry(QtCore.QRect(240, 380, 111, 30))
        self.Fever.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Fever.setObjectName("Fever")

        self.Cough = QtWidgets.QCheckBox(self.symptoms)
        self.Cough.setGeometry(QtCore.QRect(360, 380, 131, 30))
        self.Cough.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Cough.setObjectName("Cough")

        self.Vomiting = QtWidgets.QCheckBox(self.symptoms)
        self.Vomiting.setGeometry(QtCore.QRect(510, 380, 171, 30))
        self.Vomiting.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Vomiting.setObjectName("Vomiting")

        self.Sore_Throat = QtWidgets.QCheckBox(self.symptoms)
        self.Sore_Throat.setGeometry(QtCore.QRect(690, 380, 221, 30))
        self.Sore_Throat.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Sore_Throat.setObjectName("Sore_Throat")

        self.Insomnia = QtWidgets.QCheckBox(self.symptoms)
        self.Insomnia.setGeometry(QtCore.QRect(930, 380, 171, 30))
        self.Insomnia.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Insomnia.setObjectName("Insomnia")

        self.Acne = QtWidgets.QCheckBox(self.symptoms)
        self.Acne.setGeometry(QtCore.QRect(1130, 380, 101, 30))
        self.Acne.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Acne.setObjectName("Acne")

        self.Nose_Bleed = QtWidgets.QCheckBox(self.symptoms)
        self.Nose_Bleed.setGeometry(QtCore.QRect(1270, 380, 201, 30))
        self.Nose_Bleed.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Nose_Bleed.setObjectName("Nose_Bleed")

        self.Diarrhea = QtWidgets.QCheckBox(self.symptoms)
        self.Diarrhea.setGeometry(QtCore.QRect(430, 510, 171, 30))
        self.Diarrhea.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Diarrhea.setObjectName("Diarrhea")

        self.Costiveness = QtWidgets.QCheckBox(self.symptoms)
        self.Costiveness.setGeometry(QtCore.QRect(610, 510, 221, 30))
        self.Costiveness.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Costiveness.setObjectName("Costiveness")

        self.Phlegm = QtWidgets.QCheckBox(self.symptoms)
        self.Phlegm.setGeometry(QtCore.QRect(850, 510, 141, 30))
        self.Phlegm.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"font: 24pt \"Avenir\";")
        self.Phlegm.setObjectName("Phlegm")

        self.suggest_button = QtWidgets.QPushButton(self.symptoms)
        self.suggest_button.setGeometry(QtCore.QRect(660, 700, 130, 26))
        self.suggest_button.setStyleSheet("background-color: rgb(0, 249, 0);\n"
"font: 24pt \"Avenir\";")
        self.suggest_button.setObjectName("suggest_button")
        self.suggest_button.clicked.connect(self.show_suggestion)
        self.stackedWidget.addWidget(self.symptoms)

        self.suggestions = QtWidgets.QWidget()
        self.suggestions.setObjectName("suggestions")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.suggestions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 1511, 901))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
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
        self.Headache.setText(_translate("MainWindow", "HEADACHE"))
        self.Stomach_Ache.setText(_translate("MainWindow", "STOMACH ACHE"))
        self.Nausea.setText(_translate("MainWindow", "NAUSEA"))
        self.Dizziness.setText(_translate("MainWindow", "DIZZINESS"))
        self.Joint_Pain.setText(_translate("MainWindow", "JOINT PAIN"))
        self.Eye_Redness.setText(_translate("MainWindow", "EYE REDNESS"))
        self.Burn.setText(_translate("MainWindow", "BURN"))
        self.Ear_Ache.setText(_translate("MainWindow", "EARACHE"))
        self.Bruise_on_Body.setText(_translate("MainWindow", "BRUISE ON THE BODY"))
        self.Cut.setText(_translate("MainWindow", "CUT"))
        self.ToothPain.setText(_translate("MainWindow", "TOOTH PAIN"))
        self.HairLoss.setText(_translate("MainWindow", "HAIR LOSS"))
        self.SkinRedness.setText(_translate("MainWindow", "SKIN REDNESS"))
        self.Breath_Shortness.setText(_translate("MainWindow", "SHORTNESS OF BREATH"))
        self.Nose_Flow.setText(_translate("MainWindow", "NOSE FLOW"))
        self.Fever.setText(_translate("MainWindow", "FEVER"))
        self.Cough.setText(_translate("MainWindow", "COUGH"))
        self.Vomiting.setText(_translate("MainWindow", "VOMITING"))
        self.Sore_Throat.setText(_translate("MainWindow", "SORETHROAT"))
        self.Insomnia.setText(_translate("MainWindow", "INSOMNIA"))
        self.Acne.setText(_translate("MainWindow", "ACNE"))
        self.Nose_Bleed.setText(_translate("MainWindow", "NOSE BLEED"))
        self.Diarrhea.setText(_translate("MainWindow", "DIARRHEA"))
        self.Costiveness.setText(_translate("MainWindow", "COSTIVENESS"))
        self.Phlegm.setText(_translate("MainWindow", "PHLEGM"))
        self.suggest_button.setText(_translate("MainWindow", "SUGGEST"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_25.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))

    def show_suggestion(self):
    # Suggestion sayfasını oluştur
        self.stackedWidget.setCurrentIndex(2)  # Örnek olarak 2. sayfa indeksi

    # Baş ağrısı (Headache) seçili ise, suggestion_label'da "Drink more water" göster
        if self.Headache.isChecked():
            suggestion_label = QtWidgets.QLabel(self.suggestions)
            suggestion_label.setGeometry(QtCore.QRect(200, 200, 400, 100))
            suggestion_label.setText("Drink more water")
            suggestion_label.setStyleSheet("font-size: 24pt; color: black;")
            suggestion_label.setAlignment(QtCore.Qt.AlignCenter)
            suggestion_label.setObjectName("suggestion_label")
        self.stackedWidget.addWidget(suggestion_label)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
