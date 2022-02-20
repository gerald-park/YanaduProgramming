import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton
from PyQt5 import uic

class UI(QMainWindow) :
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Main.ui",self)

        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.clickedBtn)

        self.show()

    def clickedBtn(self):
        self.textEdit.setPlainText("Please subscribe the Channel")

app = QApplication(sys.argv)
window = UI()
app.exec_()