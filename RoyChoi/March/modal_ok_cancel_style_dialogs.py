from PyQt5.QtWidgets import *
import sys
from PyQt5.Qt import *

Punctuation = [',', '.', '!', '?', '-', '_']

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("modal ok cancel type practice")
        self.format = dict(thousandsseparator=",",
        decimalmarker=".", decimalplaces=2,
        rednegatives=False)
        self.cetralwidet = QWidget()
        self.setCentralWidget(self.cetralwidet)
        self.numberLabel = QLabel("12345676")

        self.setFormatButton1 = QPushButton()
        self.setFormatButton1.setText("Setting1")
        self.setFormatButton1.clicked.connect(self.setNumberFormat1)

        self.setFormatButton2 = QPushButton()
        self.setFormatButton2.setText("Setting2")
        self.setFormatButton2.clicked.connect(self.setNumberFormat2)

        gridlayout = QGridLayout()
        gridlayout.addWidget(self.numberLabel, 0, 0)
        gridlayout.addWidget(self.setFormatButton1, 0, 1)
        gridlayout.addWidget(self.setFormatButton2, 0, 2)
        self.cetralwidet.setLayout(gridlayout)

    def setNumberFormat2(self):
        dialog2 = NumberFormatDlg2(self.format, self)
        dialog2.show()

    def setNumberFormat1(self):
        dialog1 = NumberFormatDlg(self.format, self)
        # dialog1 has accept() and reject() method
        # accept() terminates event loop with return value true
        # reject() terminates event loop with return value false
        # both methods emit accepted rejected signal respectively for users to connect custom slots
        if dialog1.exec_():
            self.format = dialog1.numberFormat()
            print(self.format)

class NumberFormatDlg(QDialog):
    def __init__(self, format, parent=None):
        super().__init__(parent)

        # define widgets with default value passed by parent
        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        # copy original data to modify
        self.format = format.copy()

        # set layout
        gridlayout = QGridLayout()
        gridlayout.addWidget(thousandsLabel, 0, 0)
        gridlayout.addWidget(self.thousandsEdit, 0, 1)
        gridlayout.addWidget(decimalMarkerLabel, 1, 0)
        gridlayout.addWidget(self.decimalMarkerEdit, 1, 1)
        gridlayout.addWidget(decimalPlacesLabel, 2, 0)
        gridlayout.addWidget(self.decimalPlacesSpinBox, 2, 1)
        gridlayout.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
        gridlayout.addWidget(buttonBox, 4, 0, 1, 2)
        self.setLayout(gridlayout)

        # make connections
        buttonBox.accepted.connect(self.myaccept)
        buttonBox.rejected.connect(self.reject)

    def numberFormat(self):
        return self.format

    def myaccept(self):
        class DecimalError(Exception): pass
        class ThousandsError(Exception): pass
        thousands = self.thousandsEdit.text()
        decimal = self.decimalMarkerEdit.text()
        try:
            if len(decimal) == 0:
                raise DecimalError("The decimal marker may not be empty")
            if len(decimal) > 1:
                raise DecimalError("The decimal marker must be one character")
            if decimal not in Punctuation:
                raise DecimalError("The decimal marker must be a punctuation symbol")
            if thousands == decimal:
                raise ThousandsError("the thousands separator and the decimal marker must be different")
            if len(thousands) > 1:
                raise ThousandsError("Thousands separator may only be empty or one character")
            self.format["thousandsseparator"] = thousands
            self.format["decimalmarker"] = decimal
            self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
            self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
            self.numberFormat()
            self.accept()
        except DecimalError as e:
            QMessageBox.warning(self, "DecimalError", str(e))
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
        except ThousandsError as e:
            QMessageBox.warning(self, "ThousandsError", str(e))
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
        except Exception as e:
            print(e)

class NumberFormatDlg2(QDialog):
    def __init__(self, format, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        punctuationRe = QRegExp(r"[[,;:\n.]")
        thousandsLabel = QLabel("&Thousands separator")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        self.thousandsEdit.setMaxLength(1)
        self.thousandsEdit.setValidator(
            QRegExpValidator(punctuationRe, self))
        decimalMarkerLabel = QLabel("Decimal &marker")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(
            QRegExpValidator(punctuationRe, self))
        self.decimalMarkerEdit.setInputMask("X")
        decimalPlacesLabel = QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Apply |
                                     QDialogButtonBox.Close)
        self.format = format
        applyButton = buttonBox.button(QDialogButtonBox.Apply)
        applyButton.clicked.connect(self.apply)
        self.setWindowTitle("Set Number Format (Modeless)")

        # set layout
        gridlayout = QGridLayout()
        gridlayout.addWidget(thousandsLabel, 0, 0)
        gridlayout.addWidget(self.thousandsEdit, 0, 1)
        gridlayout.addWidget(decimalMarkerLabel, 1, 0)
        gridlayout.addWidget(self.decimalMarkerEdit, 1, 1)
        gridlayout.addWidget(decimalPlacesLabel, 2, 0)
        gridlayout.addWidget(self.decimalPlacesSpinBox, 2, 1)
        gridlayout.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
        gridlayout.addWidget(buttonBox, 4, 0, 1, 2)
        self.setLayout(gridlayout)

    def apply(self):
        print('hi')

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()