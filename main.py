import sys
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication

import Interface
from Interface.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаем единственный экземпляр QApplication
    app.setWindowIcon(QtGui.QIcon('static/img/iconLogo.ico'))

    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('static/img/iconLogo.ico'))
    window.show()

    sys.exit(app.exec())
