import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        settings = QSettings()
        geometry = settings.value('geometry', '')
        self.restoreGeometry(geometry)
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

        fileCloseAction = QAction("&Close", self)
        fileCloseAction.triggered.connect(self.close)

        fileMenu = QMenu("&File", self)
        fileMenu.addAction(fileNewAction)
        fileMenu.addAction(fileCloseAction)

        invertAction = QAction("&Invert", self)
        boldAction = QAction(QIcon("images/bold.PNG"), "&Bold", self)
        boldAction.setCheckable(True)
        boldAction.triggered.connect(self.print_checked_option)
        lightAction = QAction(QIcon("images/light.PNG"), "&Light", self)
        lightAction.triggered.connect(self.print_checked_option)
        lightAction.setCheckable(True)
        lightAction.setChecked(True)
        alignAction = QAction("&Align", self)
        editMenu = QMenu("&Edit", self)
        editMenu.addAction(invertAction)
        editMenu.addSeparator()

        fontMenu = QMenu("&Font", self)

        self.fontActionGroup = QActionGroup(self)
        self.fontActionGroup.addAction(boldAction)
        self.fontActionGroup.addAction(lightAction)

        fontMenu.addAction(boldAction)
        fontMenu.addAction(lightAction)
        fontMenu.addSeparator()
        fontMenu.addAction(alignAction)

        self.imageLabel.addAction(lightAction)
        self.imageLabel.addAction(boldAction)

        editMenu.addMenu(fontMenu)

        MenuBar = QMenuBar()
        MenuBar.addMenu(fileMenu)
        MenuBar.addMenu(editMenu)
        self.setMenuBar(MenuBar)

        fileToolbar = QToolBar()
        fileToolbar.addAction(fileNewAction)
        self.addToolBar(Qt.TopToolBarArea, fileToolbar)

        editToolbar = QToolBar()
        editLabel = QLabel("Edit")
        editToolbar.addWidget(editLabel)
        editToolbar.addAction(boldAction)
        editToolbar.addAction(lightAction)
        self.addToolBar(Qt.TopToolBarArea, editToolbar)



    def closeEvent(self, event):
        print('terminating..')
        settings = QSettings()
        geometry = self.saveGeometry()
        settings.setValue('geometry', geometry)

    def fileNew(self):
        print('Hi')

    def print_checked_option(self):
        print(self.fontActionGroup.checkedAction().text())

    def contextMenuEvent(self, event):
        print('context menu')

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
app.setOrganizationName('Roys')
app.setOrganizationDomain('KR')
app.setApplicationName("Test main window")
main = MainWindow()
main.show()
app.exec_()
