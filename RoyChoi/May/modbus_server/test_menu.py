from PyQt5.QtWidgets import *
import sys

class Form(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        connectionMenu = menubar.addMenu('&Connection')
        connectionAction = connectionMenu.addAction('&Connection')
        disconnectionAction = connectionMenu.addAction('&Disconnection')

        connectionAction.triggered.connect(self.connected)
        disconnectionAction.triggered.connect(self.disconnected)

    def connected(self):
        print('connected')

    def disconnected(self):
        print('disconnected')

class Form2(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define menu and connect proper methods
        connectionMenu = QMenu('&Connection', self)

        connectionAction = QAction("&Connection", self)
        disconnectionAction = QAction("&Disconnection", self)
        setupAction = QAction("&Setup", self)
        menuBar = QMenuBar()
        # menuBar.addAction(connectionAction)
        menuBar.addAction(setupAction)
        menuBar.addMenu(connectionMenu)
        connectionMenu.addAction(connectionAction)
        connectionMenu.addAction(disconnectionAction)
        self.setMenuBar(menuBar)


    def connected(self):
        print('connected')

    def disconnected(self):
        print('disconnected')


app = QApplication(sys.argv)
form = Form2()
form.show()
app.exec_()
