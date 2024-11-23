import sqlite3

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QWidget
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog, QPushButton, QFileDialog
from PySide6.QtCore import Qt, QEvent

from UI_pages import Ui_TakeProfessionNonePage, Ui_TakeProfessionPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vacancy_info = self.TakeDataFromDB("Vacancy")
        self.ChangeUI(Ui_TakeProfessionPage())
        self.popup = None

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def load_file(self):
        # Открываем диалог выбора файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*);;Текстовые файлы (*.txt)",
                                                   options=options)
        self.ChangeUI(Ui_TakeProfessionPage())

    def CreatePopup(self, popup, UI):
        if self.popup is not None:
            self.popup.close()
        match popup:
            case "AddResume":
                self.popup = PopupAddResume(self, UI)
            case "Cluster":
                self.popup = PopupCluster(self, UI)
            case "ClusterEdit":
                self.popup = PopupClusterEdit(self, UI)
            case "Profession":
                self.popup = PopupProfession(self, UI)
            case "ProfessionEdit":
                self.popup = PopupProfessionEdit(self, UI)
            case "Apply":
                self.popup = PopupSave(self, UI)
            case "Delete":
                self.popup = PopupDelete(self, UI)

    def TakeDataFromDB(self, Table_name):
        connection = sqlite3.connect('vacancies-sqlite.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {Table_name}")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data


class PopupWindow(QMainWindow):
    def __init__(self, mainWind, UI):
        super().__init__()
        self.mainW = mainWind
        print("window appeard")
        self.ChangeUI(UI)
        self.show()
        self.setFocus()

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def CreatePopup(self, popup, UI):
        match popup:
            case "AddResume":
                self.popup = PopupAddResume(self, UI)
            case "Cluster":
                self.popup = PopupCluster(self, UI)
            case "ClusterEdit":
                self.popup = PopupClusterEdit(self, UI)
            case "Profession":
                self.popup = PopupProfession(self, UI)
            case "ProfessionEdit":
                self.popup = PopupProfessionEdit(self, UI)
            case "Apply":
                self.popup = PopupSave(self, UI)
            case "Delete":
                self.popup = PopupDelete(self, UI)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def Apply(self, UI=None):
        if UI is not None:
            self.mainW.ChangeUI(UI)
        self.close()

    def CloseWindow(self):
        self.close()

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            # Проверяем, находится ли курсор мыши вне окна
            if not self.geometry().contains(event.globalPos()):
                self.close()  # Закрываем окно
        return super().eventFilter(source, event)


class PopupAddResume(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)

    def load_file(self):
        # Открываем диалог выбора файла
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*);;Текстовые файлы (*.txt)",
                                                   options=options)
        self.mainW.ChangeUI(Ui_TakeProfessionPage())
        self.close()


class PopupCluster(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)


class PopupClusterEdit(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)


class PopupProfession(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)


class PopupProfessionEdit(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)


class PopupSave(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)


class PopupDelete(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)
