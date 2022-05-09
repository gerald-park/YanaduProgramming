from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        gridlayout = QGridLayout()
        gridlayout.addWidget(self.tableWidget)
        self.setLayout(gridlayout)

        # self.tableWidget.itemChanged.connect(self.edit_value)
        self.tableWidget.setItem(1, 1, QTableWidgetItem('Test'))
        self.tableWidget.setItem(0, 0, QTableWidgetItem('Test'))
        self.testItem = QTableWidgetItem()
        self.testItem.setFlags(Qt.ItemFlag.NoItemFlags)
        self.tableWidget.setItem(1, 1, self.testItem)
        self.testItem = QTableWidgetItem()
        self.testItem.setFlags(Qt.ItemFlag.NoItemFlags)
        self.tableWidget.setItem(1, 1, self.testItem)


    def edit_value(self, item):
        try:
            item.setFlags(Qt.ItemIsEditable | Qt.ItemIsSelectable)
        except Exception as e:
            print(e)




app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()