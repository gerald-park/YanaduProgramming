from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from threading import Thread, Timer
from pyModbusTCP.server import ModbusServer, DataBank
from modbus.modbus_server.utilites import *

import time

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define variables in advance
        # Some of them have default value
        self.address = 0
        self.quantity = 10
        self.prevData = None
        self.connectionForm = ConnectionForm()
        self.slaveDefinitionForm = SlaveDefinitionForm()
        self.ipAddress = '127.0.0.1'
        self.port = 502
        self.updateModbusDataThread = None
        self.isThreadRunning = False
        self.columnOffset = None
        self.rowOffset = None
        self.server = None

        # Define a table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(1)

        # Do layout work
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout()
        layout.addWidget(self.tableWidget, 0, 0)
        centralWidget.setLayout(layout)

        # Define menu and connect proper methods
        connectionAction = QAction("&Connection", self)
        connectionAction.setIcon(QIcon("images/connection.png"))
        helpText = "Connection setting"
        connectionAction.setStatusTip(helpText)
        connectionAction.triggered.connect(self.ask_server_definition)

        disconnectionAction = QAction("&Disconnection", self)
        disconnectionAction.setIcon(QIcon("images/disconnection.png"))
        helpText = "Disconnect communication"
        disconnectionAction.setStatusTip(helpText)
        disconnectionAction.triggered.connect(self._close_server)

        setupAction = QAction("&Setup", self)
        helpText = "Setup slave definition"
        setupAction.setStatusTip(helpText)
        setupAction.triggered.connect(self.ask_slave_definition)

        connectionMenu = QMenu('&Connection', self)
        connectionMenu.addAction(connectionAction)
        connectionMenu.addAction(disconnectionAction)

        menuBar = QMenuBar()
        menuBar.addAction(setupAction)
        menuBar.addMenu(connectionMenu)
        self.setMenuBar(menuBar)

        self.sizeLabel = QLabel("{0}, {1}".format(self.width(), self.height()))
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready", 5000)
        self.statusBar.addPermanentWidget(self.sizeLabel)

        self.tableWidget.itemChanged.connect(self._handler_cell_value_changed)
        self.ask_server_definition()
        self.ask_slave_definition()

    def resizeEvent(self, event):
        self.sizeLabel.setText("{0}, {1}".format(event.size().width(), event.size().height()))

    def _close_server(self):
        try:
            if self.server is not None:
                if self.server.is_run:
                    self.server.stop()
                    self.statusBar.showMessage("Server disconnected successfully", 5000)
                    print('Server disconnected successfully')
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Disconnection error', 'disconnection failed!')

    def ask_server_definition(self):
        if self.connectionForm.exec_():
            try:
                self.ipAddress, self.port = self.connectionForm.get_connection_info()
            except Exception as e:
                print(e)
        self._open_server()

    def ask_slave_definition(self):
        if self.slaveDefinitionForm.exec_():
            try:
                self.address, self.quantity = self.slaveDefinitionForm.get_slave_definition_info()
                self.close_thread()
                self.set_default_value()
                self.start_thread()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, 'Value error', 'cannot apply the setting!')

    def _open_server(self):
        try:
            if self.server is None:
                self.server = ModbusServer(self.ipAddress, self.port, no_block=True)
            self.server.start()
            self.setWindowTitle('Modbus Slave, Ip Address : {0}, Port : {1}'.format(self.ipAddress, self.port))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Connection error', 'cannot make a connection!')
            self.ask_server_definition()
        self.statusBar.showMessage("Server opened successfully", 5000)
        print('server opened successfully')

    def thread_main(self):
        if self.isThreadRunning:
            self._handler_data_bank_changed()
            self.updateModbusDataThread = Timer(0.5, self.thread_main).start()

    def start_thread(self):
        self.isThreadRunning = True
        self.thread_main()

    def close_thread(self):
        self.isThreadRunning = False
        if self.updateModbusDataThread is not None:
            self.updateModbusDataThread.cancel()

    def set_default_value(self):
        self.tableWidget.itemChanged.disconnect(self._handler_cell_value_changed)
        self.prevData = DataBank.get_words(self.address, self.quantity)
        columnCount = int(len(self.prevData)/10+1)
        self.columnOffset = int(self.address/10)
        self.rowOffset = self.address - self.columnOffset * 10
        self.tableWidget.setColumnCount(columnCount)
        for i in range(columnCount):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(str((i+self.columnOffset)*10)))
        for i in range(10):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(str(i)))
        for i in range(columnCount * 10):
            row = i % 10
            col = int(i / 10)
            if i >= len(self.prevData) + self.rowOffset or i < self.rowOffset:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemFlag.NoItemFlags)
                self.tableWidget.setItem(row, col, item)
            else:
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(self.prevData[i-self.rowOffset])))
        self.tableWidget.viewport().update()
        self.tableWidget.itemChanged.connect(self._handler_cell_value_changed)
        self.resize(self.tableWidget.width()+176, self.tableWidget.height()+196)

    def _handler_cell_value_changed(self, item):
        row = item.row()
        col = item.column()
        index = col * 10 + row
        if index >= self.quantity + self.rowOffset:
            return
        pre_val = DataBank.get_words(index)[0]
        if item.text() == str(pre_val):
            return
        else:
            try:
                val = int(item.text())
                DataBank.set_words(self.columnOffset*10 + index, [val])
            except Exception as e:
                QMessageBox.warning(self, 'Warning', 'Only integer is acceptable')
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(pre_val)))
                print(e)

    def _handler_data_bank_changed(self):
        newData = DataBank.get_words(self.address, self.quantity)
        for i in range(self.quantity):
            if self.prevData[i] != newData[i]:
                index = i + self.address - self.columnOffset * 10
                row = index % 10
                col = int(index / 10)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(newData[i])))
                self.prevData[i] = newData[i]
        self.tableWidget.viewport().update()


class ConnectionForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Connection Setting')
        self.ipAddress = '127.0.0.1'
        self.port = 502

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        buttonBox.setOrientation(Qt.Orientation.Vertical)

        addressLabel = QLabel("&IP Address")
        set_label_bold_font(addressLabel)
        self.addressEdit = QLineEdit(self.ipAddress)
        addressLabel.setBuddy(self.addressEdit)

        portLabel = QLabel("&Port")
        set_label_bold_font(portLabel)
        self.portEdit = QLineEdit(str(self.port))
        portLabel.setBuddy(self.portEdit)

        layout = QGridLayout()
        layout.addWidget(addressLabel, 0, 0)
        layout.addWidget(self.addressEdit, 1, 0)
        layout.addWidget(portLabel, 0, 1)
        layout.addWidget(self.portEdit, 1, 1)


        frame = QFrame()
        frame.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Sunken)
        frame.setLayout(layout)

        totalLayout = QGridLayout()
        totalLayout.addWidget(buttonBox, 0, 1)
        totalLayout.addWidget(frame, 1, 0)


        self.setLayout(totalLayout)

        buttonBox.accepted.connect(self.my_accept)
        buttonBox.rejected.connect(self.reject)

    def my_accept(self):
        try:
            self.ipAddress = self.addressEdit.text()
            self.port = int(self.portEdit.text())
            self.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Value error', 'Wrong value!')
            self.portEdit.selectAll()
            self.portEdit.setFocus()

    def get_connection_info(self):
        return self.ipAddress, self.port


class SlaveDefinitionForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Setup Slave Definition')
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        self.address = 0
        self.quantity = 10
        addressLabel = QLabel("&Address:")
        set_label_bold_font(addressLabel)
        self.addressEdit = QLineEdit(str(self.address))
        addressLabel.setBuddy(self.addressEdit)

        quantityLabel = QLabel("&Quantity:")
        set_label_bold_font(quantityLabel)
        self.quantityEdit = QLineEdit(str(self.quantity))
        quantityLabel.setBuddy(self.quantityEdit)

        layout = QGridLayout()
        layout.addWidget(addressLabel, 0, 0)
        layout.addWidget(self.addressEdit, 0, 2)
        layout.addWidget(quantityLabel, 1, 0)
        layout.addWidget(self.quantityEdit, 1, 2)
        layout.addWidget(buttonBox, 2, 0, 1, 3)
        self.setLayout(layout)

        buttonBox.accepted.connect(self.my_accept)
        buttonBox.rejected.connect(self.reject)

        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)

    def my_accept(self):
        try:
            self.address = int(self.addressEdit.text())
            self.quantity = int(self.quantityEdit.text())
            self.accept()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Value error', 'Wrong value!, only integer is acceptable')
            self.quantityEdit.selectAll()
            self.quantityEdit.setFocus()

    def get_slave_definition_info(self):
        return self.address, self.quantity


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()