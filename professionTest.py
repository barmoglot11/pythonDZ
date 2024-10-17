import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from professionPage import Ui_ProfessionPage

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_ProfessionPage()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())