# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfessionPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_ProfessionPage(object):
    def setupUi(self, ProfessionPage):
        if not ProfessionPage.objectName():
            ProfessionPage.setObjectName(u"ProfessionPage")
        ProfessionPage.resize(1920, 1120)
        palette = QPalette()
        brush = QBrush(QColor(1, 1, 1, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        ProfessionPage.setPalette(palette)
        ProfessionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.professionPage = QWidget(ProfessionPage)
        self.professionPage.setObjectName(u"professionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.professionPage.sizePolicy().hasHeightForWidth())
        self.professionPage.setSizePolicy(sizePolicy)
        self.professionPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.professionPage)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.professionPage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setLayoutDirection(Qt.LeftToRight)
        self.headerFrame.setStyleSheet(u"background-color: #FFFFFF;\n"
"border-bottom: 2px solid #E7E7E7;")
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(self.headerFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(180, 80))
        self.label.setMaximumSize(QSize(180, 80))
        self.label.setStyleSheet(u"background-image: url(:/Logo/Icons And Logo/Logo.png);\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.headerFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
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
        self.pushButton.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(24)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.headerFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton_2.setPalette(palette2)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.headerFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.title = QFrame(self.professionPage)
        self.title.setObjectName(u"title")
        self.horizontalLayout_4 = QHBoxLayout(self.title)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 0, 30, 0)
        self.titleButton = QHBoxLayout()
        self.titleButton.setSpacing(20)
        self.titleButton.setObjectName(u"titleButton")
        self.title_2 = QLabel(self.title)
        self.title_2.setObjectName(u"title_2")
        sizePolicy1.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy1)
        palette3 = QPalette()
        brush3 = QBrush(QColor(80, 30, 188, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.title_2.setPalette(palette3)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleButton.addWidget(self.title_2)

        self.pushButtonAddTags = QPushButton(self.title)
        self.pushButtonAddTags.setObjectName(u"pushButtonAddTags")
        self.pushButtonAddTags.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonAddTags.sizePolicy().hasHeightForWidth())
        self.pushButtonAddTags.setSizePolicy(sizePolicy1)
        self.pushButtonAddTags.setMinimumSize(QSize(205, 48))
        self.pushButtonAddTags.setMaximumSize(QSize(205, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.pushButtonAddTags.setPalette(palette4)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(17)
        font2.setBold(True)
        self.pushButtonAddTags.setFont(font2)
        self.pushButtonAddTags.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        self.pushButtonAddTags.setIconSize(QSize(24, 24))

        self.titleButton.addWidget(self.pushButtonAddTags)


        self.horizontalLayout_4.addLayout(self.titleButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.find = QFrame(self.title)
        self.find.setObjectName(u"find")
        self.horizontalLayout_2 = QHBoxLayout(self.find)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.findInput = QLineEdit(self.find)
        self.findInput.setObjectName(u"findInput")
        self.findInput.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.findInput.sizePolicy().hasHeightForWidth())
        self.findInput.setSizePolicy(sizePolicy2)
        self.findInput.setMinimumSize(QSize(685, 48))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.findInput.setPalette(palette5)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setKerning(True)
        self.findInput.setFont(font3)
        self.findInput.setAcceptDrops(True)
        self.findInput.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #5B5B5B;\n"
"	border-radius: 10px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	color: #101010;\n"
"}")

        self.horizontalLayout_2.addWidget(self.findInput)

        self.pushButtonFind = QPushButton(self.find)
        self.pushButtonFind.setObjectName(u"pushButtonFind")
        self.pushButtonFind.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonFind.sizePolicy().hasHeightForWidth())
        self.pushButtonFind.setSizePolicy(sizePolicy1)
        self.pushButtonFind.setMinimumSize(QSize(48, 48))
        self.pushButtonFind.setFont(font)
        self.pushButtonFind.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons And Logo/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonFind.setIcon(icon)
        self.pushButtonFind.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButtonFind)


        self.horizontalLayout_4.addWidget(self.find)


        self.verticalLayout.addWidget(self.title, 0, Qt.AlignTop)

        self.professionsFrame = QFrame(self.professionPage)
        self.professionsFrame.setObjectName(u"professionsFrame")
        self.professionsFrame.setStyleSheet(u"background-color: none;")
        self.professions = QHBoxLayout(self.professionsFrame)
        self.professions.setSpacing(20)
        self.professions.setObjectName(u"professions")
        self.professions.setContentsMargins(30, -1, 30, -1)
        self.gridProfessions = QGridLayout()
        self.gridProfessions.setObjectName(u"gridProfessions")
        self.gridProfessions.setHorizontalSpacing(22)
        self.gridProfessions.setVerticalSpacing(20)
        self.profession = QFrame(self.professionsFrame)
        self.profession.setObjectName(u"profession")
        self.profession.setMinimumSize(QSize(346, 407))
        self.profession.setMaximumSize(QSize(346, 407))
        self.profession.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.profession)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.professionButtons = QHBoxLayout()
        self.professionButtons.setObjectName(u"professionButtons")
        self.professionName = QLabel(self.profession)
        self.professionName.setObjectName(u"professionName")
        self.professionName.setMinimumSize(QSize(248, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName.setPalette(palette6)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setKerning(True)
        self.professionName.setFont(font4)
        self.professionName.setStyleSheet(u"border: none;")

        self.professionButtons.addWidget(self.professionName)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(10)
        self.buttons.setObjectName(u"buttons")
        self.pushButtonRedact = QPushButton(self.profession)
        self.pushButtonRedact.setObjectName(u"pushButtonRedact")
        self.pushButtonRedact.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact.setIconSize(QSize(24, 24))

        self.buttons.addWidget(self.pushButtonRedact)

        self.pushButtonDelete = QPushButton(self.profession)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete.setIconSize(QSize(24, 24))

        self.buttons.addWidget(self.pushButtonDelete)


        self.professionButtons.addLayout(self.buttons)


        self.verticalLayout_6.addLayout(self.professionButtons)

        self.professionInfo = QVBoxLayout()
        self.professionInfo.setSpacing(10)
        self.professionInfo.setObjectName(u"professionInfo")
        self.city = QHBoxLayout()
        self.city.setSpacing(10)
        self.city.setObjectName(u"city")
        self.iconCity = QPushButton(self.profession)
        self.iconCity.setObjectName(u"iconCity")
        self.iconCity.setMinimumSize(QSize(20, 20))
        self.iconCity.setMaximumSize(QSize(20, 20))
        self.iconCity.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity.setIconSize(QSize(24, 24))

        self.city.addWidget(self.iconCity)

        self.textCity = QLabel(self.profession)
        self.textCity.setObjectName(u"textCity")
        self.textCity.setMaximumSize(QSize(16777215, 20))
        palette7 = QPalette()
        brush4 = QBrush(QColor(91, 91, 91, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity.setPalette(palette7)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(13)
        font5.setBold(True)
        self.textCity.setFont(font5)
        self.textCity.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city.addWidget(self.textCity)


        self.professionInfo.addLayout(self.city)

        self.money = QHBoxLayout()
        self.money.setSpacing(10)
        self.money.setObjectName(u"money")
        self.iconMoney = QPushButton(self.profession)
        self.iconMoney.setObjectName(u"iconMoney")
        self.iconMoney.setMinimumSize(QSize(20, 20))
        self.iconMoney.setMaximumSize(QSize(20, 20))
        self.iconMoney.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney.setIconSize(QSize(24, 24))

        self.money.addWidget(self.iconMoney)

        self.textMoney = QLabel(self.profession)
        self.textMoney.setObjectName(u"textMoney")
        self.textMoney.setMaximumSize(QSize(16777215, 20))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney.setPalette(palette8)
        self.textMoney.setFont(font5)
        self.textMoney.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money.addWidget(self.textMoney)


        self.professionInfo.addLayout(self.money)

        self.description = QVBoxLayout()
        self.description.setSpacing(5)
        self.description.setObjectName(u"description")
        self.titleDescription = QLabel(self.profession)
        self.titleDescription.setObjectName(u"titleDescription")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription.setPalette(palette9)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.titleDescription.setFont(font6)
        self.titleDescription.setStyleSheet(u"border: none;")

        self.description.addWidget(self.titleDescription)

        self.textDescription = QTextBrowser(self.profession)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setStyleSheet(u"border: none;")

        self.description.addWidget(self.textDescription)


        self.professionInfo.addLayout(self.description)


        self.verticalLayout_6.addLayout(self.professionInfo)

        self.pushButtonMore = QPushButton(self.profession)
        self.pushButtonMore.setObjectName(u"pushButtonMore")
        sizePolicy1.setHeightForWidth(self.pushButtonMore.sizePolicy().hasHeightForWidth())
        self.pushButtonMore.setSizePolicy(sizePolicy1)
        self.pushButtonMore.setMinimumSize(QSize(0, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore.setPalette(palette10)
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setUnderline(True)
        self.pushButtonMore.setFont(font7)
        self.pushButtonMore.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButtonMore, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession, 0, 0, 1, 1)

        self.professionAdd = QFrame(self.professionsFrame)
        self.professionAdd.setObjectName(u"professionAdd")
        self.professionAdd.setMinimumSize(QSize(346, 407))
        self.professionAdd.setMaximumSize(QSize(346, 407))
        self.professionAdd.setLayoutDirection(Qt.LeftToRight)
        self.professionAdd.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: 2px dashed #501EBC;\n"
"border-radius: 10px;")
        self.pushButtonAdd = QPushButton(self.professionAdd)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(125, 113, 96, 96))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(96)
        sizePolicy3.setVerticalStretch(96)
        sizePolicy3.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy3)
        self.pushButtonAdd.setMinimumSize(QSize(96, 96))
        self.pushButtonAdd.setMaximumSize(QSize(96, 96))
        self.pushButtonAdd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(80, 30, 188);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 19, 116);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons And Logo/Add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setIconSize(QSize(56, 56))
        self.textAdd = QLabel(self.professionAdd)
        self.textAdd.setObjectName(u"textAdd")
        self.textAdd.setGeometry(QRect(80, 230, 191, 28))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(28)
        sizePolicy4.setHeightForWidth(self.textAdd.sizePolicy().hasHeightForWidth())
        self.textAdd.setSizePolicy(sizePolicy4)
        self.textAdd.setMinimumSize(QSize(0, 28))
        self.textAdd.setMaximumSize(QSize(16777215, 28))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textAdd.setPalette(palette11)
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(18)
        font8.setBold(True)
        self.textAdd.setFont(font8)
        self.textAdd.setStyleSheet(u"border: none;")
        self.textAdd_2 = QLabel(self.professionAdd)
        self.textAdd_2.setObjectName(u"textAdd_2")
        self.textAdd_2.setGeometry(QRect(110, 260, 131, 28))
        sizePolicy4.setHeightForWidth(self.textAdd_2.sizePolicy().hasHeightForWidth())
        self.textAdd_2.setSizePolicy(sizePolicy4)
        self.textAdd_2.setMinimumSize(QSize(0, 28))
        self.textAdd_2.setMaximumSize(QSize(16777215, 28))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textAdd_2.setPalette(palette12)
        self.textAdd_2.setFont(font8)
        self.textAdd_2.setStyleSheet(u"border: none;")

        self.gridProfessions.addWidget(self.professionAdd, 1, 1, 1, 1)

        self.profession_3 = QFrame(self.professionsFrame)
        self.profession_3.setObjectName(u"profession_3")
        self.profession_3.setMinimumSize(QSize(346, 407))
        self.profession_3.setMaximumSize(QSize(346, 407))
        self.profession_3.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.profession_3)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_7 = QHBoxLayout()
        self.professionButtons_7.setObjectName(u"professionButtons_7")
        self.professionName_7 = QLabel(self.profession_3)
        self.professionName_7.setObjectName(u"professionName_7")
        self.professionName_7.setMinimumSize(QSize(248, 0))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName_7.setPalette(palette13)
        self.professionName_7.setFont(font4)
        self.professionName_7.setStyleSheet(u"border: none;")

        self.professionButtons_7.addWidget(self.professionName_7)

        self.buttons_7 = QHBoxLayout()
        self.buttons_7.setSpacing(10)
        self.buttons_7.setObjectName(u"buttons_7")
        self.pushButtonRedact_7 = QPushButton(self.profession_3)
        self.pushButtonRedact_7.setObjectName(u"pushButtonRedact_7")
        self.pushButtonRedact_7.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_7.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_7.setIconSize(QSize(24, 24))

        self.buttons_7.addWidget(self.pushButtonRedact_7)

        self.pushButtonDelete_7 = QPushButton(self.profession_3)
        self.pushButtonDelete_7.setObjectName(u"pushButtonDelete_7")
        self.pushButtonDelete_7.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_7.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_7.setIconSize(QSize(24, 24))

        self.buttons_7.addWidget(self.pushButtonDelete_7)


        self.professionButtons_7.addLayout(self.buttons_7)


        self.verticalLayout_7.addLayout(self.professionButtons_7)

        self.professionInfo_2 = QVBoxLayout()
        self.professionInfo_2.setSpacing(10)
        self.professionInfo_2.setObjectName(u"professionInfo_2")
        self.city_2 = QHBoxLayout()
        self.city_2.setSpacing(10)
        self.city_2.setObjectName(u"city_2")
        self.iconCity_2 = QPushButton(self.profession_3)
        self.iconCity_2.setObjectName(u"iconCity_2")
        self.iconCity_2.setMinimumSize(QSize(20, 20))
        self.iconCity_2.setMaximumSize(QSize(20, 20))
        self.iconCity_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity_2.setIconSize(QSize(24, 24))

        self.city_2.addWidget(self.iconCity_2)

        self.textCity_2 = QLabel(self.profession_3)
        self.textCity_2.setObjectName(u"textCity_2")
        self.textCity_2.setMaximumSize(QSize(16777215, 20))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity_2.setPalette(palette14)
        self.textCity_2.setFont(font5)
        self.textCity_2.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city_2.addWidget(self.textCity_2)


        self.professionInfo_2.addLayout(self.city_2)

        self.money_2 = QHBoxLayout()
        self.money_2.setSpacing(10)
        self.money_2.setObjectName(u"money_2")
        self.iconMoney_2 = QPushButton(self.profession_3)
        self.iconMoney_2.setObjectName(u"iconMoney_2")
        self.iconMoney_2.setMinimumSize(QSize(20, 20))
        self.iconMoney_2.setMaximumSize(QSize(20, 20))
        self.iconMoney_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_2.setIconSize(QSize(24, 24))

        self.money_2.addWidget(self.iconMoney_2)

        self.textMoney_2 = QLabel(self.profession_3)
        self.textMoney_2.setObjectName(u"textMoney_2")
        self.textMoney_2.setMaximumSize(QSize(16777215, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney_2.setPalette(palette15)
        self.textMoney_2.setFont(font5)
        self.textMoney_2.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_2.addWidget(self.textMoney_2)


        self.professionInfo_2.addLayout(self.money_2)

        self.description_2 = QVBoxLayout()
        self.description_2.setSpacing(5)
        self.description_2.setObjectName(u"description_2")
        self.titleDescription_2 = QLabel(self.profession_3)
        self.titleDescription_2.setObjectName(u"titleDescription_2")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription_2.setPalette(palette16)
        self.titleDescription_2.setFont(font6)
        self.titleDescription_2.setStyleSheet(u"border: none;")

        self.description_2.addWidget(self.titleDescription_2)

        self.textDescription_2 = QTextBrowser(self.profession_3)
        self.textDescription_2.setObjectName(u"textDescription_2")
        self.textDescription_2.setStyleSheet(u"border: none;")

        self.description_2.addWidget(self.textDescription_2)


        self.professionInfo_2.addLayout(self.description_2)


        self.verticalLayout_7.addLayout(self.professionInfo_2)

        self.pushButtonMore_3 = QPushButton(self.profession_3)
        self.pushButtonMore_3.setObjectName(u"pushButtonMore_3")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_3.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_3.setSizePolicy(sizePolicy1)
        self.pushButtonMore_3.setMinimumSize(QSize(0, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore_3.setPalette(palette17)
        self.pushButtonMore_3.setFont(font7)
        self.pushButtonMore_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButtonMore_3, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession_3, 0, 1, 1, 1)

        self.profession_4 = QFrame(self.professionsFrame)
        self.profession_4.setObjectName(u"profession_4")
        self.profession_4.setMinimumSize(QSize(346, 407))
        self.profession_4.setMaximumSize(QSize(346, 407))
        self.profession_4.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.profession_4)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_8 = QHBoxLayout()
        self.professionButtons_8.setObjectName(u"professionButtons_8")
        self.professionName_8 = QLabel(self.profession_4)
        self.professionName_8.setObjectName(u"professionName_8")
        self.professionName_8.setMinimumSize(QSize(248, 0))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName_8.setPalette(palette18)
        self.professionName_8.setFont(font4)
        self.professionName_8.setStyleSheet(u"border: none;")

        self.professionButtons_8.addWidget(self.professionName_8)

        self.buttons_8 = QHBoxLayout()
        self.buttons_8.setSpacing(10)
        self.buttons_8.setObjectName(u"buttons_8")
        self.pushButtonRedact_8 = QPushButton(self.profession_4)
        self.pushButtonRedact_8.setObjectName(u"pushButtonRedact_8")
        self.pushButtonRedact_8.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_8.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_8.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_8.setIconSize(QSize(24, 24))

        self.buttons_8.addWidget(self.pushButtonRedact_8)

        self.pushButtonDelete_8 = QPushButton(self.profession_4)
        self.pushButtonDelete_8.setObjectName(u"pushButtonDelete_8")
        self.pushButtonDelete_8.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_8.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_8.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_8.setIconSize(QSize(24, 24))

        self.buttons_8.addWidget(self.pushButtonDelete_8)


        self.professionButtons_8.addLayout(self.buttons_8)


        self.verticalLayout_8.addLayout(self.professionButtons_8)

        self.professionInfo_3 = QVBoxLayout()
        self.professionInfo_3.setSpacing(10)
        self.professionInfo_3.setObjectName(u"professionInfo_3")
        self.city_3 = QHBoxLayout()
        self.city_3.setSpacing(10)
        self.city_3.setObjectName(u"city_3")
        self.iconCity_3 = QPushButton(self.profession_4)
        self.iconCity_3.setObjectName(u"iconCity_3")
        self.iconCity_3.setMinimumSize(QSize(20, 20))
        self.iconCity_3.setMaximumSize(QSize(20, 20))
        self.iconCity_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity_3.setIconSize(QSize(24, 24))

        self.city_3.addWidget(self.iconCity_3)

        self.textCity_3 = QLabel(self.profession_4)
        self.textCity_3.setObjectName(u"textCity_3")
        self.textCity_3.setMaximumSize(QSize(16777215, 20))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity_3.setPalette(palette19)
        self.textCity_3.setFont(font5)
        self.textCity_3.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city_3.addWidget(self.textCity_3)


        self.professionInfo_3.addLayout(self.city_3)

        self.money_3 = QHBoxLayout()
        self.money_3.setSpacing(10)
        self.money_3.setObjectName(u"money_3")
        self.iconMoney_3 = QPushButton(self.profession_4)
        self.iconMoney_3.setObjectName(u"iconMoney_3")
        self.iconMoney_3.setMinimumSize(QSize(20, 20))
        self.iconMoney_3.setMaximumSize(QSize(20, 20))
        self.iconMoney_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_3.setIconSize(QSize(24, 24))

        self.money_3.addWidget(self.iconMoney_3)

        self.textMoney_3 = QLabel(self.profession_4)
        self.textMoney_3.setObjectName(u"textMoney_3")
        self.textMoney_3.setMaximumSize(QSize(16777215, 20))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney_3.setPalette(palette20)
        self.textMoney_3.setFont(font5)
        self.textMoney_3.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_3.addWidget(self.textMoney_3)


        self.professionInfo_3.addLayout(self.money_3)

        self.description_3 = QVBoxLayout()
        self.description_3.setSpacing(5)
        self.description_3.setObjectName(u"description_3")
        self.titleDescription_3 = QLabel(self.profession_4)
        self.titleDescription_3.setObjectName(u"titleDescription_3")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription_3.setPalette(palette21)
        self.titleDescription_3.setFont(font6)
        self.titleDescription_3.setStyleSheet(u"border: none;")

        self.description_3.addWidget(self.titleDescription_3)

        self.textDescription_3 = QTextBrowser(self.profession_4)
        self.textDescription_3.setObjectName(u"textDescription_3")
        self.textDescription_3.setStyleSheet(u"border: none;")

        self.description_3.addWidget(self.textDescription_3)


        self.professionInfo_3.addLayout(self.description_3)


        self.verticalLayout_8.addLayout(self.professionInfo_3)

        self.pushButtonMore_4 = QPushButton(self.profession_4)
        self.pushButtonMore_4.setObjectName(u"pushButtonMore_4")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_4.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_4.setSizePolicy(sizePolicy1)
        self.pushButtonMore_4.setMinimumSize(QSize(0, 0))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore_4.setPalette(palette22)
        self.pushButtonMore_4.setFont(font7)
        self.pushButtonMore_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButtonMore_4, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession_4, 0, 2, 1, 1)

        self.profession_5 = QFrame(self.professionsFrame)
        self.profession_5.setObjectName(u"profession_5")
        self.profession_5.setMinimumSize(QSize(346, 407))
        self.profession_5.setMaximumSize(QSize(346, 407))
        self.profession_5.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.profession_5)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_9 = QHBoxLayout()
        self.professionButtons_9.setObjectName(u"professionButtons_9")
        self.professionName_9 = QLabel(self.profession_5)
        self.professionName_9.setObjectName(u"professionName_9")
        self.professionName_9.setMinimumSize(QSize(248, 0))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName_9.setPalette(palette23)
        self.professionName_9.setFont(font4)
        self.professionName_9.setStyleSheet(u"border: none;")

        self.professionButtons_9.addWidget(self.professionName_9)

        self.buttons_9 = QHBoxLayout()
        self.buttons_9.setSpacing(10)
        self.buttons_9.setObjectName(u"buttons_9")
        self.pushButtonRedact_9 = QPushButton(self.profession_5)
        self.pushButtonRedact_9.setObjectName(u"pushButtonRedact_9")
        self.pushButtonRedact_9.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_9.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_9.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_9.setIconSize(QSize(24, 24))

        self.buttons_9.addWidget(self.pushButtonRedact_9)

        self.pushButtonDelete_9 = QPushButton(self.profession_5)
        self.pushButtonDelete_9.setObjectName(u"pushButtonDelete_9")
        self.pushButtonDelete_9.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_9.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_9.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_9.setIconSize(QSize(24, 24))

        self.buttons_9.addWidget(self.pushButtonDelete_9)


        self.professionButtons_9.addLayout(self.buttons_9)


        self.verticalLayout_9.addLayout(self.professionButtons_9)

        self.professionInfo_4 = QVBoxLayout()
        self.professionInfo_4.setSpacing(10)
        self.professionInfo_4.setObjectName(u"professionInfo_4")
        self.city_4 = QHBoxLayout()
        self.city_4.setSpacing(10)
        self.city_4.setObjectName(u"city_4")
        self.iconCity_4 = QPushButton(self.profession_5)
        self.iconCity_4.setObjectName(u"iconCity_4")
        self.iconCity_4.setMinimumSize(QSize(20, 20))
        self.iconCity_4.setMaximumSize(QSize(20, 20))
        self.iconCity_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity_4.setIconSize(QSize(24, 24))

        self.city_4.addWidget(self.iconCity_4)

        self.textCity_4 = QLabel(self.profession_5)
        self.textCity_4.setObjectName(u"textCity_4")
        self.textCity_4.setMaximumSize(QSize(16777215, 20))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity_4.setPalette(palette24)
        self.textCity_4.setFont(font5)
        self.textCity_4.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city_4.addWidget(self.textCity_4)


        self.professionInfo_4.addLayout(self.city_4)

        self.money_4 = QHBoxLayout()
        self.money_4.setSpacing(10)
        self.money_4.setObjectName(u"money_4")
        self.iconMoney_4 = QPushButton(self.profession_5)
        self.iconMoney_4.setObjectName(u"iconMoney_4")
        self.iconMoney_4.setMinimumSize(QSize(20, 20))
        self.iconMoney_4.setMaximumSize(QSize(20, 20))
        self.iconMoney_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_4.setIconSize(QSize(24, 24))

        self.money_4.addWidget(self.iconMoney_4)

        self.textMoney_4 = QLabel(self.profession_5)
        self.textMoney_4.setObjectName(u"textMoney_4")
        self.textMoney_4.setMaximumSize(QSize(16777215, 20))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney_4.setPalette(palette25)
        self.textMoney_4.setFont(font5)
        self.textMoney_4.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_4.addWidget(self.textMoney_4)


        self.professionInfo_4.addLayout(self.money_4)

        self.description_4 = QVBoxLayout()
        self.description_4.setSpacing(5)
        self.description_4.setObjectName(u"description_4")
        self.titleDescription_4 = QLabel(self.profession_5)
        self.titleDescription_4.setObjectName(u"titleDescription_4")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription_4.setPalette(palette26)
        self.titleDescription_4.setFont(font6)
        self.titleDescription_4.setStyleSheet(u"border: none;")

        self.description_4.addWidget(self.titleDescription_4)

        self.textDescription_4 = QTextBrowser(self.profession_5)
        self.textDescription_4.setObjectName(u"textDescription_4")
        self.textDescription_4.setStyleSheet(u"border: none;")

        self.description_4.addWidget(self.textDescription_4)


        self.professionInfo_4.addLayout(self.description_4)


        self.verticalLayout_9.addLayout(self.professionInfo_4)

        self.pushButtonMore_5 = QPushButton(self.profession_5)
        self.pushButtonMore_5.setObjectName(u"pushButtonMore_5")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_5.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_5.setSizePolicy(sizePolicy1)
        self.pushButtonMore_5.setMinimumSize(QSize(0, 0))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore_5.setPalette(palette27)
        self.pushButtonMore_5.setFont(font7)
        self.pushButtonMore_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButtonMore_5, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession_5, 0, 3, 1, 1)

        self.profession_6 = QFrame(self.professionsFrame)
        self.profession_6.setObjectName(u"profession_6")
        self.profession_6.setMinimumSize(QSize(346, 407))
        self.profession_6.setMaximumSize(QSize(346, 407))
        self.profession_6.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.profession_6)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_10 = QHBoxLayout()
        self.professionButtons_10.setObjectName(u"professionButtons_10")
        self.professionName_10 = QLabel(self.profession_6)
        self.professionName_10.setObjectName(u"professionName_10")
        self.professionName_10.setMinimumSize(QSize(248, 0))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName_10.setPalette(palette28)
        self.professionName_10.setFont(font4)
        self.professionName_10.setStyleSheet(u"border: none;")

        self.professionButtons_10.addWidget(self.professionName_10)

        self.buttons_10 = QHBoxLayout()
        self.buttons_10.setSpacing(10)
        self.buttons_10.setObjectName(u"buttons_10")
        self.pushButtonRedact_10 = QPushButton(self.profession_6)
        self.pushButtonRedact_10.setObjectName(u"pushButtonRedact_10")
        self.pushButtonRedact_10.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_10.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_10.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_10.setIconSize(QSize(24, 24))

        self.buttons_10.addWidget(self.pushButtonRedact_10)

        self.pushButtonDelete_10 = QPushButton(self.profession_6)
        self.pushButtonDelete_10.setObjectName(u"pushButtonDelete_10")
        self.pushButtonDelete_10.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_10.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_10.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_10.setIconSize(QSize(24, 24))

        self.buttons_10.addWidget(self.pushButtonDelete_10)


        self.professionButtons_10.addLayout(self.buttons_10)


        self.verticalLayout_10.addLayout(self.professionButtons_10)

        self.professionInfo_5 = QVBoxLayout()
        self.professionInfo_5.setSpacing(10)
        self.professionInfo_5.setObjectName(u"professionInfo_5")
        self.city_5 = QHBoxLayout()
        self.city_5.setSpacing(10)
        self.city_5.setObjectName(u"city_5")
        self.iconCity_5 = QPushButton(self.profession_6)
        self.iconCity_5.setObjectName(u"iconCity_5")
        self.iconCity_5.setMinimumSize(QSize(20, 20))
        self.iconCity_5.setMaximumSize(QSize(20, 20))
        self.iconCity_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity_5.setIconSize(QSize(24, 24))

        self.city_5.addWidget(self.iconCity_5)

        self.textCity_5 = QLabel(self.profession_6)
        self.textCity_5.setObjectName(u"textCity_5")
        self.textCity_5.setMaximumSize(QSize(16777215, 20))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity_5.setPalette(palette29)
        self.textCity_5.setFont(font5)
        self.textCity_5.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city_5.addWidget(self.textCity_5)


        self.professionInfo_5.addLayout(self.city_5)

        self.money_5 = QHBoxLayout()
        self.money_5.setSpacing(10)
        self.money_5.setObjectName(u"money_5")
        self.iconMoney_5 = QPushButton(self.profession_6)
        self.iconMoney_5.setObjectName(u"iconMoney_5")
        self.iconMoney_5.setMinimumSize(QSize(20, 20))
        self.iconMoney_5.setMaximumSize(QSize(20, 20))
        self.iconMoney_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_5.setIconSize(QSize(24, 24))

        self.money_5.addWidget(self.iconMoney_5)

        self.textMoney_5 = QLabel(self.profession_6)
        self.textMoney_5.setObjectName(u"textMoney_5")
        self.textMoney_5.setMaximumSize(QSize(16777215, 20))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney_5.setPalette(palette30)
        self.textMoney_5.setFont(font5)
        self.textMoney_5.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_5.addWidget(self.textMoney_5)


        self.professionInfo_5.addLayout(self.money_5)

        self.description_5 = QVBoxLayout()
        self.description_5.setSpacing(5)
        self.description_5.setObjectName(u"description_5")
        self.titleDescription_5 = QLabel(self.profession_6)
        self.titleDescription_5.setObjectName(u"titleDescription_5")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription_5.setPalette(palette31)
        self.titleDescription_5.setFont(font6)
        self.titleDescription_5.setStyleSheet(u"border: none;")

        self.description_5.addWidget(self.titleDescription_5)

        self.textDescription_5 = QTextBrowser(self.profession_6)
        self.textDescription_5.setObjectName(u"textDescription_5")
        self.textDescription_5.setStyleSheet(u"border: none;")

        self.description_5.addWidget(self.textDescription_5)


        self.professionInfo_5.addLayout(self.description_5)


        self.verticalLayout_10.addLayout(self.professionInfo_5)

        self.pushButtonMore_6 = QPushButton(self.profession_6)
        self.pushButtonMore_6.setObjectName(u"pushButtonMore_6")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_6.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_6.setSizePolicy(sizePolicy1)
        self.pushButtonMore_6.setMinimumSize(QSize(0, 0))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore_6.setPalette(palette32)
        self.pushButtonMore_6.setFont(font7)
        self.pushButtonMore_6.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButtonMore_6, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession_6, 0, 4, 1, 1)

        self.profession_7 = QFrame(self.professionsFrame)
        self.profession_7.setObjectName(u"profession_7")
        self.profession_7.setMinimumSize(QSize(346, 407))
        self.profession_7.setMaximumSize(QSize(346, 407))
        self.profession_7.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.profession_7)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.professionButtons_12 = QHBoxLayout()
        self.professionButtons_12.setObjectName(u"professionButtons_12")
        self.professionName_12 = QLabel(self.profession_7)
        self.professionName_12.setObjectName(u"professionName_12")
        self.professionName_12.setMinimumSize(QSize(248, 0))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.professionName_12.setPalette(palette33)
        self.professionName_12.setFont(font4)
        self.professionName_12.setStyleSheet(u"border: none;")

        self.professionButtons_12.addWidget(self.professionName_12)

        self.buttons_12 = QHBoxLayout()
        self.buttons_12.setSpacing(10)
        self.buttons_12.setObjectName(u"buttons_12")
        self.pushButtonRedact_12 = QPushButton(self.profession_7)
        self.pushButtonRedact_12.setObjectName(u"pushButtonRedact_12")
        self.pushButtonRedact_12.setMinimumSize(QSize(24, 24))
        self.pushButtonRedact_12.setMaximumSize(QSize(24, 24))
        self.pushButtonRedact_12.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Edit_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Edit_purple.png);\n"
"}")
        self.pushButtonRedact_12.setIconSize(QSize(24, 24))

        self.buttons_12.addWidget(self.pushButtonRedact_12)

        self.pushButtonDelete_12 = QPushButton(self.profession_7)
        self.pushButtonDelete_12.setObjectName(u"pushButtonDelete_12")
        self.pushButtonDelete_12.setMinimumSize(QSize(24, 24))
        self.pushButtonDelete_12.setMaximumSize(QSize(24, 24))
        self.pushButtonDelete_12.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Trash_grey.png);\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	image: url(:/Icons/Icons And Logo/Trash_purple.png);\n"
"}")
        self.pushButtonDelete_12.setIconSize(QSize(24, 24))

        self.buttons_12.addWidget(self.pushButtonDelete_12)


        self.professionButtons_12.addLayout(self.buttons_12)


        self.verticalLayout_12.addLayout(self.professionButtons_12)

        self.professionInfo_7 = QVBoxLayout()
        self.professionInfo_7.setSpacing(10)
        self.professionInfo_7.setObjectName(u"professionInfo_7")
        self.city_7 = QHBoxLayout()
        self.city_7.setSpacing(10)
        self.city_7.setObjectName(u"city_7")
        self.iconCity_7 = QPushButton(self.profession_7)
        self.iconCity_7.setObjectName(u"iconCity_7")
        self.iconCity_7.setMinimumSize(QSize(20, 20))
        self.iconCity_7.setMaximumSize(QSize(20, 20))
        self.iconCity_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity_7.setIconSize(QSize(24, 24))

        self.city_7.addWidget(self.iconCity_7)

        self.textCity_7 = QLabel(self.profession_7)
        self.textCity_7.setObjectName(u"textCity_7")
        self.textCity_7.setMaximumSize(QSize(16777215, 20))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textCity_7.setPalette(palette34)
        self.textCity_7.setFont(font5)
        self.textCity_7.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city_7.addWidget(self.textCity_7)


        self.professionInfo_7.addLayout(self.city_7)

        self.money_7 = QHBoxLayout()
        self.money_7.setSpacing(10)
        self.money_7.setObjectName(u"money_7")
        self.iconMoney_7 = QPushButton(self.profession_7)
        self.iconMoney_7.setObjectName(u"iconMoney_7")
        self.iconMoney_7.setMinimumSize(QSize(20, 20))
        self.iconMoney_7.setMaximumSize(QSize(20, 20))
        self.iconMoney_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_7.setIconSize(QSize(24, 24))

        self.money_7.addWidget(self.iconMoney_7)

        self.textMoney_7 = QLabel(self.profession_7)
        self.textMoney_7.setObjectName(u"textMoney_7")
        self.textMoney_7.setMaximumSize(QSize(16777215, 20))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.textMoney_7.setPalette(palette35)
        self.textMoney_7.setFont(font5)
        self.textMoney_7.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_7.addWidget(self.textMoney_7)


        self.professionInfo_7.addLayout(self.money_7)

        self.description_7 = QVBoxLayout()
        self.description_7.setSpacing(5)
        self.description_7.setObjectName(u"description_7")
        self.titleDescription_7 = QLabel(self.profession_7)
        self.titleDescription_7.setObjectName(u"titleDescription_7")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.titleDescription_7.setPalette(palette36)
        self.titleDescription_7.setFont(font6)
        self.titleDescription_7.setStyleSheet(u"border: none;")

        self.description_7.addWidget(self.titleDescription_7)

        self.textDescription_7 = QTextBrowser(self.profession_7)
        self.textDescription_7.setObjectName(u"textDescription_7")
        self.textDescription_7.setStyleSheet(u"border: none;")

        self.description_7.addWidget(self.textDescription_7)


        self.professionInfo_7.addLayout(self.description_7)


        self.verticalLayout_12.addLayout(self.professionInfo_7)

        self.pushButtonMore_8 = QPushButton(self.profession_7)
        self.pushButtonMore_8.setObjectName(u"pushButtonMore_8")
        sizePolicy1.setHeightForWidth(self.pushButtonMore_8.sizePolicy().hasHeightForWidth())
        self.pushButtonMore_8.setSizePolicy(sizePolicy1)
        self.pushButtonMore_8.setMinimumSize(QSize(0, 0))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonMore_8.setPalette(palette37)
        self.pushButtonMore_8.setFont(font7)
        self.pushButtonMore_8.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	color: #010101;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"	color: #501EBC;\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButtonMore_8, 0, Qt.AlignHCenter)


        self.gridProfessions.addWidget(self.profession_7, 1, 0, 1, 1)


        self.professions.addLayout(self.gridProfessions)

        self.verticalScrollBar = QScrollBar(self.professionsFrame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette38 = QPalette()
        brush5 = QBrush(QColor(231, 231, 231, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.verticalScrollBar.setPalette(palette38)
        self.verticalScrollBar.setStyleSheet(u"QScrollBar:vertical {\n"
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
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7p"
                        "x;\n"
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
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.professions.addWidget(self.verticalScrollBar)


        self.verticalLayout.addWidget(self.professionsFrame, 0, Qt.AlignTop)

        ProfessionPage.setCentralWidget(self.professionPage)

        self.retranslateUi(ProfessionPage)

        QMetaObject.connectSlotsByName(ProfessionPage)
    # setupUi

    def retranslateUi(self, ProfessionPage):
        ProfessionPage.setWindowTitle(QCoreApplication.translate("ProfessionPage", u"Your Vacancy", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("ProfessionPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.title_2.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.pushButtonAddTags.setText(QCoreApplication.translate("ProfessionPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u0433\u0438", None))
        self.findInput.setText("")
        self.findInput.setPlaceholderText(QCoreApplication.translate("ProfessionPage", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.pushButtonFind.setText("")
        self.professionName.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.pushButtonAdd.setText("")
        self.textAdd.setText(QCoreApplication.translate("ProfessionPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e", None))
        self.textAdd_2.setText(QCoreApplication.translate("ProfessionPage", u"\u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.professionName_7.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact_7.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_7.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity_2.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity_2.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney_2.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_2.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription_2.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription_2.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore_3.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.professionName_8.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact_8.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_8.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_8.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_8.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity_3.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity_3.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney_3.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_3.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription_3.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription_3.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore_4.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.professionName_9.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact_9.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_9.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_9.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_9.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity_4.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity_4.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney_4.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_4.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription_4.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription_4.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore_5.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.professionName_10.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact_10.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_10.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_10.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_10.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity_5.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity_5.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney_5.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_5.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription_5.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription_5.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore_6.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
        self.professionName_12.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.pushButtonRedact_12.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonRedact_12.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButtonDelete_12.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete_12.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.iconCity_7.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity_7.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney_7.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_7.setText(QCoreApplication.translate("ProfessionPage", u"21 000 - 25 000", None))
        self.titleDescription_7.setText(QCoreApplication.translate("ProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription_7.setHtml(QCoreApplication.translate("ProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10.5pt; font-weight:600; color:#101010;\">\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c\u0438, \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u044b, \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u043d\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043f\u0440\u0435\u0434\u043e"
                        "\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u0445<br />\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u2014 \u0443\u0431\u0435\u0434\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u0441\u043e\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u043e\u043a\u0443\u043f\u043a\u0443. \u042d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c \u0432 \u0441\u0435\u0431\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044e \u0442\u043e\u0432\u0430\u0440\u0430, \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u0435 \u0435\u0433\u043e \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432 \u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438</span></"
                        "p></body></html>", None))
        self.pushButtonMore_8.setText(QCoreApplication.translate("ProfessionPage", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0449\u0451", None))
    # retranslateUi

