from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class PenPropertiesDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setRange(0, 24)
        self.widthSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        styleLabel = QLabel("&Style")
        self.styleComboBox = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")


        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch(1)
        buttonlayout.addWidget(okButton)
        buttonlayout.addWidget(cancelButton)
        buttonlayout.addStretch(1)
        layout.addLayout(buttonlayout, 2, 0, 1, 3)
        self.setLayout(layout)

app = QApplication(sys.argv)
form = PenPropertiesDlg()
form.show()
app.exec_()