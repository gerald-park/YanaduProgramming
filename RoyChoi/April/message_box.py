from PyQt5.QtWidgets import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        criticalButton = QPushButton("criticall")
        criticalButton.clicked.connect(self.critical_messagebox)
        informationButton = QPushButton('information')
        informationButton.clicked.connect(self.information_messagebox)
        questionButton = QPushButton('question')
        questionButton.clicked.connect(self.question_messagebox)
        warningButton = QPushButton('warning')
        warningButton.clicked.connect(self.warning_messagebox)

        layout = QGridLayout()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(layout)
        layout.addWidget(criticalButton, 0, 0)
        layout.addWidget(informationButton, 0, 1)
        layout.addWidget(questionButton, 0, 2)
        layout.addWidget(warningButton, 0, 3)

    def critical_messagebox(self):
        ret = QMessageBox.critical(self, "critical", "something critical happened", QMessageBox.Ok|QMessageBox.No)
        if ret == QMessageBox.Ok:
            print('okay is pressed')

    def information_messagebox(self):
        ret = QMessageBox.information(self, "information", "something informative happened", QMessageBox.Discard|QMessageBox.No)

    def question_messagebox(self):
        ret = QMessageBox.question(self, "question", "some question happened", QMessageBox.Apply|QMessageBox.No)

    def warning_messagebox(self):
        ret = QMessageBox.warning(self, "warning", "something warning happened", QMessageBox.Ignore|QMessageBox.No)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
