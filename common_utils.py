from PyQt5 import QtWidgets, QtCore

class extended_button_clicked(QtWidgets.QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

    def set_main_window(self,main_window):
        self.main_window=main_window
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("This button is clicked")