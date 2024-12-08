import sqlite3

from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QMainWindow, QFileDialog

from BackEnd.Readers import ReadDocx
from UI_pages import Ui_TakeProfessionPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWind = self
        self.vacancy_info = self.TakeDataFromDB("Vacancy")
        self.ChangeUI(Ui_TakeProfessionPage())
        self.popup = None

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def load_file(self):

        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл",
                                                        "",
                                                        "Документы Word (*.docx);;PDF файлы (*.pdf);;Все файлы (*)",
                                                        options=options)

        if self.file_name:
            ReadDocx(self.file_name)
        else:
            print("Error: No file")

        self.ChangeUI(Ui_TakeProfessionPage())

    def CreatePopup(self, popup, UI, data=None):
        if self.popup is not None:
            self.popup.close()
        match popup:
            case "AddResume":
                self.popup = PopupAddResume(self, UI)
            case "Cluster":
                self.popup = PopupCluster(self, UI, data)
            case "ClusterEdit":
                self.popup = PopupClusterEdit(self, UI)
            case "Profession":
                self.popup = PopupProfession(self, UI, data)
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

    def ChangeDataInDB(self, Table_name, *dataToChange):
        connection = sqlite3.connect('vacancies-sqlite.db')
        cursor = connection.cursor()
        match Table_name:
            case 'Cluster':
                dataProf = dataToChange[-1]
                dataID = dataToChange[0]
                cursor.execute('''
                    UPDATE Cluster
                    SET ClusterProfession = ?
                    WHERE ClusterID = ?
                ''', (dataProf, dataID))

    def UpdateUI(self):
        self.ui.setupUi(self)


class PopupWindow(QMainWindow):
    def __init__(self, mainWind, UI):
        super().__init__()
        self.mainWindows = list()
        self.mainWindows.append(mainWind)
        print("window appeard")
        self.ChangeUI(UI)
        self.show()
        self.setFocus()

    def ChangeUI(self, UI):
        self.ui = UI
        self.ui.setupUi(self)

    def CreatePopup(self, popup, UI, data=None):
        match popup:
            case "AddResume":
                self.popup = PopupAddResume(self, UI)
            case "Cluster":
                self.popup = PopupCluster(self, UI, data)
            case "ClusterEdit":
                self.popup = PopupClusterEdit(self, UI)
            case "Profession":
                self.popup = PopupProfession(self, UI, data)
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
            self.mainWindows[0].ChangeUI(UI)
        self.close()

    def CloseWindow(self):
        self.close()

    def TakeDataFromDB(self, Table_name):
        connection = sqlite3.connect('vacancies-sqlite.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {Table_name}")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data

    def ChangeDataInDB(self, table_name, *dataToChange):
        connection = sqlite3.connect('vacancies-sqlite.db')
        cursor = connection.cursor()
        data = dataToChange[0]
        match table_name:
            case 'Cluster':
                dataProf = data[-1]
                dataID = data[0]
                cursor.execute('''
                    UPDATE Cluster
                    SET ClusterProfession = ?
                    WHERE ClusterID = ?
                ''', (dataProf, dataID))
            case 'Vacancy':
                dataID = data[0]
                dataName = data[1]
                dataDescription = data[2]
                cursor.execute('''
                                UPDATE Vacancy
                                SET VacancyName = ?,
                                    VacancyDesc = ?
                                WHERE VacancyID = ?
                            ''', (dataName, dataDescription, dataID))
        connection.commit()
        cursor.close()
        connection.close()

    def UpdateUI(self):

        self.mainWindows[-1].ui.setupUi(self.mainWindows[-1])
        self.ui.setupUi(self)


class PopupAddResume(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)

    def load_file(self):

        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл",
                                                        "",
                                                        "Документы Word (*.docx);;PDF файлы (*.pdf);;Все файлы (*)",
                                                        options=options)
        if self.file_name:
            ReadDocx(self.file_name)
        else:
            print("Error: No file")

        self.mainW.ChangeUI(Ui_TakeProfessionPage())


class PopupCluster(PopupWindow):
    def __init__(self, mainWind, UI, data):
        self.data = list()
        if data is not None:
            self.data = data
        else:
            self.data.extend(["", ""])
        super().__init__(mainWind, UI)


class PopupClusterEdit(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)

    def Apply(self):
        dataToChange = self.ui.Save()
        self.ChangeDataInDB('Cluster', dataToChange)


        self.mainWindows[-1].UpdateUI()
        self.mainWindows[-1].ui.setupUi(self.mainWindows[-1])
        self.close()


class PopupProfession(PopupWindow):
    def __init__(self, mainWind, UI, data):
        self.data = list()
        if data is not None:
            self.data = data
        else:
            self.data.extend(["", "", "", "", 0])
        super().__init__(mainWind, UI)


class PopupProfessionEdit(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)

    def Apply(self):
        dataToChange = self.ui.Save()
        self.ChangeDataInDB('Vacancy', dataToChange)

        self.mainWindows[-1].ui.setupUi(self.mainWindows[-1])
        self.mainWindows[-1].UpdateUI()
        self.close()


class PopupSave(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)

    def Save(self):
        self.mainWindows[-1].Apply()
        self.close()


class PopupDelete(PopupWindow):
    def __init__(self, mainWind, UI):
        super().__init__(mainWind, UI)
