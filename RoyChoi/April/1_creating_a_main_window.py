import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)
        gridlayout = QGridLayout()
        self.label = QLabel("Hello, World")
        gridlayout.addWidget(self.label, 0, 0)
        self.imageLabel.setLayout(gridlayout)
        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea |
                                      Qt.RightDockWidgetArea)
        logDockWidget.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.listWidget = QListWidget()
        self.form = Form()
        self.form.setSizeGripEnabled(True)
        # logDockWidget.setWidget(self.listWidget)
        logDockWidget.setWidget(self.form)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        self.printer = None

        self.sizeLabel = QLabel("umm i am ..")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(True)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

        fileNewAction = QAction(QIcon("images/filenew.PNG"), "&New", self)
        fileNewAction.setShortcut(QKeySequence.New)
        helpText = "Create a new image"
        fileNewAction.setToolTip(helpText)
        fileNewAction.setStatusTip(helpText)
        fileNewAction.triggered.connect(self.fileNew)


        fileMenu = QMenuBar()
        fileMenu.addAction(fileNewAction)
        self.setMenuBar(fileMenu)

        toolbar = QToolBar()
        toolbar.addAction(fileNewAction)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

    def fileNew(self):
        print('Hi')

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        pushButton1 = QPushButton()
        pushButton2 = QPushButton()
        gridLayout = QGridLayout()
        gridLayout.addWidget(pushButton1, 0, 0)
        gridLayout.addWidget(pushButton2, 0, 1)
        self.setLayout(gridLayout)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()
