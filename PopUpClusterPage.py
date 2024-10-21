# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopUpClusterPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Logo
import Icons

class Ui_PopUpClusterPage(object):
    def setupUi(self, PopUpClusterPage):
        if not PopUpClusterPage.objectName():
            PopUpClusterPage.setObjectName(u"PopUpClusterPage")
        PopUpClusterPage.resize(1380, 680)
        PopUpClusterPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.popUpClusterPage = QWidget(PopUpClusterPage)
        self.popUpClusterPage.setObjectName(u"popUpClusterPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popUpClusterPage.sizePolicy().hasHeightForWidth())
        self.popUpClusterPage.setSizePolicy(sizePolicy)
        self.popUpClusterPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.popUpClusterPage)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.name = QHBoxLayout()
        self.name.setSpacing(0)
        self.name.setObjectName(u"name")
        self.title = QHBoxLayout()
        self.title.setSpacing(15)
        self.title.setObjectName(u"title")
        self.titleName = QLabel(self.popUpClusterPage)
        self.titleName.setObjectName(u"titleName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleName.sizePolicy().hasHeightForWidth())
        self.titleName.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(16, 16, 16, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleName.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(30)
        font.setBold(True)
        self.titleName.setFont(font)
        self.titleName.setStyleSheet(u"color: #101010;")

        self.title.addWidget(self.titleName)

        self.pushButtonRedact = QPushButton(self.popUpClusterPage)
        self.pushButtonRedact.setObjectName(u"pushButtonRedact")
        self.pushButtonRedact.setMinimumSize(QSize(36, 36))
        self.pushButtonRedact.setMaximumSize(QSize(36, 36))
        self.pushButtonRedact.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact.setIconSize(QSize(24, 24))

        self.title.addWidget(self.pushButtonRedact)

        self.pushButtonDelete = QPushButton(self.popUpClusterPage)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(36, 36))
        self.pushButtonDelete.setMaximumSize(QSize(36, 36))
        self.pushButtonDelete.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete.setIconSize(QSize(24, 24))

        self.title.addWidget(self.pushButtonDelete)


        self.name.addLayout(self.title)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.name.addItem(self.horizontalSpacer_3)

        self.pushButtonClose = QPushButton(self.popUpClusterPage)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonClose.sizePolicy().hasHeightForWidth())
        self.pushButtonClose.setSizePolicy(sizePolicy1)
        self.pushButtonClose.setMinimumSize(QSize(48, 48))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.pushButtonClose.setFont(font1)
        self.pushButtonClose.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons And Logo/Close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonClose.setIcon(icon)
        self.pushButtonClose.setIconSize(QSize(24, 24))

        self.name.addWidget(self.pushButtonClose)


        self.verticalLayout_2.addLayout(self.name)

        self.description = QVBoxLayout()
        self.description.setSpacing(10)
        self.description.setObjectName(u"description")
        self.vacancy = QLabel(self.popUpClusterPage)
        self.vacancy.setObjectName(u"vacancy")
        sizePolicy1.setHeightForWidth(self.vacancy.sizePolicy().hasHeightForWidth())
        self.vacancy.setSizePolicy(sizePolicy1)
        self.vacancy.setMinimumSize(QSize(0, 30))
        self.vacancy.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.vacancy.setFont(font2)
        self.vacancy.setStyleSheet(u"color: #501EBC;")

        self.description.addWidget(self.vacancy)

        self.listWidget = QListWidget(self.popUpClusterPage)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(1320, 510))
        self.listWidget.setMaximumSize(QSize(1320, 510))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.listWidget.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.listWidget.setFont(font3)
        self.listWidget.setStyleSheet(u"QWidget {\n"
"   color: #101010;\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #E7E7E7;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #5B5B5B;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #5B5B5B;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #5B5B5B;\n"
"	height: 15px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-left-radi"
                        "us: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #501EBC;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty(u"showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(4)

        self.description.addWidget(self.listWidget)


        self.verticalLayout_2.addLayout(self.description)

        PopUpClusterPage.setCentralWidget(self.popUpClusterPage)

        self.retranslateUi(PopUpClusterPage)

        QMetaObject.connectSlotsByName(PopUpClusterPage)
    # setupUi

    def retranslateUi(self, PopUpClusterPage):
        PopUpClusterPage.setWindowTitle(QCoreApplication.translate("PopUpClusterPage", u"Your Vacancy", None))
        self.titleName.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.pushButtonRedact.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonClose.setText("")
        self.vacancy.setText(QCoreApplication.translate("PopUpClusterPage", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("PopUpClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c \u0432\u044b\u0441\u043e\u043a\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u0430\u043b\u043e\u043d\u0430", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0441\u0435\u0442\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432 \u0431\u044b\u0442\u043e\u0432\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("PopUpClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("PopUpClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c \u0432\u044b\u0441\u043e\u043a\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u0430\u043b\u043e\u043d\u0430", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u0441\u0435\u0442\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432 \u0431\u044b\u0442\u043e\u0432\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432 \u0441\u0444\u0435\u0440\u0435 \u043f\u0440\u043e\u0434\u0430\u0436", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("PopUpClusterPage", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u043a\u0430\u0441\u0441\u0438\u0440", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("PopUpClusterPage", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u043d\u0442 \u041c\u0430\u0433\u043d\u0438\u0442", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

