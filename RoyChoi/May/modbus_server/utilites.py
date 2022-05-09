from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def set_label_bold_font(label):
    font = QFont()
    font.setBold(True)
    label.setFont(font)

def print_hi():
    print('hi')