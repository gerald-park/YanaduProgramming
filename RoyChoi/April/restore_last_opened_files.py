from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
import sys

class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fname = None
        self.settings = QSettings("Nasa", "Space-x")
        self.lastFilenames = self.settings.value("previous")
        self.lineEdit = QLineEdit()
        self.imageLabel = QLabel()
        if self.lastFilenames is None:
            self.lastFilenames = []
        else:
            self.set_pixmap(self.lastFilenames[0])





        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit, 0, 0)
        gridLayout.addWidget(self.imageLabel, 1, 0)
        centralWidget.setLayout(gridLayout)

        openAction = QAction("Open", self)
        openAction.triggered.connect(self.open_file_dialog)

        recentMenu = QMenu("Recent", self)

        fileMenu = QMenu("file", self)
        fileMenu.addAction(openAction)
        fileMenu.addMenu(recentMenu)

        menubar = QMenuBar()
        self.setMenuBar(menubar)
        menubar.addMenu(fileMenu)

        for i in self.lastFilenames:
            self.append_action(recentMenu, i, self.recent_action_triggered)

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileNames(self, 'Open File', './images', 'All File(*);; My Image File(*.png *.jpg)')[0][0]
        self.set_pixmap(fname)

    def set_pixmap(self, filename):
        self.fname = filename
        self.pixmap = QPixmap(filename)
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.resize(self.pixmap.width(), self.pixmap.height())

    def append_action(self, menu, action_text, slot):
        action = QAction(action_text, self)
        action.triggered.connect(slot)
        menu.addAction(action)

    def recent_action_triggered(self):
        self.set_pixmap(self.sender().text())

    def closeEvent(self, event):
        super().closeEvent(event)
        if self.fname is None:
            return
        if self.fname in self.lastFilenames:
            self.lastFilenames.remove(self.fname)
        self.lastFilenames.insert(0, self.fname)
        if len(self.lastFilenames) > 5:
            self.lastFilenames = self.lastFilenames[:5]
        self.settings.setValue("previous", self.lastFilenames)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()