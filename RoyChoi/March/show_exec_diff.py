from PyQt5.QtWidgets import *
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        button1 = QPushButton('button1')
        grid_layout.addWidget(button1)
        central_widget.setLayout(grid_layout)
        button1.clicked.connect(self.show_dialog)

    def show_dialog(self):
        form = Form()
        form.exec_()



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()