from PyQt5.QtWidgets import *
import sys

class StringListDlg(QDialog):
    def __init__(self, item_list, parent=None):
        super().__init__(parent)
        self.selection = None

        self.listWidget = QListWidget()
        for i in item_list:
            self.listWidget.addItem(QListWidgetItem(i))

        self.listWidget.takeItem(0)
        self.addButton = QPushButton('&Add...')
        self.editButton = QPushButton('&Edit...')
        self.removeButton = QPushButton('&Remove...')
        self.upButton = QPushButton('&Up...')
        self.downButton = QPushButton('&Down...')
        self.sortButton = QPushButton('&Sort...')
        self.closeButton = QPushButton('&Close...')

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.listWidget, 0, 0, 7, 1)
        gridLayout.addWidget(self.addButton, 0, 1)
        gridLayout.addWidget(self.editButton, 1, 1)
        gridLayout.addWidget(self.removeButton, 2, 1)
        gridLayout.addWidget(self.upButton, 3, 1)
        gridLayout.addWidget(self.downButton, 4, 1)
        gridLayout.addWidget(self.sortButton, 5, 1)
        gridLayout.addWidget(self.closeButton, 6, 1)
        self.setLayout(gridLayout)

        self.listWidget.clicked.connect(self.store_selection)
        self.removeButton.clicked.connect(self.remove_item)
        self.addButton.clicked.connect(self.add_item)
        self.show()

    def store_selection(self, value):
        self.selection = value.row()
        print(value.row())

    def remove_item(self):
        if self.selection is None:
            QMessageBox.warning(self, "Warning", "Please select a item")
        else:
            self.listWidget.takeItem(self.selection)

    def add_item(self):
        addDialogue = AddDialogue()
        if addDialogue.exec_():
            print('accepted')
        else:
            print('rejected')

class AddDialogue(QDialog):
    def __init__(self):
        super().__init__()
        editLabel = QLabel("&Type a item to add")
        self.editBox = QLineEdit()
        editLabel.setBuddy(self.editBox)
        gridLayout = QGridLayout()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        gridLayout.addWidget(editLabel, 0, 0)
        gridLayout.addWidget(self.editBox, 1, 0)
        gridLayout.addWidget(self.buttonBox, 2, 0)

        self.setLayout(gridLayout)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


if __name__ == "__main__":
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
    "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
    "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
    "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
    "Orange"]
    app = QApplication(sys.argv)
    form = StringListDlg(fruit)
    form.exec_()