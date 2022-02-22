from PyQt5.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout()
        self.centralwidget = QWidget()
        self.mdi = QMdiArea()
        self.cascade = QPushButton('cascade')
        self.cascade.clicked.connect(self.cascade_windows)
        self.tile = QPushButton('tile')
        self.tile.clicked.connect(self.tile_windows)
        self.tabbed = QPushButton('tabbed')
        self.tabbed.clicked.connect(self.tabbed_windows)
        self.endtabbed = QPushButton('end tabbed')
        self.endtabbed.clicked.connect(self.end_tabbed_windows)
        self.window1 = QMainWindow()
        self.window1.setWindowTitle('sub window1')
        self.label1 = QLabel('Window1')
        self.window1.centralwidget = QWidget()
        self.window1.layout = QGridLayout()
        self.window1.layout.addWidget(self.label1)
        self.window1.centralwidget.setLayout(self.window1.layout)
        self.window1.setCentralWidget(self.window1.centralwidget)
        self.window2 = QMainWindow()
        self.window2.setWindowTitle('sub window2')
        self.window3 = QMainWindow()
        self.window3.setWindowTitle('sub window3')
        self.window4 = QMainWindow()
        self.window4.setWindowTitle('sub window4')
        self.mdi.addSubWindow(self.window1)
        self.mdi.addSubWindow(self.window2)
        self.mdi.addSubWindow(self.window3)
        self.mdi.addSubWindow(self.window4)
        layout.addWidget(self.mdi, 0, 0, 1, 4)
        layout.addWidget(self.cascade, 1, 0)
        layout.addWidget(self.tile, 1, 1)
        layout.addWidget(self.tabbed, 1, 2)
        layout.addWidget(self.endtabbed, 1, 3)

        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(layout)

    def cascade_windows(self):
        self.mdi.cascadeSubWindows()

    def tile_windows(self):
        self.mdi.tileSubWindows()

    def tabbed_windows(self):
        self.mdi.setViewMode(1)

    def end_tabbed_windows(self):
        self.mdi.setViewMode(0)

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
