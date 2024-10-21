import sys

from PyQt5 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog, QPushButton
from PySide6.QtCore import Qt

from TakeProfessionNonePage import Ui_TakeProfessionNonePage
from TakeProfessionPage import Ui_TakeProfessionPage
from ClusterPage import Ui_ClusterPage
from ProfessionPage import Ui_ProfessionPage
from PopUpAddResumePage import Ui_PopUpProfessionChangePage
from PopUpClusterChangePage import Ui_PopUpClusterChangePage
from PopUpClusterPage import Ui_PopUpClusterPage
from PopUpDeleteAttentionPage import Ui_PopUpDeleteAttentionPage
from PopUpProfessionChangePage import Ui_PopUpProfessionChangePage
from PopUpProfessionPage import Ui_PopUpProfessionPage
from PopUpSaveAttentionPage import Ui_PopUpSaveAttentionPage

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_TakeProfessionNonePage()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('iconLogo.ico'))

    window = QtWidgets.QWidget()
    window.setWindowIcon(QtGui.QIcon('iconLogo.ico'))
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())