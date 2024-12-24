import sys

from PyQt5 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication

import Interface
from Interface.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('static/img/iconLogo.ico'))

    window = QtWidgets.QWidget()
    window.setWindowIcon(QtGui.QIcon('static/img/iconLogo.ico'))
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
