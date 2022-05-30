from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        QTimer.singleShot(0, self.load_files)

    def load_files(self):
        for i in range(10):
            print('Hi')
            sleep(1)

    def print_hi(self):
            print('hi')

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
