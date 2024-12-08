import sys

from PyQt5 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication

from MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('iconLogo.ico'))

    window = QtWidgets.QWidget()
    window.setWindowIcon(QtGui.QIcon('iconLogo.ico'))
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
