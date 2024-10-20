# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TakeProfessionPage.ui'
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
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollBar, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)
import Logo
import Icons

class Ui_TakeProfessionPage(object):
    def setupUi(self, TakeProfessionPage):
        if not TakeProfessionPage.objectName():
            TakeProfessionPage.setObjectName(u"TakeProfessionPage")
        TakeProfessionPage.resize(1920, 1110)
        TakeProfessionPage.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-family: Roboto;")
        self.takeProfessionPage = QWidget(TakeProfessionPage)
        self.takeProfessionPage.setObjectName(u"takeProfessionPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeProfessionPage.sizePolicy().hasHeightForWidth())
        self.takeProfessionPage.setSizePolicy(sizePolicy)
        self.takeProfessionPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.takeProfessionPage)
        self.verticalLayout_15.setSpacing(30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 30)
        self.headerFrame = QFrame(self.takeProfessionPage)
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
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(24)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
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
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.pushButton_2.setPalette(palette1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
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
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_15.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.title = QFrame(self.takeProfessionPage)
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
        palette2 = QPalette()
        brush1 = QBrush(QColor(80, 30, 188, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_2.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.title_2.setFont(font1)
        self.title_2.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleButton.addWidget(self.title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleButton.addItem(self.horizontalSpacer)

        self.pushButtonAddTags = QPushButton(self.title)
        self.pushButtonAddTags.setObjectName(u"pushButtonAddTags")
        self.pushButtonAddTags.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButtonAddTags.sizePolicy().hasHeightForWidth())
        self.pushButtonAddTags.setSizePolicy(sizePolicy1)
        self.pushButtonAddTags.setMinimumSize(QSize(324, 48))
        self.pushButtonAddTags.setMaximumSize(QSize(324, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButtonAddTags.setPalette(palette3)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(18)
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


        self.verticalLayout_15.addWidget(self.title, 0, Qt.AlignTop)

        self.vacancyFrame = QFrame(self.takeProfessionPage)
        self.vacancyFrame.setObjectName(u"vacancyFrame")
        self.vacancy = QVBoxLayout(self.vacancyFrame)
        self.vacancy.setSpacing(20)
        self.vacancy.setObjectName(u"vacancy")
        self.titleVacancy = QHBoxLayout()
        self.titleVacancy.setSpacing(20)
        self.titleVacancy.setObjectName(u"titleVacancy")
        self.titleVacancy.setContentsMargins(30, -1, 30, -1)
        self.title_3 = QLabel(self.vacancyFrame)
        self.title_3.setObjectName(u"title_3")
        sizePolicy1.setHeightForWidth(self.title_3.sizePolicy().hasHeightForWidth())
        self.title_3.setSizePolicy(sizePolicy1)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_3.setPalette(palette4)
        self.title_3.setFont(font1)
        self.title_3.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleVacancy.addWidget(self.title_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleVacancy.addItem(self.horizontalSpacer_3)


        self.vacancy.addLayout(self.titleVacancy)

        self.professionFrame = QHBoxLayout()
        self.professionFrame.setSpacing(0)
        self.professionFrame.setObjectName(u"professionFrame")
        self.label_2 = QLabel(self.vacancyFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 0))
        self.label_2.setBaseSize(QSize(30, 0))

        self.professionFrame.addWidget(self.label_2)

        self.profession = QFrame(self.vacancyFrame)
        self.profession.setObjectName(u"profession")
        self.profession.setMinimumSize(QSize(1860, 306))
        self.profession.setMaximumSize(QSize(16667, 407))
        self.profession.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.profession)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.nameProfession = QHBoxLayout()
        self.nameProfession.setSpacing(20)
        self.nameProfession.setObjectName(u"nameProfession")
        self.nameButton = QPushButton(self.profession)
        self.nameButton.setObjectName(u"nameButton")
        self.nameButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.nameButton.sizePolicy().hasHeightForWidth())
        self.nameButton.setSizePolicy(sizePolicy1)
        self.nameButton.setMinimumSize(QSize(0, 40))
        self.nameButton.setMaximumSize(QSize(1000, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton.setPalette(palette5)
        self.nameButton.setFont(font)
        self.nameButton.setLayoutDirection(Qt.RightToLeft)
        self.nameButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")
        self.nameButton.setAutoDefault(False)

        self.nameProfession.addWidget(self.nameButton)

        self.city = QHBoxLayout()
        self.city.setSpacing(10)
        self.city.setObjectName(u"city")
        self.iconCity = QPushButton(self.profession)
        self.iconCity.setObjectName(u"iconCity")
        self.iconCity.setMinimumSize(QSize(28, 28))
        self.iconCity.setMaximumSize(QSize(28, 28))
        self.iconCity.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Map_grey.png);\n"
"}")
        self.iconCity.setIconSize(QSize(24, 24))

        self.city.addWidget(self.iconCity)

        self.textCity = QLabel(self.profession)
        self.textCity.setObjectName(u"textCity")
        self.textCity.setMaximumSize(QSize(16777215, 20))
        palette6 = QPalette()
        brush3 = QBrush(QColor(91, 91, 91, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textCity.setPalette(palette6)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.textCity.setFont(font3)
        self.textCity.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.city.addWidget(self.textCity)


        self.nameProfession.addLayout(self.city)

        self.money = QHBoxLayout()
        self.money.setSpacing(10)
        self.money.setObjectName(u"money")
        self.iconMoney = QPushButton(self.profession)
        self.iconMoney.setObjectName(u"iconMoney")
        self.iconMoney.setMinimumSize(QSize(28, 28))
        self.iconMoney.setMaximumSize(QSize(28, 30))
        self.iconMoney.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney.setIconSize(QSize(24, 24))

        self.money.addWidget(self.iconMoney)

        self.textMoney = QLabel(self.profession)
        self.textMoney.setObjectName(u"textMoney")
        self.textMoney.setMaximumSize(QSize(16777215, 20))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney.setPalette(palette7)
        self.textMoney.setFont(font3)
        self.textMoney.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money.addWidget(self.textMoney)


        self.nameProfession.addLayout(self.money)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.nameProfession.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.nameProfession)

        self.description = QVBoxLayout()
        self.description.setSpacing(5)
        self.description.setObjectName(u"description")
        self.titleDescription = QLabel(self.profession)
        self.titleDescription.setObjectName(u"titleDescription")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.titleDescription.setPalette(palette8)
        self.titleDescription.setFont(font2)
        self.titleDescription.setStyleSheet(u"border: none;")

        self.description.addWidget(self.titleDescription)

        self.textDescription = QTextBrowser(self.profession)
        self.textDescription.setObjectName(u"textDescription")
        self.textDescription.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"   color: #101010;\n"
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
"	border-bottom-left-radiu"
                        "s: 7px;\n"
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
        self.textDescription.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.description.addWidget(self.textDescription)


        self.verticalLayout.addLayout(self.description)


        self.professionFrame.addWidget(self.profession)

        self.label_3 = QLabel(self.vacancyFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setBaseSize(QSize(30, 0))

        self.professionFrame.addWidget(self.label_3)


        self.vacancy.addLayout(self.professionFrame)


        self.verticalLayout_15.addWidget(self.vacancyFrame, 0, Qt.AlignTop)

        self.otherVacancyFrame = QFrame(self.takeProfessionPage)
        self.otherVacancyFrame.setObjectName(u"otherVacancyFrame")
        self.otherVacancy = QVBoxLayout(self.otherVacancyFrame)
        self.otherVacancy.setSpacing(20)
        self.otherVacancy.setObjectName(u"otherVacancy")
        self.titleMoreVacancy = QHBoxLayout()
        self.titleMoreVacancy.setSpacing(20)
        self.titleMoreVacancy.setObjectName(u"titleMoreVacancy")
        self.titleMoreVacancy.setContentsMargins(30, -1, 30, -1)
        self.title_4 = QLabel(self.otherVacancyFrame)
        self.title_4.setObjectName(u"title_4")
        sizePolicy1.setHeightForWidth(self.title_4.sizePolicy().hasHeightForWidth())
        self.title_4.setSizePolicy(sizePolicy1)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.title_4.setPalette(palette9)
        self.title_4.setFont(font1)
        self.title_4.setStyleSheet(u"color: rgb(80, 30, 188);")

        self.titleMoreVacancy.addWidget(self.title_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleMoreVacancy.addItem(self.horizontalSpacer_4)


        self.otherVacancy.addLayout(self.titleMoreVacancy)

        self.miniClustersFrame = QHBoxLayout()
        self.miniClustersFrame.setSpacing(20)
        self.miniClustersFrame.setObjectName(u"miniClustersFrame")
        self.miniClustersFrame.setContentsMargins(30, -1, 30, -1)
        self.miniClusters = QGridLayout()
        self.miniClusters.setSpacing(20)
        self.miniClusters.setObjectName(u"miniClusters")
        self.miniCluster_6 = QFrame(self.otherVacancyFrame)
        self.miniCluster_6.setObjectName(u"miniCluster_6")
        self.miniCluster_6.setMinimumSize(QSize(347, 104))
        self.miniCluster_6.setMaximumSize(QSize(347, 104))
        self.miniCluster_6.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.miniCluster_6)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.nameButton_7 = QPushButton(self.miniCluster_6)
        self.nameButton_7.setObjectName(u"nameButton_7")
        sizePolicy1.setHeightForWidth(self.nameButton_7.sizePolicy().hasHeightForWidth())
        self.nameButton_7.setSizePolicy(sizePolicy1)
        self.nameButton_7.setMinimumSize(QSize(0, 30))
        self.nameButton_7.setMaximumSize(QSize(320, 30))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_7.setPalette(palette10)
        self.nameButton_7.setFont(font2)
        self.nameButton_7.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_7.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_6.addWidget(self.nameButton_7, 0, Qt.AlignLeft)

        self.money_6 = QHBoxLayout()
        self.money_6.setSpacing(10)
        self.money_6.setObjectName(u"money_6")
        self.iconMoney_6 = QPushButton(self.miniCluster_6)
        self.iconMoney_6.setObjectName(u"iconMoney_6")
        self.iconMoney_6.setMinimumSize(QSize(20, 20))
        self.iconMoney_6.setMaximumSize(QSize(20, 20))
        self.iconMoney_6.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_6.setIconSize(QSize(24, 24))

        self.money_6.addWidget(self.iconMoney_6)

        self.textMoney_6 = QLabel(self.miniCluster_6)
        self.textMoney_6.setObjectName(u"textMoney_6")
        self.textMoney_6.setMaximumSize(QSize(16777215, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_6.setPalette(palette11)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.textMoney_6.setFont(font4)
        self.textMoney_6.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_6.addWidget(self.textMoney_6)


        self.verticalLayout_6.addLayout(self.money_6)


        self.miniClusters.addWidget(self.miniCluster_6, 0, 4, 1, 1)

        self.miniCluster_7 = QFrame(self.otherVacancyFrame)
        self.miniCluster_7.setObjectName(u"miniCluster_7")
        self.miniCluster_7.setMinimumSize(QSize(347, 104))
        self.miniCluster_7.setMaximumSize(QSize(347, 104))
        self.miniCluster_7.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.miniCluster_7)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.nameButton_8 = QPushButton(self.miniCluster_7)
        self.nameButton_8.setObjectName(u"nameButton_8")
        sizePolicy1.setHeightForWidth(self.nameButton_8.sizePolicy().hasHeightForWidth())
        self.nameButton_8.setSizePolicy(sizePolicy1)
        self.nameButton_8.setMinimumSize(QSize(0, 30))
        self.nameButton_8.setMaximumSize(QSize(320, 30))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_8.setPalette(palette12)
        self.nameButton_8.setFont(font2)
        self.nameButton_8.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_8.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_7.addWidget(self.nameButton_8, 0, Qt.AlignLeft)

        self.money_7 = QHBoxLayout()
        self.money_7.setSpacing(10)
        self.money_7.setObjectName(u"money_7")
        self.iconMoney_7 = QPushButton(self.miniCluster_7)
        self.iconMoney_7.setObjectName(u"iconMoney_7")
        self.iconMoney_7.setMinimumSize(QSize(20, 20))
        self.iconMoney_7.setMaximumSize(QSize(20, 20))
        self.iconMoney_7.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_7.setIconSize(QSize(24, 24))

        self.money_7.addWidget(self.iconMoney_7)

        self.textMoney_7 = QLabel(self.miniCluster_7)
        self.textMoney_7.setObjectName(u"textMoney_7")
        self.textMoney_7.setMaximumSize(QSize(16777215, 20))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_7.setPalette(palette13)
        self.textMoney_7.setFont(font4)
        self.textMoney_7.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_7.addWidget(self.textMoney_7)


        self.verticalLayout_7.addLayout(self.money_7)


        self.miniClusters.addWidget(self.miniCluster_7, 1, 0, 1, 1)

        self.miniCluster_8 = QFrame(self.otherVacancyFrame)
        self.miniCluster_8.setObjectName(u"miniCluster_8")
        self.miniCluster_8.setMinimumSize(QSize(347, 104))
        self.miniCluster_8.setMaximumSize(QSize(347, 104))
        self.miniCluster_8.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.miniCluster_8)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.nameButton_10 = QPushButton(self.miniCluster_8)
        self.nameButton_10.setObjectName(u"nameButton_10")
        sizePolicy1.setHeightForWidth(self.nameButton_10.sizePolicy().hasHeightForWidth())
        self.nameButton_10.setSizePolicy(sizePolicy1)
        self.nameButton_10.setMinimumSize(QSize(0, 30))
        self.nameButton_10.setMaximumSize(QSize(320, 30))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_10.setPalette(palette14)
        self.nameButton_10.setFont(font2)
        self.nameButton_10.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_10.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_9.addWidget(self.nameButton_10, 0, Qt.AlignLeft)

        self.money_9 = QHBoxLayout()
        self.money_9.setSpacing(10)
        self.money_9.setObjectName(u"money_9")
        self.iconMoney_9 = QPushButton(self.miniCluster_8)
        self.iconMoney_9.setObjectName(u"iconMoney_9")
        self.iconMoney_9.setMinimumSize(QSize(20, 20))
        self.iconMoney_9.setMaximumSize(QSize(20, 20))
        self.iconMoney_9.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_9.setIconSize(QSize(24, 24))

        self.money_9.addWidget(self.iconMoney_9)

        self.textMoney_9 = QLabel(self.miniCluster_8)
        self.textMoney_9.setObjectName(u"textMoney_9")
        self.textMoney_9.setMaximumSize(QSize(16777215, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_9.setPalette(palette15)
        self.textMoney_9.setFont(font4)
        self.textMoney_9.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_9.addWidget(self.textMoney_9)


        self.verticalLayout_9.addLayout(self.money_9)


        self.miniClusters.addWidget(self.miniCluster_8, 1, 1, 1, 1)

        self.miniCluster_3 = QFrame(self.otherVacancyFrame)
        self.miniCluster_3.setObjectName(u"miniCluster_3")
        self.miniCluster_3.setMinimumSize(QSize(347, 104))
        self.miniCluster_3.setMaximumSize(QSize(347, 104))
        self.miniCluster_3.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.miniCluster_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.nameButton_4 = QPushButton(self.miniCluster_3)
        self.nameButton_4.setObjectName(u"nameButton_4")
        sizePolicy1.setHeightForWidth(self.nameButton_4.sizePolicy().hasHeightForWidth())
        self.nameButton_4.setSizePolicy(sizePolicy1)
        self.nameButton_4.setMinimumSize(QSize(0, 30))
        self.nameButton_4.setMaximumSize(QSize(320, 30))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_4.setPalette(palette16)
        self.nameButton_4.setFont(font2)
        self.nameButton_4.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_4.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_3.addWidget(self.nameButton_4, 0, Qt.AlignLeft)

        self.money_3 = QHBoxLayout()
        self.money_3.setSpacing(10)
        self.money_3.setObjectName(u"money_3")
        self.iconMoney_3 = QPushButton(self.miniCluster_3)
        self.iconMoney_3.setObjectName(u"iconMoney_3")
        self.iconMoney_3.setMinimumSize(QSize(20, 20))
        self.iconMoney_3.setMaximumSize(QSize(20, 20))
        self.iconMoney_3.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_3.setIconSize(QSize(24, 24))

        self.money_3.addWidget(self.iconMoney_3)

        self.textMoney_3 = QLabel(self.miniCluster_3)
        self.textMoney_3.setObjectName(u"textMoney_3")
        self.textMoney_3.setMaximumSize(QSize(16777215, 20))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_3.setPalette(palette17)
        self.textMoney_3.setFont(font4)
        self.textMoney_3.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_3.addWidget(self.textMoney_3)


        self.verticalLayout_3.addLayout(self.money_3)


        self.miniClusters.addWidget(self.miniCluster_3, 0, 1, 1, 1)

        self.miniCluster_2 = QFrame(self.otherVacancyFrame)
        self.miniCluster_2.setObjectName(u"miniCluster_2")
        self.miniCluster_2.setMinimumSize(QSize(347, 104))
        self.miniCluster_2.setMaximumSize(QSize(347, 104))
        self.miniCluster_2.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.miniCluster_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.nameButton_2 = QPushButton(self.miniCluster_2)
        self.nameButton_2.setObjectName(u"nameButton_2")
        sizePolicy1.setHeightForWidth(self.nameButton_2.sizePolicy().hasHeightForWidth())
        self.nameButton_2.setSizePolicy(sizePolicy1)
        self.nameButton_2.setMinimumSize(QSize(0, 30))
        self.nameButton_2.setMaximumSize(QSize(320, 30))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_2.setPalette(palette18)
        self.nameButton_2.setFont(font2)
        self.nameButton_2.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_2.addWidget(self.nameButton_2, 0, Qt.AlignLeft)

        self.money_2 = QHBoxLayout()
        self.money_2.setSpacing(10)
        self.money_2.setObjectName(u"money_2")
        self.iconMoney_2 = QPushButton(self.miniCluster_2)
        self.iconMoney_2.setObjectName(u"iconMoney_2")
        self.iconMoney_2.setMinimumSize(QSize(20, 20))
        self.iconMoney_2.setMaximumSize(QSize(20, 20))
        self.iconMoney_2.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_2.setIconSize(QSize(24, 24))

        self.money_2.addWidget(self.iconMoney_2)

        self.textMoney_2 = QLabel(self.miniCluster_2)
        self.textMoney_2.setObjectName(u"textMoney_2")
        self.textMoney_2.setMaximumSize(QSize(16777215, 20))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_2.setPalette(palette19)
        self.textMoney_2.setFont(font4)
        self.textMoney_2.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_2.addWidget(self.textMoney_2)


        self.verticalLayout_2.addLayout(self.money_2)


        self.miniClusters.addWidget(self.miniCluster_2, 0, 0, 1, 1)

        self.miniCluster_9 = QFrame(self.otherVacancyFrame)
        self.miniCluster_9.setObjectName(u"miniCluster_9")
        self.miniCluster_9.setMinimumSize(QSize(347, 104))
        self.miniCluster_9.setMaximumSize(QSize(347, 104))
        self.miniCluster_9.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.miniCluster_9)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.nameButton_11 = QPushButton(self.miniCluster_9)
        self.nameButton_11.setObjectName(u"nameButton_11")
        sizePolicy1.setHeightForWidth(self.nameButton_11.sizePolicy().hasHeightForWidth())
        self.nameButton_11.setSizePolicy(sizePolicy1)
        self.nameButton_11.setMinimumSize(QSize(0, 30))
        self.nameButton_11.setMaximumSize(QSize(320, 30))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_11.setPalette(palette20)
        self.nameButton_11.setFont(font2)
        self.nameButton_11.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_11.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_10.addWidget(self.nameButton_11, 0, Qt.AlignLeft)

        self.money_10 = QHBoxLayout()
        self.money_10.setSpacing(10)
        self.money_10.setObjectName(u"money_10")
        self.iconMoney_10 = QPushButton(self.miniCluster_9)
        self.iconMoney_10.setObjectName(u"iconMoney_10")
        self.iconMoney_10.setMinimumSize(QSize(20, 20))
        self.iconMoney_10.setMaximumSize(QSize(20, 20))
        self.iconMoney_10.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_10.setIconSize(QSize(24, 24))

        self.money_10.addWidget(self.iconMoney_10)

        self.textMoney_10 = QLabel(self.miniCluster_9)
        self.textMoney_10.setObjectName(u"textMoney_10")
        self.textMoney_10.setMaximumSize(QSize(16777215, 20))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_10.setPalette(palette21)
        self.textMoney_10.setFont(font4)
        self.textMoney_10.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_10.addWidget(self.textMoney_10)


        self.verticalLayout_10.addLayout(self.money_10)


        self.miniClusters.addWidget(self.miniCluster_9, 1, 2, 1, 1)

        self.miniCluster_10 = QFrame(self.otherVacancyFrame)
        self.miniCluster_10.setObjectName(u"miniCluster_10")
        self.miniCluster_10.setMinimumSize(QSize(347, 104))
        self.miniCluster_10.setMaximumSize(QSize(347, 104))
        self.miniCluster_10.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.miniCluster_10)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.nameButton_12 = QPushButton(self.miniCluster_10)
        self.nameButton_12.setObjectName(u"nameButton_12")
        sizePolicy1.setHeightForWidth(self.nameButton_12.sizePolicy().hasHeightForWidth())
        self.nameButton_12.setSizePolicy(sizePolicy1)
        self.nameButton_12.setMinimumSize(QSize(0, 30))
        self.nameButton_12.setMaximumSize(QSize(320, 30))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.Button, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_12.setPalette(palette22)
        self.nameButton_12.setFont(font2)
        self.nameButton_12.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_12.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_11.addWidget(self.nameButton_12, 0, Qt.AlignLeft)

        self.money_11 = QHBoxLayout()
        self.money_11.setSpacing(10)
        self.money_11.setObjectName(u"money_11")
        self.iconMoney_11 = QPushButton(self.miniCluster_10)
        self.iconMoney_11.setObjectName(u"iconMoney_11")
        self.iconMoney_11.setMinimumSize(QSize(20, 20))
        self.iconMoney_11.setMaximumSize(QSize(20, 20))
        self.iconMoney_11.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_11.setIconSize(QSize(24, 24))

        self.money_11.addWidget(self.iconMoney_11)

        self.textMoney_11 = QLabel(self.miniCluster_10)
        self.textMoney_11.setObjectName(u"textMoney_11")
        self.textMoney_11.setMaximumSize(QSize(16777215, 20))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_11.setPalette(palette23)
        self.textMoney_11.setFont(font4)
        self.textMoney_11.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_11.addWidget(self.textMoney_11)


        self.verticalLayout_11.addLayout(self.money_11)


        self.miniClusters.addWidget(self.miniCluster_10, 1, 3, 1, 1)

        self.miniCluster_11 = QFrame(self.otherVacancyFrame)
        self.miniCluster_11.setObjectName(u"miniCluster_11")
        self.miniCluster_11.setMinimumSize(QSize(347, 104))
        self.miniCluster_11.setMaximumSize(QSize(347, 104))
        self.miniCluster_11.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.miniCluster_11)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.nameButton_13 = QPushButton(self.miniCluster_11)
        self.nameButton_13.setObjectName(u"nameButton_13")
        sizePolicy1.setHeightForWidth(self.nameButton_13.sizePolicy().hasHeightForWidth())
        self.nameButton_13.setSizePolicy(sizePolicy1)
        self.nameButton_13.setMinimumSize(QSize(0, 30))
        self.nameButton_13.setMaximumSize(QSize(320, 30))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.Button, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_13.setPalette(palette24)
        self.nameButton_13.setFont(font2)
        self.nameButton_13.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_13.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_12.addWidget(self.nameButton_13, 0, Qt.AlignLeft)

        self.money_12 = QHBoxLayout()
        self.money_12.setSpacing(10)
        self.money_12.setObjectName(u"money_12")
        self.iconMoney_12 = QPushButton(self.miniCluster_11)
        self.iconMoney_12.setObjectName(u"iconMoney_12")
        self.iconMoney_12.setMinimumSize(QSize(20, 20))
        self.iconMoney_12.setMaximumSize(QSize(20, 20))
        self.iconMoney_12.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_12.setIconSize(QSize(24, 24))

        self.money_12.addWidget(self.iconMoney_12)

        self.textMoney_12 = QLabel(self.miniCluster_11)
        self.textMoney_12.setObjectName(u"textMoney_12")
        self.textMoney_12.setMaximumSize(QSize(16777215, 20))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_12.setPalette(palette25)
        self.textMoney_12.setFont(font4)
        self.textMoney_12.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_12.addWidget(self.textMoney_12)


        self.verticalLayout_12.addLayout(self.money_12)


        self.miniClusters.addWidget(self.miniCluster_11, 1, 4, 1, 1)

        self.miniCluster_5 = QFrame(self.otherVacancyFrame)
        self.miniCluster_5.setObjectName(u"miniCluster_5")
        self.miniCluster_5.setMinimumSize(QSize(347, 104))
        self.miniCluster_5.setMaximumSize(QSize(347, 104))
        self.miniCluster_5.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.miniCluster_5)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.nameButton_6 = QPushButton(self.miniCluster_5)
        self.nameButton_6.setObjectName(u"nameButton_6")
        sizePolicy1.setHeightForWidth(self.nameButton_6.sizePolicy().hasHeightForWidth())
        self.nameButton_6.setSizePolicy(sizePolicy1)
        self.nameButton_6.setMinimumSize(QSize(0, 30))
        self.nameButton_6.setMaximumSize(QSize(320, 30))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_6.setPalette(palette26)
        self.nameButton_6.setFont(font2)
        self.nameButton_6.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_5.addWidget(self.nameButton_6, 0, Qt.AlignLeft)

        self.money_5 = QHBoxLayout()
        self.money_5.setSpacing(10)
        self.money_5.setObjectName(u"money_5")
        self.iconMoney_5 = QPushButton(self.miniCluster_5)
        self.iconMoney_5.setObjectName(u"iconMoney_5")
        self.iconMoney_5.setMinimumSize(QSize(20, 20))
        self.iconMoney_5.setMaximumSize(QSize(20, 20))
        self.iconMoney_5.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_5.setIconSize(QSize(24, 24))

        self.money_5.addWidget(self.iconMoney_5)

        self.textMoney_5 = QLabel(self.miniCluster_5)
        self.textMoney_5.setObjectName(u"textMoney_5")
        self.textMoney_5.setMaximumSize(QSize(16777215, 20))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_5.setPalette(palette27)
        self.textMoney_5.setFont(font4)
        self.textMoney_5.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_5.addWidget(self.textMoney_5)


        self.verticalLayout_5.addLayout(self.money_5)


        self.miniClusters.addWidget(self.miniCluster_5, 0, 3, 1, 1)

        self.miniCluster_4 = QFrame(self.otherVacancyFrame)
        self.miniCluster_4.setObjectName(u"miniCluster_4")
        self.miniCluster_4.setMinimumSize(QSize(347, 104))
        self.miniCluster_4.setMaximumSize(QSize(347, 104))
        self.miniCluster_4.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.miniCluster_4)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.nameButton_5 = QPushButton(self.miniCluster_4)
        self.nameButton_5.setObjectName(u"nameButton_5")
        sizePolicy1.setHeightForWidth(self.nameButton_5.sizePolicy().hasHeightForWidth())
        self.nameButton_5.setSizePolicy(sizePolicy1)
        self.nameButton_5.setMinimumSize(QSize(0, 30))
        self.nameButton_5.setMaximumSize(QSize(320, 30))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.Button, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_5.setPalette(palette28)
        self.nameButton_5.setFont(font2)
        self.nameButton_5.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_5.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_4.addWidget(self.nameButton_5, 0, Qt.AlignLeft)

        self.money_4 = QHBoxLayout()
        self.money_4.setSpacing(10)
        self.money_4.setObjectName(u"money_4")
        self.iconMoney_4 = QPushButton(self.miniCluster_4)
        self.iconMoney_4.setObjectName(u"iconMoney_4")
        self.iconMoney_4.setMinimumSize(QSize(20, 20))
        self.iconMoney_4.setMaximumSize(QSize(20, 20))
        self.iconMoney_4.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_4.setIconSize(QSize(24, 24))

        self.money_4.addWidget(self.iconMoney_4)

        self.textMoney_4 = QLabel(self.miniCluster_4)
        self.textMoney_4.setObjectName(u"textMoney_4")
        self.textMoney_4.setMaximumSize(QSize(16777215, 20))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_4.setPalette(palette29)
        self.textMoney_4.setFont(font4)
        self.textMoney_4.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_4.addWidget(self.textMoney_4)


        self.verticalLayout_4.addLayout(self.money_4)


        self.miniClusters.addWidget(self.miniCluster_4, 0, 2, 1, 1)

        self.miniCluster_12 = QFrame(self.otherVacancyFrame)
        self.miniCluster_12.setObjectName(u"miniCluster_12")
        self.miniCluster_12.setMinimumSize(QSize(347, 104))
        self.miniCluster_12.setMaximumSize(QSize(347, 104))
        self.miniCluster_12.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.miniCluster_12)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.nameButton_14 = QPushButton(self.miniCluster_12)
        self.nameButton_14.setObjectName(u"nameButton_14")
        sizePolicy1.setHeightForWidth(self.nameButton_14.sizePolicy().hasHeightForWidth())
        self.nameButton_14.setSizePolicy(sizePolicy1)
        self.nameButton_14.setMinimumSize(QSize(0, 30))
        self.nameButton_14.setMaximumSize(QSize(320, 30))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.Button, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_14.setPalette(palette30)
        self.nameButton_14.setFont(font2)
        self.nameButton_14.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_14.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_13.addWidget(self.nameButton_14, 0, Qt.AlignLeft)

        self.money_13 = QHBoxLayout()
        self.money_13.setSpacing(10)
        self.money_13.setObjectName(u"money_13")
        self.iconMoney_13 = QPushButton(self.miniCluster_12)
        self.iconMoney_13.setObjectName(u"iconMoney_13")
        self.iconMoney_13.setMinimumSize(QSize(20, 20))
        self.iconMoney_13.setMaximumSize(QSize(20, 20))
        self.iconMoney_13.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_13.setIconSize(QSize(24, 24))

        self.money_13.addWidget(self.iconMoney_13)

        self.textMoney_13 = QLabel(self.miniCluster_12)
        self.textMoney_13.setObjectName(u"textMoney_13")
        self.textMoney_13.setMaximumSize(QSize(16777215, 20))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_13.setPalette(palette31)
        self.textMoney_13.setFont(font4)
        self.textMoney_13.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_13.addWidget(self.textMoney_13)


        self.verticalLayout_13.addLayout(self.money_13)


        self.miniClusters.addWidget(self.miniCluster_12, 2, 0, 1, 1)

        self.miniCluster_13 = QFrame(self.otherVacancyFrame)
        self.miniCluster_13.setObjectName(u"miniCluster_13")
        self.miniCluster_13.setMinimumSize(QSize(347, 104))
        self.miniCluster_13.setMaximumSize(QSize(347, 104))
        self.miniCluster_13.setStyleSheet(u"QFrame {\n"
"	border-right: 2px solid #E7E7E7;\n"
"	border-bottom: 2px solid #E7E7E7;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.miniCluster_13)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(20, 20, 20, 20)
        self.nameButton_15 = QPushButton(self.miniCluster_13)
        self.nameButton_15.setObjectName(u"nameButton_15")
        sizePolicy1.setHeightForWidth(self.nameButton_15.sizePolicy().hasHeightForWidth())
        self.nameButton_15.setSizePolicy(sizePolicy1)
        self.nameButton_15.setMinimumSize(QSize(0, 30))
        self.nameButton_15.setMaximumSize(QSize(320, 30))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.Button, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.nameButton_15.setPalette(palette32)
        self.nameButton_15.setFont(font2)
        self.nameButton_15.setLayoutDirection(Qt.LeftToRight)
        self.nameButton_15.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"   color: #101010;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom: 4px solid #501EBC;\n"
"	border-radius: 2px;\n"
"}")

        self.verticalLayout_14.addWidget(self.nameButton_15, 0, Qt.AlignLeft)

        self.money_14 = QHBoxLayout()
        self.money_14.setSpacing(10)
        self.money_14.setObjectName(u"money_14")
        self.iconMoney_14 = QPushButton(self.miniCluster_13)
        self.iconMoney_14.setObjectName(u"iconMoney_14")
        self.iconMoney_14.setMinimumSize(QSize(20, 20))
        self.iconMoney_14.setMaximumSize(QSize(20, 20))
        self.iconMoney_14.setStyleSheet(u"QAbstractButton {\n"
"	border: none;\n"
"	image: url(:/Icons/Icons And Logo/Wallet_grey.png);\n"
"}")
        self.iconMoney_14.setIconSize(QSize(24, 24))

        self.money_14.addWidget(self.iconMoney_14)

        self.textMoney_14 = QLabel(self.miniCluster_13)
        self.textMoney_14.setObjectName(u"textMoney_14")
        self.textMoney_14.setMaximumSize(QSize(16777215, 20))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.textMoney_14.setPalette(palette33)
        self.textMoney_14.setFont(font4)
        self.textMoney_14.setStyleSheet(u"border: none;\n"
"color: #5B5B5B;")

        self.money_14.addWidget(self.textMoney_14)


        self.verticalLayout_14.addLayout(self.money_14)


        self.miniClusters.addWidget(self.miniCluster_13, 2, 1, 1, 1)


        self.miniClustersFrame.addLayout(self.miniClusters)

        self.verticalScrollBar = QScrollBar(self.otherVacancyFrame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        palette34 = QPalette()
        brush4 = QBrush(QColor(231, 231, 231, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.verticalScrollBar.setPalette(palette34)
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

        self.miniClustersFrame.addWidget(self.verticalScrollBar)


        self.otherVacancy.addLayout(self.miniClustersFrame)


        self.verticalLayout_15.addWidget(self.otherVacancyFrame, 0, Qt.AlignTop)

        TakeProfessionPage.setCentralWidget(self.takeProfessionPage)

        self.retranslateUi(TakeProfessionPage)

        QMetaObject.connectSlotsByName(TakeProfessionPage)
    # setupUi

    def retranslateUi(self, TakeProfessionPage):
        TakeProfessionPage.setWindowTitle(QCoreApplication.translate("TakeProfessionPage", u"Your Vacancy", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u044b", None))
        self.pushButton_3.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.title_2.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044e", None))
        self.pushButtonAddTags.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.title_3.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0412\u0430\u0448\u0430 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u044f", None))
        self.label_2.setText("")
        self.nameButton.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041f\u0440\u043e\u0434\u0430\u0432\u0435\u0446", None))
        self.iconCity.setText("")
#if QT_CONFIG(shortcut)
        self.iconCity.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textCity.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041e\u043c\u0441\u043a", None))
        self.iconMoney.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.titleDescription.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.textDescription.setHtml(QCoreApplication.translate("TakeProfessionPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u0438\u0433\u0440\u0430\u0435\u0442 \u043a\u043b\u044e\u0447\u0435\u0432\u0443\u044e \u0440\u043e\u043b\u044c \u0432 \u043c\u0438\u0440\u0435 \u0431\u0438\u0437\u043d\u0435\u0441\u0430. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u043e\u0442\u0432\u0435\u0447\u0430\u044e\u0442 \u0437\u0430 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u0441 \u043a\u043b\u0438\u0435"
                        "\u043d\u0442\u0430\u043c\u0438 \u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0443 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0438\u043b\u0438 \u0443\u0441\u043b\u0443\u0433. \u041e\u043d\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u043e\u0431\u043b\u0430\u0434\u0430\u0442\u044c \u0445\u043e\u0440\u043e\u0448\u0438\u043c\u0438 \u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0442\u0438\u0432\u043d\u044b\u043c\u0438 \u043d\u0430\u0432\u044b\u043a\u0430\u043c\u0438, \u0447\u0442\u043e\u0431\u044b \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e \u0434\u043e\u043d\u043e\u0441\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0435. \u0423\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0443\u043c\u0435\u044e\u0442 \u0432\u044b\u044f\u0432\u043b\u044f\u0442\u044c \u043f\u043e\u0442\u0440\u0435\u0431\u043d\u043e\u0441\u0442\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432"
                        " \u0438 \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0442\u044c \u0438\u043c \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u044f. \u0420\u0430\u0431\u043e\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u0447\u0430\u0441\u0442\u043e \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u0443\u043c\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u0435 \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0442\u044c \u043f\u043e\u0437\u0438\u0442\u0438\u0432\u043d\u0443\u044e \u0430\u0442\u043c\u043e\u0441\u0444\u0435\u0440\u0443 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0442\u0430\u043a\u0436\u0435 \u0437\u0430\u043d\u0438\u043c\u0430\u044e\u0442\u0441\u044f \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435\u043c \u0432\u0438\u0442\u0440\u0438\u043d \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436"
                        "\u0430\u043d\u0438\u0435\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0430 \u043d\u0430 \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u043c \u043c\u0435\u0441\u0442\u0435. \u0412\u0430\u0436\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u044c\u044e \u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u044b \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0437\u043d\u0430\u043d\u0438\u0435 \u0430\u0441\u0441\u043e\u0440\u0442\u0438\u043c\u0435\u043d\u0442\u0430 \u0438 \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0435\u0439 \u0442\u043e\u0432\u0430\u0440\u043e\u0432. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0433\u043e\u0442\u043e\u0432\u044b \u043a \u0440\u0430\u0431\u043e\u0442\u0435 \u0432 \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u0445 \u0441\u0442\u0440\u0435\u0441\u0441\u0430 \u0438 \u0432\u044b\u0441\u043e\u043a\u043e\u0439 \u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0446\u0438\u0438. \u042d\u0442\u0430 \u043f\u0440\u043e\u0444"
                        "\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0434\u043b\u044f \u043a\u0430\u0440\u044c\u0435\u0440\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430 \u0438 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f \u043d\u0430\u0432\u044b\u043a\u043e\u0432 \u043f\u0440\u043e\u0434\u0430\u0436. \u0412 \u0446\u0435\u043b\u043e\u043c, \u0440\u0430\u0431\u043e\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043a\u0430\u043a \u0443\u0432\u043b\u0435\u043a\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439, \u0442\u0430\u043a \u0438 \u0442\u0440\u0435\u0431\u0443\u044e\u0449\u0435\u0439 \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u0438\u043b\u0438\u0439. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0447\u0430\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442"
                        " \u0432 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0441\u0444\u0435\u0440\u0430\u0445, \u0432\u043a\u043b\u044e\u0447\u0430\u044f</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; font-weight:600;\">\u0440\u043e\u0437\u043d\u0438\u0447\u043d\u0443\u044e \u0442\u043e\u0440\u0433\u043e\u0432\u043b\u044e, \u0443\u0441\u043b\u0443\u0433\u0438 \u0438 B2B-\u043f\u0440\u043e\u0434\u0430\u0436\u0438. \u041e\u043d\u0438 \u043c\u043e\u0433\u0443\u0442 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u043d\u0430 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432, \u0442\u0430\u043a\u0438\u0445 \u043a\u0430\u043a \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0430, \u043e\u0434\u0435\u0436\u0434\u0430 \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u044b \u043f\u0438\u0442\u0430\u043d"
                        "\u0438\u044f. \u0423\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0447\u0430\u0441\u0442\u043e \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0442\u0441\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u0430\u043c\u0438 \u0432 \u0441\u0432\u043e\u0435\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438, \u0447\u0442\u043e \u043f\u043e\u043c\u043e\u0433\u0430\u0435\u0442 \u0438\u043c \u0443\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0442\u044c \u0434\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f \u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u043c\u0438. \u0412\u0430\u0436\u043d\u044b\u043c \u0430\u0441\u043f\u0435\u043a\u0442\u043e\u043c \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u043c\u0435\u043d\u0438\u0435 \u0441\u043f\u0440\u0430\u0432\u043b\u044f\u0442\u044c\u0441\u044f"
                        " \u0441 \u0432\u043e\u0437\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438 \u0438 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u044c \u043a\u043e\u043c\u043f\u0440\u043e\u043c\u0438\u0441\u0441\u044b. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0442\u0430\u043a\u0436\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0433\u043e\u0442\u043e\u0432\u044b \u043a \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044e \u043d\u043e\u0432\u044b\u043c \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u043c \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u044f\u043c. \u042d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0435 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u043f\u0440\u043e\u0434\u0430\u0436, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435 \u0441\u043b\u0443\u0448"
                        "\u0430\u043d\u0438\u0435 \u0438 \u0437\u0430\u0434\u0430\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432. \u041e\u043d\u0438 \u0447\u0430\u0441\u0442\u043e \u0443\u0447\u0430\u0441\u0442\u0432\u0443\u044e\u0442 \u0432 \u0430\u043a\u0446\u0438\u044f\u0445 \u0438 \u0440\u0430\u0441\u043f\u0440\u043e\u0434\u0430\u0436\u0430\u0445, \u0447\u0442\u043e \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u043e\u0442 \u043d\u0438\u0445 \u0433\u0438\u0431\u043a\u043e\u0441\u0442\u0438 \u0438 \u043a\u0440\u0435\u0430\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438. \u0412 \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0441\u043b\u0443\u0447\u0430\u044f\u0445 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u043f\u043e\u043b\u0443\u0447\u0430\u044e\u0442 \u043a\u043e\u043c\u0438\u0441\u0441\u0438\u043e\u043d\u043d\u044b\u0435 \u0437\u0430 \u0441\u0432\u043e\u0438 \u043f\u0440\u043e\u0434\u0430\u0436\u0438, \u0447\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0437\u043d\u0430\u0447\u0438\u0442"
                        "\u0435\u043b\u044c\u043d\u043e \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c \u0438\u0445 \u0434\u043e\u0445\u043e\u0434. \u0420\u0430\u0431\u043e\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u0432 \u0431\u043e\u043b\u044c\u0448\u0438\u0445 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430\u0445 \u0438\u043b\u0438 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0430\u0445. \u041a\u0440\u043e\u043c\u0435 \u0442\u043e\u0433\u043e, \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0447\u0430\u0441\u0442\u043e \u0437\u0430\u043d\u0438\u043c\u0430\u044e\u0442\u0441\u044f \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435\u043c \u043e\u0442\u0447\u0435\u0442\u043e\u0432 \u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u0445 \u0438 \u0430\u043d"
                        "\u0430\u043b\u0438\u0437\u043e\u043c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0441\u0432\u043e\u0435\u0439 \u0440\u0430\u0431\u043e\u0442\u044b. \u041e\u043d\u0438 \u043c\u043e\u0433\u0443\u0442 \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043f\u043e \u0441\u043c\u0435\u043d\u0430\u043c, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0432\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0438 \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u0447\u043d\u044b\u0435 \u0434\u043d\u0438, \u0447\u0442\u043e \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u043e\u0442 \u043d\u0438\u0445 \u0432\u044b\u0441\u043e\u043a\u043e\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0441\u0430\u043c\u043e\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438. \u041f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u0438\u0433\u0440\u0430\u044e\u0442 \u0432\u0430\u0436\u043d\u0443\u044e \u0440\u043e\u043b\u044c \u0432 \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438 \u0438\u043c\u0438"
                        "\u0434\u0436\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438, \u0442\u0430\u043a \u043a\u0430\u043a \u0438\u043c\u0435\u043d\u043d\u043e \u043e\u043d\u0438 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0431\u0440\u0435\u043d\u0434 \u043f\u0435\u0440\u0435\u0434 \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u043c\u0438. \u0425\u043e\u0440\u043e\u0448\u0438\u0435 \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b \u043c\u043e\u0433\u0443\u0442 \u0441\u0442\u0430\u0442\u044c \u043d\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u043b\u0438\u0434\u0435\u0440\u0430\u043c\u0438 \u043f\u0440\u043e\u0434\u0430\u0436, \u043d\u043e \u0438 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430\u043c\u0438, \u043e\u0431\u0443\u0447\u0430\u044f \u043d\u043e\u0432\u044b\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432. \u0412 \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u0445 \u043f\u0440\u043e\u0434\u0430\u0432"
                        "\u0446\u044b \u0442\u0430\u043a\u0436\u0435 \u0434\u043e\u043b\u0436\u043d\u044b \u0438\u043c\u0435\u0442\u044c \u043d\u0430\u0432\u044b\u043a\u0438 \u0440\u0430\u0431\u043e\u0442\u044b \u0441 \u0446\u0438\u0444\u0440\u043e\u0432\u044b\u043c\u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043c\u0438 \u0438 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430\u043c\u0438. \u042d\u0442\u043e \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e \u0432 \u044d\u043f\u043e\u0445\u0443 \u043e\u043d\u043b\u0430\u0439\u043d-\u043f\u0440\u043e\u0434\u0430\u0436, \u043a\u043e\u0433\u0434\u0430 \u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0446\u0438\u044f \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0433\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u043e\u0439. \u0423\u043c\u0435\u043d\u0438\u0435 \u0430\u0434\u0430\u043f\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f"
                        " \u043a \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f\u043c \u043d\u0430 \u0440\u044b\u043d\u043a\u0435 \u0438 \u0432 \u043f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0445 \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f\u0445 \u0442\u0430\u043a\u0436\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u0430\u0436\u043d\u044b\u043c \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430. \u0412 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u043c \u0438\u0442\u043e\u0433\u0435, \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0432\u0446\u0430 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043e\u0447\u0435\u043d\u044c \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u043e\u0439 \u0438 \u0434\u0438\u043d\u0430\u043c\u0438\u0447\u043d\u043e\u0439, \u043f\u0440\u0435\u0434"
                        "\u043b\u0430\u0433\u0430\u044f \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0434\u043b\u044f \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u043e\u0441\u0442\u0430</span></p></body></html>", None))
        self.label_3.setText("")
        self.title_4.setText(QCoreApplication.translate("TakeProfessionPage", u"\u041f\u043e\u0445\u043e\u0436\u0438\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.nameButton_7.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_6.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_6.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_6.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_8.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_7.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_7.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_10.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_9.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_9.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_9.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_4.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_3.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_3.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_2.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_2.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_2.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_11.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_10.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_10.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_10.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_12.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_11.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_11.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_11.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_13.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_12.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_12.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_12.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_6.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_5.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_5.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_5.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_4.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_4.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_14.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_13.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_13.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_13.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
        self.nameButton_15.setText(QCoreApplication.translate("TakeProfessionPage", u"\u0422\u043e\u0440\u0433\u043e\u0432\u0435\u0446 \u043d\u0430 \u0440\u044b\u043d\u043a\u0435", None))
        self.iconMoney_14.setText("")
#if QT_CONFIG(shortcut)
        self.iconMoney_14.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.textMoney_14.setText(QCoreApplication.translate("TakeProfessionPage", u"21 000 - 25 000 \u0440\u0443\u0431/\u043c\u0435\u0441", None))
    # retranslateUi

