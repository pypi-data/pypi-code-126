import os
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QPlainTextEdit,
)
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QIntValidator, QIcon

from toori import TooriClient
from .constants import *


class TooriThread(QThread):
    loggerSignal = pyqtSignal(str)
    connectedSignal = pyqtSignal(int)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.tooriClient = TooriClient(
            *args,
            **kwargs,
            loggerSignal=self.loggerSignal,
            connectedSignal=self.connectedSignal
        )

    def run(self):
        if not self.tooriClient.start():
            # Connect failed or WinDivert init failed
            pass

    def stop(self, uninit):
        self.tooriClient.disconnect_sio()
        if uninit:
            self.tooriClient.uninit_WinDivert()
        self.terminate()


class TooriMain(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        onlyInt = QIntValidator()

        self.setWindowIcon(
            QIcon(
                os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "icon.ico"
            )
        )

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setFixedSize(300, 500)
        self.setWindowTitle("Toori")

        self.tooriThread = None

        self.lineedit_host = QLineEdit()
        self.lineedit_port = QLineEdit()
        self.lineedit_filter = QComboBox()
        self.combobox_transports = QComboBox()
        self.lineedit_pkt_key = QLineEdit()
        self.plaintextedit_logs = QPlainTextEdit()

        self.plaintextedit_logs.setReadOnly(True)

        self.combobox_transports.addItems(["Polling", "Websocket", "Auto"])

        self.lineedit_host.setText(URL_DEFAULT)

        self.lineedit_port.setFixedWidth(40)
        self.lineedit_port.setValidator(onlyInt)
        self.lineedit_port.setMaxLength(5)
        self.lineedit_port.setText(str(PORT_DEFAULT))

        self.lineedit_filter.setEditable(True)
        with open(
            os.path.dirname(os.path.realpath(__file__)) + os.path.sep + ".toorifilters",
            "r",
        ) as f:
            filter_list = f.read().strip().split("\n")

        for filter_str in filter_list:
            self.lineedit_filter.addItem(filter_str.strip())

        self.btn_connect = QPushButton(self)
        self.connectedGuiUpdater(0)

        flo = QFormLayout()
        flo.addRow("Host:", self.lineedit_host)
        flo.addRow("Port:", self.lineedit_port)
        flo.addRow("Filter:", self.lineedit_filter)
        flo.addRow("Password:", self.lineedit_pkt_key)
        flo.addRow("Transport:", self.combobox_transports)
        flo.addRow(self.btn_connect)
        flo.addRow(self.plaintextedit_logs)

        self.setLayout(flo)
        self.show()

    def tooriConnect(self):
        try:
            self.tooriThread = TooriThread(
                parent=self,
                server_url=self.lineedit_host.text(),
                server_port=int(self.lineedit_port.text()),
                pkt_filter=self.lineedit_filter.currentText(),
                transport=self.combobox_transports.currentText().lower(),
                pkt_key=self.lineedit_pkt_key.text(),
            )
        except Exception as e:
            self.logger(str(e))
            return

        self.tooriThread.loggerSignal.connect(self.logger)
        self.tooriThread.connectedSignal.connect(self.connectedGuiUpdater)
        self.tooriThread.finished.connect(lambda: self.connectedGuiUpdater(0))

        self.tooriThread.start()

    def tooriDisconnect(self, uninit=False):
        if self.tooriThread:
            self.tooriThread.stop(uninit)
        self.tooriThread = None

    def connectedGuiUpdater(self, i):
        try:
            self.btn_connect.clicked.disconnect()
        except TypeError:
            pass

        if i == 0:
            self.btn_connect.clicked.connect(self.tooriConnect)
            self.btn_connect.setText("Connect")
            self.btn_connect.setStyleSheet("background-color : #00FF7F")
        elif i == 1:
            self.btn_connect.clicked.connect(lambda: self.tooriDisconnect(True))
            self.btn_connect.setText("Disconnect")
            self.btn_connect.setStyleSheet("background-color : red")

    def logger(self, content):
        self.plaintextedit_logs.appendPlainText(content)


def gui_main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    tooriMain = TooriMain()

    app.aboutToQuit.connect(tooriMain.tooriDisconnect)
    sys.exit(app.exec_())
