# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# 'mydatabase.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will
# be lost when pyuic5 is
# run again.  Do not edit this file unless you know
# what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 292)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonCreateDb = QtWidgets.QPushButton(Form)
        self.pushButtonCreateDb.setObjectName("pushButtonCreateDb")

        # connected clicked signal with create_database() method
        self.pushButtonCreateDb.clicked.connect(self.create_database)
        self.horizontalLayout_2.addWidget(self.pushButtonCreateDb)
        self.pushButtonDbcon = QtWidgets.QPushButton(Form)
        self.pushButtonDbcon.setObjectName("pushButtonDbcon")

        # connected clicked signal with db_connect() method
        self.pushButtonDbcon.clicked.connect(self.db_connect)
        self.horizontalLayout_2.addWidget(self.pushButtonDbcon)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelResult = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # method for connecting to wamp server mysql database
    def create_database(self):
        try:
            mydb = mc.connect(

                host="localhost",
                user="root",
                password="123456"
            )

            cursor = mydb.cursor()
            dbname = self.lineEdit.text()

            cursor.execute("CREATE DATABASE {} ".format(dbname))
            self.labelResult.setText("Database {} Created ".format(dbname))
        except mc.Error as e:
            self.labelResult.setText("Database creation failed ")

    # method for checking the connection
    def db_connect(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="123456",
                database="mydb"
            )
            self.labelResult.setText("There is connection")


        except mc.Error as err:
            self.labelResult.setText("Error In Connection ")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter Database Name:"))
        self.pushButtonCreateDb.setText(_translate("Form", "Database Creation"))
        self.pushButtonDbcon.setText(_translate("Form", "Database Connection"))
        self.labelResult.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())